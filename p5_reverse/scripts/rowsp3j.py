from cfgex import *
MC, S_, D = "객관식(5지선다)", "단답형", "서술형"
M, H = "보통", "높음"
FG = "도형"
Q = [396]  # A00639 ch01-06 q=1..396
CH = "07 삼각함수의 활용"
def a(lab, page, src, small, tid, tname, diff, ans, chk, pts, fmt=MC, nsub=1, mid="사인법칙과 코사인법칙", tags="사인법칙;코사인법칙;삼각형의 넓이", **kw):
    Q[0] += 1
    kw.setdefault("atype", "선택지" if fmt == MC else "값")
    R(Q[0], page, "삼각함수", mid, small, tid, tname, tags, diff, fmt, ans, src, chk, label="07-"+lab, pts=pts, nsub=nsub, **kw)
    r = ROWS[-1]; r.update({"출처대분류": "시판 기출문제집(전국연합학력평가 고2 재수록)", "학교명": "", "주관기관": "EBS(올림포스)",
        "학교/시험명": f"올림포스 전국연합학력평가 기출문제집 대수 {CH} {lab}", "메모": r["메모"].replace("P1 학교기출", "P1 시판 기출문제집(올림포스); 원출처 학평 고2 (OFFICIAL 근접중복 가능)")})
setup("A00639", "1c09Ezx8TegfVDXf--6ArRwp9hTP2vy53", "올림포스 기출 대수.pdf", "p3/A00639.pdf", "올림포스(EBS)", "2026학년도", "전국연합학력평가 기출문제집", "고2", "대수", CURR="2022 개정",
      VIS="스캔 PDF(텍스트층 없음) 95dpi 렌더 시각판독 PARTIAL p92~105 (07 삼각함수의 활용)", TEXT="텍스트층 없음 — 렌더 판독; 정답과 풀이 별책 미보유")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
G = "개념 확인 문제"
a("개념01",93,G,"사인법칙","SINE_LAW.CIRCUMRADIUS_SIDE","A=60°, B=45°, b=6√2, R과 a","하","R=6, a=6√3","","",fmt=D,nsub=2)
a("개념02",93,G,"사인법칙","SINE_LAW.CIRCUMRADIUS_SIDE","A=30°, C=60°, a=2, R과 c","하","R=2, c=2√3","","",fmt=D,nsub=2)
a("개념03",93,G,"사인법칙","SINE_LAW.CIRCUMRADIUS_SIDE","B=30°, C=45°, c=6, R과 b","하","R=3√2, b=3√2","","",fmt=D,nsub=2)
a("개념04",93,G,"사인법칙","SINE_LAW.TRIANGLE_SHAPE","삼각형 모양 판별 4가지","하","(1) a=b 이등변삼각형 (2) C=90° 직각삼각형 (3) A=90° 직각삼각형 (4) C=90° 직각삼각형","","",fmt=D,nsub=4)
a("개념05",93,G,"코사인법칙","COSINE_LAW.SIDE_ANGLE","변·각 4가지","하","(1) √13 (2) √3 (3) 120° (4) 135°","","",fmt=D,nsub=4)
a("개념06",93,G,"삼각형의 넓이","TRIANGLE_AREA.SAS","넓이·각 4가지","하","(1) 5√3 (2) 2√3 (3) π/6 (4) π/3","","",fmt=D,nsub=4)
a("개념07",93,G,"사인법칙","SINE_LAW.AMBIGUOUS_OBTUSE","A=30°, a=6, b=6√3, B 둔각, sinBcosC","하","3/4","B=120°, C=30°","",fmt=S_,trap=M)
a("개념08",93,G,"삼각형의 넓이","TRIANGLE_AREA.HERON","세 변 5, 7, 8 넓이","하","10√3","","",fmt=S_)
a("개념09",93,G,"사각형의 넓이","QUAD_AREA.PARALLELOGRAM","AB=2, AD=3, A=120° 평행사변형 넓이","하","3√3","","",fmt=S_)
a("개념10",93,G,"사각형의 넓이","QUAD_AREA.PARALLELOGRAM_COS","넓이 5, AB=2, AD=3, cos B","하","√11/6","sinB=5/6","",fmt=S_)
a("개념11",93,G,"삼각형의 넓이","TRIANGLE_AREA.ANGLE_BISECTOR","AB=3, AC=4, A=π/3 이등분선 AD","중하","12√3/7","넓이 분할","",fmt=S_,c=M)
S = {1:"2025.6 고2 6",2:"2024.6 고2 6",3:"2019.9 고2 가형 7",4:"2019.9 고2 나형 12",5:"2023.6 고2 11",6:"2019.11 고2 가형 28",7:"2023.6 고2 6",8:"2019.11 고2 나형 10",9:"2022.9 고2 9",10:"2025.6 고2 29",
11:"2024.6 고2 20",12:"2020.9 고2 27",13:"2024.10 고2 19",14:"2020.9 고2 10",15:"2024.9 고2 27",16:"2024.6 고2 29",17:"2023.9 고2 28",18:"2022.9 고2 14",19:"2023.9 고2 10",20:"2025.9 고2 25",
21:"2025.6 고2 12",22:"2021.9 고2 9",23:"2024.6 고2 16",24:"2022.6 고2 16",25:"2023.11 고2 18",26:"2023.6 고2 19",27:"2022.9 고2 20",28:"2021.9 고2 19"}
PG = {}
for p, rg in [(94,range(1,5)),(95,range(5,8)),(96,range(8,11)),(97,range(11,13)),(98,range(13,16)),(99,range(16,19)),(100,range(19,22)),(101,range(22,25)),(102,range(25,27)),(103,range(27,29))]:
    for i in rg: PG[i] = p
