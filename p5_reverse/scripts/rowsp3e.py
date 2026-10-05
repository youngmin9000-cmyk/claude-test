from cfgex import *
MC, S_, D = "객관식(5지선다)", "단답형", "서술형"
M, H = "보통", "높음"
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
Q = [69]  # A00639 ch01 q=1..69
CH = "02 로그"
def a(lab, page, src, small, tid, tname, diff, ans, chk, pts, fmt=MC, nsub=1, **kw):
    Q[0] += 1
    kw.setdefault("atype", "선택지" if fmt == MC else "값")
    R(Q[0], page, "지수함수와 로그함수", "로그", small, tid, tname, "로그;로그의 성질", diff, fmt, ans, src, chk, label="02-"+lab, pts=pts, nsub=nsub, **kw)
    r = ROWS[-1]; r.update({"출처대분류": "시판 기출문제집(전국연합학력평가 고2 재수록)", "학교명": "", "주관기관": "EBS(올림포스)",
        "학교/시험명": f"올림포스 전국연합학력평가 기출문제집 대수 {CH} {lab}", "메모": r["메모"].replace("P1 학교기출", "P1 시판 기출문제집(올림포스); 원출처 학평 고2 (OFFICIAL 근접중복 가능)")})
setup("A00639", "1c09Ezx8TegfVDXf--6ArRwp9hTP2vy53", "올림포스 기출 대수.pdf", "p3/A00639.pdf", "올림포스(EBS)", "2026학년도", "전국연합학력평가 기출문제집", "고2", "대수", CURR="2022 개정",
      VIS="스캔 PDF(텍스트층 없음) 95dpi 렌더 시각판독(일부 220~260dpi 확대) PARTIAL p18~33 (02 로그)", TEXT="텍스트층 없음 — 렌더 판독; 정답과 풀이 별책 미보유")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
