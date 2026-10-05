from cfgex import *
MC, S_, D = "객관식(5지선다)", "단답형", "서술형"
M, H = "보통", "높음"
Q = [291]  # A00639 ch01-04 q=1..291
CH = "05 삼각함수"
def a(lab, page, src, small, tid, tname, diff, ans, chk, pts, fmt=MC, nsub=1, mid="삼각함수", tags="삼각함수", **kw):
    Q[0] += 1
    kw.setdefault("atype", "선택지" if fmt == MC else "값")
    R(Q[0], page, "삼각함수", mid, small, tid, tname, tags, diff, fmt, ans, src, chk, label="05-"+lab, pts=pts, nsub=nsub, **kw)
    r = ROWS[-1]; r.update({"출처대분류": "시판 기출문제집(전국연합학력평가 고2 재수록)", "학교명": "", "주관기관": "EBS(올림포스)",
        "학교/시험명": f"올림포스 전국연합학력평가 기출문제집 대수 {CH} {lab}", "메모": r["메모"].replace("P1 학교기출", "P1 시판 기출문제집(올림포스); 원출처 학평 고2 (OFFICIAL 근접중복 가능)")})
setup("A00639", "1c09Ezx8TegfVDXf--6ArRwp9hTP2vy53", "올림포스 기출 대수.pdf", "p3/A00639.pdf", "올림포스(EBS)", "2026학년도", "전국연합학력평가 기출문제집", "고2", "대수", CURR="2022 개정",
      VIS="스캔 PDF(텍스트층 없음) 95dpi 렌더 시각판독 PARTIAL p68~77 (05 삼각함수)", TEXT="텍스트층 없음 — 렌더 판독; 정답과 풀이 별책 미보유")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
RD = dict(mid="호도법과 부채꼴", tags="호도법;부채꼴;호의 길이;넓이")
DF = dict(mid="삼각함수의 정의", tags="삼각함수;동경;일반각")
RL = dict(mid="삼각함수 사이의 관계", tags="삼각함수;sin²+cos²=1;tan=sin/cos")
G = "개념 확인 문제"
a("개념01",69,G,"호도법","TRIG.RADIAN.CONVERT","육십분법↔호도법 6가지","하","(1) 3π/4 (2) −π/3 (3) 13π/3 (4) 120° (5) 315° (6) −18°","","",fmt=D,nsub=6,**RD)
a("개념02",69,G,"일반각","TRIG.GENERAL_ANGLE.QUADRANT","각의 사분면 6가지","하","(1) 제4 (2) 제2 (3) 제4 (4) 제2 (5) 제1 (6) 제3","","",fmt=D,nsub=6,**DF)
a("개념03",69,G,"부채꼴","TRIG.SECTOR.ARC_AREA","부채꼴 l, S 2가지","하","(1) l=π/4, S=π/16 (2) l=2π/9, S=π/27","","",fmt=D,nsub=2,**RD)
a("개념04",69,G,"부채꼴","TRIG.SECTOR.ANGLE_AREA","r=3, l=3π 중심각·넓이","하","θ=π, S=9π/2","","",fmt=D,nsub=2,**RD)
a("개념05",69,G,"부채꼴","TRIG.SECTOR.ARC_ANGLE_FROM_AREA","r, S로 l, θ 2가지","하","(1) l=9π, θ=3π/4 (2) l=4π, θ=π/6","","",fmt=D,nsub=2,**RD)
a("개념06",69,G,"부채꼴","TRIG.SECTOR.MAX_AREA_PERIMETER","둘레 52 부채꼴 넓이 최대 반지름·중심각","중하","r=13, θ=2","S=r(26−r)","",fmt=D,nsub=2,c=M,**RD)
a("개념07",69,G,"삼각함수의 정의","TRIG.SPECIAL_ANGLE.VALUES","특수각 sin, cos, tan 4가지","하","(1) 1/2, −√3/2, −√3/3 (2) −√3/2, 1/2, −√3 (3) −√2/2, −√2/2, 1 (4) 1/2, √3/2, √3/3","","",fmt=D,nsub=4,**DF)
a("개념08",69,G,"삼각함수의 정의","TRIG.DEF.POINT","P(5,−12) sin, cos, tan","하","(1) −12/13 (2) 5/13 (3) −12/5","","",fmt=D,nsub=3,**DF)
a("개념09",69,G,"삼각함수의 부호","TRIG.SIGN.QUADRANT","부호 조건 사분면 4가지","하","(1) 제3 (2) 제2 (3) 제2 또는 제4 (4) 제1 또는 제2","","",fmt=D,nsub=4,**DF)
a("개념10",69,G,"삼각함수 사이의 관계","TRIG.IDENTITY.FROM_COS","제3사분면 cos=−3/5, sin, tan","하","sin=−4/5, tan=4/3","","",fmt=D,nsub=2,**RL)
a("개념11",69,G,"삼각함수 사이의 관계","TRIG.IDENTITY.FROM_SIN","제4사분면 sin=−1/3, cos, tan","하","cos=2√2/3, tan=−√2/4","","",fmt=D,nsub=2,**RL)
a("개념12",69,G,"삼각함수 사이의 관계","TRIG.SUM_TO_PRODUCT.SQUARE","sin+cos=−1/2, sin·cos","하","−3/8","","",fmt=S_,**RL)
a("개념13",69,G,"삼각함수 사이의 관계","TRIG.CUBE_SUM.FROM_PRODUCT","sin·cos=1/2 (제1사분면), sin³+cos³","하","√2/2","s+c=√2","",fmt=S_,**RL)
S = {1:"2025.9 고2 6",2:"2024.9 고2 7",3:"2024.6 고2 3",4:"2023.11 고2 23",5:"2024.10 고2 23",6:"2023.9 고2 23",7:"2023.6 고2 3",8:"2022.6 고2 3",9:"2025.6 고2 3",10:"2022.9 고2 7",
11:"2019.11 고2 가형 10",12:"2022.11 고2 25",13:"2021.9 고2 13",14:"2020.6 고2 18",15:"2019.6 고2 가형 17",16:"2025.6 고2 26",17:"2024.10 고2 13",18:"2022.11 고2 13",19:"2024.6 고2 15",20:"2023.6 고2 17",
21:"2019.11 고2 나형 15",22:"2025.9 고2 4",23:"2024.6 고2 7",24:"2024.9 고2 4",25:"2025.6 고2 7",26:"2023.6 고2 9",27:"2023.9 고2 6",28:"2021.9 고2 6",29:"2020.6 고2 24",30:"2025.6 고2 13",31:"2021.11 고2 16"}
PG = {}
for p, rg in [(70,range(1,6)),(71,range(6,12)),(72,range(12,15)),(73,range(15,18)),(74,range(18,22)),(75,range(22,27)),(76,range(27,32))]:
    for i in rg: PG[i] = p
