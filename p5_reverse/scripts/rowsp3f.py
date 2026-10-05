from cfgex import *
MC, S_, D = "객관식(5지선다)", "단답형", "서술형"
M, H = "보통", "높음"
GR = "그래프"
Q = [147]  # A00639 ch01 q=1..69, ch02 q=70..147
CH = "03 지수함수와 로그함수"
def a(lab, page, src, small, tid, tname, diff, ans, chk, pts, fmt=MC, nsub=1, mid="지수함수와 로그함수", tags="지수함수;로그함수", **kw):
    Q[0] += 1
    kw.setdefault("atype", "선택지" if fmt == MC else "값")
    R(Q[0], page, "지수함수와 로그함수", mid, small, tid, tname, tags, diff, fmt, ans, src, chk, label="03-"+lab, pts=pts, nsub=nsub, **kw)
    r = ROWS[-1]; r.update({"출처대분류": "시판 기출문제집(전국연합학력평가 고2 재수록)", "학교명": "", "주관기관": "EBS(올림포스)",
        "학교/시험명": f"올림포스 전국연합학력평가 기출문제집 대수 {CH} {lab}", "메모": r["메모"].replace("P1 학교기출", "P1 시판 기출문제집(올림포스); 원출처 학평 고2 (OFFICIAL 근접중복 가능)")})
setup("A00639", "1c09Ezx8TegfVDXf--6ArRwp9hTP2vy53", "올림포스 기출 대수.pdf", "p3/A00639.pdf", "올림포스(EBS)", "2026학년도", "전국연합학력평가 기출문제집", "고2", "대수", CURR="2022 개정",
      VIS="스캔 PDF(텍스트층 없음) 95dpi 렌더 시각판독(일부 260dpi 확대) PARTIAL p34~53 (03 지수함수와 로그함수)", TEXT="텍스트층 없음 — 렌더 판독; 정답과 풀이 별책 미보유")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
