import olefile, zlib, struct, sys
from hwpx import records, para_text
def dump(path):
    o=olefile.OleFileIO(path)
    comp=o.openstream('FileHeader').read()[36]&1
    secs=sorted([s for s in o.listdir() if s[0]=='BodyText'],key=lambda s:int(s[1][7:]))
    recs=[]
    for s in secs:
        d=o.openstream(s).read()
        if comp: d=zlib.decompress(d,-15)
        recs+=list(records(d))
    # build paragraph list: each PARA_HEADER(66) at level L starts a para; ctrl headers (71) at level L+1 belong to it
    out=[]; stack=[]
    i=0; paras=[]
    for idx,(tag,lvl,b) in enumerate(recs):
        if tag==66: paras.append({'lvl':lvl,'text':None,'ctrls':[]})
        elif tag==67 and paras: paras[-1]['text']=para_text(b) if paras[-1]['text'] is None else paras[-1]['text']
        elif tag==71:
            cid=b[:4][::-1].decode('latin1')
            # find owning paragraph: last para with lvl == lvl-1
            for p in reversed(paras):
                if p['lvl']==lvl-1: p['ctrls'].append([cid,None]); break
        elif tag==88:
            ln=struct.unpack('<H',b[4:6])[0]; sc=b[6:6+2*ln].decode('utf-16le',errors='replace').replace('\r',' ').replace('\n',' ')
            for p in reversed(paras):
                if p['ctrls'] and p['ctrls'][-1][0]=='eqed' and p['ctrls'][-1][1] is None and p['lvl']==lvl-2: p['ctrls'][-1][1]=sc; break
    lines=[]
    for p in paras:
        t=p['text'] or ''
        k=0; res=''
        parts=t.split('[CTRL11]')
        ctr=[c for c in p['ctrls'] if c[0] not in ('secd','cold','head','foot','pgnp','pghd','nwno','atno','tcmt','bokm','fn  ','en  ')]
        for j,part in enumerate(parts):
            res+=part
            if j<len(parts)-1:
                c=ctr[k] if k<len(ctr) else ['?',None]; k+=1
                res+=('⟦'+c[1]+'⟧') if c[0]=='eqed' and c[1] else '['+c[0].strip()+']'
        lines.append(('  '*p['lvl'])+res)
    return '\n'.join(l for l in lines if l.strip())
if __name__=='__main__': print(dump(sys.argv[1]))
