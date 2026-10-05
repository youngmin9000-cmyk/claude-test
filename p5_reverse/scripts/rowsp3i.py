from cfgex import *
MC, S_, D = "객관식(5지선다)", "단답형", "서술형"
M, H = "보통", "높음"
GR = "그래프"
Q = [337]  # A00639 ch01-05 q=1..337
CH = "06 삼각함수의 그래프"
def a(lab, page, src, small, tid, tname, diff, ans, chk, pts, fmt=MC, nsub=1, mid="삼각함수의 그래프", tags="삼각함수;그래프;주기", **kw):
    Q[0] += 1
    kw.setdefault("atype", "선택지" if fmt == MC else "값")
    R(Q[0], page, "삼각함수", mid, small, tid, tname, tags, diff, fmt, ans, src, chk, label="06-"+lab, pts=pts, nsub=nsub, **kw)
    r = ROWS[-1]; r.update({"출처대분류": "시판 기출문제집(전국연합학력평가 고2 재수록)", "학교명": "", "주관기관": "EBS(올림포스)",
        "학교/시험명": f"올림포스 전국연합학력평가 기출문제집 대수 {CH} {lab}", "메모": r["메모"].replace("P1 학교기출", "P1 시판 기출문제집(올림포스); 원출처 학평 고2 (OFFICIAL 근접중복 가능)")})
setup("A00639", "1c09Ezx8TegfVDXf--6ArRwp9hTP2vy53", "올림포스 기출 대수.pdf", "p3/A00639.pdf", "올림포스(EBS)", "2026학년도", "전국연합학력평가 기출문제집", "고2", "대수", CURR="2022 개정",
      VIS="스캔 PDF(텍스트층 없음) 95dpi 렌더 시각판독(일부 220dpi 확대) PARTIAL p78~91 (06 삼각함수의 그래프)", TEXT="텍스트층 없음 — 렌더 판독; 정답과 풀이 별책 미보유")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