G = "개념 확인 문제"
a("개념01",19,G,"로그의 정의","LOG.DEF.CONVERT","지수↔로그 변환 4가지","하","(1) log₃81=4 (2) log₂(1/8)=−3 (3) (1/5)⁻³=125 (4) 10⁻²=0.01","","",fmt=D,nsub=4)
a("개념02",19,G,"로그의 정의","LOG.DOMAIN.BASE_ARG","로그 정의 x 범위 2가지","하","(1) x>4 (2) 2<x<3 또는 x>3","밑 조건 x−2>0, ≠1","",fmt=D,nsub=2)
a("개념03",19,G,"로그의 정의","LOG.EVAL.BASIC","로그 값 4가지","하","(1) 4 (2) 1/2 (3) −4 (4) −4","","",fmt=D,nsub=4)
a("개념04",19,G,"로그의 성질","LOG.PROPERTIES.SIMPLIFY","로그식 간단히 2가지","하","(1) 1 (2) 9/2","(2) log₂16+1/2","",fmt=D,nsub=2)
a("개념05",19,G,"로그의 밑의 변환","LOG.BASE_POWER.EVAL","log₉27, log₈(1/16)","하","(1) 3/2 (2) −4/3","","",fmt=D,nsub=2)
a("개념06",19,G,"로그의 성질","LOG.PROPERTIES.EVAL","로그식 값 4가지","하","(1) 2 (2) −1 (3) 3 (4) −2","","",fmt=D,nsub=4)
a("개념07",19,G,"로그의 성질","LOG.PROPERTIES.SIMPLIFY","로그식 간단히 2가지","하","(1) 1/2 (2) log₃8 (=3log₃2)","(2) log₃4+½log₃4","",fmt=D,nsub=2)
a("개념08",19,G,"로그의 밑의 변환","LOG.EXPRESS.AB","log2=a, log3=b로 log6, log₃36","하","(1) a+b (2) 2(a+b)/b","","",fmt=D,nsub=2)
a("개념09",19,G,"상용로그","LOG.COMMON.SHIFT","log3.14=0.4969로 log314, log0.0314","하","(1) 2.4969 (2) −1.5031","","",fmt=D,nsub=2)
a("개념10",19,G,"상용로그","LOG.COMMON.FROM_LOG23","log12, log0.6","하","(1) 1.0791 (2) −0.2219","","",fmt=D,nsub=2)
a("개념11",19,G,"상용로그","LOG.COMMON.CHARACTERISTIC","log156=a+0.1931, log0.0156=b+0.1931, a+b","하","0","a=2, b=−2","",fmt=S_)
a("개념12",19,G,"로그의 성질","LOG.TELESCOPE.PRODUCT","Σlog(1−1/k) k=2..100","하","−2","log(1/100)","",fmt=S_)
S = {1:"2024.10 고2 25",2:"2019.6 고2 나형 23",3:"2019.6 고2 가형 24",4:"2016.9 고2 가형 25",5:"2025.6 고2 15",6:"2024.6 고2 14",7:"2025.6 고2 2",8:"2017.11 고2 나형 3",9:"2017.9 고2 나형 4",10:"2024.6 고2 2",
11:"2023.9 고2 22",12:"2020.6 고2 2",13:"2019.6 고2 나형 4",14:"2018.9 고2 가형 22",15:"2021.6 고2 2",16:"2016.6 고2 가형 23",17:"2022.6 고2 2",18:"2019.6 고2 가형 2",19:"2016.6 고2 나형 23",20:"2022.11 고2 3",
21:"2023.6 고2 2",22:"2017.3 고2 가형 22",23:"2017.3 고2 나형 6",24:"2025.9 고2 24",25:"2024.9 고2 6",26:"2021.6 고2 7",27:"2019.9 고2 나형 17",28:"2018.6 고2 나형 28",29:"2024.10 고2 16",30:"2019.6 고2 나형 19",
31:"2020.6 고2 28",32:"2019.6 고2 가형 9",33:"2015.9 고2 나형 9",34:"2016.3 고2 나형 14",35:"2025.9 고2 13",36:"2023.9 고2 9",37:"2019.11 고2 가형 6",38:"2022.9 고2 24",39:"2022.6 고2 26",40:"2021.6 고2 27",
41:"2020.6 고2 26",42:"2024.6 고2 27",43:"2023.9 고2 16",44:"2023.11 고2 17",45:"2019.6 고2 가형 28",46:"2019.11 고2 가형 9",47:"2017.3 고2 나형 25",48:"2018.3 고2 나형 16",49:"2017.6 고2 가형 26",50:"2024.9 고2 26",
51:"2025.6 고2 5",52:"2024.6 고2 5",53:"2023.6 고2 5",54:"2021.6 고2 5",55:"2016.9 고2 나형 23",56:"2016.6 고3 나형 12",57:"2020.6 고2 13",58:"2016.3 고2 나형 9",59:"2016.6 고2 가형 12",60:"2014.9 고2 A형 14",
61:"2016.11 고2 나형 16",62:"2016.3 고2 가형 17"}
PG = {**{i:20 for i in range(1,7)}, **{i:21 for i in range(7,12)}, **{i:22 for i in range(12,18)}, **{i:23 for i in range(18,24)}, **{i:24 for i in range(24,30)}, **{i:25 for i in range(30,35)}, **{i:26 for i in range(35,40)}, **{i:27 for i in range(40,45)}, **{i:28 for i in range(45,51)}, **{i:29 for i in range(51,55)}, **{i:30 for i in range(55,59)}, **{i:31 for i in range(59,61)}, 61:32, 62:32}
def b(n, small, tid, tname, diff, ans, chk, pts, fmt=MC, **kw):
    a(f"{n:02d}", PG[n], f"학평 {S[n]}번 (26456-{n+56:04d})", small, tid, tname, diff, ans, chk, pts, fmt, **kw)
