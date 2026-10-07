import json, re, sys, cfgex
from cfgp5 import *
cfg=json.load(open(sys.argv[1]))
items=[json.loads(l) for l in open(cfg['items'],encoding='utf-8') if l.strip()]
def unit(it):
    s=it['small']
    if re.search(r'정적분|부정적분|넓이|속도|거리|위치|가속도',s): return '적분','정적분' if '부정' not in s else '부정적분'
    if re.search(r'극한|연속',s) and '정적분' not in s: return '함수의 극한과 연속', ('함수의 연속' if '연속' in s else '함수의 극한')
    if re.search(r'미분가능|미분계수|도함수|평균변화율',s): return '미분','미분계수와 도함수'
    return '미분','도함수의 활용'
cfgex.ROWS.clear()
setup(cfg['qid'],cfg['src'],cfg['fname'],cfg['path'],cfg['srccat'],"2015 개정",cfg['term'],cfg['grade'],cfg['course'],CURR="2015 개정",KEY=None,KEYPAGE="",KEYSRC="",VIS="스캔 PDF 100dpi(필요시 250~300dpi 확대) 렌더 시각판독",TEXT="스캔 PDF(텍스트층 없음) — 렌더 판독 확정")
builder.SOL_PAGE.update({k:0 for k in range(1,3000)})
for q,it in enumerate(items,1):
    big,mid=unit(it); small=it['small']; n=it['n']
    lab=f"STEP UP {str(n)[2:]}" if isinstance(n,str) else f"{n:03d}"
    part="Part1 대단원별 실전문항" if (isinstance(n,str) or n<=150) else "Part2 대단원통합 N-1제"
    fig="그림(스캔 렌더 판독)" if it.get('fig') else "없음"
    note=f"정답지(땅우N-1제_수2 해설.pdf 9.3MB, master UNMAPPED·drive_id 없음) 전송한계로 미연결 — 독립풀이(수기/sympy) 근거: {it['why']}"
    kw={}
    if it.get('fig'): kw.update(status="독립풀이(그림 조건 렌더 판독; 정답지 미연결)")
    R(q,it['p'],big,mid,small,f"S2.{mid}.{small}",f"{small} — 땅우N-1제 수학Ⅱ {part} {lab}번",mid+";"+small,it['diff'],it['fmt'],it['ans'],it['stem'][:220],note,label=lab,fig=fig,final=it['ans'],**kw)
    ROWS[-1].update({"출처대분류":cfg['srccat'],"학교/시험명":f"땅우 N-1제 수학Ⅱ {part} {lab}번 (본문 p{it['p']})"})
build(cfg['qid'],list(ROWS),cfg['cum']); print(len(ROWS))
