import json,base64,re,sys,glob,os
fid,out=sys.argv[1],sys.argv[2]
P='/root/.claude/projects/-home-user-claude-test/b3c9c0b1-2d20-5f6f-a984-cabdebc0e83c'
best=None
for f in sorted(glob.glob(P+'/tool-results/*download*'),key=os.path.getmtime,reverse=True):
    try:
        d=json.load(open(f))
        if d.get('id')==fid: best=d['content']; break
    except Exception: pass
if not best:
    for line in open(P+'.jsonl'):
        if fid in line and '"content\\":\\"0M8R4' in line or (fid in line and '"content":"0M8R4' in line):
            m=re.search(r'content\\?":\\?"([A-Za-z0-9+/=]{100,})',line)
            if m: best=m.group(1)
open(out,'wb').write(base64.b64decode(best)); print(out,len(best))
