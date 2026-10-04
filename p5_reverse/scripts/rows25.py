from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h25/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h25/A.hwp','rb').read()).hexdigest()
setup(QID="A02525", SRC="1UrY2mMJI55UY-YgYyR5Xhm_pN4ZD0udz", SHA=SQ, TAG="DSM2I2MA", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-2_중단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I2MA", EXAM="Ⅲ-2 정적분 중단원평가(발전)", MID="정적분",
      ANS_QID="A02503", ANS_SRC="1g75osEnTLpHDiwZcLz6G8pwTJFkh8DcE", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"; MC = "5지선다"
DI = "정적분"; FI = "정적분으로 정의된 함수"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
R(1, DI, "INTEG.DEF.COMBINE_RATIONAL_TO_POLY", "구간 뒤집기로 결합 후 인수분해 정적분", "정적분 성질;인수분해", "단일개념",
  "중하", "(x³−1)/(x−1)." + E, MC, "③", "선택지번호", L, M, M, "개별 적분은 x=1에서 발산",
  "∫₀¹x³/(x−1)dx+∫₁⁰1/(x−1)dx", "∫₀¹(x²+x+1)=11/6 (해설 일치). 단 각 항은 x=1에서 이상적분·발산 — 교과 관례상 결합 처리", final="③ (11/6)",
  ready="REVIEW", status="해설 일치·원문 엄밀성 문제(개별 적분 발산)", trust="중간(원문 모호)", review="REVIEW-원문모호")
R(2, DI, "INTEG.DEF.PIECEWISE_SHIFTED", "평행이동한 구간별 함수 곱의 정적분", "구간별 함수;평행이동;정적분", "단일개념",
  "중", "x=0 분할." + E, S, "−19/12", "값", M, M, M, "x+1≤1 ⇔ x≤0", "f=2−x²(x≤1), 2−x(x>1), ∫₋₁²xf(x+1)dx", "−11/12−2/3=−19/12")
R(3, DI, "INTEG.DEF.EVEN_FUNCTION_SPLIT", "우함수 성질로 정적분을 a,b,c로 표현", "우함수;구간 분할", "대칭+적분",
  "중하", "∫₋₁⁰=a/2." + E, S, "a/2+b+c", "식", L, M, M, "", "f(−x)=f(x), ∫₋₁¹=a, ∫₀³=b, ∫₃⁴=c, ∫₋₁⁴f", "a/2+b+c", fig="설명 그림(gso)")
R(4, FI, "INTEG.FUNC.MAXMIN_ON_INTERVAL", "적분 정의 함수의 닫힌구간 최대·최소", "적분과 미분;증감표;최대최소", "적분+최대최소",
  "중하", "f'=x(x−2)." + E, S, "최댓값 4/3, 최솟값 0", "값", M, M, M, "", "f(x)=∫₋₁ˣ(t²−2t)dt, [0,3]", "f(0)=4/3, f(2)=0, f(3)=4/3")
R(5, FI, "INTEG.FUNC.PROPERTIES_FROM_GRAPH_TFQ", "그래프로 주어진 f의 적분함수 성질 판정(ㄱㄴㄷ)", "적분과 미분;극값;최댓값", "그래프+판정",
  "중", "g'=f." + E, MC, "③", "선택지번호", L, H, M, "극소≠최대", "[0,5]에서 g=∫₀ˣf, f 그래프, ㄱ x=1 극대 ㄴ x=3 최대 ㄷ ∫₁³g'<0",
  "해설 판독: f 부호 +(0,1), −(1,3), +(3,5) → ㄱ참 ㄴ거짓 ㄷ참 (그림 의존)", final="③ (ㄱ, ㄷ)", **G)
R(6, DI, "INTEG.DEF.ABS_QUADRATIC_PLUS", "절댓값 이차식 포함 정적분", "절댓값;구간 분할", "단일개념",
  "중하", "내부 8, 외부 6x²+2." + E, S, "88", "값", M, M, L, "해설 외부 식 부호 오타(계산은 정상)", "∫₋₂³(|3x²−3|+3x²+5)dx", "16+16+56=88")
R(7, FI, "INTEG.FUNC.CONVOLUTION_TYPE_X_MINUS_T", "∫₁ˣ(x−t)f(t)dt 꼴 미분, x=1 대입", "적분과 미분;항등식", "단일개념",
  "중", "a=−1, b=−1." + E, S, "1", "값", L, M, M, "", "∫₁ˣ(x−t)f(t)dt=ax²+2x+b, ab", "1")
R(8, FI, "INTEG.FUNC.EQUATION_WITH_FPRIME_INTEGRAL", "∫₀ˣf'(t)dt 포함 함수방정식", "적분과 미분;적분상수", "단일개념",
  "중하", "f'=−2x+3, f(0)=0." + E, MC, "①", "선택지번호", L, M, M, "", "f=2x²−6x+3∫₀ˣf'(t)dt, f(2)", "f=−x²+3x → 2", final="① (2)")
R(9, DI, "INTEG.DEF.BETWEEN_ROOTS_FORMULA", "두 근 사이 이차식 정적분 −(β−α)³/6", "근과 계수의 관계;정적분 공식", "근과계수+적분",
  "중하", "β−α=√13." + E, S, "−13√13/6", "값", L, M, M, "", "x²−5x+3=0 두 근 α<β, ∫ₐᵝ(x²−5x+3)dx", "−(√13)³/6")
R(10, FI, "INTEG.FUNC.MOVING_INTERVAL_MIN", "구간 [x,x+1] 적분함수의 최솟값", "적분과 미분;최솟값;이차함수", "그래프+적분",
  "중", "g'=f(x+1)−f(x)=4x−4." + E, S, "−13/3", "값", M, M, M, "그래프로 f=2x(x−3) 판독", "이차항 계수 2인 f 그래프, g=∫ₓ^{x+1}f, 최솟값",
  "해설 판독 근 0,3 → f=2x²−6x, g(1)=∫₁²f=−13/3 (그림 의존)", **G)
build("Batch282", ROWS, 11351)
