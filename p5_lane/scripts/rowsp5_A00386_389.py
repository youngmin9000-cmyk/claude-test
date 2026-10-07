import cfgex
from cfgp5 import *
D="서술형"
NOTE_B="공식 빈칸 워크시트(정답지 없음) — 표준 공식으로 독립 작성"
NOTE_F="개념·공식 정리 자료(빈칸 아님, 문항 아님) — 원문 기재 내용을 독립 검증"
REF=dict(ready="REVIEW", status="원문 기재 내용 독립 검증 일치(개념정리 자료)", trust="중간(원문 추출+독립검증; 문항형 아님)", review="REVIEW-개념정리자료(문항 아님)")
def src(QID,SRC,FN,PATH,SUBJ,GRADE,VIS):
    cfgex.ROWS.clear()
    setup(QID,SRC,FN,PATH,"자체 제작(공식 정리지)","2026","공식 확인 워크시트",GRADE,SUBJ,CURR="2022 개정",VIS=VIS,TEXT=VIS)
    builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
def row(q,page,big,mid,small,tid,tname,ans,nsub=1,note=NOTE_B,diff="하",fig="없음",extra=None,**kw):
    R(q,page,big,mid,small,tid,tname,mid+";"+small,diff,D,ans,"공식 빈칸" if note==NOTE_B else "개념 정리",note,label=f"항목{q}",nsub=nsub,atype="식",fig=fig,**kw)
    ROWS[-1].update({"출처대분류":"자체 제작 공식 정리 워크시트","학교/시험명":f"{cfgex.P['QID']} 공식 확인 항목{q}"})
