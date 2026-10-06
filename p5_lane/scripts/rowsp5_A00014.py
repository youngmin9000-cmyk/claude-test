import json
from cfgp5 import *
MC, S_, D = "객관식(5지선다)", "단답형", "서술형"
M, H = "보통", "높음"
G = json.load(open(OUT + "p5l/A00014/graph_feat.json"))
ITEMS = []
def it(q, bp, big, mid, small, tid, tname, tags, diff, fmt, ans, chk, lab, nsub=1, **kw): ITEMS.append((q, bp, big, mid, small, tid, tname, tags, diff, fmt, ans, chk, lab, nsub, kw))
LIM = ("함수의 극한과 연속", "함수의 극한", "함수의 극한 계산")
it(1,186,"함수의 극한과 연속","함수의 극한","극한의 성질","LIMIT.PROOF.BASIC_PROPERTY","극한 계산의 대전제로 lim 1/x²=0, lim 1/√x=0 보이기","극한;증명","하",D,"① lim1/x·lim1/x=0 ② √(lim 1/x)=0","정답 p338 대조 일치","p186 예제1",2,atype="서술")
P190 = [("x→0 (x²+3x)/(3x²−6x)","−1/2","LIMIT.RATIONAL.ZERO_OVER_ZERO"),("x→∞ (x²+3x)/(3x²−6x)","1/3","LIMIT.RATIONAL.INF_SAME_DEGREE"),
 ("x→−∞ 1/(√(x²−2x)+x)","1","LIMIT.IRRATIONAL.NEG_INF_CONJUGATE"),("x→∞ e^{3x+1}/e^{x²}","0","LIMIT.EXP.EXPONENT_DIFF"),
 ("x→∞ log2x/logx","1","LIMIT.LOG.RATIO"),("x→∞ log(2x²+2x+3)/log(x²+x+3)","1","LIMIT.LOG.RATIO_POLY"),
 ("x→0 x·cos(1/x)","0","LIMIT.SQUEEZE.BOUNDED"),("x→1 (x⁹−1)/(x−1)","9","LIMIT.DERIVATIVE_DEF.POWER"),
 ("x→1 (x⁹+2x⁸−3)/(x−1)","25","LIMIT.DERIVATIVE_DEF.POLY"),("f′(2)=3, x→2 {f(x²−2)−f(2)}/(x⁴−16)","3/8","LIMIT.DERIVATIVE_DEF.COMPOSITE"),
 ("x→1 (1/(x−1))∫₁ˣ t³dt","1","LIMIT.INTEGRAL_FUNC.FTC"),("x→0 (1/x)∫₀ˣ (t−1)(t−2)dt","2","LIMIT.INTEGRAL_FUNC.FTC")]
for k,(t,a,tid) in enumerate(P190,1):
    sm = "극한 계산" if k<=7 else ("미분계수의 정의" if k<=10 else "정적분으로 정의된 함수의 극한")
    big = "함수의 극한과 연속" if k<=7 else ("미분" if k<=10 else "적분")
    it(1+k,190,big,"함수의 극한" if k<=7 else ("미분계수" if k<=10 else "정적분"),sm,tid,t,"극한","하" if k not in (3,6,10) else "중하",S_,a,"독립계산·정답 p338~339 대조 일치",f"p190 예제1-{k}",c=("보통" if k in (3,6,10) else "낮음"))
it(14,237,"수열","여러 가지 수열","계차수열","SEQ.DIFFERENCE.GENERAL_TERM","계차수열로 일반항 4가지","계차수열;일반항","중하",D,"⑴ n²−n+1 ⑵ (1−(−2)ⁿ)/3 ⑶ 2ⁿ−1 ⑷ 2ⁿ⁺¹−2","n=1~3 검산; 정답 p339 일치","p237 예제1",4,c=M)
it(15,238,"수열","여러 가지 수열","주기수열","SEQ.PERIODIC.BLOCK_PERIOD","반복 묶음과 주기 4가지","주기수열","하",D,"⑴(1,0,−1,−1,0,1),6 ⑵(1,0),2 ⑶(1,2,1,−1,−2,−1),6 ⑷(1,0,−1,0),4 [정답지 표기 원문 보존]",
   "독립풀이: ②=(1,2,1,−1,−2,−1),6 / ③=(1,0),2 — 정답지 ⑵·⑶ 순서가 문제 ②·③과 뒤바뀜(라벨 오류)","p238 예제2",4,
   review="REVIEW-정답충돌(정답지 ⑵⑶ 라벨 뒤바뀜)",ready="REVIEW",status="독립풀이·정답지 내용 일치하나 문항 대응 라벨 불일치 — 원 정답 보존",trust="중간",
   conflict="정답지 ⑵(1,0),2·⑶(1,2,1,−1,−2,−1),6 ↔ 문제 ②1,2,1,−1,−2,−1…·③1,0,1,0… — 라벨 교차",final="① (1,0,−1,−1,0,1),6 ② (1,2,1,−1,−2,−1),6 ③ (1,0),2 ④ (1,0,−1,0),4")
