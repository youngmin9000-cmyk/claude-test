from cfgex import *
MC, D = "객관식(5지선다)", "서술형"
M, H = "보통", "높음"
def a(q, pg, big, mid, small, tid, tname, tags, diff, ans, summ, chk, pts, fmt=MC, **kw):
    kw.setdefault("atype", "선택지" if fmt == MC else "값"); R(q, pg, big, mid, small, tid, tname, tags, diff, fmt, ans, summ, chk, pts=pts, **kw)
LC, DF, IG = "함수의 극한과 연속", "미분", "적분"
G = dict(fig="그래프")
VR = "가로 양면 스캔 PDF(텍스트층 없음) 짝수쪽 −90°·홀수쪽 +90° 회전 렌더 시각판독"
# ── A00852 대영고 2022 2-2 중간 수학Ⅱ — 정답 A00851 p1, 서답 채점기준 p2~3
K52 = dict(enumerate("③"+"X"+"③③②①③⑤⑤②④②④⑤④①①②", 1)); K52[2] = "①, ⑤"
K52.update({19: "(1) 3 (2) 8x−4 (3) 30x⁴+32x³−15x²−8x+1", 20: "(예) f=−1(x<0),1(x≥0), g=1(x<0),−1(x≥0); p=|x|+1, q=−1(x<1),1(x≥1)", 21: "f(x)=x³−6x²−4x+24, f'(1)=−13"})
setup("A00852", "1XqgDFZQB0oZRiGUWrDBOahnQX6Jfn5aY", "2022년 2학년 2학기 중간고사 수학2.pdf", "p2/A00852.pdf", "대영고", "2022학년도", "2학기 중간고사", "고2", "수학Ⅱ",
      KEY=K52, KEYPAGE="A00851 p1 정답/배점표(수학Ⅱ 코드03), p2~3 서답형 채점기준표", KEYSRC="1p_WN5RSXX_HA7xcBtTvLj2LuKl10aYFM", VIS=VR, TEXT="텍스트층 없음 — 렌더 판독")