cum=172
# ---- A00386 중1 공식정리 서브노트 (filled concept summary, 17 chapters)
src("A00386","1zIqZM7aJi9YV5tUMHLJXXvtT-MVfctVX","중1 공식정리 서브노트.hwp","p5l/A00386/src.hwp","중1 수학","중1","HWP 본문·수식 추출(로컬 파서), 도형 그림은 gso 객체(텍스트 없음)")
C=[("수와 연산","소인수분해","자연수의 성질","NUM.PRIME_FACTOR.CONCEPT_SUMMARY","소수·합성수, 소인수분해, 약수 개수 (m+1)(n+1), 제곱수 조건, 최대공약수·최소공배수 및 활용",7,""),
 ("수와 연산","정수와 유리수","정수와 유리수","NUM.INTEGER_RATIONAL.CONCEPT_SUMMARY","부호, 정수, 유리수(a/b, b≠0) 분류, 절댓값, 부등호, 수의 대소",6,""),
 ("수와 연산","정수와 유리수의 계산","수의 사칙계산","NUM.RATIONAL_OPS.CONCEPT_SUMMARY","유리수 덧셈·뺄셈·곱셈·나눗셈 부호규칙, 교환·결합·분배법칙, 혼합계산 순서",8,""),
 ("변화와 관계","문자와 식","문자와 식","ALG.EXPR.CONCEPT_SUMMARY","곱셈·나눗셈 기호 생략 규칙, 식의 값, 항·계수·차수·동류항, 일차식 계산",8,"원문 [5] 항목 번호 (7) 중복(동류항) — 표기 오류만, 내용 이상 없음"),
 ("변화와 관계","일차방정식","등식의 성질","ALG.EQUALITY.CONCEPT_SUMMARY","등식·항등식·방정식, 등식의 성질 4가지(c≠0 나눗셈)",5,""),
 ("변화와 관계","일차방정식","일차방정식","ALG.LINEAR_EQ.CONCEPT_SUMMARY","이항, 풀이 절차, 0·x=0(해 무수), 0·x=k≠0(해 없음), 활용(연속 정수, 10a+b, 시간=거리/속력, 소금=농도/100×소금물)",6,""),
 ("변화와 관계","좌표평면과 그래프","비례와 함수","FUNC.PROPORTION.CONCEPT_SUMMARY","정비례 y=ax, 반비례 y=a/x (a≠0), 함수·함숫값·정의역·공역·치역",5,"원문 [5](2) 공역 정의 '변수 y가 취하는 모든 값의 집합'은 부정확(그것은 치역; 공역은 y값이 속하는 집합) — REVIEW"),
 ("변화와 관계","좌표평면과 그래프","함수의 그래프와 활용","FUNC.GRAPH.CONCEPT_SUMMARY","좌표·사분면 부호, y=ax(원점 지나는 직선, a>0이면 1·3사분면, |a| 클수록 y축에 가까움), y=a/x(쌍곡선), 활용 절차",7,""),
 ("자료와 가능성","자료의 정리와 해석","도수분포와 그래프","STAT.FREQ_DIST.CONCEPT_SUMMARY","변량·계급·도수, 계급값, 히스토그램, 도수분포다각형(넓이 동일), 평균=Σ(계급값×도수)/Σ도수",5,""),
 ("자료와 가능성","자료의 정리와 해석","상대도수와 누적도수","STAT.REL_CUM_FREQ.CONCEPT_SUMMARY","상대도수=도수/전체(합 1), 누적도수, 분포표와 그래프",4,""),
 ("도형과 측정","기본 도형","기본 도형","GEO.BASIC.CONCEPT_SUMMARY","점·선·면, 직선의 결정, 두 점 사이 거리·중점, 각의 분류, 맞꼭지각, 수직·수선, 평행, 동위각·엇각과 평행선",9,"원문 번호 [3] 누락([2]→[4]); 직선·반직선·선분 정의 칸이 그림(gso)으로만 표시되어 텍스트 공란 — 그림 판독 필요"),
 ("도형과 측정","기본 도형","위치 관계","GEO.POSITION.CONCEPT_SUMMARY","점과 직선, 평면/공간 두 직선(꼬인 위치), 평면의 결정 조건 4가지, 직선과 평면, 두 평면",6,""),
 ("도형과 측정","작도와 합동","작도와 합동","GEO.CONSTRUCTION_CONGRUENCE.CONCEPT_SUMMARY","작도(눈금 없는 자·컴퍼스), 각 이등분선·수직이등분선·같은 각 작도, 삼각형 결정조건, 삼각형 변 조건, SSS·SAS·ASA",9,""),
 ("도형과 측정","평면도형의 성질","평면도형의 성질","GEO.POLYGON_CIRCLE.CONCEPT_SUMMARY","다각형·대각선 n−3, n(n−3)/2, 원·호·현·활꼴·부채꼴, 중심각과 호(비례)·현(비례 아님), 원과 직선 d<r/d=r/d>r, 접선⊥반지름",6,""),
 ("도형과 측정","입체도형의 성질","입체도형의 성질","GEO.SOLID.CONCEPT_SUMMARY","다면체, n각기둥(면 n+2, 꼭짓점 2n, 모서리 3n), n각뿔(n+1, n+1, 2n), n각뿔대(n+2, 2n, 3n), 정다면체 5종 표, 회전체 성질",6,""),
 ("도형과 측정","평면도형의 측정","평면도형의 측정","GEO.ANGLE_SECTOR.CONCEPT_SUMMARY","삼각형 내각 합 180°, 외각=이웃하지 않은 두 내각의 합, 내각 합 180°(n−2), 외각 합 360°, 원주 2πr, 넓이 πr², 호 2πr·a/360, 부채꼴 πr²·a/360=½rl",4,""),
 ("도형과 측정","입체도형의 측정","입체도형의 측정","GEO.SOLID_MEASURE.CONCEPT_SUMMARY","기둥 겉넓이 2×밑넓이+옆넓이, 원기둥 2πr²+2πrh, V=πr²h, 뿔 겉넓이 밑넓이+옆넓이, 원뿔 πr²+πrl, V=⅓πr²h, 구 S=4πr², V=4/3πr³",5,"")]
