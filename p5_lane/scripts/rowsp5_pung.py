import json, re, sys, cfgex
from cfgp5 import *
cfg=json.load(open(sys.argv[1]))
d=json.load(open(cfg['items']))
def clean(s): return re.sub(r'\s+',' ',s.replace('⟦','').replace('⟧',''))[:220]
items=[]
for F in cfg['files']:
    for i,x in enumerate(d[F['k']],1): items.append((F,i,x))
key={n:x['ans'] for n,(F,i,x) in enumerate(items,1)}
cfgex.ROWS.clear()
setup(cfg['qid'],cfg['src'],cfg['fname'],cfg['path'],"풍산자 필수유형(시판 문제집)","2022 개정",cfg['term'],"고2","수학Ⅱ",CURR="2022 개정",KEY=key,KEYPAGE="각 HWP 후반 정답·풀이",KEYSRC="",VIS="HWP 본문·수식 추출(로컬 파서); 그림(gso)은 텍스트 미추출",TEXT="HWP 텍스트층(수식 스크립트 포함) — FULL_TEXT")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
for n,(F,i,x) in enumerate(items,1):
    k=F['k']; tag=f"{k}:{i}"
    sec=re.sub(r'[{}]','',x['sec'] or F['sec0']).replace(' over ','/')
    small=re.sub(r'^\d\d ','',sec)
    diff='상' if i>=F['hard'] else ('하' if i<=len(d[k])*0.3 else '중')
    fmt='객관식' if '①' in x['text'] else '서술형'
    kw={}; fig="없음"; final=None; note="원문 정답·풀이 동봉(동일 HWP) — 독립풀이(sympy/수기) 대조"
    if i in F['fig']:
        fig="그림(HWP gso, 미추출)"; kw.update(status="원문 정답 기재 — 그림 조건 미판독으로 독립검증 보류", trust="중간(원문 정답 의존)")
    if tag in cfg.get('hold',{}):
        final,why=cfg['hold'][tag]; kw.update(ready="HOLD",review="HOLD-원문정답충돌",status="독립풀이 ≠ 원문 정답(원문 정답 보존)",trust="낮음(충돌)",conflict=why); note+="; 충돌: "+why
    if tag in cfg.get('rev',{}):
        kw.update(ready="REVIEW",review="REVIEW-원문조건검토",status="독립풀이·원문 정답 대조(원문 조건 검토 필요)",trust="중간"); note+="; "+cfg['rev'][tag]
    if tag in cfg.get('typo',{}): note+="; "+cfg['typo'][tag]
    R(n,int(k)+1,F['big'],F['mid'],small,f"S2.{F['mid']}.{sec[:2]}",f"{small} — {F['name']} {i}번",F['mid']+";"+small,diff,fmt,x['ans']+(f" | 독립: {final}" if final else ""),clean(x['text']),note,label=f"{F['name']}-{i}",fig=fig,final=final,**kw)
    ROWS[-1].update({"출처대분류":"시판 문제집(풍산자 필수유형)","학교/시험명":f"풍산자 필수유형 수학Ⅱ {F['name']} {i}번","해설연결상태":"동일 파일 정답·풀이"})
build(cfg['qid'],list(ROWS),cfg['cum']); print(len(ROWS))
