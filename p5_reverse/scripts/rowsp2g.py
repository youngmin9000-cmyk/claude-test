from cfgex import *
MC, D = "객관식(5지선다)", "서술형"
M, H = "보통", "높음"
def a(q, pg, big, mid, small, tid, tname, tags, diff, ans, summ, chk, pts, fmt=MC, **kw):
    kw.setdefault("atype", "선택지" if fmt == MC else "값"); R(q, pg, big, mid, small, tid, tname, tags, diff, fmt, ans, summ, chk, pts=pts, **kw)
LC, DF = "함수의 극한과 연속", "미분"
G = dict(fig="그래프")
# ── A00827 대영고 2023 2-2 중간 수학Ⅱ — 정답 A00824(jpg, 정답/배점표+채점기준 1), 채점기준 A00825·A00826(jpg); A00820(수2)은 동일 이미지 회전본 DUPLICATE
K = dict(enumerate("⑤④④②③①③②⑤④⑤③③②①①⑤②", 1))
K.update({19: "2a−2+h", 20: "−5", 21: "45", 22: "−1", 23: "f(x)=x³−4x²+5x−6"})
setup("A00827", "1JSy5a6B_kqm7WcK_dDFxko4iX92pzJiZ", "2023학년도 2학년 2학기 중간고사.pdf", "p2/A00827.pdf", "대영고", "2023학년도", "2학기 중간고사", "고2", "수학Ⅱ",
      KEY=K, KEYPAGE="A00824 정답/배점표 사진(2023.09.25, 코드03), A00825·A00826 서답형 채점기준표 사진", KEYSRC="1jRyXmuN-J1rQL9ifktemp8IuDH363Mgk; 1W4_gFRIst3N1DVg11UTlOEZuM_-JK7DZ; 10xesep38e9IA4xtoGy8wwZG4gg6oXeuP",
      VIS="스캔 PDF(텍스트층 없음) — 동일 이미지 정방향본 A00820으로 렌더 시각판독(6쪽)", TEXT="텍스트층 없음 — 렌더 판독")