GP = dict(mid="삼각함수의 그래프", tags="삼각함수;그래프;주기;최대최소")
PR = dict(mid="삼각함수의 성질", tags="삼각함수;각변환")
EQ = dict(mid="삼각방정식과 삼각부등식", tags="삼각방정식;삼각부등식")
G = "개념 확인 문제"
a("개념01",79,G,"삼각함수의 그래프","TRIGF.PERIOD_RANGE","주기와 치역 6가지","하","(1) π, [−2,2] (2) 4π, [−1/2,1/2] (3) π/2, 실수 전체 (4) 6π, [−1/2,1/2] (5) π, [−3,3] (6) 2π, 실수 전체","","",fmt=D,nsub=6,**GP)
a("개념02",79,G,"삼각함수의 최대·최소","TRIGF.PARAM_FROM_MAX_PERIOD","y=asin bx+1 최댓값 6, 주기 2π/3, a, b","하","a=5, b=3","","",fmt=D,nsub=2,**GP)
a("개념03",79,G,"삼각함수의 성질","TRIG.ANGLE_REDUCTION.EVAL","각변환 값 6가지","하","(1) −√3/2 (2) −√2/2 (3) −√3/3 (4) −1/2 (5) −√2/2 (6) √3","","",fmt=D,nsub=6,**PR)
a("개념04",79,G,"삼각함수의 성질","TRIG.ANGLE_REDUCTION.SIMPLIFY","식 간단히 2가지","하","(1) 1 (2) 1","","",fmt=D,nsub=2,**PR)
a("개념05",79,G,"삼각방정식","TRIGEQ.BASIC","sin=1/2, cos=−√3/2, tan=1 해","하","(1) π/6, 5π/6 (2) 5π/6, 7π/6 (3) π/4, 5π/4","","",fmt=D,nsub=3,**EQ)
a("개념06",79,G,"삼각부등식","TRIGINEQ.BASIC","삼각부등식 3가지","하","(1) π/3<x<2π/3 (2) π/4<x<7π/4 (3) 0≤x≤π/6, π/2<x≤7π/6, 3π/2<x<2π","","",fmt=D,nsub=3,c=M,**EQ)
a("개념07",79,G,"삼각방정식","TRIGEQ.QUADRATIC_SUB","이차식 꼴 삼각방정식 2가지","하","(1) π/3, 5π/3 (2) π/6, 5π/6","","",fmt=D,nsub=2,**EQ)
a("개념08",79,G,"삼각부등식","TRIGINEQ.QUADRATIC_SUB","이차식 꼴 삼각부등식 2가지","중하","(1) 0≤x<π/6 또는 5π/6<x<2π (2) π/3<x<5π/3","","",fmt=D,nsub=2,c=M,**EQ)
a("개념09",79,G,"삼각함수의 성질","TRIG.SYMMETRIC_SUM","대칭 합 4가지","중하","(1) 0 (2) −1 (3) 4 (4) 4","짝지어 상쇄/sin²+cos²","",fmt=D,nsub=4,c=M,**PR)
a("개념10",79,G,"삼각부등식","TRIGINEQ.APPLIED.PROJECTILE","f(θ)=v²sin2θ/10≥45√2, θ 범위","하","π/8≤θ≤3π/8","sin2θ≥√2/2","",fmt=S_,**EQ)
S = {1:"2024.6 고2 25",2:"2024.9 고2 12",3:"2025.6 고2 9",4:"2024.10 고2 3",5:"2023.6 고2 24",6:"2025.6 고2 25",7:"2023.6 고2 10",8:"2024.6 고2 9",9:"2022.6 고2 10",10:"2025.9 고2 18",
11:"2025.9 고2 27",12:"2024.10 고2 11",13:"2023.11 고2 9",14:"2020.11 고2 12",15:"2020.9 고2 25",16:"2021.11 고2 10",17:"2024.6 고2 12",18:"2018.3 고3 가형 25",19:"2020.6 고2 19",20:"2020.6 고2 15",
21:"2023.11 고2 5",22:"2025.6 고2 16",23:"2019.9 고2 가형 15",24:"2024.9 고2 19",25:"2022.6 고2 18",26:"2019.6 고2 나형 29",27:"2025.6 고2 19",28:"2025.6 고2 4",29:"2024.6 고2 4",30:"2023.6 고2 4",
31:"2019.6 고2 나형 3",32:"2024.9 고2 8",33:"2023.9 고2 8",34:"2020.9 고2 14",35:"2019.9 고2 가형 28",36:"2020.11 고2 27",37:"2019.11 고2 가형 16",38:"2020.6 고2 17",39:"2023.6 고2 28",40:"2021.6 고2 13",
41:"2024.9 고2 25",42:"2024.6 고2 18",43:"2025.6 고2 17",44:"2023.6 고2 15",45:"2025.9 고2 10",46:"2019.11 고2 가형 18"}
PG = {}
for p, rg in [(80,range(1,5)),(81,range(5,10)),(82,range(10,14)),(83,range(14,19)),(84,range(19,22)),(85,range(22,26)),(86,range(26,31)),(87,range(31,36)),(88,range(36,40)),(89,range(40,44)),(90,range(44,47))]:
    for i in rg: PG[i] = p
def b(n, small, tid, tname, diff, ans, chk, pts, fmt=MC, **kw):
    a(f"{n:02d}", PG[n], f"학평 {S[n]}번 (26456-{n+274:04d})", small, tid, tname, diff, ans, chk, pts, fmt, **kw)