G = "개념 확인 문제"
a("개념01",35,G,"지수함수의 성질","EXPF.RANGE_ASYMPTOTE","지수함수 치역·점근선 4가지","하","(1) y>0, y=0 (2) y>0, y=0 (3) y>−2, y=−2 (4) y<1, y=1","","",fmt=D,nsub=4)
a("개념02",35,G,"지수함수의 성질","EXPF.COMPARE.SAME_BASE","두 수 크기 비교 4가지","하","(1) ∛2<⁵√4 (2) ∛0.2>⁵√0.04 (3) ∛9>⁵√27 (4) (0.4)^{√2}<(0.16)^{√2/3}","같은 밑 변환","",fmt=D,nsub=4)
a("개념03",35,G,"지수함수의 최대·최소","EXPF.MINMAX.LINEAR_EXP","y=2^{x−2} [−2,1] 최대·최소","하","최댓값 1/2, 최솟값 1/16","","",fmt=D,nsub=2)
a("개념04",35,G,"지수함수의 최대·최소","EXPF.MINMAX.LINEAR_EXP","y=(1/2)^{x−3}−2 [−1,4] 최대·최소","하","최댓값 14, 최솟값 −3/2","","",fmt=D,nsub=2)
a("개념05",35,G,"지수함수의 성질","EXPF.INCREASING.BASE_COND","y=(a²+a−1)ˣ 증가 a 범위","하","a<−2 또는 a>1","a²+a−1>1","",fmt=D)
a("개념06",35,G,"로그함수의 성질","LOGF.DOMAIN_ASYMPTOTE","로그함수 정의역·점근선 4가지","하","(1) x>0, x=0 (2) x>0, x=0 (3) x>1, x=1 (4) x>0, x=0","","",fmt=D,nsub=4)
a("개념07",35,G,"로그함수의 성질","LOGF.COMPARE","두 로그 크기 비교 4가지","하","(1) log₃5>log₃2 (2) log_{1/3}(1/2)<log_{1/3}(1/5) (3) log_{1/4}3>log_{1/2}3 (4) 같다","(4) 둘 다 −½log₃2","",fmt=D,nsub=4)
a("개념08",35,G,"로그함수의 최대·최소","LOGF.MINMAX.LINEAR_ARG","y=log₂(x+1)−2 [1,7] 최대·최소","하","최댓값 1, 최솟값 −1","","",fmt=D,nsub=2)
a("개념09",35,G,"로그함수의 최대·최소","LOGF.MINMAX.LINEAR_ARG","y=log_{1/2}(x−1)+1 [3,9] 최대·최소","하","최댓값 0, 최솟값 −2","","",fmt=D,nsub=2)
a("개념10",35,G,"로그함수의 그래프","LOGF.GRAPH.STAIRCASE_YX","y=log₂x, y=x 점선 a, b, log₂ab","하","3","a=2, b=4","",fmt=S_,fig=GR)
a("개념11",35,G,"지수함수의 그래프","EXPF.AREA.TRANSLATE_STRIP","(1/3)ˣ, 9(1/3)ˣ, y=1, y=3 둘러싼 넓이","중하","4","평행이동 2 × 높이 2","",fmt=S_,c=M)
a("개념12",35,G,"상용로그","LOG.COMMON.INTEGER_DIFF","10<x<100, log√x와 logx² 차 정수, log x","중하","4/3","(3/2)logx=2","",fmt=S_)
a("개념13",35,G,"지수함수와 로그함수의 관계","LOGF.INVERSE.POINT","f=log₂(x−1) 역함수, P(2,b), Q(a,b), a+b","하","38","f(x)=2ˣ+1, b=5, a=33","",fmt=S_)
a("개념14",35,G,"지수함수와 로그함수의 관계","LOGF.INVERSE.COMPOSE","f=log₃(2x²+1), (f⁻¹∘f⁻¹)(2)","하","2","f⁻¹(2)=2","",fmt=S_)
S = {1:"2023.6 고2 7",2:"2022.6 고2 9",3:"2019.11 고2 나형 11",4:"2023.11 고2 8",5:"2025.6 고2 14",6:"2020.9 고2 가형 26",7:"2024.6 고2 11",8:"2021.9 고2 8",9:"2013.11 고2 A형 15",10:"2011.11 고2 나형 10",
11:"2022.6 고2 6",12:"2020.6 고2 7",13:"2019.9 고2 나형 8",14:"2019.6 고2 가형 11",15:"2021.6 고2 8",16:"2025.6 고2 11",17:"2019.6 고2 나형 13",18:"2014.6 고2 A형 25",19:"2022.9 고2 27",20:"2019.9 고2 가형 11",
21:"2019.9 고2 가형 13",22:"2024.6 고2 19",23:"2020.11 고2 18",24:"2016.11 고2 가형 28",25:"2014.6 고2 A형 18",26:"2024.6 고2 8",27:"2025.9 고2 7",28:"2025.6 고2 8",29:"2020.6 고2 9",30:"2025.9 고2 16",
31:"2021.6 고2 14",32:"2024.9 고2 18",33:"2022.6 고2 7",34:"2019.6 고2 가형 12",35:"2018.11 고2 가형 15",36:"2019.6 고2 나형 28",37:"2023.9 고2 24",38:"2024.6 고2 24",39:"2020.11 고2 23",40:"2019.9 고2 가형 10",
41:"2024.9 고2 9",42:"2021.9 고2 14",43:"2023.9 고2 18",44:"2022.9 고2 11",45:"2024.6 고2 28",46:"2023.6 고2 16",47:"2019.9 고2 나형 16",48:"2025.6 고2 10",49:"2024.6 고2 10",50:"2023.6 고2 8",
51:"2022.11 고2 24",52:"2019.9 고2 나형 19",53:"2024.10 고2 18",54:"2021.9 고2 11",55:"2025.6 고2 18",56:"2025.9 고2 19",57:"2024.9 고2 20",58:"2019.6 고2 가형 19"}
PG = {}
for p, rg in [(36,range(1,5)),(37,range(5,9)),(38,range(9,14)),(39,range(14,20)),(40,range(20,23)),(41,range(23,25)),(42,range(25,28)),(43,range(28,33)),(44,range(33,37)),(45,range(37,43)),(46,range(43,46)),(47,range(46,48)),(48,range(48,52)),(49,range(52,54)),(50,range(54,56)),(51,range(56,59))]:
    for i in rg: PG[i] = p