a(1, 1, LC, "함수의 극한", "극한의 대소", "LIMIT.SQUEEZE.RATIO", "3x−1<f<(3x²+4x+1)/(x+1), lim f/x", "함수의 극한의 대소 관계", "하", "⑤ (3)", "", "양변 3", "4")
a(2, 1, LC, "함수의 연속", "유리함수 연속", "CONTINUITY.REMOVABLE.PARAM", "(x²+ax+2)/(x+1), x=−1에서 b 연속, a+b", "함수의 연속", "하", "④ (4)", "", "a=3, b=1", "4")
a(3, 1, DF, "미분계수", "곱의 미분", "DERIV.PRODUCT.VALUE", "(2x+1)(x²+x−1) x=1 미분계수", "도함수", "하", "④ (11)", "", "2+9", "4.1")
a(4, 1, DF, "도함수의 활용", "접선", "TANGENT.GIVEN_SLOPE", "2x²−x 기울기 3 접선 a−b", "접선의 방정식", "하", "② (5)", "", "y=3x−2", "4.1")
a(5, 2, LC, "함수의 극한", "∞−∞ 꼴", "LIMIT.SQRT_DIFF.INFINITY", "6/(√(x²+x)−√(x²−2x))", "함수의 극한", "하", "③ (4)", "", "분모→3/2", "4.2")
a(6, 2, DF, "미분계수", "순간변화율", "RATE.MOON_THROW.INSTANT", "s=32t−0.8t², t=35 순간변화율", "순간변화율", "하", "① (−24)", "", "32−56", "4.3")
a(7, 2, DF, "도함수의 활용", "도함수 그래프", "MONO.DERIV_GRAPH.FALSE_ONE", "f' 그래프로 증감·극값 옳지 않은 것", "함수의 증가와 감소", "중하", "③", "", "(3,4)에서 f'<0", "4.2", c=M, **G)
a(8, 2, DF, "도함수의 활용", "역함수 존재", "MONO.INVERTIBLE_CUBIC.PARAM", "x³−6x²+kx+5 역함수 존재 정수 k 최소", "함수의 증가와 감소", "하", "② (12)", "", "144−12k≤0", "4.3")
a(9, 3, LC, "함수의 연속", "불연속 유형", "CONTINUITY.DISCONTINUITY_TYPES.MATCH", "불연속 그래프 I, II와 이유 연결", "함수의 연속", "하", "⑤ (I−ㄷ, II−ㄴ)", "", "", "4.3", **G)
a(10, 3, DF, "미분계수", "미분계수의 정의", "DERIV.LIMIT_FORM.COMBINED", "(f(1+Δx)−f(1−3Δx))/(2Δx), f=x²+3x−2", "미분계수", "하", "④ (10)", "", "4f'(1)/2", "4.4")
a(11, 3, DF, "미분가능성", "구간별 함수", "DIFFERENTIABILITY.PIECEWISE.PARAMS", "x³−x²+ax (x≥1), bx²+1 미분가능 aᵇ", "미분가능성", "중하", "⑤ (9)", "", "a=3, b=2", "4.5", c=M)
a(12, 3, DF, "미분계수", "다항식 나눗셈과 미분", "DERIV.DIVISION_SQUARE.REMAINDER", "x⁵+x²+1을 (x−1)²로 나눈 나머지 px+q, p−q", "미분;나머지정리", "중하", "③ (11)", "", "R=7x−4", "4.6", c=M)
a(13, 4, DF, "도함수의 활용", "평균값 정리", "MVT.SLOPE_RANGE.INTEGER_MAX", "−x²+4x−1 [−1,2] 평균변화율 정수 k 최대", "평균값 정리", "중하", "③ (5)", "", "기울기 범위 (0,6)", "4.5", c=M, trap=M)
a(14, 4, DF, "도함수의 활용", "극값", "EXTREMA.EVEN_QUARTIC.FIND", "우함수 사차, x=1 극솟값 1, 극댓값 4, f(2)", "극대와 극소", "중하", "② (28)", "", "3x⁴−6x²+4", "4.7", c=M)
a(15, 4, LC, "함수의 연속", "사잇값 정리", "IVT.ROOT_COUNT.TABLE", "f(0)=2, f(1)=−2, f(2)=3, f(3)=4, f(x)−2x=0 (0,3) 최소 실근", "사잇값의 정리", "중하", "① (1)", "", "g: 2, −4, −1, −2", "4.8", c=M, trap=M)
a(16, 4, DF, "도함수의 활용", "접선", "TANGENT.DOUBLE_TANGENT.QUARTIC", "x⁴−6x²+8x 두 점 공통접선 a+b", "접선의 방정식", "중", "① (−1)", "", "f−(ax+b)=(x²−3)², a=8, b=−9", "4.9", c=M, i=M)
a(17, 5, DF, "도함수의 활용", "절댓값 극값", "EXTREMA.ABS_CUBIC.TWO_LOCAL_MAX", "|x³−6x²+9x+k| x=a, b 극대, 3f(a)=f(b), k", "극대와 극소", "중", "⑤ (−3)", "a<b", "3(4+k)=−k", "5", c=M, i=M)
a(18, 5, DF, "도함수의 활용", "극한과 도형", "LIMIT.PARABOLA_CHORD.INTERCEPT", "y=x²과 기울기 1 직선 AB=√2t, y절편 g(t)/2t² 극한", "함수의 극한;이차방정식", "중하", "② (1/8)", "", "g=(t²−1)/4", "5.1", c=M, **G)
a(19, 5, DF, "미분계수", "평균변화율", "RATE.AVERAGE.QUADRATIC", "x²−2x, a→a+h 평균변화율(서답1)", "평균변화율", "하", "2a−2+h", "", "", "4", fmt=D, label="서답1")
a(20, 5, DF, "도함수의 활용", "접선", "TANGENT.CUBIC.SECOND_INTERSECTION", "x³−3x² (2,−4) 접선 재교점 (a,b), a+b(서답2)", "접선의 방정식", "하", "−5", "", "y=−4 → (−1,−4)", "4", fmt=D, label="서답2")
a(21, 6, DF, "도함수의 활용", "증가와 감소", "MONO.INCREASING_INTERVALS.COEFF", "x³+ax²+bx+c 증가 (−∞,−1],[2,∞), 극솟값 −5, abc(서답3)", "함수의 증가와 감소", "중하", "45", "", "a=−3/2, b=−6, c=5", "4", fmt=D, label="서답3", c=M)
a(22, 6, LC, "함수의 연속", "최대·최소", "CONTINUITY.PIECEWISE.MAXMIN", "x+3a / −x²+a 연속, [0,4] M+m(서답4)", "최대·최소 정리", "하", "−1", "", "a=−1, M=1, m=−2", "4", fmt=D, label="서답4")
a(23, 6, LC, "함수의 극한", "다항함수 결정", "LIMIT.POLY_DETERMINE.TWO_CONDITIONS", "(f−x³)/x²→−4, f/(x²−2x−3)→2 (x→3) f(서답5)", "함수의 극한", "중하", "f(x)=x³−4x²+5x−6", "", "c=−3b+9, (3+b)/4=2", "4", fmt=D, label="서답5", c=M)
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{726+i}", ROWS[i*10:(i+1)*10], 15524+i*10)
