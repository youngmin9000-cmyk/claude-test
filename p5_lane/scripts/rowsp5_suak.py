import json, re, sys, cfgex
from cfgp5 import *
cfg=json.load(open(sys.argv[1]))
d=json.load(open(cfg['items']))
def clean(s): return re.sub(r'\s+',' ',s.replace('⟦','').replace('⟧','').replace('수악모아',''))[:220]
FA=cfg['final']  # 서술형/해설형 정답 정리
def ansof(i,x):
    if str(i) in FA: return FA[str(i)]
    return x['ans'].replace('⟦','').replace('⟧','').strip()
key={i:ansof(i,x) for i,x in enumerate(d,1)}
cfgex.ROWS.clear()
setup(cfg['qid'],cfg['src'],cfg['fname'],cfg['path'],cfg['srccat'],"2015 개정",cfg['term'],cfg['grade'],cfg['course'],CURR="2015 개정",KEY=key,KEYPAGE="각 문항 앞 (정답) 표기",KEYSRC="",VIS="HWP 본문·수식 추출(로컬 파서); 그림(gso)은 텍스트 미추출",TEXT="HWP 텍스트층(수식 스크립트 포함) — FULL_TEXT")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
for i,x in enumerate(d,1):
    tag=str(i); small=x['sec'] or cfg['sec0']
    t=x['text']; fmt='객관식' if '①' in t else '서술형'
    diff='상' if ('(가)' in t or '(1)' in t and len(t)>300 or len(t)>420) else ('하' if len(t)<130 else '중')
    kw={}; fig="없음"; final=None; note="원문 정답 동봉(동일 HWP, 서술형은 풀이 포함) — 독립풀이(전수 브루트포스/수기) 대조"
    if i in cfg['fig']:
        fig="그림(HWP gso, 미추출)"; kw.update(ready="REVIEW",review="REVIEW-그림판독",status="원문 정답 기재 — 그림 조건 미판독으로 독립검증 보류", trust="중간(원문 정답 의존)")
    if tag in cfg.get('hold',{}):
        final,why,rv=cfg['hold'][tag]; kw.update(ready="HOLD",review=rv,status="독립풀이 ≠ 원문 정답(원문 정답 보존)" if rv=="HOLD-원문정답충돌" else "원문 손상/보기 부재 — 독립검증 불가 또는 불일치",trust="낮음",conflict=why); note+="; "+why
    if tag in cfg.get('rev',{}):
        kw.update(ready="REVIEW",review="REVIEW-원문조건검토",status="독립풀이·원문 정답 대조(원문 조건 검토 필요)",trust="중간"); note+="; "+cfg['rev'][tag]
    R(i,1,cfg['big'],cfg['mid'],small,f"S{cfg['course'][:2]}.{cfg['mid']}.{small}",f"{small} — {x['src']} 기출",cfg['mid']+";"+small,diff,fmt,key[i]+(f" | 독립: {final}" if final else ""),clean(t),note,label=f"{small}-{i}",fig=fig,final=final,**kw)
    ROWS[-1].update({"출처대분류":cfg['srccat'],"학교/시험명":f"{x['src']} 기출","해설연결상태":"동일 파일 정답(서술형 풀이)"})
build(cfg['qid'],list(ROWS),cfg['cum']); print(len(ROWS))