for i,(big,mid,sm,tid,a,ns,iss) in enumerate(C,1):
    kw=dict(REF)
    if iss: kw["review"]="REVIEW-원문표기확인"
    row(i,1,big,mid,sm,tid,f"중1 개념정리 {i:02d}. {sm}",a+(" ※"+iss if iss else ""),nsub=ns,note=NOTE_F,fig="그림 포함(gso)" if i==11 else "없음",**kw)
build("A00386",list(ROWS),cum); cum+=len(ROWS); n386=len(ROWS)
# ---- A00387 중1 공식 (filled tables; starts at section 3)
src("A00387","1rBhyjhwRBhZgT5qMyH1F4todOc52naEX","중1 공식.hwp","p5l/A00387/src.hwp","중1 수학","중1","HWP 본문·표 추출(로컬 파서) — 문서는 '3. 평면도형 공식'부터 시작(1·2절 없음)")
L=[("평면도형의 성질","다각형·원·부채꼴 공식","GEO.POLYGON_SECTOR.FORMULA_TABLE","평면도형 공식표(대각선·내각·외각·원·부채꼴)","n각형 꼭짓점 n; 한 꼭짓점 대각선 n−3; 대각선 총수 n(n−3)/2; 삼각형 개수 n−2; 내각 합 180°(n−2); 정n각형 한 내각 180°(n−2)/n; 외각 합 360°; 한 외각 360°/n; 원주 2πr; 원 넓이 πr²; 호 2πr·x/360; 부채꼴 πr²·x/360=½rl",14),
 ("입체도형의 성질","정다면체","GEO.REGULAR_POLYHEDRA.TABLE","정다면체 조건 및 면·꼭짓점·모서리 표","조건: 면이 모두 합동인 정다각형, 각 꼭짓점에 모인 면 수 동일; 정사면체(정삼각형,3,F4,V4,E6) 정육면체(정사각형,3,6,8,12) 정팔면체(정삼각형,4,8,6,12) 정십이면체(정오각형,3,12,20,30) 정이십면체(정삼각형,5,20,12,30) — 오일러 V−E+F=2 전부 성립",6),
 ("입체도형의 성질","회전체","GEO.SOLID_REVOLUTION.TABLE","회전체(원기둥·원뿔·원뿔대·구) 회전 전 도형과 단면","회전 전: 직사각형/직각삼각형/사다리꼴/반원; 축에 수직 단면: 모두 원; 축 포함 단면: 직사각형/이등변삼각형/사다리꼴(등변)/원",3),
 ("입체도형의 측정","겉넓이와 부피","GEO.SOLID_MEASURE.FORMULA_TABLE","기둥·뿔·구의 겉넓이와 부피","기둥: 겉넓이 밑넓이×2+옆넓이, 부피 밑넓이×높이; 뿔: 겉넓이 밑넓이+옆넓이, 부피 ⅓×밑넓이×높이; 구: S=4πr², V=4/3πr³",3)]
