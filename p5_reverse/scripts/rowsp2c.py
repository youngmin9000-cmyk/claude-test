from cfgex import *
MC, D = "객관식(5지선다)", "서술형"
M, H = "보통", "높음"
def a(q, pg, big, mid, small, tid, tname, tags, diff, ans, summ, chk, pts, fmt=MC, **kw):
    kw.setdefault("atype", "선택지" if fmt == MC else "값"); R(q, pg, big, mid, small, tid, tname, tags, diff, fmt, ans, summ, chk, pts=pts, **kw)
EL, TR = "지수함수와 로그함수", "삼각함수"
G = dict(fig="그래프"); F = dict(fig="도형")
# ── A00847 대영고 2022 2-1 중간 수학Ⅰ (HWP 내 BMP 7장, 정답 미동봉 — 정답 zip A00848 20MB BLOCKED)
setup("A00847", "1kPo3ID07WibNQWByNWmYVjJKlkoO3K3A", "2022년 2학년 1학기 중간고사 수학1.hwp", "p2/A00847.hwp", "대영고", "2022학년도", "1학기 중간고사", "고2", "수학Ⅰ",
      VIS="HWP5 BinData BMP 7장(olefile 추출) 시각판독", TEXT="HWP 본문 텍스트 없음(그림 개체만)")