TR = ("삼각함수","삼각함수의 성질","각변환")
it(16,252,*TR,"TRIG.ANGLE_REDUCTION.SIMPLIFY","sin(π/2±x), cos(π/2±x), cos(3π/2+x), sin(7π/2−x) 간단히","삼각함수;각변환","하",D,"⑴cos x ⑵cos x ⑶−sin x ⑷sin x ⑸sin x ⑹−cos x","독립 검산; 정답 p339 일치","p252 예제1",6)
it(17,253,*TR,"TRIG.ANGLE_REDUCTION.F0_METHOD","예제1을 f(0), f(π/2) 판정법으로 다시 각변환","삼각함수;각변환","하",D,"⑴cos x ⑵cos x ⑶−sin x ⑷sin x ⑸sin x ⑹−cos x","정답지 '정답 동일' 명시","p253 예제2",6)
cub = "; ".join(f"{i}) {v}" for i,v in enumerate(G['cubic'],1))
qua = "; ".join(f"{i}) {v}" for i,v in enumerate(G['quartic'],1))
it(18,270,"미분","도함수의 활용","함수의 그래프 그리기","DERIV.GRAPH_SKETCH.CUBIC_SET","삼차함수 30개 그래프 그리기","극값;그래프","중하",D,"그래프(정답 p340~342 그림). 극값 요약: "+cub,"SymPy로 30개 극값·정류점 계산, 정답 그림 수치 표지 표본 대조 일치","p270 예제1",30,fig="그래프",atype="그래프",c=M)
it(19,270,"미분","도함수의 활용","함수의 그래프 그리기","DERIV.GRAPH_SKETCH.QUARTIC_SET","사차함수 30개 그래프 그리기","극값;그래프","중",D,"그래프(정답 p343~345 그림). 극값 요약: "+qua,"SymPy 계산; 원문 1번과 27번 동일식(x⁴−8x³+18x²−28) 중복 수록","p270 예제2",30,fig="그래프",atype="그래프",c=M)
it(20,275,"미분","미분가능성","구간별 함수의 미분가능성","DERIV.PIECEWISE.DIFFERENTIABLE_PARAM","g=ax²+3(x<1)/2x+b(x≥1) 미분가능, a+b","미분가능성","하",S_,"3","연속 a+3=2+b, 미분계수 2a=2 → a=1, b=2; 정답 p340 일치","p275 예제1")
it(21,295,"미분","합성함수","합성함수의 그래프","FUNC.COMPOSITE.GRAPH_SKETCH_FG","f, g 그래프(3가지) → f(g(x)) 그래프 그리기","합성함수;그래프","중",D,"그래프 작도 문항(정답 부록 미수록, 본문 설명으로 대체)","정답지 없음 — 그림 판독 필요","p295 예제1",3,fig="그래프",atype="그래프",c=M,
   review="HOLD-정답미수록(그래프 작도)",ready="HOLD",status="정답 미수록 작도 문항",trust="낮음")
it(22,300,"미분","합성함수","합성함수의 그래프","FUNC.COMPOSITE.GRAPH_SKETCH_FF","f 그래프(3가지) → f(f(x)) 그래프 그리기","합성함수;그래프","중",D,"그래프 작도 문항(정답 부록 미수록)","정답지 없음 — 그림 판독 필요","p300 예제1",3,fig="그래프",atype="그래프",c=M,
   review="HOLD-정답미수록(그래프 작도)",ready="HOLD",status="정답 미수록 작도 문항",trust="낮음")
KEY = {q: ans for q,_,_,_,_,_,_,_,_,_,ans,_,_,_,_ in ITEMS if q not in (21,22)}
KEY[15] = "⑴(1,0,−1,−1,0,1),6 ⑵(1,0),2 ⑶(1,2,1,−1,−2,−1),6 ⑷(1,0,−1,0),4"
setup("A00014", "1CJjWVZH9L-YW48x0twVectr44-bj0QPw", "전자책_맑은개념수학시리즈2024_수1&수2_0413_@Logic_Files.pdf", "p5l/A00014/src.pdf", "일격필살팀(맑은개념수학)", "2024", "개념서 예제", "고2~고3", "수학Ⅰ·수학Ⅱ", CURR="2015 개정",
      KEY=KEY, KEYPAGE="부록 정답 p338~345(PDF 339~345)", KEYSRC="",
      VIS="전자책 PDF(텍스트층 있음, 345쪽) 텍스트 추출 + 예제 쪽만 대조", TEXT="PREVIEW_ONLY 캐시 → 원본 텍스트층 전체 추출(FULL_TEXT 확인)")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
for q, bp, big, mid, small, tid, tname, tags, diff, fmt, ans, chk, lab, nsub, kw in ITEMS:
    kw.setdefault("atype", "선택지" if fmt == MC else "값")
    R(q, bp+1, big, mid, small, tid, tname, tags, diff, fmt, ans, f"맑은개념수학 수1&수2 {lab}", chk, label=lab, nsub=nsub, **kw)
    r = ROWS[-1]; r.update({"출처대분류": "시판 개념서(전자책) 예제", "학교명": "", "주관기관": "일격필살팀(오르비)", "학교/시험명": f"맑은개념수학 수학I&수학II {lab}",
        "원본페이지": f"책 p{bp} (PDF p{bp+1})", "문항이미지/좌표": f"PDF p{bp+1} {lab}"})
n = len(ROWS); print(n)
build("A00014", ROWS, 0)
