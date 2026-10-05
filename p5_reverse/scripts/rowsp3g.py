from cfgex import *
MC, S_, D = "객관식(5지선다)", "단답형", "서술형"
M, H = "보통", "높음"
GR = "그래프"
Q = [224]  # A00639 ch01-03 q=1..224
CH = "04 지수함수와 로그함수의 활용"
def a(lab, page, src, small, tid, tname, diff, ans, chk, pts, fmt=MC, nsub=1, mid="지수방정식과 지수부등식", tags="지수방정식;지수부등식", **kw):
    Q[0] += 1
    kw.setdefault("atype", "선택지" if fmt == MC else "값")
    R(Q[0], page, "지수함수와 로그함수", mid, small, tid, tname, tags, diff, fmt, ans, src, chk, label="04-"+lab, pts=pts, nsub=nsub, **kw)
    r = ROWS[-1]; r.update({"출처대분류": "시판 기출문제집(전국연합학력평가 고2 재수록)", "학교명": "", "주관기관": "EBS(올림포스)",
        "학교/시험명": f"올림포스 전국연합학력평가 기출문제집 대수 {CH} {lab}", "메모": r["메모"].replace("P1 학교기출", "P1 시판 기출문제집(올림포스); 원출처 학평 고2 (OFFICIAL 근접중복 가능)")})
setup("A00639", "1c09Ezx8TegfVDXf--6ArRwp9hTP2vy53", "올림포스 기출 대수.pdf", "p3/A00639.pdf", "올림포스(EBS)", "2026학년도", "전국연합학력평가 기출문제집", "고2", "대수", CURR="2022 개정",
      VIS="스캔 PDF(텍스트층 없음) 95dpi 렌더 시각판독(일부 240~260dpi 확대) PARTIAL p54~67 (04 지수함수와 로그함수의 활용)", TEXT="텍스트층 없음 — 렌더 판독; 정답과 풀이 별책 미보유")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