a(1, 1, LC, "함수의 극한", "∞/∞ 꼴", "LIMIT.RATIONAL.INFINITY", "(3x+2)/(x−1) x→∞", "함수의 극한", "하", "③ (3)", "", "최고차 계수비", "3.9")
a(2, 1, LC, "함수의 극한", "극한의 존재", "LIMIT.EXISTENCE.PIECEWISE_CHOICES", "x=0에서 극한 존재 함수 모두", "좌극한·우극한", "하", "①, ⑤", "", "x|x|→0, j→0", "4.0", atype="선택지(복수)", trap=M)
a(3, 1, DF, "미분계수", "미분계수와 극한", "DERIV.LIMIT.FACTOR_DENOM", "f'(2)=6, (f(x)−f(2))/(x³−8)", "미분계수", "하", "③ (1/2)", "", "6/12", "4.0")
a(4, 1, DF, "도함수", "다항함수 미분", "DERIV.POLY.SOLVE_COEFF", "x³−2x²+ax+b, f(1)=3, f'(1)=−2, f(−1)", "도함수", "하", "③ (3)", "", "a=−1, b=5", "4.0")
a(5, 2, LC, "함수의 연속", "유리함수 연속", "CONTINUITY.RATIONAL.DISCRIMINANT", "(x−1)/(x²+ax+7) 모든 실수 연속 정수 a 개수", "함수의 연속", "하", "② (11)", "", "a²<28", "4.1")
a(6, 2, LC, "함수의 극한", "미정계수", "LIMIT.SQRT.UNDETERMINED", "(√(x+a)+b)/(x−2)→1/2, a+b", "함수의 극한", "중하", "① (−2)", "", "a=−1, b=−1", "4.2", c=M)
a(7, 2, DF, "도함수의 활용", "접선", "TANGENT.PERPENDICULAR_SLOPE", "x²+2 위 A(−1/4) 접선과 수직, 곡선에 접하는 직선 2a−b", "접선의 방정식", "중하", "③ (3)", "", "기울기 2, y=2x+1", "4.2", c=M)
a(8, 2, DF, "미분계수", "순간변화율", "RATE.TORRICELLI.INSTANT", "V=90000(1−t/60)², t=10 순간변화율", "순간변화율", "하", "⑤ (−2500)", "", "−3000(5/6)", "4.2")
a(9, 3, LC, "함수의 극한", "다항함수 결정", "LIMIT.POLY_DETERMINE.TWO_CONDITIONS", "두 극한 조건 f(3)", "함수의 극한;미분계수", "중", "⑤ (14)", "", "f=x³−2x²+5x−10", "4.5", c=M)
a(10, 3, LC, "함수의 극한", "극한의 성질", "LIMIT.PROPERTIES.TRUTH_COUNT", "극한 명제 참 개수", "함수의 극한의 성질", "중", "② (1)", "", "ㄱ만 참", "4.6", trap=H)
a(11, 3, LC, "함수의 연속", "사잇값 정리", "IVT.ROOT_IN_INTERVAL.COUNT_P", "f=g가 (0,2)에서 실근 정수 p 개수", "사잇값의 정리", "중", "④ (47)", "", "h 증가, −47<p<1", "4.4", c=M)
a(12, 3, DF, "미분가능성", "연속과 미분가능", "DIFFERENTIABILITY.CONTINUOUS_NOT_DIFF.CHOOSE", "x=0 연속·미분불가 함수 고르기", "미분가능성과 연속성", "중하", "② (ㄱ, ㄷ)", "", "ㅁ 미분가능", "4.6", trap=M)
a(13, 4, LC, "함수의 극한", "그래프 극한", "LIMIT.GRAPH.COMPOSITE_ARG", "그래프로 lim_{x→1⁻}f(1)+lim_{x→−2⁺}f(−2x)", "함수의 극한", "중하", "④ (6)", "", "f(1)=1(상수), x→−2⁺ ⇒ −2x→4⁻ 좌극한 5; 아래첨자 작음(4배 확대 판독)", "4.7", trap=M, **G)
a(14, 4, DF, "도함수", "함수방정식", "DERIV.FUNC_EQUATION.MULTIPLICATIVE", "f(x+y)=3f(x)f(y), f'(0)=2, f'(2)/f(2)", "도함수의 정의", "중", "⑤ (6)", "", "f(0)=1/3, f'=6f", "4.8", c=M, i=M)
a(15, 4, DF, "미분계수", "합 극한", "DERIV.ALTERNATING_SUM.LINEAR", "(1/h)∑(−1)ᵏf(kh)=100, f(1)=1, f(3)", "미분계수", "중", "④ (5)", "", "a·50=100", "4.9", c=M)
a(16, 4, DF, "도함수의 활용", "접선", "TANGENT.FROM_EXTERNAL_POINT", "(0,−3)에서 x²+1 접선, a<0, b−a", "접선의 방정식", "하", "① (1)", "", "t=−2: y=−4x−3", "4.7")
a(17, 5, DF, "도함수의 활용", "접선과 극한", "TANGENT.CUBIC.SECOND_INTERSECTION_LIMIT", "x³−2nx 접선 재교점 AB²/f'(n) 극한", "접선의 방정식;수열의 극한", "중", "① (12)", "", "B(−2), g~36n², f'(n)=3n²−2n", "5.2", c=M, i=M)
a(18, 5, LC, "함수의 연속", "근의 개수 함수", "CONTINUITY.ROOT_COUNT_FUNCTION.REFLECT", "g=|x|−2 반사 정의 f 근 개수 h(k) 불연속 a 합", "함수의 연속", "상", "② (−1)", "", "불연속 k=−2, −1, 2", "5.0", c=M, i=H)
a(19, 6, DF, "도함수", "다항함수 미분", "DERIV.POLY.THREE_BASIC", "3x−100, (2x−1)², (2x³−x)(3x²+4x−1) 미분(서답1)", "도함수", "하", "(1) 3 (2) 8x−4 (3) 30x⁴+32x³−15x²−8x+1", "", "곱의 미분", "6", fmt=D, label="서답1", nsub=3)
a(20, 6, LC, "함수의 연속", "연속 반례 구성", "CONTINUITY.CONSTRUCT_EXAMPLES", "불연속 f,g 곱 연속 / q∘p 연속 예(서답2)", "함수의 연속", "중", "예시 답안(개방형)", "", "채점기준 예시와 동치 여부 개별 판정 필요", "7", fmt=D, label="서답2", nsub=2, c=M,
  ready="REVIEW", status="개방형 예시답안(유일정답 없음)", trust="중간", review="REVIEW-개방형답안")