def b(n, small, tid, tname, diff, ans, chk, pts, fmt=MC, **kw):
    a(f"{n:02d}", PG[n], f"학평 {S[n]}번 (26456-{n+241:04d})", small, tid, tname, diff, ans, chk, pts, fmt, **kw)
b(1,"부채꼴","TRIG.SECTOR.ANGLE_FROM_AREA","r=6, S=15π 중심각","하","⑤ (5π/6)","","3",**RD)
b(2,"부채꼴","TRIG.SECTOR.ARC_FROM_AREA_ANGLE","θ=π/4, S=18π 호의 길이","하","② (3π)","r=12","3",**RD)
b(3,"부채꼴","TRIG.SECTOR.RADIUS_FROM_ARC","θ=3π/4, l=2π/3 반지름","하","⑤ (8/9)","","2",**RD)
b(4,"부채꼴","TRIG.SECTOR.RADIUS_FROM_ARC","θ=4π/5, l=12π 반지름","하","15","","3",S_,**RD)
b(5,"부채꼴","TRIG.SECTOR.ARC_FROM_AREA","r=8, S=28π, l=aπ","하","7","","3",S_,**RD)
b(6,"부채꼴","TRIG.SECTOR.RADIUS_FROM_ARC_AREA","l=2π, S=6π 반지름","하","6","","3",S_,**RD)
b(7,"부채꼴","TRIG.SECTOR.AREA","r=4, θ=5π/12 넓이","하","① (10π/3)","","2",**RD)
b(8,"부채꼴","TRIG.SECTOR.ANGLE_FROM_ARC","r=6, l=4π 중심각","하","④ (2π/3)","","2",**RD)
b(9,"부채꼴","TRIG.SECTOR.ANGLE_FROM_AREA","r=2, S=π/3 중심각","하","④ (π/6)","","2",**RD)
b(10,"부채꼴","TRIG.SECTOR.AREA_FROM_ARC_ANGLE","θ=π/6, l=π 넓이","하","③ (3π)","r=6","3",**RD)
b(11,"부채꼴","TRIG.SECTOR.TRIANGLE_AREA","θ=π/3, l=π 삼각형 OAB 넓이","하","② (9√3/4)","r=3","3",fig="도형",**RD)
b(12,"부채꼴","TRIG.SEMICIRCLE.SECTOR_SPLIT","반원 호 AC=π, 부채꼴 OBC=15π, OA","중하","6","r²−r−30=0","3",S_,fig="도형",c=M,**RD)
b(13,"일반각","TRIG.COTERMINAL.SECTOR_AREA","θ와 8θ 동경 일치 (0<θ<π/2), r=2 넓이","중하","③ (4π/7)","7θ=2π","3",c=M,**RD)
b(14,"부채꼴","TRIG.SECTOR_IN_TRIANGLE.FILL_BLANK","이등변삼각형 OAB, 반원, 부채꼴 MPQ 넓이 과정","중","④ (1/6)","f=sin(θ/2), g=θ, h=π−2θ","4",fig="도형",c=M,**RD)
b(15,"부채꼴","TRIG.SECTOR.INSCRIBED_SEMICIRCLE","r=4, θ=π/6 부채꼴, 내접 반원 S₁−S₂","중","④ (4π/9)","반원 반지름 4/3","4",fig="도형",c=M,**RD)
b(16,"삼각함수의 정의","TRIG.DEF.REFLECT_YX","A와 y=x 대칭 B, cosα·sinβ=1/3, k²","중하","2","1/(k²+1)=1/3","4",S_,c=M,**DF)
b(17,"일반각","TRIG.COTERMINAL.LINE_POINT","y=x+1 위 P, θ와 7θ 동경 일치, P x좌표","중하","⑤ ((√3+1)/2)","θ=π/3","3",c=M,**DF)
b(18,"삼각함수의 정의","TRIG.DEF.TAN_SUM_ZERO","P(a,b), Q(a²,−2b²), tanθ₁+tanθ₂=0, sinθ₁","하","② (√5/5)","b/a=1/2","3",**DF)
b(19,"삼각함수의 정의","TRIG.DEF.CIRCLE_LINE","원 x²+y²=r²과 x=−2, 2cosα=3sinβ, r(sinα+cosβ)","중","③ (−2/3)","√(r²−4)=4/3","4",c=M,**DF)
b(20,"삼각함수의 정의","TRIG.DEF.CURVE_POINT","y=√x 위 P, cos²θ−2sin²θ=−1, OP","중하","③ (√3/2)","tan²θ=2 → t=1/2","4",c=M,**DF)
b(21,"삼각함수의 정의","TRIG.DEF.TWO_CIRCLES","y=2와 두 원 제2사분면 교점, sinα·cosβ","중하","⑤ (−2/3)","A(−1,2), B(−√5,2)","4",fig="그래프",c=M,**DF)
b(22,"삼각함수 사이의 관계","TRIG.IDENTITY.FROM_COS","제4사분면 cos=1/3, tan","하","① (−2√2)","","3",**RL)
b(23,"삼각함수 사이의 관계","TRIG.IDENTITY.FROM_COS","제2사분면 cos=−3/4, sin","하","⑤ (√7/4)","","3",**RL)
b(24,"삼각함수 사이의 관계","TRIG.IDENTITY.FROM_RATIO","제2사분면 sin=−3cos, cos","하","③ (−√10/10)","","3",**RL)
b(25,"삼각함수 사이의 관계","TRIG.IDENTITY.SIMPLIFY_EQ","cos/tan+sin=√3, cos (제2사분면)","하","① (−√6/3)","1/sin=√3","3",**RL)
b(26,"삼각함수 사이의 관계","TRIG.IDENTITY.FROM_SIN","제3사분면 sin=−1/3, tan","하","④ (√2/4)","","3",**RL)
b(27,"삼각함수 사이의 관계","TRIG.IDENTITY.FROM_TAN","제3사분면 tan=2, cos","하","② (−√5/5)","","3",**RL)
b(28,"삼각함수 사이의 관계","TRIG.IDENTITY.COS_TAN","cos·tan=3/5 (제1사분면), cos","하","④ (4/5)","sin=3/5","3",**RL)
b(29,"삼각함수 사이의 관계","TRIG.IDENTITY.SQUARE_EQ","2cos²−sin²=1, 60sin²","하","20","sin²=1/3","3",S_,**RL)
b(30,"삼각함수 사이의 관계","TRIG.IDENTITY.VIETA_ROOTS","5x²+x+k=0 두 근 sint, cost, k·tant","중하","② (9/5)","k=−12/5, sin=3/5, cos=−4/5","3",c=M,**RL)
b(31,"삼각함수 사이의 관계","TRIG.IDENTITY.FOURTH_POWER","sin⁴+cos⁴=23/32 (제2사분면), sin−cos","중하","⑤ (√7/2)","sc=−3/8","4",c=M,**RL)
a("도전01",77,"학평 2019.9 고2 나형 29번 (26456-0273)","부채꼴","TRIG.TWO_CIRCLES.COMMON_AREA","원 O₁(r=6), AB=6√2, 정삼각형 외접원 O₂, 공통부분 p+q√3+rπ","상","13","O₂ 큰 활꼴 16π+6√3 + O₁ 작은 활꼴 9π−18 → p=−18, q=6, r=25","4",fmt=S_,c=H,i=H,fig="도형",**RD)
a("도전02",77,"학평 2019.9 고2 나형 20번 (26456-0274)","부채꼴","TRIG.SECTOR.INSCRIBED_CIRCLE_RADII","cos∠BAP=4/5, r₁(부채꼴 OBP 내접), r₂, r₁r₂","상","① (3/40)","r₁=sinα/(1+sinα)=3/8, r₂=(1−3/5)/2=1/5","4",c=H,i=H,fig="도형",**RD)
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{781+i}", ROWS[i*10:(i+1)*10], 16046+i*10)