E = dict(mid="지수방정식과 지수부등식", tags="지수방정식;지수부등식")
Lq = dict(mid="로그방정식과 로그부등식", tags="로그방정식;로그부등식")
AP = dict(mid="지수함수와 로그함수의 활용", tags="지수;로그;실생활 활용")
G = "개념 확인 문제"
a("개념01",55,G,"지수방정식","EXPEQ.SAME_BASE","지수방정식 3가지","하","(1) x=−5/2 (2) x=−3 (3) x=−1/3","","",fmt=D,nsub=3,**E)
a("개념02",55,G,"지수부등식","EXPINEQ.SAME_BASE","지수부등식 3가지","하","(1) x<9/4 (2) x≤4 (3) x<2","밑<1 부등호 반전","",fmt=D,nsub=3,**E)
a("개념03",55,G,"로그방정식","LOGEQ.SAME_BASE","로그방정식 3가지","하","(1) x=7 (2) x=7/5 (3) x=−1 또는 x=2","진수 조건 확인","",fmt=D,nsub=3,**Lq)
a("개념04",55,G,"로그부등식","LOGINEQ.SAME_BASE","로그부등식 3가지","중하","(1) 4<x≤6 (2) −2≤x<0 또는 2<x≤4 (3) x>7","진수 조건 확인","",fmt=D,nsub=3,c=M,trap=M,**Lq)
a("개념05",55,G,"지수방정식","EXPEQ.SUBSTITUTION.QUADRATIC","3^{2x}−2·3ˣ−3=0","하","x=1","t=3","",fmt=S_,**E)
a("개념06",55,G,"지수부등식","EXPINEQ.SUBSTITUTION.NATURAL_SUM","3^{2x+1}−26·3ˣ−9≤0 자연수 x 합","하","3","(3t+1)(t−9)≤0 → x≤2","",fmt=S_,**E)
a("개념07",55,G,"로그방정식","LOGEQ.SUBSTITUTION.QUADRATIC","(logx)²+2logx−3=0","하","x=10 또는 x=1/1000","","",fmt=S_,**Lq)
a("개념08",55,G,"지수방정식의 활용","EXPEQ.APPLIED.GROWTH","박테리아 aˣ, 2시간 16마리, 1024마리 이상 최소 시간","하","5시간","a=4, 4ˣ≥1024","",fmt=S_,**AP)
a("개념09",55,G,"로그방정식","LOGEQ.TELESCOPE_SUM","Σlog₂(1+1/k)=5 n","하","31","log₂(n+1)=5","",fmt=S_,**Lq)
a("개념10",55,G,"지수방정식의 활용","EXPEQ.APPLIED.HEATING","3^{T−T₀}=(7t+6)ᵏ, 570°C 도달 시각","중하","723/7분 (≈103.3분)","k=90 (3²⁷⁰=27ᵏ), 7t+6=3⁶=729; 비정수 결과 — 원문 확대 판독 일치","",fmt=S_,c=M,review="REVIEW-정답지미연결;REVIEW-비정수결과확인",**AP)
a("개념11",55,G,"지수방정식의 활용","EXPEQ.APPLIED.NEWTON_COOLING","T=T_S+D·10^{−kt}, 75°C→10분 후 50°C, k","하","0.0301","10^{−10k}=1/2","",fmt=S_,**AP)
S = {1:"2025.6 고2 23",2:"2024.10 고2 22",3:"2025.9 고2 22",4:"2014.9 고2 A형 4",5:"2017.4 고3 가형 6",6:"2021.6 고2 11",7:"2022.9 고2 23",8:"2023.9 고2 25",9:"2019.9 고2 가형 24",10:"2019.10 고3 가형 6",
11:"2019.11 고2 가형 23",12:"2021.11 고2 5",13:"2022.6 고2 24",14:"2023.6 고2 13",15:"2021.6 고2 19",16:"2024.6 고2 13",17:"2020.6 고2 12",18:"2020.9 고2 28",19:"2024.6 고2 23",20:"2023.6 고2 23",
21:"2022.6 고2 23",22:"2021.11 고2 24",23:"2023.11 고2 25",24:"2012.11 고2 A형 4",25:"2015.4 고3 B형 5",26:"2019.6 고2 나형 26",27:"2012.9 고2 A형 9",28:"2014.9 고2 A형 9",29:"2022.11 고2 18",30:"2025.9 고2 9",
31:"2025.6 고2 24",32:"2022.6 고2 12",33:"2019.6 고2 가형 13",34:"2021.9 고2 27",35:"2020.9 고2 15",36:"2013.11 고2 A형 9",37:"2011.11 고2 나형 14",38:"2012.11 고2 A형 26",39:"2020.9 고2 18",40:"2012.9 고2 A형 24",
41:"2025.9 고2 11",42:"2023.6 고2 18",43:"2022.9 고2 19",44:"2019.9 고2 가형 27",45:"2019.6 고2 가형 27",46:"2015.11 고2 가형 11",47:"2024.9 고2 11",48:"2025.6 고2 28",49:"2015.11 고2 가형 12",50:"2013.9 고2 A형 9",
51:"2016.11 고2 가형 12",52:"2021.6 고2 12"}
PG = {}
for p, rg in [(56,range(1,7)),(57,range(7,13)),(58,range(13,19)),(59,range(19,26)),(60,range(26,30)),(61,range(30,36)),(62,range(36,40)),(63,range(40,43)),(64,range(43,45)),(65,range(45,49)),(66,range(49,53))]:
    for i in rg: PG[i] = p
def b(n, small, tid, tname, diff, ans, chk, pts, fmt=MC, **kw):
    a(f"{n:02d}", PG[n], f"학평 {S[n]}번 (26456-{n+185:04d})", small, tid, tname, diff, ans, chk, pts, fmt, **kw)
