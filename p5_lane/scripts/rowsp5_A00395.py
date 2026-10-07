import cfgex
from cfgp5 import *
D="서술형"
NOTE="기본개념 빈칸·그래프 워크시트(정답지 없음) — 독립 작성(sympy 검산)"
cfgex.ROWS.clear()
setup("A00395","1jPa79hYWipsM2DBkGpHJZcdtU0nMzCmw","수학2 시작 전 기본개념.hwpx","p5l/A00395/src.hwpx","자체 제작(공식 정리지)","2026","공식 확인 워크시트","고2","공통수학1·2",CURR="2022 개정",VIS="HWPX section0.xml 본문·수식 추출(로컬)",TEXT="HWPX section0.xml 본문·수식 추출(로컬)")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
def row(q,big,mid,small,tid,tname,ans,nsub=1,fig="없음",diff="하",fmt=D,atype="식"):
    R(q,1,big,mid,small,tid,tname,mid+";"+small,diff,fmt,ans,"그래프 그리기" if fig!="없음" else "공식 빈칸",NOTE,label=f"항목{q}",nsub=nsub,atype=atype,fig=fig)
    ROWS[-1].update({"출처대분류":"자체 제작 공식 정리 워크시트","학교/시험명":f"A00395 기본개념 항목{q}"})
G="그래프 작도(답안 그림)"
F=[("함수","일차함수","일차함수 그래프","FUNC.LINEAR.GRAPH_SKETCH","y=2x+1","기울기 2, y절편 1, x절편 −1/2인 직선(증가)"),
 ("함수","일차함수","일차함수 그래프","FUNC.LINEAR.GRAPH_SKETCH","y=−3x+5","기울기 −3, y절편 5, x절편 5/3인 직선(감소)"),
 ("함수","절댓값 함수","절댓값 그래프","FUNC.ABS.GRAPH_SKETCH","y=|x|","꼭짓점 (0,0)인 V자, x≥0에서 y=x, x<0에서 y=−x"),
 ("함수","이차함수","이차함수 그래프","FUNC.QUADRATIC.GRAPH_SKETCH","y=x²−3x+2","y=(x−3/2)²−1/4: 꼭짓점 (3/2, −1/4), 아래로 볼록, x절편 1, 2, y절편 2"),
 ("함수","이차함수","이차함수 그래프","FUNC.QUADRATIC.GRAPH_SKETCH","y=−2x²+4x−5","y=−2(x−1)²−3: 꼭짓점 (1, −3), 위로 볼록, x절편 없음, y절편 −5"),
 ("함수","가우스 함수","최대정수함수 그래프","FUNC.FLOOR.GRAPH_SKETCH","y=[x]","계단함수: n≤x<n+1에서 y=n (왼쪽 끝 채운 점, 오른쪽 끝 빈 점)"),
 ("함수","유리함수","유리함수 그래프","FUNC.RATIONAL.GRAPH_SKETCH","y=3/(x−5)+1","점근선 x=5, y=1; 1·3사분면형(k=3>0); x절편 2, y절편 2/5"),
 ("함수","유리함수","유리함수 그래프","FUNC.RATIONAL.GRAPH_SKETCH","y=−2/(x+3)+1","점근선 x=−3, y=1; 2·4사분면형(k=−2<0); x절편 −1, y절편 1/3"),
 ("함수","유리함수","유리함수 그래프","FUNC.RATIONAL.GRAPH_SKETCH","y=(2x+1)/(x−5)","y=11/(x−5)+2: 점근선 x=5, y=2; x절편 −1/2, y절편 −1/5"),
 ("함수","무리함수","무리함수 그래프","FUNC.IRRATIONAL.GRAPH_SKETCH","y=√x","정의역 x≥0, 치역 y≥0, 시작점 (0,0), 증가"),
 ("함수","무리함수","무리함수 그래프","FUNC.IRRATIONAL.GRAPH_SKETCH","y=−√(2x−1)+5","정의역 x≥1/2, 치역 y≤5, 시작점 (1/2, 5), 감소, x절편 13, y절편 없음"),
 ("함수","무리함수","무리함수 그래프","FUNC.IRRATIONAL.GRAPH_SKETCH","y=√(x+5)−3","정의역 x≥−5, 치역 y≥−3, 시작점 (−5, −3), 증가, x절편 4, y절편 √5−3")]
for i,(b,m,s,tid,f,a) in enumerate(F,1): row(i,b,m,s,tid,f"{f}의 그래프 그리기",a,fig=G,fmt="그래프 작도",atype="그래프")
row(13,"다항식","다항식의 연산","곱셈 공식","POLY.EXPANSION_FORMULA.RECALL","곱셈공식 1)2)3)6)7)8)9)10) 전개","1) a²+2ab+b² 2) a²−2ab+b² 3) a²−b² 6) a²+b²+c²+2ab+2bc+2ca 7) a³+3a²b+3ab²+b³ 8) a³−3a²b+3ab²−b³ 9) a³+b³ 10) a³−b³ ※원문 번호 4)·5) 누락(원문 그대로)",nsub=8)
row(14,"다항식","다항식의 연산","곱셈 공식의 변형","POLY.FORMULA_VARIANT.RECALL","곱셈공식 변형 a²+b², (a±b)², a³±b³","1) ① (a+b)²−2ab ② (a−b)²+2ab 2) (a−b)²+4ab 3) (a+b)²−4ab 4) (a+b)³−3ab(a+b) 5) (a−b)³+3ab(a−b)",nsub=6)
row(15,"도형의 방정식","평면좌표","두 점 사이의 거리","COORD.DISTANCE.TWO_POINTS","A(x₁,y₁), B(x₂,y₂) 사이의 거리","AB=√{(x₂−x₁)²+(y₂−y₁)²}")
row(16,"도형의 방정식","직선의 방정식","직선의 방정식","LINE.EQUATION.POINT_SLOPE_TWO_POINT","기울기·한 점, 두 점을 지나는 직선","① y−y₁=m(x−x₁) ② y−y₁=(y₂−y₁)/(x₂−x₁)·(x−x₁) (x₁≠x₂; x₁=x₂이면 x=x₁)",nsub=2)
row(17,"도형의 방정식","직선의 방정식","두 직선의 위치 관계","LINE.TWO_LINES.POSITION","y=mx+n, y=m'x+n'의 일치·평행·한 점·수직 조건","① m=m', n=n' ② m=m', n≠n' ③ m≠m' ④ mm'=−1",nsub=4)
row(18,"도형의 방정식","직선의 방정식","점과 직선 사이의 거리","LINE.POINT_LINE_DISTANCE","점 (x₁,y₁)과 직선 ax+by+c=0 사이의 거리","d=|ax₁+by₁+c|/√(a²+b²)")
build("A00395",list(ROWS),213); print(len(ROWS))