def b(n, small, tid, tname, diff, ans, chk, pts, fmt=MC, **kw):
    a(f"{n:02d}", PG[n], f"학평 {S[n]}번 (26456-{n+122:04d})", small, tid, tname, diff, ans, chk, pts, fmt, **kw)
E = dict(mid="지수함수", tags="지수함수;그래프")
Lg = dict(mid="로그함수", tags="로그함수;그래프")
b(1,"지수함수의 그래프","EXPF.GRAPH.ASYMPTOTE_INTERCEPT","y=2^{x+a}+b 점근선 y=3, y절편 5, a+b","하","② (4)","b=3, 2ᵃ=2","3",fig=GR,**E)
b(2,"지수함수의 그래프","EXPF.GRAPH.ASYMPTOTE_POINT","y=3ˣ+a 점근선 y=5, (2,b), a+b","하","⑤ (19)","a=5, b=14","3",**E)
b(3,"지수함수의 그래프","EXPF.GRAPH.SLOPE_TWO_LEVELS","y=2ˣ/3 와 y=1, y=4 교점 A, B 기울기","하","② (3/2)","x차 log₂4=2","3",fig=GR,**E)
b(4,"지수함수의 그래프","EXPF.INTERSECT.FIRST_QUADRANT","(1/16)(1/2)^{x−m}과 2ˣ+1 제1사분면 교점 최소 m","중하","③ (6)","x=0에서 2^{m−4}>2","3",c=M,**E)
b(5,"지수함수의 그래프","EXPF.MIDPOINT.VERTICAL_GAP","y=2ˣ 위 A, B 중점 M, MN 길이","중","③ (√6/16)","s=√(3/2), MN=s(s²−1)²/2","4",fig=GR,c=M,**E)
b(6,"지수함수의 평행이동","EXPF.TRANSLATE.MATCH","y=5ˣ 평행이동 = (1/9)5^{x−1}+2, 5ᵃ+b","중하","47","a=1+log₅9, b=2","4",S_,c=M,**E)
b(7,"지수함수의 평행이동","EXPF.TRANSLATE.ORIGIN_ASYMPTOTE","y=4ˣ−6 평행이동, 원점·점근선 y=−2, ab","하","④ (−2)","b=4, a=−1/2","3",**E)
b(8,"지수함수의 평행이동","EXPF.TRANSLATE.POINT_ASYMPTOTE","y=3ˣ 평행이동 (7,5), 점근선 y=2, m+n","하","② (8)","n=2, m=6","3",**E)
b(9,"지수함수의 대칭이동","EXPF.REFLECT.LINE_SYMMETRY","f=aˣ, y축대칭 후 m 이동 g, x=1 대칭, f(3)=16g(3), a+m","중","② (4)","m=2, a⁴=16","4",c=M,**E)
b(10,"지수함수의 성질","EXPF.STATEMENTS.TRANSLATE","f=2^{x+k} 보기","중하","⑤ (ㄱ, ㄴ, ㄷ)","3·2ˣ+1=2^{x+log₂3}+1","4",c=M,trap=M,**E)
b(11,"지수함수의 최대·최소","EXPF.MINMAX.LINEAR_EXP","f=2^{−x}+5 [−3,−1] 최솟값","하","② (7)","","3",**E)
b(12,"지수함수의 최대·최소","EXPF.MINMAX.LINEAR_EXP","f=2+(1/3)^{2x} [−1,2] 최댓값","하","① (11)","","3",**E)
b(13,"지수함수의 최대·최소","EXPF.MINMAX.LINEAR_EXP","f=5^{x−2}+3 [1,3] 최댓값","하","⑤ (8)","","3",**E)
b(14,"지수함수의 최대·최소","EXPF.MINMAX.PARAM_FROM_MIN","(1/2)^{x+a} [−2,4] 최솟값 1/8, 최댓값","하","④ (8)","a=−1","3",**E)
b(15,"지수함수의 최대·최소","EXPF.MINMAX.TWO_PARAM","a·2^{2−x}+b 최대 5 최소 −2, f(0)","하","① (1)","a=1, b=−3","3",**E)
b(16,"지수함수의 최대·최소","EXPF.MINMAX.QUADRATIC_SUB","2^{2x}−2^{x+2}+6 (x≤3) 최대+최소","중하","③ (40)","t∈(0,8], (t−2)²+2 → 38+2 (확대 판독)","3",c=M,**E)
b(17,"지수함수의 최대·최소","EXPF.MINMAX.QUADRATIC_EXPONENT","(1/5)^{x²−4x+1} 최댓값 M at a, a+M","하","① (127)","a=2, M=125","3",**E)
b(18,"지수함수의 최대·최소","EXPF.MINMAX.QUADRATIC_EXPONENT","5^{x²−4x−2} [−1,4] 최댓값","하","125","지수 최대 3 (x=−1)","3",S_,**E)
b(19,"지수함수의 최대·최소","EXPF.COMPOSE.QUADRATIC_MINMAX","h=(1/2)^{g(x)−a}, g=(x−1)(x−3), [0,5] 최소 1/4, M","중","128","g∈[−1,8], a=6","4",S_,c=M,**E)
b(20,"지수함수의 그래프","EXPF.AREA.TRIANGLE_LEVEL","(1/3)ˣ, (1/9)ˣ와 y=9 교점 삼각형 OAB 넓이","하","① (9/2)","x=−2, −1","3",**E)
b(21,"지수함수의 그래프","EXPF.ABS.SEGMENT_LENGTH","y=|aˣ−a| A, B, C, AH=1, BC","중하","② (√5)","a=2, B(0,1), C(2,2)","3",fig=GR,c=M,**E)
b(22,"지수함수의 그래프","EXPF.PARALLELOGRAM.AREA","a^{1−x}, 4^{1−x}, y=4, y=k 평행사변형 넓이 15/2, 4ak","중상","⑤ (2^{2/3})","AB=DC → k=1/4, log_a4=3","4",fig=GR,c=M,i=M,**E)
b(23,"지수함수의 그래프","EXPF.TRANSLATED_CURVES.TRIANGLE_AREA","2^{x−3}+1, 2^{x−1}−2, y=−x+k, BC=√2, 넓이","중","③ (5/2)","A(3,2), B(5,5), C(4,6)","4",fig=GR,c=M,**E)
b(24,"지수함수의 그래프","EXPF.SQUARE.THREE_BASES","aˣ, bˣ, cˣ, y=8, y=4 정사각형, abc=2^{q/p}","중","43","b=2^{1/4}, a=2^{3/8}, c=2^{1/6} → 2^{19/24}","4",S_,fig=GR,c=M,**E)
b(25,"지수함수의 그래프","EXPF.RECTANGLE.AREA_RATIO","y=2ˣ 위 P, 직사각형 PACE, PFDB 조건, E x좌표","중","③ (6)","2ᵗ=2√2, t=3/2, E x=4t","4",fig=GR,c=M,**E)
b(26,"로그함수의 그래프","LOGF.GRAPH.POINT_ASYMPTOTE","y=log₃(x+a)+b (5,0), 점근선 x=−4, a+b","하","① (2)","a=4, b=−2","3",**Lg)
b(27,"로그함수의 그래프","LOGF.SLOPE.BASE_FIND","y=logₐx A(2,·), B(4,·) 기울기 −1/4, a","하","② (1/4)","logₐ2=−1/2","3",**Lg)
b(28,"로그함수의 성질","LOGF.INCREASING.BASE_INTEGER","y=log_{(−a²−a+7)}x 증가 정수 a 합","하","⑤ (−2)","a²+a−6<0","3",**Lg)
b(29,"로그함수의 그래프","LOGF.ASYMPTOTE_INTERSECT_YAXIS","2ˣ−1 점근선과 log₂(x+k) y축 위 교점 k","하","② (1/2)","log₂k=−1","3",**Lg)
b(30,"로그함수의 성질","LOGF.ABS_PIECEWISE.EQUATION","f=|log₃x|, f(x)+f(3x)=3 실근 합","중","③ (28/9)","x=3, 1/9","4",c=M,**Lg)
b(31,"로그함수의 성질","LOGF.PIECEWISE.RECIPROCAL_EQ","f(t)+f(1/t)=2 t 합","중하","③ (82/9)","|log₃t|=2","4",c=M,**Lg)
b(32,"로그함수의 최대·최소","LOGF.PIECEWISE.WINDOW_MINMAX_DIFF","[a−1,a+1] 최대−최소=1 a 합","중상","② (log₂(32/3))","a=3, 1, log₂(2/3)","4",c=M,i=M,trap=M,**Lg)
b(33,"로그함수의 평행이동","LOGF.TRANSLATE.POINT","log₃x (2,5) 이동, (5,a)","하","① (6)","","3",**Lg)
b(34,"로그함수의 평행이동","LOGF.TRANSLATE.QUADRANT_AVOID","2+log₂x (−8,k) 이동 제4사분면 X, k 최소","하","⑤ (−5)","x=0에서 y≥0","3",**Lg)
b(35,"로그함수의 평행이동","LOGF.TRANSLATE.MIDPOINT","log₃x 위 A(a,1), B(27,b), m 이동 중점 통과","중하","① (6)","중점 (15,2)","4",c=M,**Lg)
b(36,"로그함수의 대칭이동","LOGF.REFLECT_ORIGIN.INTERSECT_SLOPE","log₂x 원점대칭 후 5/2 이동, 교점 AB 기울기","중","34","x(5/2−x)=1 → A(1/2,−1), B(2,1), 4/3","4",S_,c=M,**Lg)
b(37,"로그함수의 최대·최소","LOGF.MINMAX.LINEAR_ARG","6log₃(x+2) [1,25] M+m","하","24","18+6","3",S_,**Lg)
b(38,"로그함수의 최대·최소","LOGF.MINMAX.LINEAR_ARG","log_{1/3}(x+3)+30 [0,6] 최댓값","하","29","","3",S_,**Lg)
b(39,"로그함수의 최대·최소","LOGF.MINMAX.LINEAR_ARG","log₂(x+1)+2 [1,7] 최댓값","하","5","","3",S_,**Lg)
b(40,"로그함수의 최대·최소","LOGF.MINMAX.QUADRATIC_ARG","log₂(x²−4x+20) [−3,3] 최솟값","하","② (4)","","3",**Lg)
b(41,"로그함수의 최대·최소","LOGF.MINMAX.PARAM_FROM_MAX","log_{1/3}(x+m) [−3,3] 최댓값 −2, m","하","② (12)","m−3=9","3",**Lg)
b(42,"로그함수의 최대·최소","LOGF.MINMAX.QUADRATIC_ARG_SUM","log₃(x²−6x+k) [0,5] 최대+최소=2+log₃4, k","중하","② (12)","k(k−9)=36","4",c=M,**Lg)
b(43,"로그함수의 그래프","LOGF.TRANSLATE.SEGMENT_DIFF","log₂x, log₂(x−p)+q, (4,2), CD−BA=3/4, p+q","중","④ (5)","p=3, q=2","4",fig=GR,c=M,**Lg)
b(44,"로그함수의 그래프","LOGF.TRIANGLE.AXIS_BISECT","log₄x 위 A(y=1), −log₄(x+1) 위 B, x축 이등분, OB","중하","③ (√10)","B(3,−1)","3",fig=GR,c=M,**Lg)
b(45,"로그함수의 그래프","LOGF.PIECEWISE.ROOTS_DISTANCE","a(4−x²), blog₂(x/3)−5a, AB=10, f(b)=2b, 5a+b","중","144","b=5a/2, b=48","4",S_,c=M,**Lg)
b(46,"로그함수의 그래프","LOGF.TRIANGLE_AREA.STATEMENTS","log₂x, log₄x, y=t 삼각형 OPQ S(t) 보기","중","⑤ (ㄱ, ㄴ, ㄷ)","S(t)/S(−t)=8ᵗ","4",fig=GR,c=M,trap=M,**Lg)
b(47,"로그함수의 그래프","LOGF.AREA.VERTICAL_SHIFT","log₂x, log₂3x 사이 x∈[1,3] 넓이","중하","② (2log₂3)","g=f+log₂3 → 2·log₂3","4",fig=GR,c=M,**Lg)
b(48,"지수함수와 로그함수의 관계","EXPLOG.INVERSE.POINT","y=2^{−x+a}+a 역함수 (a+1,1), a","하","① (1)","2^{a−1}=1","3",mid="지수함수와 로그함수의 관계",tags="역함수;지수함수;로그함수")
b(49,"지수함수와 로그함수의 관계","EXPLOG.INVERSE.POINT","5ˣ+1 역함수 (4, log₅a), a","하","③ (3)","","3",mid="지수함수와 로그함수의 관계",tags="역함수;지수함수;로그함수")
b(50,"지수함수와 로그함수의 관계","EXPLOG.INVERSE.TRANSLATE_REFLECT","log₂x+1 a 이동 후 y=x 대칭 = 2^{x−1}+5, a","하","⑤ (5)","","3",mid="지수함수와 로그함수의 관계",tags="역함수;지수함수;로그함수")
b(51,"지수함수와 로그함수의 관계","EXPLOG.INVERSE.TRANSLATE_MATCH","2ˣ (a,3) 이동, log₂(4x−b)와 y=x 대칭, a+b","하","14","log₂(x−3)+a=2+log₂(x−b/4)","3",S_,mid="지수함수와 로그함수의 관계",tags="역함수;지수함수;로그함수")
b(52,"지수함수와 로그함수의 관계","EXPF.SYMMETRY_COND.STATEMENTS","f=a^{x−k}, f(2+x)f(2−x)=1 보기","중","③ (ㄱ, ㄷ)","k=2; ㄴ 교점 수 a에 의존(반례)","4",c=M,trap=M,mid="지수함수와 로그함수의 관계",tags="역함수;지수함수;볼록성")
b(53,"지수함수와 로그함수의 관계","EXPLOG.INVERSE.ISOSCELES_LINE","aˣ+k, logₐ(x−k), y=3x+2, AB=AD, BC=CD, ak","중상","② (5√3)","C=B 대칭, b=4, a²=3, k=5","4",fig=GR,c=M,i=M,mid="지수함수와 로그함수의 관계",tags="역함수;지수함수;로그함수")
b(54,"지수함수와 로그함수의 관계","EXPLOG.ASYMPTOTE.TRIANGLE_AREA","log₂(x−p), 2ˣ+1 점근선 교점 삼각형 넓이 6, p","중하","② (log₂5)","2ᵖ+1=6","3",fig=GR,mid="지수함수와 로그함수의 관계",tags="역함수;지수함수;로그함수")
b(55,"지수함수와 로그함수의 관계","EXPLOG.INVERSE_SHIFT.QUADRILATERAL","a^{ax}, (1/a)logₐ(x−1/a)−1/a, 사각형 ABCD 넓이","상","⑤ (55/8)","a=2: A(1,4), B(9/2,1/2), C(5/2,0), D(1/2,2)","4",fig=GR,c=H,i=H,mid="지수함수와 로그함수의 관계",tags="역함수;지수함수;로그함수")
b(56,"지수함수와 로그함수의 관계","EXPLOG.REFLECT.MIN_PATH","AP+BP 최소 55, AC=a+55, a+b","중상","② (log₃12)","27u+b=a+55, a+3=u+b → 3ᵃ=2","4",c=M,i=M,mid="지수함수와 로그함수의 관계",tags="역함수;최단거리;지수함수;로그함수")
b(57,"지수함수와 로그함수의 관계","EXPLOG.INVERSE_SHIFT.SEGMENT","y=−x+2k, log₂(x−k), 2^{x+1}+k+1, AB=7√2, k","중상","④ (log₂24)","g⁻¹=f(x−1)−1, A x=k+3","4",fig=GR,c=M,i=M,mid="지수함수와 로그함수의 관계",tags="역함수;지수함수;로그함수")
b(58,"지수함수와 로그함수의 관계","EXPLOG.INVERSE.FOUR_POINTS","−log₃x+4, 3^{−x+4}, y=−x+k, AD−BC=4√2, k","중상","② (17/4+2log₃2)","대칭 A↔D, B↔C; 수치 확인 k≈5.5119 (A x=1/4, B x=9/4)","4",fig=GR,c=M,i=M,mid="지수함수와 로그함수의 관계",tags="역함수;지수함수;로그함수")
DS = {1:"2025.6 고2 20",2:"2020.6 고2 20",3:"2024.6 고2 21",4:"2023.6 고2 30",5:"2022.11 고2 30"}
def d(n, page, small, tid, tname, ans, chk, fmt=MC, **kw):
    a(f"도전{n:02d}", page, f"학평 {DS[n]}번 (26456-{180+n:04d})", small, tid, tname, "상", ans, chk, "4", fmt, c=H, i=H, **kw)
