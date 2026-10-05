from cfgex import *
MC, S_, D = "객관식(5지선다)", "단답형", "서술형"
M, H = "보통", "높음"
Q = [582]  # A00639 ch01-09 q=1..582
CH = "10 수학적 귀납법"
def a(lab, page, src, small, tid, tname, diff, ans, chk, pts, fmt=MC, nsub=1, mid="수학적 귀납법", tags="수열;귀납적 정의;수학적 귀납법", **kw):
    Q[0] += 1
    kw.setdefault("atype", "선택지" if fmt == MC else "값")
    R(Q[0], page, "수열", mid, small, tid, tname, tags, diff, fmt, ans, src, chk, label="10-"+lab, pts=pts, nsub=nsub, **kw)
    r = ROWS[-1]; r.update({"출처대분류": "시판 기출문제집(전국연합학력평가 고2 재수록)", "학교명": "", "주관기관": "EBS(올림포스)",
        "학교/시험명": f"올림포스 전국연합학력평가 기출문제집 대수 {CH} {lab}", "메모": r["메모"].replace("P1 학교기출", "P1 시판 기출문제집(올림포스); 원출처 학평 고2 (OFFICIAL 근접중복 가능)")})
setup("A00639", "1c09Ezx8TegfVDXf--6ArRwp9hTP2vy53", "올림포스 기출 대수.pdf", "p3/A00639.pdf", "올림포스(EBS)", "2026학년도", "전국연합학력평가 기출문제집", "고2", "대수", CURR="2022 개정",
      VIS="스캔 PDF(텍스트층 없음) 95dpi 렌더 시각판독 PARTIAL p140~151 (10 수학적 귀납법; p152 MEMO 빈 면)", TEXT="텍스트층 없음 — 렌더 판독; 정답과 풀이 별책 미보유")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
RC = dict(mid="수열의 귀납적 정의", tags="수열;귀납적 정의;점화식")
MI = dict(mid="수학적 귀납법", tags="수열;수학적 귀납법;증명 빈칸")
G = "개념 확인 문제"
a("개념01",141,G,"수열의 귀납적 정의","REC.EVAL.FIFTH_TERM","귀납적 정의 제5항 4가지","하","(1) −7 (2) 16 (3) 11 (4) 24","","",fmt=D,nsub=4,**RC)
a("개념02",141,G,"등차수열의 귀납적 정의","REC.ARITH.SUM_TERMS","a₁=3, a_{n+1}=aₙ+5, a₈+a₉+a₁₀","하","129","aₙ=5n−2","",fmt=S_,**RC)
a("개념03",141,G,"등비수열의 귀납적 정의","REC.GEOM.TERM","a₁=8, 2a_{n+1}=aₙ, 1/a₁₀","하","64","","",fmt=S_,**RC)
a("개념04",141,G,"여러 가지 수열의 귀납적 정의","REC.PERIODIC.TERM","a₁=3, a_{n+1}=1/(1−aₙ), a₁₀₀","하","3","주기 3","",fmt=S_,**RC)
a("개념05",141,G,"여러 가지 수열의 귀납적 정의","REC.ADD_FUNC.TERM","a₁=1, a_{n+1}=aₙ+2ⁿ, a₆","하","63","aₙ=2ⁿ−1","",fmt=S_,**RC)
a("개념06",141,G,"여러 가지 수열의 귀납적 정의","REC.MULT_FUNC.TERM","a₁=1, a_{n+1}=aₙ/(n+1), a₁₀","하","1/10! (=1/3628800)","","",fmt=S_,**RC)
a("개념07",141,G,"여러 가지 수열의 귀납적 정의","REC.LINEAR.TERM","a₁=1, a_{n+1}=2aₙ+1, a₁₀","하","1023","aₙ+1=2ⁿ","",fmt=S_,**RC)
a("개념08",141,G,"여러 가지 수열의 귀납적 정의","REC.PARITY_PIECEWISE.TERM","a_{n+1}=3aₙ(홀)/aₙ(짝), log₃a₁₀","하","5","a_{2k}=3ᵏ","",fmt=S_,**RC)
a("개념09",141,G,"수학적 귀납법","INDUCTION.INEQUALITY.FILL_BLANK","1+3+…+(2n−1)>(n−1)² 증명 빈칸","하","(가) 0 (나) (k−1)² (다) k²","","",fmt=D,nsub=3,**MI)
S = {1:"2019.9 고2 나형 13",2:"2018.9 고2 나형 28",3:"2017.11 고2 나형 28",4:"2023.9 고2 17",5:"2021.9 고2 12",6:"2019.9 고2 가형 9",7:"2020.9 고2 7",8:"2018.6 고2 가형 25",9:"2018.3 고2 나형 26",10:"2023.9 고2 13",
11:"2022.11 고2 14",12:"2018.11 고2 나형 19",13:"2022.9 고2 13",14:"2021.9 고2 18",15:"2024.10 고2 21",16:"2021.9 고2 16",17:"2019.9 고2 가형 18/나형 18",18:"2017.3 고2 나형 17",19:"2018.9 고2 나형 18",20:"2018.3 고2 나형 18",
21:"2016.11 고2 나형 19",22:"2020.9 고2 20",23:"2017.6 고2 나형 17",24:"2013.9 고2 B형 16",25:"2016.6 고2 나형 20"}
PG = {}
for p, rg in [(142,range(1,5)),(143,range(5,9)),(144,range(9,13)),(145,range(13,16)),(146,range(16,18)),(147,range(18,20)),(148,range(20,22)),(149,range(22,24)),(150,range(24,26))]:
    for i in rg: PG[i] = p