b(1,"로그의 정의","LOG.DOMAIN.ABS_BASE_INTEGER_COUNT","log_|a|(−a²−4a+21) 정의 정수 a 개수","중하","6","−7<a<3, a≠0,±1","3",S_,c=M,trap=M)
b(2,"로그의 정의","LOG.DOMAIN.ARG_NATURAL_SUM","log₃(6−x) 정의 자연수 x 합","하","15","","3",S_)
b(3,"로그의 정의","LOG.DOMAIN.BASE_ARG_INTEGER_COUNT","log_(a+3)(−a²+3a+28) 정수 a 개수","중하","8","−3<a<7, a≠−2","3",S_,trap=M)
b(4,"로그의 정의","LOG.DOMAIN.BASE_ARG_INTEGER_SUM","log_(x+6)(49−x²) 정수 x 합","중하","11","−6<x<7, x≠−5 → −4..6","3",S_,trap=M)
b(5,"로그의 정의","LOG.DOMAIN.ABS_BASE_COUNT_PARAM","log_|x+1|{(n−x)(n+1+x)} 정수 x 25개 n","중","② (14)","−n..n−1 중 −2,−1,0 제외 2n−3=25 (확대 판독 |x+1|)","4",c=M,trap=M)
b(6,"로그의 정의","LOG.DOMAIN.ALL_REAL_DISCRIMINANT","log_a(x²+ax+a+8) ∀x 정의 정수 a 합","중","① (27)","a²−4a−32<0, a>0, a≠1 → 2..7","4",c=M)
b(7,"로그의 성질","LOG.SUM.SAME_BASE","log₅(25/2)+log₅10","하","③ (3)","","2")
b(8,"로그의 성질","LOG.SUM.SAME_BASE","log₃1+log₃9","하","② (2)","","2")
b(9,"로그의 성질","LOG.SUM.SAME_BASE","log₃9+log₃√3","하","⑤ (5/2)","","3")
b(10,"로그의 성질","LOG.SUM.SAME_BASE","log₃24+log₃(3/8)","하","② (2)","","2")
b(11,"로그의 성질","LOG.SUM.SAME_BASE","log₂8+log₂(1/2)","하","2","","3",S_)
b(12,"로그의 성질","LOG.SUM.SAME_BASE","log₄2+log₄8","하","② (2)","","2")
b(13,"로그의 성질","LOG.SUM.SAME_BASE","log₂(4/3)+log₂12","하","④ (4)","","3")
b(14,"로그의 성질","LOG.SUM.SAME_BASE","log₅50+log₅(1/2)","하","2","","3",S_)
b(15,"로그의 성질","LOG.SUM.SAME_BASE","log₂√2+log₂2√2","하","② (2)","","2")
b(16,"로그의 성질","LOG.SUM.CONJUGATE","log₂(3+√5)+log₂(3−√5)","하","2","","3",S_)
b(17,"로그의 성질","LOG.DIFF.SAME_BASE","log₃36−log₃4","하","② (2)","","2")
b(18,"로그의 성질","LOG.DIFF.SAME_BASE","log₂12−log₂3","하","② (2)","","2")
b(19,"로그의 성질","LOG.DIFF.COEFF","log₃18−½log₃4","하","2","","3",S_)
b(20,"로그의 성질","LOG.DIFF.SAME_BASE","log₈₁12−log₈₁4","하","② (1/4)","","2")
b(21,"로그의 밑의 변환","LOG.RATIO.CHANGE_BASE","log₄64/log₄8","하","② (2)","","2")
b(22,"로그의 밑의 변환","LOG.PRODUCT.CHAIN","log₂3×log₃32","하","5","","3",S_)
b(23,"로그의 밑의 변환","LOG.PRODUCT.CHAIN","log₂(1/3)×log₃(1/4)","하","② (2)","","3")
b(24,"로그의 밑의 변환","LOG.PRODUCT.BASE_POWER","log₃25×(log₅9+log₂₅3)","하","5","2log₃5×(5/2)log₅3","3",S_)
b(25,"로그의 밑의 변환","LOG.PRODUCT.CHAIN_SUM","log₂5×log₅3+log₂(16/3)","하","④ (4)","","3")
b(26,"로그의 여러 가지 성질","LOG.EXP_OF_LOG.EVAL","(√2)^{1+log₂3}","하","① (√6)","2^{(1+log₂3)/2}","3")
b(27,"로그의 값이 자연수가 되는 조건","LOG.NATURAL.BASE_SUM","log_n4×log₂9 자연수 n 합","중","① (93)","4log_n3 → n=3,9,81","4",c=M)
b(28,"로그의 값이 자연수가 되는 조건","LOG.NATURAL.ARG_SUM","log₂(n/6) 자연수 n≤100 합","중하","180","12+24+48+96","4",S_)
b(29,"로그의 값이 자연수가 되는 조건","LOG.EQUATION.NATURAL_PAIR_MAX","log_n4×(4/log_m2+log₂n)=8, m+n 최대","중","④ (108)","log_n m=3/4 → (m,n)=(8,16),(27,81)","4",c=M)
b(30,"로그의 값이 자연수가 되는 조건","LOG.EXP_NATURAL.DIVISOR","{3^{log₂ab}/3^{(log₂a)(log₂b)}}⁵ 자연수 n 합","중","① (14)","3^{10/(n+1)} → n=1,4,9","4",c=M)
b(31,"로그의 값이 자연수가 되는 조건","LOG.SET.INTERSECTION_COUNT","A={√a}, B={log_√3 b}, n(C)=3 k 개수","중상","45","C=짝수 m, m²≤k, 3^{m/2}≤k → 36≤k≤80","4",S_,c=M,i=M,trap=M)
b(32,"로그의 밑의 변환","LOG.EXPRESS.CHANGE_BASE","log₅18 a,b로","하","⑤ ((a+2b)/(1−a))","log5=1−a","3")
b(33,"상용로그","LOG.EXPRESS.COMMON","log(12/5) a,b로","하","⑤ (3a+b−1)","","3")
b(34,"로그의 밑의 변환","LOG.EXPRESS.FUNCTION_SUB","f(x)=(x+1)/(2x−1), f(log₃6)","중하","⑤ ((a+2b)/(2a+b))","log₃6=(a+b)/b","4",c=M)
b(35,"로그의 성질","LOG.CONDITION.EVAL_RATIO","a³=b², log_a c=log_b c+1, log_c ab","중하","⑤ (5/6)","lnb=1.5lna, lnc=3lna","3",c=M)
b(36,"로그의 성질","LOG.CONDITION.SOLVE","log₂(m²+1/4)=−1, log₂m=5+3log₂n, m+n","하","③ (3/4)","m=1/2, n=1/4","3")
b(37,"로그의 성질","LOG.CONDITION.RATIO","log₉a³b=1+log₃ab, a/b","하","④ (9)","log₃a−log₃b=2","3")
b(38,"로그의 여러 가지 성질","LOG.EXP_OF_LOG.CHAIN","log₅2=a, log₂7=b, 25^{ab}","하","49","ab=log₅7","3",S_)
b(39,"로그의 밑의 변환","LOG.CONDITION.SOLVE_PAIR","log₁₆a=1/log_b4, log₆ab=3, a+b","중하","42","a=b², b³=216","4",S_,c=M)
b(40,"로그의 밑의 변환","LOG.CYCLIC_PRODUCT","log_a b=log_b c/2=log_c a/3=k, 120k³","중하","20","6k³=1","4",S_,c=M)
b(41,"로그의 밑의 변환","LOG.NESTED.SOLVE","log₂(log₄a)=1, log_a5×log₅b=3/2, a+b","중하","576","a=64, b=512","4",S_,c=M)
b(42,"로그의 밑의 변환","LOG.CONDITION.SQRT_BASE","log_a b=81, log_c√a=log_√b c, log_c b","중","18","AB=4C², C=9A/2 (확대 판독 √b)","4",S_,c=M)
b(43,"로그의 성질","EXP.EQUAL_POWERS.LOG_EVAL","2ᵃ=3ᵇ=c, a²+b²=2ab(a+b−1), log₆c","중","② (1/2)","(a+b)²=2ab(a+b) → 1/a+1/b=2","4",c=M,i=M)
b(44,"로그의 밑의 변환","LOG.CYCLIC_PRODUCT.NATURAL_COND","−4log_a b=54log_b c=log_c a, bc≤300 자연수 a 합","중상","⑤ (99)","k=−6, bc=a^{4/3} → a=8,27,64","4",c=M,i=M)
b(45,"로그의 성질의 활용","LOG.INEQUALITY.COUNT_FUNC","2≤log_n k<3 n 개수 f(k)=4 k 최대","중","80","n²≤k<n³; k=80 → n=5..8 (전수 확인)","4",S_,c=M)
b(46,"상용로그","LOG.COMMON.DIGIT_RANGE","10ⁿ<24¹⁰<10ⁿ⁺¹ n","하","② (13)","10log24=13.801","3")
b(47,"로그의 성질의 활용","LOG.SLOPE.PERPENDICULAR","A(−1,log₃a),B(3,log₃b) 기울기 1, b/a","하","81","log₃(b/a)=4","3",S_)
b(48,"로그의 성질의 활용","LOG.GRAPH_POINT.RECIPROCAL","y=1/x 위 (∛a,√b), log_a b+log_b a","중하","⑤ (−13/6)","log_a b=−2/3","4",c=M)
b(49,"로그의 성질의 활용","LOG.HOMOGENEOUS.RATIO_SUM","x²−4xy+y²=0, log₈a^{1/y}+log₈b^{1/x}=k, 27k","중하","36","k=(x²+y²)/(3xy)=4/3 (확대 판독 log₂, log₈)","4",S_,c=M,trap=M)
b(50,"로그의 성질의 활용","LOG.SET_EQUAL.NUMBER_LINE","A=B, PS=10/3, 30×QR","중상","60","t=log a∈(1,2): p=1−t<q=1/t−1<r=1/t+1<s=1+t, QR=2","4",S_,c=M,i=M)
b(51,"상용로그","LOG.COMMON.TABLE_READ","log0.183 (상용로그표)","하","④ (−0.7375)","0.2625−1","3")
b(52,"상용로그","LOG.COMMON.TABLE_READ","log43.5 (상용로그표)","하","① (1.6385)","","3")
b(53,"상용로그","LOG.COMMON.TABLE_READ","log619 (상용로그표)","하","④ (2.7917)","","3")
b(54,"상용로그","LOG.COMMON.TABLE_READ","log(3.14×10⁻²)","하","⑤ (−1.5031)","","3")
b(55,"상용로그","LOG.COMMON.ANTILOG","logA=2.1673, A","하","147","","3",S_)
b(56,"상용로그","LOG.COMMON.INTEGER_COND","¼log2²ⁿ+½log5ⁿ 정수 n≤50 개수","하","② (25)","n/2 정수","3")
b(57,"상용로그의 활용","LOG.APPLIED.MAGNITUDE","별 등급·광도 관계 k","하","④ (10^{7/5})","3.5=2.5logk","3")
b(58,"상용로그의 활용","LOG.APPLIED.COMPLEXITY","T/N=logN, T₂/T₁","하","① (15)","3000/200","3")
b(59,"상용로그의 활용","LOG.APPLIED.TRANSMISSION_LOSS","TL=10log(I/T), TL₁/TL₂=5/2, a","하","④ (32)","log a=2.5log4","3")
b(60,"상용로그의 활용","LOG.APPLIED.TYPHOON","V=4.86(1010−P)^{0.5}, V_A/V_B","중하","④ (1.483)","½log2.2=0.1712","4",c=M)
b(61,"상용로그의 활용","LOG.APPLIED.WELL_PUMPING","양수량 Q_A/Q_B","중하","⑤ (8/9)","log256/log512","4",c=M)
b(62,"상용로그의 활용","LOG.APPLIED.DRUG_ABSORPTION","T=c(logK−logE)/(K−E), a","중","② (4)","T_A=2clog2/K=3, T_B=(8/3)clog2/K","4",c=M)
DS = {1:"2019.11 고2 나형 21",2:"2022.6 고2 29",3:"2017.11 고2 나형 30",4:"2013.9 고2 B형 30"}
def d(n, small, tid, tname, ans, chk, fmt=MC, **kw):
    a(f"도전{n:02d}", 33, f"학평 {DS[n]}번 (26456-{118+n:04d})", small, tid, tname, "상", ans, chk, "4", fmt, c=H, i=H, **kw)
d(1,"로그의 값이 유리수가 되는 조건","LOG.RATIONAL_VALUE.SET_COUNT","4<a<b<200, log_a b 유리수 k 집합 원소 수","① (11)","전수 확인")
d(2,"로그의 값이 같아지는 조건","LOG.SET_INTERSECTION.BASE_POWER","A_m={log_m x}, n(A₄∩A_b)=4, b=2ᵏ 합","72","xᵏ=y² 전수 확인 → b=8,64",fmt=S_)
d(3,"로그의 값이 자연수가 되는 조건","LOG.SET_COUNT.POWER_TWO","n(A_m)=205 m 최대","127","a=2ᵗ, ab=2^{2n−t}; t≤6 → 205 (전수 확인)",fmt=S_)
d(4,"로그함수의 기울기","LOG.SECANT_SLOPE.MIN_M","(m,log_n m),(m+1,log_n(m+1)) 기울기<1/3 최소 m, f(3)+…+f(6)","9","f=3,2,2,2 (수치 확인)",fmt=S_)
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{758+i}", ROWS[i*10:(i+1)*10], 15824+i*10)
