import re,sys,json
L=open(sys.argv[1],encoding='utf-8').read().split('\n')
items=[];sec=None;cur=None;mode=None
SRC=re.compile(r'^\s*(\d{4})년\s*\[(.+?)\]\s*기출')
for ln in L:
    s=ln.strip()
    if s.startswith(';') and len(s)<30: sec=s[1:]; continue
    m=re.match(r'^\(정답\)\s*(.*)',s)
    if m:
        cur={'sec':sec,'ans':m.group(1),'sol':[],'src':None,'text':[],'gso':False};items.append(cur);mode='a';continue
    if cur is None: continue
    m=SRC.match(s)
    if m and mode=='a': cur['src']=f"{m.group(1)} {m.group(2)}";mode='q';continue
    if s in ('soma','수 악 모 아','[tbl]','') : continue
    if s=='[gso]': cur['gso']=True; continue
    s=s.replace('[tbl]','')
    (cur['sol'] if mode=='a' else cur['text']).append(s)
for it in items:
    it['text']=' '.join(it['text']); it['sol']=' '.join(it['sol'])
json.dump(items,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
print(len(items), sum(1 for i in items if not i['src']), sum(i['gso'] for i in items))