for i,(mid,sm,tid,tn,a,ns) in enumerate(L,1): row(i,1,"도형과 측정",mid,sm,tid,tn,a,nsub=ns,note=NOTE_F,**REF)
build("A00387",list(ROWS),cum); cum+=len(ROWS); n387=len(ROWS)
# ---- A00388 함수의 극한과 연속 (blank worksheet, 3p)
src("A00388","1DNnndhTc2A17s9m2PXgLunA9OOUil7yQ","함수의 극한과 연속 (1).pdf","p5l/A00388/src.pdf","수학Ⅱ","고2","텍스트층 PDF 3쪽 (FULL_TEXT_SAFE, 렌더 확인)")
B=("함수의 극한과 연속",)
J="판정 필요(항상 연속 아님)"
L=[(1,"함수의 극한","LIMIT.EXISTENCE.ONE_SIDED","극한값 존재 조건","lim_{x→a+}f(x)=lim_{x→a−}f(x)=α ⇔ lim_{x→a}f(x)=α",1),
 (1,"함수의 극한의 성질","LIMIT.ALGEBRA.RULES","극한의 성질(lim f=α, lim g=β)","① α±β ② αβ ③ α/β (β≠0) ④ cα",4),
 (1,"함수의 극한 계산","LIMIT.EVAL.FORMS","극한 계산 x→a, x→∞, x→−∞, 그 외","① 0/0꼴: 인수분해·유리화 후 약분 ② ∞/∞꼴: 최고차항으로 나눔(분모 차수 큼→0, 같음→최고차항 계수비, 분자 큼→발산) ③ x→−∞: x=−t 치환 ④ ∞−∞꼴: 유리화/통분",4),
 (1,"함수의 극한의 대소 관계","LIMIT.SQUEEZE.ORDER","극한의 대소관계와 조임정리","① f(x)<g(x)이면 lim f ≤ lim g ② f<h<g, lim f=lim g=α이면 lim h=α",2),
 (1,"함수의 연속","CONT.DEF.THREE_COND","x=a에서 연속의 세 조건","① f(a) 정의 ② lim_{x→a}f(x) 존재 ③ lim_{x→a}f(x)=f(a)",3),
 (2,"연속함수의 성질","CONT.ALGEBRA.EVERYWHERE","f, g가 실수 전체에서 연속일 때 f±g, fg, f/g, cf, f∘g","① 연속 ② 연속 ③ g(x)≠0인 x에서 연속 ④ 연속 ⑤ 연속",5),
 (2,"연속함수의 성질","CONT.ALGEBRA.AT_POINT","f, g가 x=a에서 연속일 때 x=a에서의 연속","① 연속 ② 연속 ③ g(a)≠0이면 연속 ④ 연속 ⑤ f∘g는 g가 a에서, f가 g(a)에서 연속이면 연속(f가 g(a)에서 연속이 아니면 "+J+")",5),
 (2,"연속함수의 성질","CONT.ALGEBRA.ONE_DISCONT","f는 x=a에서 연속, g는 x≠a에서만 연속(x=a 불연속)일 때 x=a에서의 연속","① f±g 불연속 ② fg "+J+"(f(a)=0이면 연속 가능) ③ f/g "+J+" ④ cg: c=0이면 연속, c≠0이면 불연속 ⑤ f∘g "+J,5),
 (2,"연속함수의 성질","CONT.ALGEBRA.BOTH_DISCONT","f, g 모두 x=a에서 불연속일 때 x=a에서의 연속","① f±g "+J+" ② fg "+J+" ③ f/g "+J+" ④ f∘g "+J+" (좌·우극한과 함숫값을 직접 계산)",4),
 (3,"함수의 연속","CONT.INTERVAL.FUNC_TYPES","다항·유리·무리·절댓값 함수의 연속 구간","① 다항함수: 실수 전체 ② 유리함수: 분모≠0인 실수 전체 ③ 무리함수 √(g(x)): g(x)≥0인 범위 ④ |f(x)|: f가 연속인 범위",4),
 (3,"함수의 연속","CONT.EXTREME_VALUE_THM","최대·최소 정리","f가 닫힌구간 [a,b]에서 연속이면 f는 [a,b]에서 반드시 최댓값과 최솟값을 가진다",1),
 (3,"함수의 연속","CONT.IVT","사잇값 정리","f가 [a,b]에서 연속이고 f(a)≠f(b)이면 f(a)와 f(b) 사이의 임의의 k에 대해 f(c)=k인 c가 (a,b)에 적어도 하나 존재(f(a)f(b)<0이면 (a,b)에 실근 존재)",1)]
for i,(pg,sm,tid,tn,a,ns) in enumerate(L,1):
    kw={}
    if i==8: a+=" ※원문 2쪽에 '연속 성질(2)' 제목 중복 표기"
    row(i,pg,B[0],sm.split()[0] if False else "함수의 극한과 연속",sm,tid,tn,a,nsub=ns,diff="중" if i in (8,9) else "하")
