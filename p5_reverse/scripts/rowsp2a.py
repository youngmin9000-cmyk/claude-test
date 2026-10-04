from cfgex import *
MC, D = "객관식(5지선다)", "서술형"
M, H = "보통", "높음"
def a(q, pg, big, mid, small, tid, tname, tags, diff, ans, summ, chk, pts, fmt=MC, **kw):
    kw.setdefault("atype", "선택지" if fmt == MC else "값"); R(q, pg, big, mid, small, tid, tname, tags, diff, fmt, ans, summ, chk, pts=pts, **kw)
TR, SQ = "삼각함수", "수열"
TG, TA, AR, GE, SM, IN = "삼각함수의 그래프", "삼각함수의 활용", "등차수열과 등비수열", "등비수열", "수열의 합", "수학적 귀납법"
F = dict(fig="도형")
# ── A00854 대영고 2022 2-1 기말 수학Ⅰ (가로 스캔, 회전 렌더) — 정답표·서답 채점기준 A00853 p1~3
K54 = dict(enumerate("④①①⑤⑤③②②③③④②⑤④①③⑤②", 1)); K54.update({19: "5π/6≤x≤7π/6", 20: "4√7/7", 21: "xₙ=2^{n+2}, yₙ=2n+3, P₁₀(8184, 140)"})
setup("A00854", "12DaX5o7aUcAGNmxKG3uTdfGL2xLHx-kK", "2022년 2학년 1학기 기말고사 수학1.pdf", "p2/A00854.pdf", "대영고", "2022학년도", "1학기 기말고사", "고2", "수학Ⅰ",
      KEY=K54, KEYPAGE="A00853 p1 정답/배점표(수학Ⅰ 코드03), p2~3 서답형 채점기준표", KEYSRC="1FATceW4p2MiFp4-QElJMPvMBllq2GARU",
      VIS="가로 스캔 PDF(텍스트층 없음) −90° 회전 렌더 전 6쪽 시각판독", TEXT="텍스트층 없음 — 렌더 판독")
