import re,json,sys
ANS=re.compile(r'^(⑴|\(1\)|[①②③④⑤]|⟦|ㄱ|ㄴ|ㄷ|풀이 참조)')
def clean(l): return l.replace('[gso]','').strip()
out={}
for k in (0,1,2):
    t=open(f'p5l/A00660/x/f{k}.txt').read()
    parts=t.split('[tbl]')
    head=parts[0]; blocks=parts[1:]
    # find answer start: first block whose first line matches ANS and all following
    firsts=[[clean(l) for l in b.split('\n') if clean(l)] for b in blocks]
    # split point = first index i where firsts[i][0] matches ANS and is short
    sp={0:64,1:88,2:62}[k]
    probs_raw=blocks[:sp]; ans_raw=firsts[sp:]
    # headings: scan text sequentially, record heading before each problem block
    probs=[]; sec=None
    pre=head
    for i,b in enumerate(probs_raw):
        lines=[clean(l) for l in b.split('\n') if clean(l)]
        # heading lines appear at tail of previous block text: pattern NN / name / 중요도
        txt='\n'.join(lines)
        m=re.findall(r'(?m)^(\d\d)\n(.+)\n중요도',txt)
        body=re.split(r'(?m)^\d\d\n.+\n중요도.*$',txt)[0]
        hm=re.findall(r'(?m)^(\d\d)\n(.+)\n중요도',pre)
        if hm: sec=hm[-1][0]+' '+hm[-1][1].replace('⟦bold{','').replace('⟧','').strip()
        probs.append(dict(sec=sec,text=body.strip()))
        pre=txt
    # merge split
    if k==2:
        probs[21]['text']+='\n'+probs[22]['text']; del probs[22]
    answers=[]
    for f in ans_raw:
        if answers and not ANS.match(f[0]):
            answers[-1]['sol']+=' '+' '.join(f); continue
        answers.append(dict(ans=f[0],sol=' '.join(f[1:])))
    print(k,len(probs),len(answers),file=sys.stderr)
    out[k]=[dict(p,**a) for p,a in zip(probs,answers)]
json.dump(out,open('p5l/A00660/w/items.json','w'),ensure_ascii=False,indent=0)