a(21, 6, LC, "함수의 연속", "곱함수 연속", "CONTINUITY.PRODUCT.CUBIC_SHIFT", "f·h, f(x+p)h 연속, f'(1)<0 f, f'(1)(서답3)", "함수의 연속;도함수", "상", "f(x)=x³−6x²−4x+24, f'(1)=−13", "", "f(±2)=0, f(p±2)=0 → 근 6", "7", fmt=D, label="서답3", c=H, i=H)
# ── A00850 대영고 2022 2-2 기말 수학Ⅱ — 정답 A00849 p1, 채점기준 p2~3; 원본에 학생 필기(체크·숫자) 흔적
K50 = dict(enumerate("②③④②①⑤⑤X①④③③④④②①②⑤", 1)); K50[8] = "①, ⑤"
K50.update({19: "k=5", 20: "1/20", 21: "19/6"})
setup("A00850", "1uPxCBE_lAR-gr7G_pixMn1axNaber8oJ", "2022년 2학년 2학기 기말고사 수학2.pdf", "p2/A00850.pdf", "대영고", "2022학년도", "2학기 기말고사", "고2", "수학Ⅱ",
      KEY=K50, KEYPAGE="A00849 p1 정답/배점표(수학Ⅱ 코드03), p2~3 서답형 채점기준표", KEYSRC="1VXZd0YdtNEiJbY2dyRGlv09SNsKTmgFp", VIS=VR + "; 학생 필기 흔적(10·16·17번 선택지 번호 일부 가림)", TEXT="텍스트층 없음 — 렌더 판독")
