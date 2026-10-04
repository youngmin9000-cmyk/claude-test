from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h86/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h86/A.hwp','rb').read()).hexdigest()
setup(QID="A02586", SRC="1kI01BRQBWjRnE9S8R3zx9LUUxfSadl63", SHA=SQ, TAG="DSM2D1MA", N=20,
      FNAME="15개정_고등_수학Ⅱ_2-1_중단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D1MA", EXAM="Ⅱ-1 미분계수와 도함수 중단원평가(발전) — 1. 미분계수 / 2. 도함수 2부 구성", MID="미분계수와 도함수",
      ANS_QID="A02554", ANS_SRC="10XJKT6Weyphs73w-ty1n_PU47u9Ss4w9", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
F = dict(fig="설명 그림(gso)")
AV, DC, DF, DR = "평균변화율", "미분계수", "미분가능성과 연속성", "도함수"
ND = "원문 근사중복 후보: A02595(Ⅱ-1 서술형평가) 동일 문항 존재 — 별개 원본으로 유지."
# Part 1: 1. 미분계수 (문항 1~10 -> Q001~Q010)
R(1, AV, "DERIV.AVGRATE.CONVEX_SECANT_SLOPE_ORDER", "아래로 볼록 곡선 할선 기울기 대소", "평균변화율;할선의 기울기;볼록성", "평균변화율+그래프",
  "중하", "g(i,j)=a_i+a_j." + E, S, "g(1,2)<g(1,3)<g(2,3)", "부등식", L, M, M, "", "f=x²(x≥0), a1<a2<a3에서 g(1,2), g(1,3), g(2,3) 대소", "(a_j²−a_i²)/(a_j−a_i)=a_i+a_j (그림 불필요)", memo_extra=ND, **F)
R(2, AV, "DERIV.AVGRATE.PARABOLA_SYMMETRY_FROM_GRAPH", "포물선 대칭과 할선 기울기로 평균변화율", "평균변화율;이차함수의 대칭", "평균변화율+그래프",
  "중하", "f(0)=f(2)는 그래프 판독." + E, S, "−1", "값", L, M, M, "대칭축 판독", "이차함수 그래프, AB 기울기 1일 때 0→1 평균변화율", "f(2)−f(1)=1, f(0)=f(2) → −1 (그림 의존)", memo_extra=ND, **G)
R(3, AV, "DERIV.AVGRATE.QUADRATIC_ZERO_RATE_SCALED", "평균변화율 0 조건 후 구간 2배 평균변화율", "평균변화율;이차함수", "평균변화율+식변형",
  "중하", "α+β=a." + E, S, "a", "식", L, M, M, "", "f=x²−ax+b, α→β 평균변화율 0일 때 2α→2β 평균변화율", "2(α+β)−a=a", memo_extra=ND)
R(4, AV, "DERIV.AVGRATE.INVERSE_FUNCTION_FROM_GRAPH", "역함수의 평균변화율(그래프 좌표 판독)", "평균변화율;역함수", "평균변화율+역함수",
  "중", "f(a)=b, f(c)=d는 그림 판독." + E, S, "(c−a)/(d−b)", "식", L, M, M, "역함수 좌표 교환", "y=f(x) 그래프, 역함수 g의 b→d 평균변화율", "g(d)=c, g(b)=a (그림 의존)", memo_extra=ND, **G)
R(5, DC, "DERIV.DERIVCOEF.GRAPH_SLOPE_COMPARE_SELECT", "그래프에서 원점기울기·할선·접선 비교", "평균변화율;미분계수;접선의 기울기;그래프", "그래프+보기판별",
  "중", "기울기 해석 3종." + E, S, "ㄱ, ㄷ", "보기", L, H, M, "y=x 대비 할선 기울기", "y=f(x)와 y=x 그래프, 0<a<b: ㄱ f(a)/a<f(b)/b ㄴ f(b)−f(a)<b−a ㄷ f'(a)<f'(b)", "해설: 원점 기울기 증가·할선 기울기>1·접선 기울기 증가 → ㄱ,ㄷ (그림 의존)", **G)
R(6, DF, "DERIV.DIFFABLE.SET_INCLUSION_DIFF_CONT", "미분가능 집합과 연속 집합의 포함 관계", "미분가능성;연속성;집합", "개념이해",
  "중하", "미분가능 ⇒ 연속." + E, S, "A⊂B", "포함관계", L, M, M, "역 불성립", "A={a|미분계수 존재}, B={a|연속}의 포함 관계", "A⊂B", memo_extra=ND)
R(7, DF, "DERIV.DIFFABLE.GRAPH_COUNT_DISCONT_NONDIFF", "그래프에서 불연속·미분불가능 점 개수", "연속성;미분가능성;그래프", "그래프+미분가능성",
  "중하", "그래프 판독." + E, S, "m=2, n=3", "값", L, M, M, "첨점", "(−1,4)에서 불연속 m개, 미분불가능 n개", "불연속 x=1,3, 미분불가능 x=1,2,3 (그림 의존)", memo_extra=ND, **G)
R(8, DC, "DERIV.DERIVCOEF.RECIPROCAL_LIMIT_FIND_CONSTS", "역수형 극한에서 미분계수와 상수 결정", "미분계수의 정의;극한 존재 조건", "극한+미분계수",
  "중하", "분자→0, 1/f'(2)." + E, S, "a=4, b=−2", "값", L, M, M, "", "f'(2)=a, lim (x+b)/(f(x)−f(2))=1/4", "b=−2, a=4", memo_extra=ND)
R(9, DF, "DERIV.DIFFABLE.FLOOR_TIMES_POLY_AT_INTEGER", "가우스 함수 곱의 정수점 미분가능 조건", "미분가능성;가우스 기호;좌우 미분계수", "가우스+미분가능성",
  "중", "좌 0, 우 이차식." + E, S, "0", "값", M, M, M, "좌극한 [x]=0", "f=[x](x²+2ax+b)가 x=1 미분가능일 때 a+b", "a=−1, b=1 → 0", memo_extra=ND)
R(10, DC, "DERIV.DERIVCOEF.ADD_SUBTRACT_FA_TRICK", "f(3)을 더하고 빼는 극한 변형", "미분계수의 정의;극한 변형", "극한+미분계수",
  "중하", "9f'(3)−6f(3)." + E, MC, "②", "선택지번호", L, M, M, "", "f'(3)=−1, lim (9f(x)−x²f(3))/(x−3)=3일 때 f(3)", "−9−6f(3)=3 → −2", final="② (−2)")
# Part 2: 2. 도함수 (원문 문항 1~10 -> Q011~Q020)
R(11, DR, "DERIV.DERIVFN.FUNCTIONAL_EQ_MULTIPLICATIVE", "f(x+y)=f(x)f(y) 형 함수의 f'/f", "도함수의 정의;함수방정식", "정의+함수방정식",
  "중", "f(0)=1, f'=f·f'(0)." + E, S, "2", "값", L, M, H, "f(0)=1 도출", "f(x+y)=f(x)f(y), f>0, f'(0)=2일 때 f'(x)/f(x)", "f'(x)=f(x)f'(0) → 2")
R(12, DR, "DERIV.DERIVCOEF.SHIFTED_LIMIT_FIND_COEFFS", "평행이동 극한 조건으로 삼차함수 계수 결정", "미분계수;극한 존재 조건;미정계수", "극한+미분계수",
  "중", "t=x−1 치환, f(1)=7, f'(1)=20." + E, S, "47", "값", M, M, M, "", "f=x³+ax²+bx+5, lim (f(x−1)−7)/(x²−4)=5 (x→2)일 때 f(2)", "a=16, b=−15 → f(2)=47")
R(13, DR, "DERIV.RULES.POLY_FROM_INFINITY_AND_DERIV_LIMIT", "∞ 극한·미분계수 극한·함숫값으로 다항식 결정", "다항함수 결정;극한;미분계수", "극한+미분계수",
  "중", "f=x³+2x²+ax+b." + E, S, "4", "값", M, M, M, "", "lim (f−x³)/(x²+1)=2, lim (f(x)−f(1))/(x²−1)=4, f(0)=0일 때 f(1)", "a=1, b=0 → 4", memo_extra=ND)
R(14, DR, "DERIV.RULES.DIVISIBLE_BY_SQUARE_FACTOR", "(x−1)²으로 나누어떨어질 조건", "도함수;나머지정리;중근", "미분+나머지정리",
  "중하", "f(1)=f'(1)=0." + E, S, "1/2", "값", L, M, M, "", "x¹⁰+4ax+3b가 (x−1)²으로 나누어떨어질 때 a+b", "a=−5/2, b=3 → 1/2", memo_extra=ND)
R(15, DR, "DERIV.RULES.PRODUCT_RULE_FROM_LIMITS", "극한 조건에서 함숫값·미분계수 후 곱의 미분", "곱의 미분법;미분계수", "극한+곱의미분",
  "중하", "f(2)=3, f'(2)=1, g(2)=1, g'(2)=2." + E, S, "7", "값", L, M, M, "", "lim (f−3)/(x−2)=1, lim (g−1)/(x−2)=2일 때 (fg)'(2)", "1·1+3·2=7")
R(16, DR, "DERIV.RULES.CUBIC_ROOTS_RECIPROCAL_SUM", "삼차함수 근과 f'/f로 역수합", "곱의 미분법;삼차함수의 근;로그미분 구조", "곱의미분+근",
  "중상", "f'(4)/f(4)=Σ1/(4−r)." + E, S, "−3/2", "값", M, H, H, "부호 반전", "최고차 1 삼차 f, (4,2) 접선 기울기 3, 근 a,b,c일 때 Σ1/(r−4)", "Σ1/(4−r)=3/2 → −3/2", **F)
R(17, DR, "DERIV.DERIVFN.FUNCTIONAL_EQ_SCALED_MULTIPLICATIVE", "f(x+y)=2f(x)f(y) 형 함수의 f'/f", "도함수의 정의;함수방정식", "정의+함수방정식",
  "중", "f(0)=1/2, f'=2f·f'(0)." + E, MC, "③", "선택지번호", L, M, H, "f(0)=1/2", "f(x+y)=2f(x)f(y), f>0, f'(0)=3일 때 f'(x)/f(x)", "2·3=6", final="③ (6)")
R(18, DR, "DERIV.RULES.SIGMA_POLY_DERIV_SUM_SQUARES", "Σ로 정의된 다항식의 미분계수(제곱합)", "도함수;거듭제곱 미분;수열의 합", "미분+수열",
  "중하", "h=Σn xⁿ → Σn²." + E, S, "385", "값", L, M, L, "", "f_n=x^{n−1}, g_n=nx, h=Σ_{n=1}^{10} f_n g_n일 때 h'(1)", "Σn²=385")
R(19, DR, "DERIV.DERIVFN.DEGREE_ANALYSIS_DIFF_EQ", "차수·최고차 계수 비교로 f'·f 관계식 풀기", "도함수;다항식의 차수;계수비교", "차수+계수비교",
  "중상", "k=1, n=1." + E, S, "3", "값", M, H, H, "상수함수 배제", "다항 f, (x^k+2)f'(x)=f(x), f(3)=5일 때 f(1)", "f=x+2 → 3")
R(20, DF, "DERIV.DIFFABLE.QUADRATIC_BRIDGE_TWO_LINES", "두 직선 사이를 이차함수로 매끄럽게 연결", "미분가능성;연속성;연립방정식", "연속+미분계수",
  "중", "양 끝 연속·접선 4식." + E, S, "10", "값", M, M, M, "", "x+2(x≤−1), −x+2(x≥1) 사이 ax²+bx+c 연결 미분가능, 4(a²+b²+c²)", "a=−1/2, b=0, c=3/2 → 10", **F)
for r in ROWS:
    q = r["_q"]; part, k = ("1. 미분계수", q) if q <= 10 else ("2. 도함수", q - 10)
    lab = f"[{part}] {k}"
    r["원문항번호"] = lab; r["상위원문항번호"] = lab; r["문항이미지/좌표"] = "hwp 본문 " + lab; r["해설페이지"] = "동반 정답 hwp " + lab
build("Batch256", ROWS[:10], 11117)
build("Batch257", ROWS[10:], 11127)