def b(n, small, tid, tname, diff, ans, chk, pts, fmt=MC, **kw):
    a(f"{n:02d}", PG[n], f"학평 {S[n]}번 (26456-{n+475:04d})", small, tid, tname, diff, ans, chk, pts, fmt, **kw)
b(1,"등차수열·등비수열의 귀납적 정의","REC.PARITY_PIECEWISE.TERM","a₁=3, +3(홀)/×2(짝), a₆","하","③ (33)","3,6,12,15,30,33","3",**RC)
b(2,"등차수열·등비수열의 귀납적 정의","REC.THRESHOLD_PIECEWISE.SUM","a₁=88, −3(≥65)/÷2(<65), Σ₁¹⁵","중","747","직접 계산","4",S_,c=M,**RC)
b(3,"등차수열·등비수열의 귀납적 정의","REC.DOUBLE_ROOT.ARITH","x²−2√aₙx+a_{n+1}−3=0 중근, a₁=2, a₁₀","중하","29","a_{n+1}=aₙ+3","4",S_,c=M,**RC)
b(4,"등차수열·등비수열의 귀납적 정의","REC.ARITH.AMGM_MIN","2a_{n+1}=aₙ+a_{n+2}, a₃a₂₂=a₇a₈+10, a₄+a₆ 최소","중","④ (8)","a₁d=1, 2a₁+8d≥8","4",c=M,**RC)
b(5,"여러 가지 수열의 귀납적 정의","REC.LOG_EXP_PIECEWISE.BACKWARD","log₂aₙ(홀)/2^{aₙ+1}(짝), a₈=5, a₆+a₇","중하","① (36)","a₈=a₆+1","3",c=M,**RC)
b(6,"여러 가지 수열의 귀납적 정의","REC.ADD_FUNC.TERM","a₁=6, a_{n+1}=aₙ+3ⁿ, a₄","하","③ (45)","","3",**RC)
b(7,"여러 가지 수열의 귀납적 정의","REC.LINEAR.BACKWARD","a_{n+1}=2aₙ+1, a₄=31, a₂","하","① (7)","","3",**RC)
b(8,"여러 가지 수열의 귀납적 정의","REC.QUOTIENT_SEQ.ALTERNATING_SUM","aₙ=⌊n/3⌋, bₙ=(−1)^{n−1}5^{aₙ}, Σ₁⁹b","중하","105","1−1+5−5+5−25+25−25+125","3",S_,c=M,**RC)
b(9,"여러 가지 수열의 귀납적 정의","REC.PARITY_HALVING.BACKWARD","a₃=3, (aₙ+3)/2(홀)/aₙ/2(짝), a₁≥10, Σ₁⁵","중","27","a₁=12 (역추적 전수)","4",S_,c=M,trap=M,**RC)
b(10,"여러 가지 수열의 귀납적 정의","REC.THRESHOLD_PIECEWISE.PERIODIC_SUM","a₁=2, 2aₙ−1(<8)/aₙ/3(≥8), Σ₁¹⁶","중하","④ (87)","2,3,5,9,3,… 주기 4","3",c=M,**RC)
b(11,"여러 가지 수열의 귀납적 정의","REC.SIGN_PIECEWISE.PERIODIC_SUM","a₁=1, aₙ−4(≥0)/aₙ²(<0), Σ₁²²","중","③ (58)","1,−3,9,5,1 주기 4","4",c=M,**RC)
b(12,"여러 가지 수열의 귀납적 정의","REC.ADJACENT_SUM.SOLVE","a_{n+1}+aₙ=2n², a₃+a₅=26, a₂","중하","② (2)","","4",c=M,**RC)
b(13,"여러 가지 수열의 귀납적 정의","REC.PERIODIC.PARTIAL_SUM","a₁=1/2, a_{n+1}=−1/(aₙ−1), Sₘ=11, m","중하","③ (22)","주기 3 (1/2, 2, −1) 합 3/2","3",c=M,**RC)
b(14,"여러 가지 수열의 귀납적 정의","REC.COUPLED_TRIG.PERIODIC","a₁=1, b₁=−1, a_{n+1}=aₙ+bₙ, b_{n+1}=2cos(aₙπ/3), a₂₀₂₁−b₂₀₂₁","중상","⑤ (6)","주기 확인 (수치 계산)","4",c=M,i=M,**RC)
b(15,"여러 가지 수열의 귀납적 정의","REC.THRESHOLD_PIECEWISE.PARAM","a₁≥2, aₙ/2(≥1)/(aₙ+a₁)/2(<1), a₅+2a₆=2, a₁ 합","중상","③ (96/5)","a₁=16/5, 16 (수치 확인)","4",c=M,i=M,trap=M,**RC)
b(16,"수학적 귀납법(등식)","INDUCTION.HARMONIC_WEIGHTED.FILL_BLANK","aₙ=Σ1/k, Σkaₖ=n(n+1)(2a_{n+1}−1)/4 증명 빈칸, p+f(5)/g(3)","중","⑤ (13)","p=1/2, f=m/2, g=1/(m+2)","4",c=M,**MI)
b(17,"수학적 귀납법(등식)","INDUCTION.PARTIAL_SUMS.FILL_BLANK","(n+1)Sₙ−ΣS_k=Σk³ 증명 빈칸, f(2)+g(1)","중","⑤ (11)","f=m+1, g=(m+1)³","4",c=M,**MI)
b(18,"수학적 귀납법(등식)","INDUCTION.DIVISIBILITY.FILL_BLANK","f(3^{2n}+1)=1 증명 빈칸, a+g(11)","중","② (97)","a=2, g(p)=9p−4","4",c=M,**MI)
b(19,"수학적 귀납법(등식)","INDUCTION.SIGMA_PRODUCT.FILL_BLANK","1·2n+3(2n−2)+…=n(n+1)(2n+1)/3 과정 빈칸, f(a)g(a)","중","② (55)","f=2k−1, a=3, g=4n−1","4",c=M,**MI)
b(20,"수학적 귀납법(등식)","INDUCTION.NESTED_SUM.FILL_BLANK","Σk{k+…+n}=n(n+1)(n+2)(3n+1)/24 증명 빈칸, f(4)+g(2)","중","① (34)","f=(m+1)², g=m(m+1)²/2","4",c=M,**MI)
b(21,"수학적 귀납법(등식)","INDUCTION.ARITH_GEOM_SUM.FILL_BLANK","Σ(2k−1)2^{k−1}=(2n−3)2ⁿ+3 증명 빈칸, f(4)g(2)","중하","⑤ (27)","f=2m+1, g=2m−1","4",c=M,**MI)
b(22,"수학적 귀납법(등식)","INDUCTION.ALTERNATING_HARMONIC.FILL_BLANK","Σ(−1)^{k−1}/k (2n항)=Σ1/(n+k) 증명 빈칸, a+g(5)/f(14)","중","③ (11/2)","a=1/2, f=−1/(2m+2), g=−1/(m+1)","4",c=M,trap=M,**MI)
b(23,"수학적 귀납법(부등식)","INDUCTION.HARMONIC_INEQ.FILL_BLANK","(1+1/2+…+1/n)(1+…+n)>n² 증명 빈칸, 8p·f(10)","중","⑤ (22)","p=3/2, f(k)=2(k+1)/(k+2)","4",c=M,**MI)
b(24,"수학적 귀납법(부등식)","INDUCTION.RECIPROCAL_CUBE_INEQ.FILL_BLANK","Σ1/k³<(1/2)(3−1/n²) 증명 빈칸, g(a)/f(1)","중","① (35)","a=9/8, f=1/(m+1)³, g=3m+1","4",c=M,**MI)
b(25,"수학적 귀납법(부등식)","INDUCTION.WEIGHTED_GEOM_INEQ.FILL_BLANK","Σn/(n−k)·1/2^{k−1}<4 과정 빈칸, 48g(10)/f(5)","중","② (22)","f=(n+1)/n, g=(n+1)/(2n)","4",c=M,**MI)
DS = {1:"2025.9 고2 20",2:"2024.9 고2 30",3:"2023.11 고2 21"}
def d(n, tid, tname, ans, chk, fmt=MC, **kw):
    a(f"도전{n:02d}", 151, f"학평 {DS[n]}번 (26456-{500+n:04d})", "여러 가지 수열의 귀납적 정의", tid, tname, "상", ans, chk, "4", fmt, c=H, i=H, **RC, **kw)
d(1,"REC.PARITY_PIECEWISE.BOUNDED_MAX","자연수 수열 (aₙ+3)/2(홀)/(3/2)aₙ(짝), aₙ≤a₃, a₄+a₅≤24, a₁ 합","① (31)","a₁=1,2,3,4,9,12 (전수 확인)")
d(2,"REC.SIGN_PIECEWISE.RETURN_ZERO","aₙ+d(≥0)/raₙ(<0), aₖ=a_{k+12}=0, a₂+a₃=0, a₅=16, a₁ 합","28","a₁=−2, 6, 24 (전수 확인)",fmt=S_)
d(3,"REC.PARITY_SUM.BACKWARD_RANGE","a₅=63, a_{n+2}=a_{n+1}+aₙ(곱 홀)/−2(곱 짝), a₁ 최대−최소","④ (25)","M=30, m=5 (전수 확인)")
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{812+i}", ROWS[i*10:(i+1)*10], 16337+i*10)