b(1,"지수방정식","EXPEQ.SAME_BASE","3^{4−x}=9^{x−7}","하","6","4−x=2x−14","3",S_,**E)
b(2,"지수방정식","EXPEQ.SAME_BASE","(√3)^{x−2}=27","하","8","","3",S_,**E)
b(3,"지수방정식","EXPEQ.SAME_BASE","25ˣ=(1/5)^{x−9}","하","3","","3",S_,**E)
b(4,"지수방정식","EXPEQ.SAME_BASE","(9/4)ˣ=(2/3)^{1+x}","하","② (−1/3)","","3",**E)
b(5,"지수방정식","EXPEQ.SAME_BASE","(1/8)^{2−x}=2^{x+4}","하","⑤ (5)","","3",**E)
b(6,"지수방정식","EXPEQ.SAME_BASE.QUADRATIC_EXP","2^{x−6}=(1/4)^{x²} 해 합","하","⑤ (−1/2)","2x²+x−6=0","3",**E)
b(7,"지수방정식","EXPEQ.SUBSTITUTION.QUADRATIC","4ˣ−15·2^{x+1}−64=0","하","5","t=32","3",S_,**E)
b(8,"지수방정식","EXPEQ.SUBSTITUTION.ROOT_SQUARES","9ˣ−10·3^{x+1}+81=0, α²+β²","하","10","t=27, 3","3",S_,**E)
b(9,"지수방정식","EXPEQ.SUBSTITUTION.RECIPROCAL","3ˣ−3^{4−x}=24","하","3","t²−24t−81=0","3",S_,**E)
b(10,"지수방정식","EXPEQ.SUBSTITUTION.UNIQUE_ROOT","4ˣ−k·2^{x+1}+16=0 유일 실근 a, k+a","중하","④ (6)","중근 t=4, k=4","3",c=M,trap=M,**E)
b(11,"지수부등식","EXPINEQ.SAME_BASE.NATURAL_SUM","4^{x−2}≤32 자연수 x 합","하","10","x≤9/2","3",S_,**E)
b(12,"지수부등식","EXPINEQ.SAME_BASE.COUNT","(1/3)^{x−7}≥9 자연수 개수","하","② (5)","x≤5","3",**E)
b(13,"지수부등식","EXPINEQ.SAME_BASE.COUNT","(1/5)^{x−1}≤5^{7−2x} 자연수 개수","하","6","x≤6","3",S_,**E)
b(14,"지수부등식","EXPINEQ.PRODUCT_SIGN.COUNT","(2ˣ−8)(1/3ˣ−9)≥0 정수 개수","중하","① (6)","−2≤x≤3","3",c=M,trap=M,**E)
b(15,"지수부등식","EXPINEQ.CONJUGATE_BASE.PAIR_COUNT","(√2−1)ᵐ≥(3−2√2)^{5−n} (m,n) 개수","중","④ (20)","m≤10−2n","4",c=M,trap=M,**E)
b(16,"지수부등식","EXPINEQ.SUBSTITUTION.COUNT","2^{2x+3}+2≤17·2ˣ 정수 개수","하","③ (5)","1/8≤t≤2","3",**E)
b(17,"지수부등식","EXPINEQ.SUBSTITUTION.NATURAL_SUM","4ˣ−10·2ˣ+16≤0 자연수 합","하","④ (6)","2≤t≤8","3",**E)
b(18,"지수부등식","EXPINEQ.SUBSTITUTION.PARAM_COUNT","(1/4)ˣ−(3n+16)(1/2)ˣ+48n≤0 정수해 2개 n 개수","중상","12","s∈[16,3n] 또는 [3n,16] → n=2, 11~21","4",S_,c=M,i=M,trap=M,**E)
b(19,"로그방정식","LOGEQ.DEFINITION","log₄(x−1)=3","하","65","","3",S_,**Lq)
b(20,"로그방정식","LOGEQ.DEFINITION","log_{1/2}(x+3)=−4","하","13","","3",S_,**Lq)
b(21,"로그방정식","LOGEQ.DEFINITION","log₅(x+1)=2","하","24","","3",S_,**Lq)
b(22,"로그방정식","LOGEQ.SAME_BASE.DOMAIN","2log₄(x−3)+log₂(x−10)=3","하","11","(x−3)(x−10)=8, x>10","3",S_,trap=M,**Lq)
b(23,"로그방정식","LOGEQ.RECIPROCAL_SUB.PRODUCT","log₂x−3=log_x16 해의 곱","하","8","t²−3t−4=0","3",S_,**Lq)
b(24,"로그방정식","LOGEQ.SUBSTITUTION.SUM","(log₃x)²−4log₃x+3=0, α+β","하","③ (30)","3+27","3",**Lq)
b(25,"로그방정식","LOGEQ.SUBSTITUTION.PRODUCT","(log₃x)²+4log₉x−3=0 해의 곱","하","① (1/9)","t=1, −3","3",**Lq)
b(26,"로그방정식","LOGEQ.SUBSTITUTION.PRODUCT","(log₂(x/2))(log₂4x)=4, 64αβ","중하","32","t²+t−6=0 → αβ=1/2","4",S_,c=M,**Lq)
b(27,"로그방정식","LOGEQ.SUBSTITUTION.VIETA_PRODUCT","(log₄x)²+log₄(1/x³)−1=0, αβ","하","④ (64)","t합 3","3",**Lq)
b(28,"로그방정식","LOGEQ.REMAINDER_THEOREM","x²+2x+3을 x−log₂a, x−log₂2a로 나눈 나머지 같음, a","중하","① (√2/4)","u+(u+1)=−2","3",c=M,**Lq)
b(29,"로그방정식","LOGEQ.FUNCTIONAL.FILL_BLANK","f=2^{1/log₂x}, 8f(f(x))=f(x²) 해의 곱 과정, p×q×g(4)","중","⑤ (3/4)","(가)3 (나)log₂x (다)1/8","4",c=M,**Lq)
b(30,"로그부등식","LOGINEQ.SAME_BASE.NATURAL_SUM","log(x−1)+log(x+2)≤1 자연수 합","하","① (5)","x=2,3","3",**Lq)
b(31,"로그부등식","LOGINEQ.DEFINITION.COUNT","log₂(x−1)<5 자연수 개수","하","31","1<x<33","3",S_,**Lq)
b(32,"로그부등식","LOGINEQ.CHANGE_BASE.INTEGER_RANGE","log₃(x+5)<8log₉2 정수 최대+최소","하","① (6)","−5<x<11","3",**Lq)
b(33,"로그부등식","LOGINEQ.CHANGE_BASE.NATURAL_SUM","log₄(x+3)−log₂(x−3)≥0 자연수 합","하","③ (15)","x+3≥(x−3)², x>3","3",trap=M,**Lq)
b(34,"로그부등식","LOGINEQ.ABS.INTEGER_SUM","log|x−1|+log(x+2)≤1 정수 합","중","4","x=−1,0,2,3 (x≠1)","4",S_,c=M,trap=M,**Lq)
b(35,"로그부등식","LOGINEQ.PARAM.INTEGER_COUNT","f=−log₃(mx+5) [−1,1], f(−1)<f(1) 정수 m 개수","중","④ (4)","m<0, −5<m<5","4",c=M,trap=M,**Lq)
b(36,"로그부등식","LOGINEQ.SUBSTITUTION.COUNT","(log₂x)²−log₂x⁶+8≤0 자연수 개수","하","② (13)","4≤x≤16","3",**Lq)
b(37,"로그부등식","LOGINEQ.SUBSTITUTION.SOLUTION_SET","(log_{1/9}x)(log₃(x/9))≥a 해 1/9≤x≤81, a","중하","① (−4)","t²−2t+2a≤0, 근 −2, 4","3",c=M,**Lq)
b(38,"로그부등식","LOGINEQ.ALL_X.DISCRIMINANT","(log₂(x/a))(log₂(x²/a))+2≥0 ∀x, M+16m","중","17","D=s²−16≤0 → a∈[1/16,16]","4",S_,c=M,**Lq)
b(39,"지수·로그방정식의 활용","EXPF.POINT_SYMMETRY.STATEMENTS","2ˣ, −(1/2)ˣ+t 교점·y절편 보기","중","⑤ (ㄱ, ㄴ, ㄷ)","(0,t/2) 점대칭, 넓이비 (t−2)/t","4",fig=GR,c=M,**E)
b(40,"지수·로그방정식의 활용","LOGEQ.SYSTEM.LINEAR","log₂x+log₂y=7, log₂x²−log₂y=−1, α+β","하","36","x=4, y=32","3",S_,**Lq)
b(41,"지수·로그방정식의 활용","LOGF.GRAPH.PARAM_FROM_POINTS","f=log₂(x+a)+b 그래프 (0,−2),(3,0), f(15)","하","② (2)","a=1, b=−2","3",fig=GR,**Lq)
b(42,"지수·로그방정식의 활용","EXPF.SYMMETRIC_CURVES.AREA_EQUAL","2^{x+1}, 2^{−x+1}, y=k, y=2k, 사다리꼴=삼각형 넓이, k","중","④ (2^{2/3})","(2−L)(k−1)=2L(k−1)","4",fig=GR,c=M,**E)
b(43,"지수·로그방정식의 활용","EXPLOG.REFLECT.MIDPOINT_STATEMENTS","log₂x, 2ˣ, (1/2)ˣ 삼각형 넓이비 2, 보기","중상","⑤ (ㄱ, ㄴ, ㄷ)","C=OB 중점, y₁=2/3, x₁=2^{2/3}","4",fig=GR,c=M,i=M,**Lq)
b(44,"지수·로그방정식의 활용","LOGF.COLLINEAR.RATIO_SLOPE","log₃(5x−3) 위 A, B, O 일직선, OA:OB=1:2, 기울기","중","11","10a−3=(5a−3)² → a=6/5, 기울기 5/6","4",S_,fig=GR,c=M,**Lq)
b(45,"지수·로그부등식의 활용","EXPINEQ.PIECEWISE_GRAPH","2^{f(x)}≤4ˣ 해 최대+최소 q/p, p+q","중하","71","f(x)≤2x → 6/5≤x≤12","4",S_,fig=GR,c=M,**E)
b(46,"지수·로그부등식의 활용","LOGINEQ.SET_INCLUSION.COUNT","A={log₄(log₂x)≤1}, B={x²−5ax+4a²<0}, B⊂A 자연수 a 개수","중하","① (4)","1<x≤16, a<x<4a","3",c=M,**Lq)
b(47,"지수·로그부등식의 활용","EXPLOG.SYSTEM_INEQ.RANGE","4ˣ−2ˣ−2<0, logₐx+1>0 해 1/5<x<b, a+b","하","① (6)","x<1, x>1/a","3",**Lq)
b(48,"지수·로그부등식의 활용","EXPINEQ.SEGMENT_CROSS.COUNT_FUNC","(1/2)^{x−k−2}, (1/2)^{x−k}−2, x=n 선분이 y=k와 만남, f(k)=15 k","중상","10","B≤k≤A 전수 확인","4",S_,c=M,i=M,**E)
b(49,"지수함수와 로그함수의 활용(실생활)","LOG.APPLIED.SOIL_COMPRESSION","압축지수 Cc, 간극비 0.1 하중강도 x","하","③ (12.8)","log(x/3.2)=2log2","3",**AP)
b(50,"지수함수와 로그함수의 활용(실생활)","EXP.APPLIED.GEOMETRIC_GROWTH","5km, 매주 10% 증가, 20km 이상 몇 번째","중하","② (16)","(n−1)·0.0414≥0.602","3",c=M,**AP)
b(51,"지수함수와 로그함수의 활용(실생활)","EXP.APPLIED.EARTHQUAKE","n=C_dC_g10^{(4/5)(x−9)}, a","하","④ (13/2)","10^{(4/5)(a−9)}=1/100","3",**AP)
b(52,"지수함수와 로그함수의 활용(실생활)","LOG.APPLIED.CHANNEL_CAPACITY","C=Wlog₂(1+S/N), a","하","④ (6)","1+186/a=32","3",**AP)
DS = {1:"2023.6 고2 20",2:"2020.6 고2 29",3:"2025.6 고2 30",4:"2019.6 고2 나형 30"}
def d(n, small, tid, tname, ans, chk, fmt=MC, **kw):
    a(f"도전{n:02d}", 67, f"학평 {DS[n]}번 (26456-{237+n:04d})", small, tid, tname, "상", ans, chk, "4", fmt, c=H, i=H, **kw)
d(1,"로그의 값이 유리수가 되는 조건","LOG.RATIONAL.MAX_SUM","a<b<a², logₐb 유리수, loga<3/2, a+b 최대","② (270)","a=27, b=243 (전수 확인)",mid="로그",tags="로그;유리수 조건")
d(2,"지수·로그방정식의 활용","LOGF.CIRCLE_INTERSECT.SIGN_COND","2log_{1/2}(x−7+k)+2와 원 x²+y²=64, ab<0, f(a)f(b)<0, M+m","24","k=8~16 (수치 확인)",fmt=S_,fig=GR,**Lq)
d(3,"로그부등식","LOGINEQ.BASE_SIGN.COUNT_COND","log_{2ᵏ} 조건 (가)(나) 0 아닌 정수 k 합","5","k=−11, 7, 9 (전수 확인)",fmt=S_,**Lq)
d(4,"지수·로그방정식의 활용","LOGF.INVERSE_EQ.POINT_SYMMETRY","f=g⁻¹ 해 −3/4, t, 5/4, 30(a+k+t)","75","k=1/4, a=2, t=1/4; k>1 경우 부적합 확인",fmt=S_,**Lq)
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{774+i}", ROWS[i*10:(i+1)*10], 15979+i*10)