a(1, 1, DF, "도함수의 활용", "속도", "MOTION.DIRECTION_CHANGE", "x=4t²−16t 운동 방향 바꾸는 시각", "속도와 가속도", "하", "② (2)", "", "v=8t−16", "3.9")
a(2, 1, IG, "정적분", "정적분의 성질", "INTEG.INTERVAL_ADDITIVITY", "∫₀¹+∫₁²+∫₃³(3x²+x+1)", "정적분의 성질", "하", "③ (12)", "", "∫₀²=12", "4")
a(3, 1, IG, "부정적분", "부정적분", "INTEG.INDEFINITE.INITIAL", "f=∫(x+2)(x²−2x+4)dx, f(0)=1, f(2)", "부정적분", "하", "④ (21)", "", "x⁴/4+8x+1", "4")
a(4, 1, IG, "정적분의 활용", "넓이", "AREA.PARABOLA_LINE", "x²+3x−1과 y=3 넓이", "넓이", "하", "② (125/6)", "", "5³/6", "4")
a(5, 2, IG, "부정적분", "적분 방정식", "INTEG.EQUATION.DIFFERENTIATE", "∫f=xf+4x³−3x², f(0)=2, f(−1)", "부정적분", "중하", "① (−10)", "", "f'=−12x+6", "4.1", c=M)
a(6, 2, DF, "도함수의 활용", "극값", "EXTREMA.CUBIC.FIND_COEFF", "x=1 극댓값 2, x=3 극소 a+2b+c", "극대와 극소", "하", "⑤ (10)", "", "a=−6, b=9, c=−2", "4.2")
a(7, 2, DF, "도함수의 활용", "평균값 정리", "MVT.DERIV_BOUND.MIN_VALUE", "f'≥2 (0<x<2), f(0)=1, f(2) 최소", "평균값 정리", "하", "⑤ (5)", "", "1+2·2", "4.2")
a(8, 2, DF, "도함수의 활용", "증가·감소와 극값", "DERIV.CONCEPTS.TRUE_STATEMENTS", "증가·극값 명제 옳은 것 모두", "함수의 증가와 감소;극값", "중하", "①, ⑤", "", "②③④ 반례", "4.3", atype="선택지(복수)", trap=H)
a(9, 3, DF, "도함수의 활용", "방정식의 실근", "CUBIC.ROOT_SIGN_PATTERN.PARAM", "2x³−3x²−12x+2a=0 음근 1, 양근 2 정수 a 개수", "방정식의 실근의 개수", "중", "① (9)", "", "0<2a<20", "4.4", c=M)
a(10, 3, IG, "정적분", "기함수 정적분", "INTEG.ODD_CUBIC.ABS_SHIFT", "x(x+a)(x−a) P, Q로 ∫|f(x−a)|", "정적분의 성질;우함수·기함수", "상", "④ (P−2Q)", "", "−Q−(Q−P)", "4.6", c=M, i=H)
a(11, 3, IG, "부정적분", "극값과 부정적분", "INTEG.ANTIDERIV.EXTREMA_DIFF", "f=∫(x²−x−2), 극댓값 1/6 → 극솟값", "부정적분;극값", "중하", "③ (−13/3)", "", "f(2)−f(−1)=−9/2", "4.4", c=M)
a(12, 3, IG, "정적분", "정적분으로 정의된 함수", "INTEG.DEFINED_CONSTANT.LINEAR", "f=3x+∫(t−1)f(t)dt, ∫₋₁¹f", "정적분으로 정의된 함수", "중하", "③ (4/3)", "", "k=2/3", "4.6", c=M)
a(13, 4, DF, "도함수의 활용", "부등식", "INEQ.CUBIC.NEGATIVE_DOMAIN", "x<0에서 f<g 항상 정수 k 최대", "부등식의 증명", "중", "④ (1)", "", "h(−2)=k−2<0", "4.7", c=M)
a(14, 4, IG, "정적분의 활용", "속도와 거리", "MOTION.VELOCITY.STATEMENTS", "v=8−2t, 위치·변화량·거리·복귀 보기", "속도와 거리", "중하", "④ (ㄴ, ㄷ, ㄹ)", "출발점 1", "x=1+8t−t²", "4.8", c=M, trap=M)
a(15, 5, IG, "정적분", "그래프와 정적분", "INTEG.CUBIC_FROM_EXTREMA_GRAPH", "극대(−1,3), 극소(1,−1) 삼차 ∫₋₁¹", "정적분", "중하", "② (2)", "", "f=x³−3x+1", "4.6", c=M, **G)
a(16, 5, IG, "정적분", "주기함수 정적분", "INTEG.PERIODIC.PIECEWISE", "f(x+2)=f(x) 구간별 정의 ∫₀¹¹", "정적분의 성질", "중", "① (9)", "", "주기 적분 5/3", "4.8", c=M)
a(17, 6, DF, "미분가능성", "절댓값 사차", "DIFFERENTIABILITY.ABS_QUARTIC.ONE_POINT", "|x⁴+2x³−12x²+ax+b| 미분불가 1점, a−b", "미분가능성", "상", "② (19)", "a>0", "(x+5)(x−1)³", "5.2", c=M, i=H)
a(18, 6, IG, "정적분", "정적분으로 정의된 함수", "INTEG.DEFINED.ABS_DERIV_BOUND", "f=∫{3−|f'−3|}, 극값 0, −2, 극솟값 최소", "정적분으로 정의된 함수;극값", "상", "⑤ (−4)", "", "f'≤3 → −3≤a<0, f(−2)=4a/3", "5.2", c=H, i=H)
a(19, 7, IG, "정적분", "절댓값 정적분", "INTEG.ABS_QUADRATIC.SOLVE_UPPER", "∫₀ᵏ|3x²−6x|=58 k(서답1)", "정적분", "중하", "k=5", "k>2", "k³−3k²+8=58", "6", fmt=D, label="서답1", c=M)
a(20, 7, DF, "도함수의 활용", "최대·최소", "MAXMIN.PARAM_CUBIC.INTERVAL", "x³−9kx²+24k²x [0,1] 최댓값 6k² k 곱(서답2)", "최댓값과 최솟값", "상", "1/20", "", "k=3/10(f(2k)), 1/6(f(1))", "6", fmt=D, label="서답2", c=H, i=H)
a(21, 8, IG, "정적분", "max형 함수 정적분", "INTEG.MAX_FUNCTION.QUADRATIC", "f=(g+|g−k|)/2 조건, ∫₋₁²f(서답3)", "정적분;미분가능성", "상", "19/6", "", "kn=2 → k=2, n=1", "8", fmt=D, label="서답3", c=H, i=H)
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{707+i}", ROWS[i*10:(i+1)*10], 15364+i*10)