d(1,52,"지수함수의 그래프","EXPF.ABS_PARABOLA.PIECEWISE_ROOTS","|2^{−x+3}−2|=−x²+tx−4 근 α, β, f(x)=f(t/2) 실근 2개 t 최소","① (2√6)","f(t/2)=t²/4−4≥2 (우측 점근 2); 수치 확인",**E)
d(2,52,"로그함수의 그래프","LOGF.TWO_BASES.STATEMENTS","logₐx, log_{a+2}x, y=2, 보기","⑤ (ㄱ, ㄴ, ㄷ)","S₂/S₁=logₐ(a+2)",**Lg)
d(3,53,"지수함수와 로그함수의 관계","EXPLOG.INVERSE.LARGER_ROOT_FLOOR","3ˣ−n=x 큰 근 g(n), h(n)=⌊g⌋, h(n)<h(n+1) n 합","② (105)","3ᵐ−m=n+1 → n=6,23,76 (수치 확인)",mid="지수함수와 로그함수의 관계",tags="역함수;지수함수")
d(4,53,"지수함수의 그래프","EXPF.ABS_COMPOSITE.INTERSECT_COUNT","g=a^{|f|}, f=|x−k|−4, y=16 교점 3, g(1)=16, f(a−2) 합","5","a=2, k∈{1,9,−7}",fmt=S_,**E)
d(5,53,"지수함수의 그래프","EXPF.PIECEWISE_ABS.UNIQUE_K","|f|와 y=k 두 점 만나는 k 유일, 2^{M+m}=p+√q","4","2ᵃ∈[(2+√2)/2, 2] (수치 확인) → 2+√2",fmt=S_,**E)
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{766+i}", ROWS[i*10:(i+1)*10], 15902+i*10)