a(1, 1, EL, "지수", "지수법칙", "EXP.LAWS.MONOMIAL", "(a⁻⁵b³)²÷(a²b⁻³)³=aˣbʸ x+y", "지수법칙", "하", "② (−1)", "", "a⁻¹⁶b¹⁵", "4")
a(2, 1, EL, "지수함수", "지수부등식", "EXPINEQ.SAME_BASE.COUNT", "7^{x+1}≤7⁴ 자연수 x 개수", "지수부등식", "하", "③ (3)", "", "x≤3", "4")
a(3, 1, TR, "삼각함수", "호도법", "RADIAN.CONVERT", "45°=π/α, β°=π/6, α+β", "호도법", "하", "② (34)", "", "4+30", "4")
a(4, 1, EL, "로그", "로그의 성질", "LOG.SAME_BASE.COMBINE", "log₄16+log₄3−2log₄√6", "로그의 성질", "하", "⑤ (3/2)", "", "2+log₄(1/2)", "4.1")
a(5, 2, EL, "지수함수", "지수함수의 최대·최소", "EXPFUNC.INTERVAL.MAX_PARAM", "3^{x−1}+a [−1,2] 최댓값 5 a", "지수함수의 그래프", "하", "④ (2)", "", "3+a=5", "4.1")
a(6, 2, EL, "로그", "상용로그", "CLOG.MANTISSA.SAME", "log5.02=0.7007, loga=2.7007, logb=−0.2993, a/10+10b", "상용로그", "하", "① (55.22)", "", "a=502, b=0.502", "4.1")
a(7, 2, TR, "삼각함수", "삼각함수 사이의 관계", "TRIG.COS_GIVEN.SIN_TAN_Q3", "π<θ<3π/2, cosθ=−5/13, sinθ+tanθ", "삼각함수 사이의 관계", "하", "① (96/65)", "", "−12/13+12/5", "4.2")
a(8, 2, EL, "지수", "거듭제곱근", "ROOT.NESTED.EXPONENT_EQ", "√(a∛(a√a³))×∛(a⁴√aᵏ)=1 k", "거듭제곱근의 성질", "중하", "⑤ (−15)", "", "11/12+(4+k)/12=0", "4.2", c=M)
a(9, 3, EL, "로그", "로그의 성질", "LOG.BASE_CHANGE.EXPRESS_COEFF", "log5=a, log3=b, log₁₅24 계수 합", "밑 변환;상용로그", "중하", "⑤ (3)", "", "(−3a+b+3)/(a+b)", "4.3", c=M)
a(10, 3, EL, "로그함수", "역함수", "LOGFUNC.INVERSE.VALUE", "f=log₂x 역함수 g, g(a)=2, g(b)=6, g(a+b)", "로그함수의 역함수", "하", "⑤ (12)", "", "a=1, b=log₂6", "4.3")
a(11, 3, EL, "지수함수", "지수방정식", "EXPEQ.RECIPROCAL.QUADRATIC", "3^{x+1}+3^{−x+2}−28=0 근의 합", "지수방정식", "하", "④ (1)", "", "t=9, 1/3", "4.4")
a(12, 3, TR, "삼각함수", "부채꼴", "SECTOR.PENDULUM.ARC", "막대 28, 지름 8 시계추 중심 16√3 아래, 이동거리", "호의 길이", "중", "② (16π/3)", "", "반지름 32, cosθ=√3/2", "4.6", c=M, **F)
a(13, 4, EL, "로그", "상용로그의 활용", "CLOG.DECAY.DEPTH", "20m마다 32% 감소, 4% 이상 최대 깊이", "상용로그", "중하", "② (140 m)", "log2=0.3, log6.8=0.8", "0.68ⁿ≥0.04 → n≤7", "4.7", c=M)
a(14, 4, EL, "지수", "지수의 계산", "EXP.DIFF_GIVEN.CUBE_SUM", "xᵏ−x⁻ᵏ=3, x^{3k}+x^{−3k}", "지수법칙;곱셈공식", "중", "④ (10√13)", "x>1", "합 √13, s³−3s", "4.8", c=M, trap=M)
a(15, 4, EL, "로그함수", "그래프 개형", "EXPLOG.GRAPH.RECIPROCAL_BASES", "loga+logb=0, b/a>1, aˣ와 −log_bx 개형", "지수·로그함수의 그래프", "중하", "①", "", "0<a<1<b, g=log_a x", "4.9", c=M, **G)
a(16, 5, EL, "로그함수", "로그함수와 원", "LOGFUNC.UNIT_CIRCLE.INTERSECTION", "log_a(−x)와 단위원 교점, AQ=√3 Q", "로그함수의 그래프", "중", "③ (−1/2, √3/2)", "0<a<1", "P(−1,0), Q y>0", "5", c=M, i=M)
a(17, 5, EL, "지수", "거듭제곱근", "ROOT.REAL_COUNT.SUM", "(2n−5)(n+1)의 n제곱근 실수 개수 합", "거듭제곱근", "중하", "④ (6)", "", "0+1+2+1+2", "5.1", c=M)
a(18, 6, EL, "지수함수", "지수함수의 그래프", "EXPFUNC.HORIZONTAL_SEGMENT.COUNT_PAIRS", "aˣ, bˣ와 수평선 AB=2, t≥2 (a,b) 개수", "지수함수의 그래프", "중", "③ (23)", "2≤a<b≤9", "b≤a²", "5.2", c=M, i=M, **G)
a(19, 6, EL, "로그", "상용로그의 활용", "CLOG.DEPRECIATION.VALUE", "매년 20% 감소 200만원 5년 후(서답1)", "상용로그", "중하", "63.1만 원", "log2=0.3, log6.31=0.8", "log=1.8", "6", fmt=D, label="서답1", c=M)
a(20, 7, EL, "로그함수", "로그부등식", "LOGINEQ.ABS_BOTH_SIDES", "log₂|x−2|+1≥3−|1−log₂x|(서답2)", "로그부등식", "중", "0<x≤2/3 또는 x≥4", "", "구간별 정리, 경계 등호 확인", "6", fmt=D, label="서답2", c=M, i=M)
a(21, 7, TR, "삼각함수", "삼각함수의 정의", "TRIG.UNIT_CIRCLE.TANGENT_LINE_POINT", "기울기 1, −x²−3/2 접선이 단위원과 만나는 P, cosθsinθ(서답3)", "삼각함수의 정의", "중", "−9/32", "", "y=x−5/4, (x−y)²=1−2xy", "8", fmt=D, label="서답3", c=M, i=M)
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{712+i}", ROWS[i*10:(i+1)*10], 15406+i*10)
