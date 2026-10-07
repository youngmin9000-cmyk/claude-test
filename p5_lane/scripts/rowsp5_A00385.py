import cfgex
from cfgp5 import *
D = "서술형"
NOTE = "공식 빈칸 워크시트(정답지 없음) — 표준 공식으로 독립 작성"
cfgex.ROWS.clear()
setup("A00385","1Sqmq7FdmRZkiE58z-Gzc-CUUKk4Fa_rW","다항함수의 미분법.pdf","p5l/A00385/src.pdf","자체 제작(공식 정리지)","2026","공식 확인 워크시트","고2","수학Ⅱ",CURR="2022 개정",VIS="텍스트층 PDF 2쪽 (FULL_TEXT_SAFE, 렌더 확인)",TEXT="텍스트층 PDF 2쪽 (FULL_TEXT_SAFE, 렌더 확인)")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
def row(q, page, small, tid, tname, ans, nsub=1, diff="하"):
    mid="미분"
    R(q, page, "미분", mid, small, tid, tname, small+";공식", diff, D, ans, "공식 빈칸", NOTE, label=f"항목{q}", nsub=nsub, atype="식")
    ROWS[-1].update({"출처대분류": "자체 제작 공식 정리 워크시트", "학교/시험명": f"A00385 공식 확인 항목{q}"})
L=[(1,1,"평균변화율","DIFF.AVG_RATE.DEF","평균변화율(=두 점 (a,f(a)),(b,f(b))을 잇는 직선의 기울기)","Δy/Δx=(f(b)−f(a))/(b−a)",1),
 (2,1,"미분계수","DIFF.DERIV_AT_POINT.DEF","x=a에서의 미분계수(순간변화율, 접선의 기울기) 정의 2가지","① f'(a)=lim_{h→0}(f(a+h)−f(a))/h ② f'(a)=lim_{x→a}(f(x)−f(a))/(x−a)",2),
 (3,1,"도함수","DIFF.DERIVATIVE.DEF","도함수의 정의","f'(x)=lim_{h→0}(f(x+h)−f(x))/h",1),
 (4,1,"도함수의 성질","DIFF.RULES.POWER_LINEAR","도함수의 성질 ①② (xⁿ, 상수, 실수배·합차)","① (xⁿ)'=nxⁿ⁻¹, (c)'=0 ② {kf(x)}'=kf'(x), {f(x)±g(x)}'=f'(x)±g'(x)",2),
 (5,1,"곱의 미분법","DIFF.RULES.PRODUCT","곱의 미분법 (2개·3개·거듭제곱)","{f(x)g(x)}'=f'(x)g(x)+f(x)g'(x); {fgh}'=f'gh+fg'h+fgh'; [{f(x)}ⁿ]'=n{f(x)}ⁿ⁻¹f'(x)",3),
 (6,1,"접선의 방정식","DIFF.TANGENT.EQ_COMMON","① (a,f(a))에서의 접선 ② f, g의 x=a에서의 공통접선 조건","① y−f(a)=f'(a)(x−a) ② f(a)=g(a), f'(a)=g'(a)",2),
 (7,1,"평균값 정리","DIFF.MVT.ROLLE","① 평균값 정리 ② 롤의 정리","① f가 [a,b] 연속, (a,b) 미분가능 ⇒ (f(b)−f(a))/(b−a)=f'(c)인 c∈(a,b) 존재 ② 위 조건 + f(a)=f(b) ⇒ f'(c)=0인 c∈(a,b) 존재",2),
 (8,1,"증가와 감소","DIFF.MONOTONE.DERIV_COND","증가·감소 조건 ①~④","① 구간에서 증가하려면 f'(x)≥0 ② 감소하려면 f'(x)≤0 (다항함수) ③ f'(a)>0이면 x=a에서 증가 ④ f'(a)<0이면 x=a에서 감소",4),
 (9,2,"증가와 감소","DIFF.MONOTONE.ALWAYS_INVERSE","⑤ 항상 증가(감소)·역함수 존재·일대일대응·극값이 없다 (삼차함수)","모든 x에 대해 f'(x)≥0 (또는 ≤0); 삼차함수 f'(x)=0의 판별식 D≤0",1),
 (10,2,"극대와 극소","DIFF.EXTREMA.DEF_TEST","극대·극소의 정의 및 판정, 미분가능할 때 극값 필요조건","① x=a 근방에서 f(x)≤f(a)이면 극대; f'(x)가 +→−로 바뀌면 극대 ② f(x)≥f(a)이면 극소; f'(x)가 −→+로 바뀌면 극소 ③ f'(a)=0",3),
 (11,2,"극대와 극소","DIFF.EXTREMA.CUBIC_ROOT_COUNT","④ 삼차함수 극댓값×극솟값의 부호와 실근 개수","극댓값×극솟값>0: 실근 1개; =0: 서로 다른 실근 2개(중근 포함); <0: 서로 다른 실근 3개",3),
 (12,2,"함수의 그래프","DIFF.GRAPH.LEADING_COEFF_MULTIPLICITY","① 최고차항 계수 부호 ② (x−a)^홀수·(x−a)^짝수 인수의 그래프 모양","① +: 오른쪽 끝이 위로(→+∞), −: 오른쪽 끝이 아래로 ② 홀수: x=a에서 x축을 뚫고 지나감(3 이상이면 변곡) / 짝수: x=a에서 x축에 접함",4),
 (13,2,"최대와 최소","DIFF.MAXMIN.CLOSED_INTERVAL","닫힌구간에서의 최대·최소","[a,b]에서 극값과 양 끝값 f(a), f(b) 중 가장 큰 값이 최댓값, 가장 작은 값이 최솟값",1),
 (14,2,"속도와 가속도","DIFF.MOTION.POS_VEL_ACC","① 위치·속도·가속도 미분관계 ② 운동방향 바뀜·최고높이 ③ 지면 도달 ④ 두 물체 반대/같은 방향","① v=dx/dt, a=dv/dt ② v=0 (부호 변화) ③ x(t)=0(높이 0) ④ 반대방향: v₁v₂<0, 같은방향: v₁v₂>0",5)]
for q,pg,sm,tid,tn,a,ns in L: row(q,pg,sm,tid,tn,a,nsub=ns)
build("A00385", list(ROWS), 158); print(len(ROWS))
