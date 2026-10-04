from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h36/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h36/A.hwp','rb').read()).hexdigest()
setup(QID="A02536", SRC="1QBVcxkexuB0oBidFc3o5oUbZHNXY6oxN", SHA=SQ, TAG="DSM2I2SV", N=24,
      FNAME="15개정_고등_수학Ⅱ_3-2서술형평가_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I2SV", EXAM="Ⅲ-2 정적분 서술형평가", MID="정적분",
      ANS_QID="A02505", ANS_SRC="1pfBvOBbAkZtt7v-3IgV5h93Zj6akniQa", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형"
DI = "정적분"; FI = "정적분으로 정의된 함수"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
F = dict(fig="설명 그림(gso)")
R(1, DI, "INTEG.DEF.MIN_VALUE_AM_GM", "정적분 값의 최솟값(산술·기하평균)", "정적분 계산;산술기하평균;최솟값", "적분+부등식",
  "중", "9a²−9+3/a²." + E, S, "6√3−9", "값", M, M, M, "a≠0, a²>0", "∫₀³(ax−1/a)²dx 최솟값", "9a²+3/a²≥2√27 → 6√3−9", _pt="5")
R(2, FI, "INTEG.FUNC.DERIV_LIMIT_SYMMETRIC", "적분으로 정의된 함수의 대칭 차분 극한", "미분계수 정의;적분과 미분의 관계", "극한+적분",
  "하", "극한=f'(1)." + E, S, "2", "값", L, M, L, "", "f(x)=∫₀ˣ(3t²−2t+1)dt, lim[f(1+h)−f(1−h)]/2h", "f'(1)=3−2+1=2", _pt="5")
R(3, DI, "INTEG.DEF.INTERVAL_REVERSE_COMBINE", "구간 뒤집기·합치기로 정적분 방정식", "정적분 성질;위끝·아래끝 교환", "단일개념",
  "하", "∫₁ⁿ4x=2n²−2." + E, S, "2", "값", L, L, L, "", "∫₁ⁿ(x+1)²dx+∫ₙ¹(x−1)²dx=6인 자연수 n", "2n²−2=6 → n=2", _pt="5")
R(4, DI, "INTEG.DEF.SUM_OF_ADJACENT_INTERVALS", "Σ 인접 구간 정적분 합 → 한 구간", "정적분 성질;구간 합;시그마", "적분+시그마",
  "하", "∫₀^{a+1}." + E, S, "3", "값", L, M, L, "", "f=2x−3, Σₙ₌₀ᵃ∫ₙⁿ⁺¹f=4인 자연수 a", "a²−a−2=4 → 3", _pt="5")
R(5, DI, "INTEG.DEF.PIECEWISE_CONTINUITY", "연속 조건 후 구간별 정적분", "연속;구간별 함수;정적분", "연속+적분",
  "중하", "a=−3." + E, S, "196/15", "값", M, M, L, "", "f=(x−1)⁴(x≤2), x²+a(x>2) 연속, ∫₀⁴f", "2/5+38/3=196/15", _pt="6")
R(6, DI, "INTEG.DEF.CUSTOM_OPERATION_PIECEWISE", "새 연산 정의 후 구간별 정적분", "새로운 연산;구간별 함수;정적분", "정의+적분",
  "중하", "x²<4: (x²+4)/2, x²≥4: 2x." + E, S, "31/3", "값", M, M, M, "해설 중간식 (x⁴+4)/2 오타(계산은 x²+4)", "a∗b 정의, ∫₀³(x²∗4)dx", "16/3+5=31/3", _pt="5")
R(7, DI, "INTEG.DEF.FLOOR_FUNCTION_SQUARED", "가우스 기호 제곱의 정적분", "가우스 기호;구간 분할;Σk²", "적분+시그마",
  "중하", "Σk² (k=1..9)." + E, S, "285", "값", L, M, M, "x=10 한 점 무시", "∫₀¹⁰[x]²dx", "1²+…+9²=285", _pt="6")
R(8, DI, "INTEG.DEF.ABS_COMPOSITE", "합성함수 절댓값 정적분", "합성함수;절댓값;구간 분할", "합성+절댓값",
  "중하", "|x²−1|." + E, S, "8/3", "값", M, M, L, "", "f=|x−2|, g=x²+1, ∫₋₂¹(f∘g)dx", "4/3+4/3=8/3", _pt="6")
R(9, DI, "INTEG.DEF.ABS_DERIVATIVE_FROM_GRAPH", "|f'| 정적분을 그래프 함숫값으로", "절댓값;도함수 부호;그래프", "그래프+적분",
  "중하", "f(1)−2f(2)+f(3)." + E, S, "22", "값", L, M, M, "f' 부호 구간", "그래프 y=f(x)로 ∫₁³|f'(x)|dx", "해설 판독 f(1)=5, f(2)=−4, f(3)=9 → 22 (그림 의존)", _pt="6", **G)
R(10, DI, "INTEG.DEF.LIMIT_DEFINED_FUNCTION", "극한으로 정의된 함수의 정적분", "수열의 극한;구간별 함수;정적분", "극한+적분",
  "중상", "|3x|>1, <1 구분." + E, S, "5/2", "값", M, H, M, "경계점 값은 적분 무관", "f(x)=lim (3x−2){(3x)²ⁿ−4}/{(3x)²ⁿ+2}, ∫₋₁²f", "−8/3+8/3+5/2=5/2", _pt="6")
R(11, DI, "INTEG.DEF.ODD_EVEN_SYMMETRIC", "기함수·우함수 성질로 대칭 구간 적분", "우함수;기함수;대칭 구간", "단일개념",
  "하", "짝수차만." + E, S, "8", "값", L, L, L, "", "f=x³+2, ∫₋₁¹f(x){f'(x)+1}dx", "2∫₀¹(6x²+2)=8", _pt="5")
R(12, DI, "INTEG.DEF.ODD_FUNCTION_DERIV_PARITY", "기함수 조건에서 f' 우함수 이용", "기함수;우함수;도함수", "대칭+적분",
  "중", "x³f' 기함수." + E, S, "2", "값", L, M, M, "", "f(x)+f(−x)=0, f(a)=1, ∫₋ₐᵃf'(x)(1−x³)dx", "2(f(a)−f(0))=2", _pt="5")
R(13, DI, "INTEG.DEF.FRACTIONAL_PART_PERIODIC", "x−[x] 주기함수 정적분", "가우스 기호;주기함수", "단일개념",
  "하", "20×1/2." + E, S, "10", "값", L, M, L, "", "∫₀²⁰(x−[x])dx", "20∫₀¹x=10", _pt="6")
R(14, DI, "INTEG.DEF.SYMMETRY_PERIOD_CONDITIONS", "대칭·주기 조건으로 정적분", "주기함수;선대칭;정적분", "대칭+주기",
  "중", "단위구간 7개." + E, S, "35/3", "값", L, M, H, "", "f(1−x)=f(1+x), f(x+2)=f(x), ∫₀³f=5, ∫₋₂⁵f", "∫₀¹f=5/3 → 7×5/3=35/3", _pt="7")
R(15, DI, "INTEG.DEF.PERIODIC_COMPOSITE_FROM_GRAPH", "그래프 주기함수 합성 정적분", "주기함수;합성함수;그래프", "그래프+합성",
  "중", "주기 2." + E, S, "16", "값", L, M, M, "그래프 판독", "그래프 y=f(x), g=x², ∫₋₂¹⁰(g∘f)dx", "해설 판독 f=−x+2k 톱니 → 6∫₋₂⁰x²=16 (그림 의존)", _pt="7", **G)
R(16, FI, "INTEG.FUNC.CONSTANT_INTEGRAL_SYSTEM", "정적분 상수 치환 연립", "정적분 상수;연립방정식", "단일개념",
  "중하", "a−b=−2, 2a−b=−4." + E, S, "1", "값", L, M, M, "", "f=x+1+∫₀¹g, g=2x−3+∫₀²f, f(1)−g(1)", "a=−2,b=0 → 0−(−1)=1", _pt="5")
R(17, FI, "INTEG.FUNC.DIVISIBLE_SQUARE_REMAINDER", "(x−1)²로 나누어떨어짐 → 나머지", "나머지정리;f(1)=f'(1)=0;적분과 미분", "적분+나머지정리",
  "중", "a=1, g(1)=−1." + E, S, "−1", "값", L, M, M, "", "f=x²−ax+∫₁ˣg(t)dt가 (x−1)²으로 나누어떨어질 때 g를 x−1로 나눈 나머지", "g(1)=−1", _pt="6")
R(18, FI, "INTEG.FUNC.EQUATION_DIFFERENTIATE_SUM", "적분방정식 미분 후 Σ 계산", "적분과 미분;적분상수;Σk²", "적분+시그마",
  "중", "f=x⁴−x²." + E, S, "330", "값", M, M, M, "", "x²f(x)=⅔x⁶−½x⁴−⅙+2∫₁ˣtf(t)dt, Σf(√k)", "385−55=330", _pt="5")
R(19, FI, "INTEG.FUNC.CONVOLUTION_TYPE_X_MINUS_T", "∫(x−t)f(t)dt 꼴 두 번 미분", "적분과 미분;항등식", "단일개념",
  "중", "f=6x, a=−3/2, b=2." + E, S, "2", "값", M, M, M, "x를 밖으로", "x³+2ax+b=∫₁ˣ(x−t)f(t)dt, 4a+b+f(1)", "−6+2+6=2", _pt="6")
R(20, FI, "INTEG.FUNC.CONVOLUTION_TYPE_X_MINUS_T", "∫₀ˣ(x−t)f(t)dt 꼴에서 f 최솟값", "적분과 미분;최솟값", "적분+최대최소",
  "중하", "f=6x²+8." + E, S, "8", "값", L, M, M, "", "∫₀ˣ(x−t)f(t)dt=½x⁴+4x², f 최솟값", "8", _pt="6")
R(21, FI, "INTEG.FUNC.CONSTANT_INTEGRAL_SELF", "정적분 상수 치환(자기 참조)", "정적분 상수", "단일개념",
  "하", "k=4+2k." + E, S, "−2", "값", L, L, L, "", "f(x)=2x+∫₀²f(x)dx, f(1)", "k=−4 → −2", _pt="5")
R(22, FI, "INTEG.FUNC.CONVOLUTION_OPERATION", "합성곱 연산 정의 후 함수 결정", "새로운 연산;적분과 미분;항등식", "정의+적분",
  "상", "f=f'+12x²." + E, S, "60", "값", M, H, H, "차수 결정", "(f∗g)(x)=∫₀ˣf(t)g(x−t)dt, g=x−1, (f∗g)=x⁴−24x, f(1)", "f=12x²+24x+24 → 60", _pt="6")
R(23, DI, "INTEG.DEF.ABS_PARAM_MAXIMIZE", "절댓값 정적분 매개변수 최대화", "절댓값;정적분;최대최소;도함수", "적분+최대최소",
  "중", "F(a)=a³/3−a/2+1/3." + E, S, "0", "값", M, M, M, "극소는 최소, 최대는 끝점", "0≤a≤1, ∫₀¹x|x−a|dx 최대인 a", "F(0)=1/3>F(1)=1/6 → a=0", _pt="5")
R(24, FI, "INTEG.FUNC.VARIABLE_BOTH_LIMITS_EXTREMUM", "위·아래끝 모두 변수인 함수 극값", "적분과 미분;극값", "적분+극값",
  "중하", "f'=2ax+a²−2a." + E, S, "4", "값", L, M, M, "", "f(x)=∫ₓ^{x+a}t(t−2)dt, x=−1에서 극소, a>0", "a²−4a=0 → 4 (f''=2a>0 극소 확인)", _pt="5")
for i in range(3):
    build(f"Batch{274+i}", ROWS[i*10:(i+1)*10], 11287+i*10)