b(1,"삼각함수의 그래프","TRIGF.POINT.CONSTANT","6cos(x+π/2)+k가 (5π/6, 9) 통과, k","하","12","6cos(4π/3)=−3","3",S_,**GP)
b(2,"삼각함수의 그래프","TRIGF.TAN.TRANSLATE_POINT","f=atan(πx/4), A(3,−2) 평행이동 A'도 그래프 위, a+b","중하","② (6)","a=2, b=4","3",c=M,**GP)
b(3,"삼각함수의 주기와 최대·최소","TRIGF.GRAPH_READ.AMPLITUDE_PERIOD","y=asin bx+1 그래프, a+b","하","③ (4)","a=2, 주기 π → b=2","3",fig=GR,**GP)
b(4,"삼각함수의 주기와 최대·최소","TRIGF.PERIOD.COS","cos(πx/4) 주기","하","④ (8)","","2",**GP)
b(5,"삼각함수의 주기와 최대·최소","TRIGF.PERIOD.EQUAL","cos(2x/3)와 tan(3x/a) 주기 같음, a","하","9","3π=aπ/3","3",S_,**GP)
b(6,"삼각함수의 주기와 최대·최소","TRIGF.PERIOD.EVAL","6cos ax+10 주기 4π, f(4π/3)","하","7","a=1/2","3",S_,**GP)
b(7,"삼각함수의 주기와 최대·최소","TRIGF.GRAPH_READ.SIN_ABC","y=asin bx+c 그래프, abc","하","⑤ (3)","a=2, c=3, b=1/2","3",fig=GR,**GP)
b(8,"삼각함수의 주기와 최대·최소","TRIGF.GRAPH_READ.TAN","y=tan ax+b 그래프, ab","하","② (1/2)","주기 4π → a=1/4, b=2","3",fig=GR,**GP)
b(9,"삼각함수의 주기와 최대·최소","TRIGF.GRAPH_READ.COS_ABC","y=acos bx+c 그래프, abc","하","③ (−6)","a=2, c=−1, 주기 2π/3 → b=3 (확대 판독)","3",fig=GR,**GP)
b(10,"삼각함수의 주기와 최대·최소","TRIGF.RESTRICTED_DOMAIN.MINMAX","acos(bx−π/4) [0,π] 최대 4, 최소 −2√2, a+b","중","④ (5)","a=4, bπ−π/4=3π/4","4",c=M,**GP)
b(11,"삼각함수의 주기와 최대·최소","TRIGF.LEVEL_SET.SUM_COND","asin(πx/4)+b [0,8], f(x)=n 원소 합 22, a²+b²","중상","10","a+3b=6 → (3,1)","4",S_,c=M,i=M,**GP)
b(12,"삼각함수의 성질","TRIG.ANGLE_REDUCTION.EQ_COS","cos(3π/2−θ)tanθ=8/3, cosθ","중하","② (−1/3)","3c²−8c−3=0","3",c=M,**PR)
b(13,"삼각함수의 성질","TRIG.ANGLE_REDUCTION.EQ_SIN2","2sin(π/2−θ)=sinθtan(π+θ), sin²θ","하","④ (2/3)","2cos²=sin²","3",**PR)
b(14,"삼각함수의 성질","TRIG.ANGLE_REDUCTION.EVAL","cosθ=1/4, 3sin(π/2+θ)+cos(π−θ)","하","③ (1/2)","2cosθ","3",**PR)
b(15,"삼각함수의 성질","TRIG.ANGLE_REDUCTION.FROM_TAN","제2사분면 tan=−4/3, 5sin(π+θ)+10cos(π/2−θ)","하","4","5sinθ","3",S_,**PR)
b(16,"삼각함수의 성질","TRIG.ANGLE_REDUCTION.POINT","P(4,−3), sin(π/2+θ)−sinθ","하","⑤ (7/5)","","3",**PR)
b(17,"삼각함수의 최대·최소","TRIGF.QUADRATIC_SUB.MINMAX","2cos²x+2sin x+k 최댓값 15/2, 최솟값","중하","③ (3)","k=5, s=−1에서 최소","3",c=M,**GP)
b(18,"삼각함수의 최대·최소","TRIGF.QUADRATIC_SUB.MAX","sin²x+sin(x+π/2)+1 최댓값 M, 4M","하","9","−c²+c+2 → 9/4","3",S_,**GP)
b(19,"삼각함수의 최대·최소","TRIG.CIRCLE.MAX_COORD","원 위 P, ∠PAB=θ, PQ=3, Q x좌표 최대 sin²θ","중","③ (9/16)","Qx=1−2s²+3s","4",fig="도형",c=M,**GP)
b(20,"삼각함수의 그래프의 활용","TRIGF.TAN_LINE.INTERSECT_COUNT","tan πx [0,2]와 y=−10x/3+n 세 점, n 최대","중","⑤ (6)","x=2에서 n−20/3≤0","4",c=M,**GP)
b(21,"삼각함수의 그래프의 활용","TRIGF.TAN.LEVEL_COUNT","tan x (0,5π)와 y=2 교점 수","하","③ (5)","","3",**GP)
b(22,"삼각함수의 그래프의 활용","TRIGF.LOG_EQ.ROOT_SUM","asin(πx/b)+a², 최대−최소 2, log 방정식 근 합 6, a+b","중","④ (4)","a=−2, f=3 → b=6","4",c=M,**GP)
b(23,"삼각함수의 그래프의 활용","TRIGF.RIGHT_TRIANGLE.AREA","asin bx, ∠OAB=π/2, 넓이 4, a+b","중","③ (2+π/4)","a=π/(2b), a=2, b=π/4","4",fig=GR,c=M,**GP)
b(24,"삼각함수의 그래프의 활용","TRIGF.EQUILATERAL.HEIGHT","3sin(πx/2), y=−t, 정삼각형 한 변 4, t","중","③ (√3)","AB=주기, 2t=2√3","4",c=M,**GP)
b(25,"삼각함수의 그래프의 활용","TRIGF.ODD_LINE.TRIANGLE_AREA","3sin2nx, 원점 지나는 직선 O,A,B, 넓이 π/12 n 최대","중상","④ (18)","f(p)=n/6≤3","4",c=M,i=M,trap=M,**GP)
b(26,"삼각함수의 그래프의 활용","TRIGF.QUADRANT_AVOID.INTEGER_COUNT","ksin(2x+π/3)+k²−6 제1사분면 X 정수 k 개수","중","5","|k|+k²−6≤0","4",S_,c=M,**GP)
b(27,"삼각방정식","TRIGEQ.ABS_COS.PAIR_COUNT","f=|2ᵐcos x−2ⁿ|, (f−32)(f−16)=0 근 6개 (m,n) 개수","중상","② (4)","m=5, n=1~4 (전수 확인)","4",c=M,i=M,**EQ)
b(28,"삼각방정식","TRIGEQ.TAN.BASIC","√3tan x=1 (π/2,3π/2)","하","④ (7π/6)","","3",**EQ)
b(29,"삼각방정식","TRIGEQ.COS.BASIC","2cos x+1=0 [0,π]","하","④ (2π/3)","","3",**EQ)
b(30,"삼각방정식","TRIGEQ.SIN.BASIC","2sin x−1=0 (−π/2,π/2)","하","④ (π/6)","","3",**EQ)
b(31,"삼각방정식","TRIGEQ.SIN.SHIFT","sin(x−π/6)=1/2 [0,π/2]","하","④ (π/3)","","2",**EQ)
b(32,"삼각방정식","TRIGEQ.QUADRATIC_SUB.SUM","cos²x−1=2sin x (0,2π] 해 합","하","④ (3π)","sin x=0 → π, 2π","3",trap=M,**EQ)
b(33,"삼각방정식","TRIGEQ.QUADRATIC_SUB.SUM","2sin²x+3sin x−2=0 해 합","하","③ (π)","","3",**EQ)
b(34,"삼각방정식","TRIGEQ.MULTI_ANGLE.ROOT_SUM","sin nx=1/5 [0,π) 해 합 f(n), f(2)+f(5)","중","⑤ (7π/2)","π/2+3π","4",c=M,**EQ)
b(35,"삼각방정식","TRIGEQ.SHIFTED_RANGE.ROOT_SUM","(2/√3)sin(x+π/3)−7/8=0 근 합 qπ/p, p+q","중","10","sin u=7√3/16<sin(π/3) → u합 3π, x합 7π/3","4",S_,c=M,trap=M,**EQ)
b(36,"삼각방정식","TRIGEQ.VIETA.COS_TAN","x²−k=0 두 근 6cosθ, 5tanθ, k","중","20","6s²−5s−6=0 → s=−2/3","4",S_,c=M,**EQ)
b(37,"삼각방정식","TRIGEQ.WINDOW.COUNT_FUNC","sin(πx/2)=k [t,t+1] 해 개수 f(t), a²+b²+k²","중상","③ (3)","a=1/2, b=3/2, k²=1/2","4",c=M,i=M,**EQ)
b(38,"삼각방정식","TRIGEQ.SYMMETRIC_ROOTS","sin x=k 두 근 α<β, sin((β−α)/2)=5/7, k","중하","① (2√6/7)","cosα=5/7","4",c=M,**EQ)
b(39,"삼각방정식","TRIGEQ.ALTERNATING.ROOT_SUM","sin πx=(−1)^{n+1}/n [0,4] 근 합 f(n), Σf","중","35","3+10+6+10+6","4",S_,c=M,**EQ)
b(40,"삼각부등식","TRIGINEQ.SIN.SYMMETRIC","3sin x−2>0 해 α<x<β, cos(α+β)","하","① (−1)","α+β=π","3",**EQ)
b(41,"삼각부등식","TRIGINEQ.COS_LT_SIN.NATURAL_SUM","cos(πx/5)<sin(πx/5) (0,10] 자연수 합","하","20","5/4<x<25/4","3",S_,**EQ)
b(42,"삼각부등식","TRIGINEQ.DOMAIN_PARAM.MAX_K","sin x+cos(π/8)<0 [−π,k] 해 −π−α<x<α, k 최대","중","④ (11π/8)","해 (−5π/8,−3π/8), 다음 구간 11π/8부터 (확대 판독)","4",c=M,trap=M,**EQ)
b(43,"삼각부등식","TRIGINEQ.PRODUCT_SIGN.INTEGER_COUNT","(sin(πx/12)−1/2)(cos(πx/12)−1/2)<0 정수 개수","중","② (10)","15° 단위 전수 확인","4",c=M,**EQ)
b(44,"삼각방정식과 삼각부등식의 활용","TRIGF.EQUILATERAL.AMPLITUDE","acos(2x/3)+a, A, B, C 정삼각형, a","중","⑤ (2√3π/3)","BC=2π, 높이 3a/2","4",fig=GR,c=M,**EQ)
b(45,"삼각방정식과 삼각부등식의 활용","TRIGEQ.ZERO.DISTANCE","sin(x/2)+√3/2 x축 교점 AB","하","① (2π/3)","x=8π/3, 10π/3","3",**EQ)
b(46,"삼각방정식과 삼각부등식의 활용","TRIGF.TRAPEZOID_AREA.ROOT_SUM","acos bx+c 최대3 최소−1, 사다리꼴 넓이 6π, f(x)=2 해 합","중","② (13π/2)","b=2/3; x=π/2, 5π/2, 7π/2","4",fig=GR,c=M,**EQ)
DS = {1:"2025.9 고2 29",2:"2024.10 고2 29",3:"2024.6 고2 30"}
def d(n, tid, tname, ans, chk, fmt=S_, **kw):
    a(f"도전{n:02d}", 91, f"학평 {DS[n]}번 (26456-{320+n:04d})", "삼각함수의 그래프의 활용", tid, tname, "상", ans, chk, "4", fmt, c=H, i=H, **kw)
d(1,"TRIGF.COMPOSITE_ABS.SYMMETRY_COUNT","f=(3/a)|x−3|−b, g=sin(πx/b)+3, 조건 (가)(나), 2a+b 최대×최소","133","b∈{1,2,3,6}, b≤9/a<2b → M=19, m=7",**GP)
d(2,"TRIGEQ.TWO_LEVELS.ROOT_COUNT","(sin x−k/4)(sin x+k²/4−3k/4)=0 해 2개 정수 k 곱","48","k=−3,−2,2,4 (전수 확인)",**EQ)
d(3,"TRIGF.ABS_WINDOW.MAX_HALF","|2sin(πx/k)+1/2| [t,t+1] 최댓값 1/2 t=α, β뿐, kα+β","47","허용 구간 길이 k/6=1 → k=6, α=6, β=11",**GP)
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{786+i}", ROWS[i*10:(i+1)*10], 16092+i*10)