a(1, 1, TR, TA, "사인법칙", "SINE_LAW.PERIMETER.SUM_SINES", "R=4, sinA+sinB+sinC=3/4 a+b+c", "사인법칙", "하", "④ (6)", "", "2R×3/4", "4.0")
a(2, 1, TR, TA, "삼각형의 넓이", "PARALLELOGRAM.AREA.SAS", "AB=3, BC=4, ∠B=60° 평행사변형 넓이", "삼각형의 넓이", "하", "① (6√3)", "", "3·4·sin60°", "4.0", **F)
a(3, 1, SQ, AR, "등차수열의 일반항", "ARITH.CONDITIONS.TERM", "a₃+a₅=30, a₁₁−a₇=24 a₁₅", "등차수열", "하", "① (81)", "", "d=6, a₄=15", "4.0")
a(4, 1, SQ, SM, "∑의 성질", "SIGMA.QUADRATIC_EXPAND", "∑aₙ=15, ∑aₙ²=30, ∑(aₙ+1)²", "합의 기호", "하", "⑤ (70)", "", "30+30+10", "4.0")
a(5, 2, TR, TA, "삼각방정식", "TRIGEQ.SIN2X.SUM_FIRST_ROOTS", "sin2x=1/4 양수 근 작은 순 4개 합", "삼각방정식", "중하", "⑤ (3π)", "", "2x 합 6π", "4.2", c=M)
a(6, 2, TR, TG, "삼각함수의 그래프", "TRIGGRAPH.TRANSFORM.STATEMENTS", "2tan/2sin(3x−π/2)−1 성질 옳은 것", "삼각함수의 그래프", "중하", "③", "", "|2sin(3x−π/2)−1| 주기 2π/3", "4.4", trap=M)
a(7, 2, TR, TA, "삼각부등식", "TRIGINEQ.QUADRATIC_SIN.ALWAYS", "sin²(x−π/2)−4sinx+k<0 항상, 정수 k 최대", "삼각부등식", "중", "② (−5)", "", "s=−1에서 최대 4+k<0", "4.6", c=M, trap=M)
a(8, 2, TR, TA, "코사인법칙", "SINE_RATIO.COS_LAW", "sinA:sinB:sinC=3:5:6 cosB", "사인법칙;코사인법칙", "하", "② (5/9)", "", "(9+36−25)/36", "4.1")
a(9, 3, TR, TA, "사인·코사인법칙", "TRIANGLE.SHAPE_FROM_CONDITIONS.CIRCUMCIRCLE", "bsinB=csinC, sinAcosC=sinB, AB=4 외접원 넓이", "사인법칙;코사인법칙", "중", "③ (8π)", "", "b=c, a²=2b² → 직각이등변", "4.2", c=M, i=M)
a(10, 3, TR, TA, "코사인법칙", "COS_LAW.MEDIAN_LENGTH", "AB=3, BC=4, cosA=3/8, 4BM²", "코사인법칙", "중", "③ (34)", "", "AC=4, BM²=17/2", "4.6", c=M, **F)
a(11, 3, SQ, SM, "합과 일반항", "SUM_TO_TERM.ODD_INDEX_SUM", "∑aₖ=n²−4n+3, ∑a_{2k−1}", "합과 일반항의 관계", "중하", "④ (153)", "", "a₁=0, aₙ=2n−5 (n≥2)", "4.7", c=M, trap=M)
a(12, 3, SQ, GE, "등비중항", "GEOM.CUBIC_ROOTS.VIETA", "x³−kx²+21x−8=0 세 근 등비 k", "등비수열;근과 계수", "중하", "② (21/2)", "", "가운데 근 2", "4.5", c=M)
a(13, 4, SQ, GE, "등비수열의 활용", "GEOM.ANNUITY.BEGIN_YEAR", "연 2% 복리 매년 초 20만 원 20년 원리합계", "등비수열의 합", "중하", "⑤ (4,998,000원)", "1.02²⁰=1.49", "20만×1.02×24.5", "4.3", c=M)
a(14, 4, SQ, SM, "∑의 계산", "SIGMA.DOUBLE.TETRAHEDRAL", "∑∑i=969 n", "자연수의 거듭제곱의 합", "중하", "④ (17)", "", "n(n+1)(n+2)=5814", "4.7")
a(15, 4, SQ, SM, "여러 가지 수열의 합", "SIGMA.PARTIAL_FRACTION.ODD_SQUARES", "1/(5²−1)+1/(7²−1)+… 20항", "부분분수", "중하", "① (5/44)", "", "1/(4(k+1)(k+2))", "4.6", c=M)
a(16, 4, SQ, SM, "여러 가지 수열의 합", "SIGMA.RATIONALIZE.ARITH_SQRT", "직선 위 (n,aₙ), ∑1/(√aₖ+√aₖ₊₁)", "유리화;등차수열", "중", "③ (2√5)", "a₃=4, a₈=6", "d=2/5, (√a₂₅−√a₁)/d", "4.8", c=M, fig="그래프")
a(17, 5, TR, TA, "사인·코사인법칙", "CIRCLE.ANGLE_BISECTOR.CHORD_POWER", "AB=1, AC=3, A=120°, 이등분선 연장 DE", "코사인법칙;원의 성질", "중", "⑤ (13/4)", "", "AD=3/4, BD·DC=AD·DE", "5.1", c=M, i=M, **F)
a(18, 5, SQ, SM, "∑의 계산", "SIGMA.LOG_LEVEL_COUNT", "3으로 나눠 몫<1까지 횟수 aₖ, ∑₁¹⁵⁰", "합의 기호;거듭제곱", "중", "② (634)", "", "3^m>k: 2+12+54+216+350", "5.2", c=M, i=M)
a(19, 6, TR, TA, "삼각부등식", "TRIGINEQ.SYSTEM.COS_TAN", "2cosx+√3≤0, −1<tanx<1 동시(서답1)", "삼각부등식", "중하", "5π/6≤x≤7π/6", "0≤x<2π", "그래프 교집합", "6", fmt=D, label="서답1", c=M)
a(20, 6, TR, TA, "삼각형의 넓이", "CIRCUMCENTER.TRIANGLE_OAB.AREA", "AB=AC=4, cosA=3/4 외심 O, △OAB 넓이(서답2)", "사인법칙;삼각형의 넓이", "중", "4√7/7", "", "R=4√2/√7, ∠AOB=π−A", "7", fmt=D, label="서답2", c=M, i=M)
a(21, 6, SQ, AR, "등차·등비 혼합", "SEQ.LOG_POINTS.MIDPOINT_LINE", "Q_n(f(n),g(n)) 중점 조건, xₙ·yₙ 일반항, P₁₀(서답3)", "등차수열;등비수열;상용로그", "상", "xₙ=2^{n+2}, yₙ=2n+3, P₁₀(8184, 140)", "", "k=11, f 공차 log2, g 공차 2", "7", fmt=D, label="서답3", nsub=3, c=H, i=H)
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{704+i}", ROWS[i*10:(i+1)*10], 15343+i*10)
