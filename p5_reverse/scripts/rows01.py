from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h01/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h01/A.hwp','rb').read()).hexdigest()
setup(QID="A02501", SRC="1BhdksK-tR8sV9hu_Z-veGYgI4H-11yjA", SHA=SQ, TAG="DSM2I1SV", N=20,
      FNAME="15개정_고등_수학Ⅱ_3-1서술형평가_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I1SV", EXAM="Ⅲ-1 부정적분 서술형평가", MID="부정적분",
      ANS_QID="A02523", ANS_SRC="1zVZuSs9cIG9jkLcSi6gKSVHh3iX77gnY", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형"
U = "부정적분"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
R(1, U, "INTEG.INDEF.DEFINITION_DERIVATIVE_OF_PRODUCT", "∫F=fg → F=(fg)'", "부정적분 정의;곱의 미분", "단일개념",
  "하", "F=(fg)'." + E, S, "−4", "값", L, L, L, "", "f=2x²−1, g=4x+3, ∫F(x)dx=f(x)g(x), F(0)", "F=24x²+12x−4 → −4", _pt="5")
R(2, U, "INTEG.INDEF.DERIV_LIMIT_SYMMETRIC", "부정적분 함수의 대칭 차분 극한", "부정적분;미분계수 정의", "극한+적분",
  "하", "2f'(1)." + E, S, "6", "값", L, M, L, "", "f=∫(x³+x+1)dx, lim[f(1+h)−f(1−h)]/h", "2·3=6", _pt="5")
R(3, U, "INTEG.INDEF.INTEGRAL_OF_DERIVATIVE", "∫(d/dx g)dx=g+C와 조건으로 상수 결정", "부정적분과 미분;적분상수", "단일개념",
  "중하", "a=15, C=15." + E, S, "2", "값", L, M, M, "", "f=∫{d/dx(2x⁴−ax²)}dx, f(1)=2, f'(2)=4, a+f(2)", "15+(−13)=2", _pt="5")
R(4, U, "INTEG.INDEF.DERIVATIVE_OF_INTEGRAL_LOG", "d/dx∫ 와 로그·삼각 방정식", "부정적분과 미분;로그 밑 조건;삼각함수", "적분+방정식",
  "중하", "sin(π/2)=1." + E, S, "x=3", "값", L, M, M, "밑 x≠1", "sin{(π/2)log_x(d/dx∫x dx)}=x²−4x+4의 해", "x²−4x+3=0, x≠1 → 3", _pt="5")
R(5, U, "INTEG.INDEF.SEQUENCE_PRODUCT_TELESCOPE", "부정적분 수열의 곱(망원곱)", "부정적분;적분상수;곱", "적분+수열",
  "하", "n/(n+1) 곱." + E, S, "1/11", "값", L, M, L, "", "f_n=∫nxⁿdx, f_n(0)=0, f₁(1)×…×f₁₀(1)", "1/11", _pt="5")
R(6, U, "INTEG.INDEF.FROM_DERIVATIVE_CONSTANT", "도함수로 함수 복원(적분상수)", "부정적분;적분상수", "단일개념",
  "하", "C=3." + E, S, "−3", "값", L, L, L, "해설 본문 '+5' 표기 오타(계산은 −5)", "f'=2x³−3x−5, f(0)=3, f(1)", "1/2−3/2−5+3=−3", _pt="5")
R(7, U, "INTEG.INDEF.EQUATION_LINEAR_FUNCTION", "부정적분 포함 등식에서 일차함수 결정", "부정적분과 미분;항등식", "단일개념",
  "중하", "b=a−1, a+b=3." + E, S, "−1/2", "값", L, M, M, "", "일차 f, 2∫f=f+xf−x−1, f(1)=3, x절편", "f=2x+1 → −1/2", _pt="6")
R(8, U, "INTEG.INDEF.SUM_PRODUCT_DERIVATIVES", "합·곱의 도함수로 두 함수 결정", "부정적분;인수분해;다항함수", "적분+인수분해",
  "중", "f=x²+2, g=x−1." + E, S, "3", "값", M, M, M, "인수 배분 f(0),g(0)로 결정", "(f+g)'=2x+1, (fg)'=3x²−2x+2, f(0)=2, g(0)=−1, f(1)−g(1)", "3", _pt="6")
R(9, U, "INTEG.INDEF.TANGENT_SLOPE_MIN_VALUE", "접선 기울기와 최솟값으로 이차함수", "부정적분;최솟값;접선 기울기", "단일개념",
  "하", "C−8=5." + E, S, "f(x)=½x²−4x+13", "식", L, M, L, "", "최솟값 5, 접선 기울기 x−4인 이차함수 f", "½(x−4)²+5", _pt="6")
R(10, U, "INTEG.INDEF.DIFFERENCE_QUOTIENT_IDENTITY", "증분 등식에서 도함수 → 함수", "도함수 정의;부정적분;연립", "극한+적분",
  "중", "f'=mx, m=4." + E, S, "11", "값", L, M, M, "", "f(t+h)−f(t)=mth+2h², f(1)=5, f(3)=21, f(2)", "f=2x²+3 → 11", _pt="6")
R(11, U, "INTEG.INDEF.FUNCTIONAL_EQUATION", "함수방정식에서 도함수 → 함수", "도함수 정의;함수방정식;부정적분", "함수방정식+적분",
  "중", "f'=−3x²." + E, S, "f(x)=−x³", "식", M, H, M, "f(0)=0, lim f(h)/h=0", "f(x+y)=f(x)+f(y)−3xy(x+y), f'(1)=−3", "f=−x³ (대입 검산 일치)", _pt="6")
R(12, U, "INTEG.INDEF.PIECEWISE_DERIVATIVE_GRAPH", "구간별 도함수 그래프로 연속함수 복원", "부정적분;연속;그래프", "그래프+연속",
  "중상", "x≤−1 직선, x>−1 포물선." + E, S, "7", "값", M, H, M, "그래프 판독", "f' 그래프(직선+포물선), f(−3)=−1, f 연속, f(2)",
  "해설 판독: f'=x+3(x≤−1), x²+1(x>−1) → C₁=7/2, C₂=7/3 → 7 (그림 의존)", _pt="7", **G)
R(13, U, "INTEG.INDEF.EXTREMA_FROM_DERIVATIVE", "도함수와 극솟값으로 함수 복원, 극댓값", "부정적분;극값;증감표", "적분+극값",
  "중", "a=−1, C=2." + E, S, "32/27", "값", M, M, M, "", "f'=3x²−2x+a, x=1 극솟값 1, a+M", "M=59/27 → 32/27", _pt="7")
R(14, U, "INTEG.INDEF.CUBIC_FROM_DERIVATIVE_GRAPH", "도함수 그래프와 극값으로 삼차함수 복원", "부정적분;극값;그래프", "그래프+극값",
  "중", "f'=ax(x−2)." + E, S, "f(x)=x³−3x²+3", "식", M, M, M, "그래프 판독", "f' 포물선 그래프(근 0,2), 극댓값 3, 극솟값 −1",
  "a=3, C=3 (근 0,2는 그림 의존)", _pt="7", **G)
R(15, U, "INTEG.INDEF.APPLIED_RATE", "변화율 적분 활용(음속)", "부정적분;변화율;활용", "적분+활용",
  "하", "v=0.4t+331." + E, S, "1412.5 Hz", "값", L, M, L, "단위 cm→m", "dv/dt=0.4, v(0)=331, v=μλ, 20℃ λ=24cm, μ", "339/0.24=1412.5", _pt="6")
R(16, U, "INTEG.INDEF.FUNCTION_FROM_INTEGRAL_RELATION", "∫(f−g)=f'+g' 관계로 g 결정", "부정적분;미분;계수비교", "적분+항등식",
  "상", "g 삼차, 계수비교." + E, S, "g(x)=x³+2x²−9x−4", "식", H, H, H, "차수 결정", "f=x³+2x²+3x+4, f−g의 한 부정적분이 f'+g', g",
  "g=x³+2x²−9x−4 (검산: ∫(12x+8)=6x²+8x−6=f'+g')", _pt="7")
R(17, U, "INTEG.INDEF.SUM_OF_INTEGRALS_CONSTANT", "부정적분 합 정리 후 적분상수", "부정적분;전개;적분상수", "단일개념",
  "하", "½x⁴+12x²+C." + E, S, "34", "값", L, M, L, "", "F=∫(x+2)³dx+∫(x−2)³dx, F(√2)=4, F(2)", "C=−22 → 34", _pt="6")
R(18, U, "INTEG.INDEF.F_AND_ANTIDERIVATIVE_RELATION", "f와 부정적분 F의 관계식 미분", "부정적분;미분;항등식", "단일개념",
  "중", "f'=12x." + E, S, "20", "값", L, M, M, "", "(x−1)f(x)−F(x)=4x³−6x², f(1)=2, f(−2)", "f=6x²−4 → 20", _pt="6")
R(19, U, "INTEG.INDEF.RELATION_GPRIME_EQ_F", "g'=f 관계와 극값", "부정적분;미분;극값", "적분+극값",
  "중", "xf'=12x³−6x²−6x." + E, S, "7", "값", M, M, M, "원문 식 표기 문제",
  "f(0)=1, g'=f, g=xf−3x⁴+2x³+3x² (원문엔 'g=xf=3x⁴+…'로 표기), 4M+m",
  "해설 해석(g=xf−3x⁴+2x³+3x²): f=4x³−3x²−6x+1, M=11/4, m=−4 → 7. 원문 표기('=') 그대로면 f(0)=0이 되어 f(0)=1과 모순",
  final="7 (해설 해석 기준)", _pt="6",
  ready="REVIEW", status="원문 기호 오타 의심('=' vs '−') — 해설 해석으로 답 일치", trust="중간(원문 오타)", review="REVIEW-원문오타")
R(20, U, "INTEG.INDEF.SERIES_TELESCOPING", "도함수 급수의 적분과 망원합", "부정적분;부분분수;Σ", "적분+수열",
  "중", "1/(k(k+1))." + E, S, "−1/2012", "값", M, M, M, "", "f'=x+x²/2+…+x²⁰¹¹/2011, f(0)=−1, f(1)", "1−1/2012−1", _pt="6")
for i in range(2):
    build(f"Batch{284+i}", ROWS[i*10:(i+1)*10], 11371+i*10)