build("A00388",list(ROWS),cum); cum+=len(ROWS); n388=len(ROWS)
# ---- A00389 다항함수의 적분법 (blank worksheet, 2p)
src("A00389","1Nu2RFIK3Zibk80-gsW2N3jG1IOC17ldt","다항함수의 적분법.pdf","p5l/A00389/src.pdf","수학Ⅱ","고2","텍스트층 PDF 2쪽 (FULL_TEXT_SAFE, 렌더 확인)")
L=[(1,"부정적분","INTEG.INDEFINITE.DEF_POWER","부정적분 정의, ∫xⁿdx","① F'(x)=f(x)일 때 ∫f(x)dx=F(x)+C ② ∫xⁿdx=xⁿ⁺¹/(n+1)+C (n≠−1)",2,None),
 (1,"부정적분","INTEG.INDEFINITE.LINEARITY","부정적분의 성질","① ∫{f±g}dx=∫f dx±∫g dx ② ∫cf dx=c∫f dx (c≠0)",2,None),
 (1,"부정적분","INTEG.INDEFINITE.DERIV_RELATION","부정적분과 미분의 관계","① d/dx(∫f(x)dx)=f(x) ② ∫(d/dx f(x))dx=f(x)+C",2,None),
 (1,"정적분","INTEG.DEFINITE.FTC_EVAL","정적분 계산","∫_a^b f(x)dx=[F(x)]_a^b=F(b)−F(a)",1,None),
 (1,"정적분","INTEG.DEFINITE.PROPERTIES","정적분의 성질 ①~⑥","① ∫_a^b f dx±∫_a^b g dx ② c∫_a^b f dx ③ ∫_a^b f dx ④ 0 ⑤ f 우함수: 2∫_0^a f dx, f 기함수: 0 ⑥ −∫_b^a f dx",6,None),
 (1,"정적분","INTEG.DEFINITE.DERIV_OF_INTEGRAL","정적분으로 정의된 함수의 미분·극한 ①~⑤","① f(x) ② f(x+a)−f(x) ③ ∫_a^x f(t)dt+xf(x) ④ f(a) ⑤ 원문 'lim_{x→a}(1/x)∫_a^{x+a}f(t)dt' — 의도(x→0)라면 f(a); 원문 그대로(x→a, a≠0)면 (1/a)∫_a^{2a}f(t)dt",5,"⑤ 극한 기호 x→a는 x→0의 오기로 의심(원문 보존, 판정 보류)"),
 (2,"정적분의 활용","INTEG.AREA.FORMULAS","넓이: f와 x축, f와 g 사이, 이차·삼차 넓이 공식","① ∫_a^b|f(x)|dx ② ∫_a^b|f(x)−g(x)|dx ③ y=a(x−α)(x−β)와 x축: |a|(β−α)³/6 ④ y=a(x−α)²(x−β)와 x축: |a|(β−α)⁴/12",4,None),
 (2,"정적분의 활용","INTEG.MOTION.POSITION_DISTANCE","속도와 위치: 위치, 위치 변화량, 거리","① x(a)=x₀+∫_0^a v(t)dt ② t=a~b 위치 변화량 ∫_a^b v(t)dt ③ 거리 ∫_a^b|v(t)|dt",3,None)]
for i,(pg,sm,tid,tn,a,ns,hold) in enumerate(L,1):
    kw={}
    if hold: kw=dict(ready="HOLD",review="HOLD-원문오기의심",status="독립풀이(정답지 미연결)·원문 오기 의심")
    row(i,pg,"적분","다항함수의 적분법",sm,tid,tn,a+((" ※"+hold) if hold else ""),nsub=ns,diff="중" if i in (5,6,7) else "하",**kw)
build("A00389",list(ROWS),cum); cum+=len(ROWS); n389=len(ROWS)
print(n386,n387,n388,n389,cum)
