import re,json,sys
ANS=re.compile(r'^(⑴|\(1\)|[①②③④⑤]|⟦|ㄱ|ㄴ|ㄷ|풀이 참조)')
def clean(l): return l.replace('[gso]','').strip()
def istable(f):
    s=' '.join(f); return bool(re.match(r'^⟦\s*[a-zA-Z]\s*⟧$',f[0])) or any(c in s for c in '↗↘')
def isans(f):
    if not f or istable(f): return False
    return bool(ANS.match(f[0])) or (':' in f[0] and len(f[0])<40)
def parse(path,sp,merge=()):
    t=open(path).read(); parts=t.split('[tbl]'); head=parts[0]; blocks=parts[1:]
    F=[[clean(l) for l in b.split('\n') if clean(l)] for b in blocks]
    probs=[]; sec=None; pre=head
    for i,b in enumerate(blocks[:sp]):
        txt='\n'.join(F[i])
        hm=re.findall(r'(?m)^(\d\d)\n(.+)\n중요도',pre)
        if hm: sec=hm[-1][0]+' '+re.sub(r'bold|[{}⟦⟧]','',hm[-1][1]).strip()
        body=re.split(r'(?m)^\d\d\n.+\n중요도.*$',txt)[0]
        probs.append(dict(sec=sec,text=body.strip())); pre=txt
    for m in sorted(merge,reverse=True):
        probs[m-1]['text']+='\n'+probs[m]['text']; del probs[m]
    ans=[]
    for f in F[sp:]:
        if not f: continue
        if isans(f) or not ans: ans.append(dict(ans=f[0],sol=' '.join(f[1:])))
        else: ans[-1]['sol']+=' '+' '.join(f)
    return probs,ans
if __name__=='__main__':
    spec=json.loads(sys.argv[1]); out={}
    for k,v in spec['files'].items():
        p,a=parse(v['path'],v['sp'],v.get('merge',[]))
        print(k,len(p),len(a),file=sys.stderr)
        out[k]=[dict(x,**y) for x,y in zip(p,a)]
    json.dump(out,open(spec['out'],'w'),ensure_ascii=False)
