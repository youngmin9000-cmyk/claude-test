import re,sys,json
def parse(path):
    L=open(path).read().split('\n')
    end=next((i for i,s in enumerate(L) if s.strip().startswith('[빠른 정답]')),len(L))
    quick=[s.strip().replace('[gso]','') for s in L[end+1:] if s.startswith(' ') and not s.startswith('  ') or s.startswith('  (')] if end<len(L) else []
    L=L[:end]
    ishead=lambda s: s.startswith(' ') and not s.startswith('  ') and s.strip()!=''
    isans=lambda s: re.match(r'^ {5}\S',s) or re.match(r'^ {6}\(',s)
    heads=[i for i,s in enumerate(L) if ishead(s)]
    # keep heads that have an answer line before next head
    items=[]; sec=''; act=None; secs={}; acts={}
    cur_sec=''; cur_act=None
    marks=[]
    for i,s in enumerate(L):
        m=re.match(r'^\s{4}(\d-\d-\d\.\s*.+|중단원 마무리하기|대단원 마무리하기|대단원 평가.*)$',s)
        if m and i>0 and L[i-1].strip()=='[tbl]': cur_sec=m.group(1).strip(); cur_act=None
        elif re.match(r'^\[([^\]]+)\]\s*$',s) and not s.startswith('[tbl]') and not s.startswith('[gso]'): cur_act=s.strip('[] ')
        secs[i]=cur_sec; acts[i]=cur_act
        if ishead(s): cur_act_reset=True
    valid=[]
    for k,h in enumerate(heads):
        nxt=heads[k+1] if k+1<len(heads) else len(L)
        if any(isans(L[j]) for j in range(h+1,nxt)): valid.append(h)
    for k,h in enumerate(valid):
        nxt=valid[k+1] if k+1<len(valid) else len(L)
        span=L[h:nxt]
        a=next(j for j,s in enumerate(span) if j>0 and isans(s))
        stmt=[span[0].strip()]+[s.strip() for j,s in enumerate(span[1:],1) if j!=a and not s.startswith('    ') and not re.match(r'^\[([^\]]+)\]\s*$',s) and s.strip() not in ('[tbl]','[gso]','')]
        sol=[s.strip() for j,s in enumerate(span[1:],1) if j!=a and s.startswith('    ') and not isans(s)]
        # activity: label line immediately before head (within 2 lines)
        act=acts[h-1] if h>0 and re.match(r'^\[([^\]]+)\]\s*$',L[h-1]) else None
        items.append(dict(sec=secs[h],act=act,stmt=' '.join(stmt),ans=span[a].strip().replace('[gso]',''),sol=' / '.join(sol)))
    return items,quick
if __name__=='__main__':
    it,q=parse(sys.argv[1]); json.dump(it,open(sys.argv[2],'w'),ensure_ascii=False)
    print('items',len(it),'quick',len(q))