def b(n, small, tid, tname, diff, ans, chk, pts, fmt=MC, **kw):
    a(f"{n:02d}", PG[n], f"학평 {S[n]}번 (26456-{n+323:04d})", small, tid, tname, diff, ans, chk, pts, fmt, **kw)
b(1,"사인법칙","SINE_LAW.SIDE","BC=5, A=π/6, B=π/4, AC","하","② (5√2)","","3")
b(2,"사인법칙","SINE_LAW.SIDE_FROM_R","R=6, sinA=1/4, BC","하","③ (3)","","3")
b(3,"사인법칙","SINE_LAW.SIDE_FROM_R","R=5, ∠BAC=π/4, BC","하","⑤ (5√2)","","3")
b(4,"사인법칙","SINE_LAW.CIRCUMRADIUS","BC=5, ∠BAC=π/6, R","하","⑤ (5)","","3")
b(5,"사인법칙","SINE_LAW.PERIMETER_SUM","R=4, 둘레 12, sinA+sinB+sin(A+B)","하","① (3/2)","12/(2R)","3")
b(6,"사인법칙","CYCLIC_QUAD.AREA","R=6, AB=CD=3√3, BD=8√2, S²/13","중상","192","좌표 수치 확인","4",S_,fig=FG,c=M,i=M)
b(7,"코사인법칙","COSINE_LAW.SIDE","AB=3, AC=6, cosA=5/9, BC","하","③ (5)","","3",fig=FG)
b(8,"코사인법칙","COSINE_LAW.ANGLE","AB=4, BC=5, CA=√11, cos∠ABC","하","② (3/4)","","3")
b(9,"코사인법칙","COSINE_LAW.SIDE_FROM_SIN","AB=3, BC=6, sinθ=2√14/9, AC","하","④ (5)","cosθ=5/9","3",fig=FG)
b(10,"코사인법칙","COSINE_LAW.STEWART_POWER","AB=4, AC=5, cosA=1/8, BD:DC=1:2, E, F, FC","중상","45","AD=√11, cos∠BAD=23/(8√11), FC=23√11/22","4",S_,fig=FG,c=M,i=M)
b(11,"코사인법칙","COSINE_LAW.SEMICIRCLE_CHORDS","반원 C, D, E, DE=EB, CD:DE=1:√2, ∠COE=π/2, cos∠OBE","중","④ (√5/5)","tan(β/2)=1/2","4",fig=FG,c=M)
b(12,"코사인법칙","COSINE_LAW.SECTOR_FOOT","r=2, 중심각 3π/2, ∠BAP=π/6, OH²=m+n√3, m²+n²","중","20","OH²=4−2√3","4",S_,fig=FG,c=M)
b(13,"사인법칙과 코사인법칙","SINE_COSINE.BISECTOR_CIRCLE_AREA","AB=2, BC=4, 원 C, AD=DE 호, BD=√6, 원 넓이","중상","③ (8π/5)","AD=1, DC=2, cos∠BAD=−1/4","4",fig=FG,c=M,i=M)
b(14,"사인법칙과 코사인법칙","SINE_LAW.RATIO_COS","2/sinA=3/sinB=4/sinC, cosC","하","② (−1/4)","a:b:c=2:3:4","3")
b(15,"사인법칙과 코사인법칙","SINE_COSINE.PARALLELOGRAM_CIRCUMCIRCLES","둘레 20, cosB=1/4, ABC 외접원 32π/3, ABD 외접원 qπ/p","중상","271","AB=4, AD=6, BD²=64 → 256π/15","4",S_,fig=FG,c=M,i=M)
b(16,"사인법칙과 코사인법칙","SINE_COSINE.CIRCUMRADIUS_RATIO","CD=2√7, cos∠BDA=√7/4, R₁:R₂=4:3, BC+BD","중상","28","sinC=9/16, BC=16, BD=12","4",S_,fig=FG,c=M,i=M)
b(17,"사인법칙과 코사인법칙","SINE_COSINE.CHORD_SIMILAR","AB=2, cosA=√3/6, DE=5, CD+CE=5√3, 외접원 넓이 qπ/p","상","191","CE=2√3, CD=3√3, BC²=60, R²=180/11","4",S_,fig=FG,c=H,i=H)
b(18,"사인법칙과 코사인법칙","SINE_COSINE.SECTOR_ARC_RATIO","r=6, AB=8√2, ∠BPA>90°, AP:BP=3:1, BP","중","⑤ (4√6/3)","cos∠APB=−1/3","4",fig=FG,c=M)
b(19,"삼각형의 넓이","TRIANGLE_AREA.COS_FROM_AREA","AB=6, BC=7, 넓이 15, cos∠ABC","하","② (2√6/7)","sin=5/7","3",fig=FG)
b(20,"삼각형의 넓이","TRIANGLE_AREA.OBTUSE_SIDE","AB=8, BC=12, B 둔각, 넓이 12√15, AC","하","16","cosB=−1/4","3",S_)
b(21,"삼각형의 넓이","TRIANGLE_AREA.RATIO_CIRCUMCIRCLE","AB:BC=3:2, B=π/3, 외접원 넓이 7π, 넓이","하","① (9√3/2)","AC=√21, k²=3","3",fig=FG)
b(22,"삼각형의 넓이","TRIANGLE_AREA.SIN_INEQUALITY","AB=AC=2, 넓이>1 θ 범위, 2α+β","하","① (7π/6)","sinθ>1/2","3")
b(23,"삼각형의 넓이","CYCLIC_QUAD.PRODUCT_FROM_AREA","원 내접 ABCD, AB=4, AD=5, BD=√33, BCD 넓이 2√6, BC×CD","중","① (10)","cosA=1/5, sinC=2√6/5","4",fig=FG,c=M)
b(24,"삼각형의 넓이","SECTOR.TRIANGLE_AREA_SEGMENT","r=2 사분원, AC=1, BOD 넓이 7/6, OD","중","③ (4/3)","sin∠BOC=cos∠AOC=7/8","4",fig=FG,c=M)
b(25,"삼각형의 넓이","TRIANGLE_AREA.CIRCUMCIRCLE_SUB","2AB=AC, M, N(3:5), MN=AB, AMN 외접원 16π, ABC 넓이","중","④ (15√15)","cosA=−1/4, k²=15","4",fig=FG,c=M)
b(26,"삼각형의 넓이","SEMICIRCLE.AREA_FILL_BLANK","반원 PQC, QDB 넓이 과정, p×f(π/16)×g(π/8)","중","① (√2π/4)","p=1, f=4θ, g=2cos2θ","4",fig=FG,c=M)
b(27,"삼각형의 넓이","SINE_LAW.BISECTOR_LENGTH","AB=4, CA=8, a(sinB+sinC)=6√3, AP","중","② (8/3)","sinA=√3/2, A=120°","4",fig=FG,c=M)
b(28,"삼각형의 넓이","SEMICIRCLE.TRIANGLE_AREA_COORD","AB=10 반원, 4sinθ=3cosθ, PA=PC=PD, ADC 넓이","중","③ (64/5)","좌표: A(−5,0), D(−0.84,−2.88), C(6.2,−1.6)","4",fig=FG,c=M)
DS = {1:("2025.9 고2 21",104),2:("2025.6 고2 21",104),3:("2023.6 고2 29",105),4:("2022.11 고2 20",105)}
def d(n, tid, tname, ans, chk, fmt=MC, **kw):
    src, pg = DS[n]
    a(f"도전{n:02d}", pg, f"학평 {src}번 (26456-{351+n:04d})", "사인법칙과 코사인법칙", tid, tname, "상", ans, chk, "4", fmt, c=H, i=H, fig=FG, **kw)
d(1,"CYCLIC_QUAD.INCIRCLE_BISECT","R=√21/3, AB=2, AC=√7, AC가 BCD 내접원 넓이 이등분, 내접원 반지름","① (√3−(2/7)√21)","AD=AB=2, BC=3, CD=1 (수치 확인)")
d(2,"SEMICIRCLE.PARALLEL_CHORD","AB=6 반원, cos∠CAB=1/3, DB=AC, BE∥CD, CE","⑤ (2√33/11)","좌표 E(−17/11, 20√2/11)")
d(3,"FOLDING.CIRCUMRADIUS_RATIO","직각이등변 접기, BDE:DCF 외접원 2:1, DF=q/p, p+q","17","ED:DF=2:1 → DF=5/12",fmt=S_)
d(4,"SINE_COSINE.BISECTOR_STATEMENTS","R=√3, 이등분선 D, BD=√3, 보기","⑤ (ㄱ, ㄴ, ㄷ)","A=60°, BC=3; ㄷ BE 합 9/4 (기호 계산)")
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{792+i}", ROWS[i*10:(i+1)*10], 16151+i*10)
