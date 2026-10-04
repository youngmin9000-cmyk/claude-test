import olefile, zlib, struct, sys, re
def records(data):
    i=0
    while i+4<=len(data):
        h=struct.unpack('<I',data[i:i+4])[0]; i+=4
        tag=h&0x3ff; lvl=(h>>10)&0x3ff; sz=h>>20
        if sz==0xfff: sz=struct.unpack('<I',data[i:i+4])[0]; i+=4
        yield tag,lvl,data[i:i+sz]; i+=sz
def para_text(b):
    out=[];i=0
    while i+1<len(b):
        c=struct.unpack('<H',b[i:i+2])[0]
        if c<32:
            if c in (0,10,13): out.append('\n' if c in (10,13) else ''); i+=2
            elif c==9: out.append('\t'); i+=16
            elif c in (1,2,3,11,12,14,15,16,17,18,21,22,23): out.append('[CTRL%d]'%c if c in(11,) else ''); i+=16
            else: i+=16 if c not in (24,25,26,27,28,29,30,31) else 2
        else: out.append(chr(c)); i+=2
    return ''.join(out)
def dump(path):
    o=olefile.OleFileIO(path)
    hdr=o.openstream('FileHeader').read(); comp=hdr[36]&1
    secs=sorted([s for s in o.listdir() if s[0]=='BodyText'],key=lambda s:int(s[1][7:]))
    out=[]
    for s in secs:
        d=o.openstream(s).read()
        if comp: d=zlib.decompress(d,-15)
        for tag,lvl,b in records(d):
            if tag==67: out.append(para_text(b))
            elif tag==88:
                ln=struct.unpack('<H',b[4:6])[0]; sc=b[6:6+2*ln].decode('utf-16le',errors='replace')
                out.append(' ⟦EQ:'+sc+'⟧ ')
    bins=[s for s in o.listdir() if s[0]=='BinData']
    return ''.join(x if x.startswith(' ⟦') else x+'\n' for x in out), bins
if __name__=='__main__':
    t,b=dump(sys.argv[1]); print(t); print('BINDATA',b)
