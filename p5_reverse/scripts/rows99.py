from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h99/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h99/A.hwp','rb').read()).hexdigest()
setup(QID="A02499", SRC="1eshV0vdN75dQ_beo_AhrWDl6P0FrBgjp", SHA=SQ, TAG="DSM2I102N", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-1-02_소단원평가_기본_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I102N", EXAM="Ⅲ-1-02 부정적분의 계산 소단원평가(기본)", MID="부정적분",
      ANS_QID="A02498", ANS_SRC="1tW1CRUCfJh2eT0TBVWT045ioAc5HhSlK", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
MC = "5지선다"
S = "서술형(단답)"
U = "부정적분"
R(1, U, "INTEG.INDEF.THROUGH_ORIGIN_THEN_EXTREMUM", "원점 통과로 적분상수 결정 후 극솟값", "부정적분;적분상수;극값", "적분+극값",
  "하", "C=0, f'=(3x−1)(x−1)." + E, MC, "③", "선택지번호", L, L, L, "", "f=∫(3x²−4x+1)dx, 원점 통과, 극솟값", "f=x³−2x²+x, f(1)=0", final="③ (0)")
R(2, U, "INTEG.INDEF.DIVISIBILITY_FACTOR_CONDITIONS", "인수정리로 미정계수·적분상수 연립", "부정적분;인수정리;연립방정식", "적분+인수정리",
  "중하", "f(1)=f(2)=0." + E, S, "−17", "값", L, M, M, "", "f'=6x²+2x+a, f가 x²−3x+2로 나누어떨어질 때 a", "a+C=−3, 2a+C=−20 → −17")
R(3, U, "INTEG.INDEF.TELESCOPING_COEFF_SUM", "부정적분 계수의 부분분수 합(망원합)", "부정적분;부분분수;적분상수", "적분+수열합",
  "중하", "Σ1/(k(k+1))=10/11." + E, MC, "⑤", "선택지번호", M, M, M, "1/(k(k+1)) 꼴 인식", "f=∫(x+x²/2+…+x¹⁰/10)dx, f(1)=2, f(0)", "10/11+C=2 → C=12/11", final="⑤ (12/11)")
R(4, U, "INTEG.INDEF.PARAM_FAMILY_INEQUALITY_MAX_N", "자연수 매개 부정적분 함숫값 부등식의 최대 n", "부정적분;부등식;수의 대소", "적분+부등식",
  "중", "1/(n+1)+1/(n+2)>1/7." + E, S, "12", "값", L, M, M, "경계 n=12,13 비교", "f_n=∫(xⁿ+xⁿ⁺¹)dx, f_n(0)=0, f_n(1)>1/7인 n 최댓값", "n=12: 27/182>1/7, n=13: 29/210<1/7 → 12")
R(5, U, "INTEG.INDEF.CONSTANT_FROM_DIFFERENCE_CONDITION", "다른 함수와의 차 조건으로 적분상수", "부정적분;적분상수", "단일개념",
  "하", "C=2." + E, S, "1", "값", L, L, L, "", "f'=3x²+2x+1, g=x³+x²+x, f(1)−g(1)=2, f(−1)", "f=x³+x²+x+2 → 1")
R(6, U, "INTEG.INDEF.F_AND_ANTIDERIVATIVE_RELATION", "xf−F 관계식 미분으로 이차함수 결정", "부정적분;미분;항등식", "단일개념",
  "중하", "xf'=x(3x−8)." + E, S, "f(x)=(3/2)x²−8x−6", "식", L, M, M, "", "xf−F=x³−4x², f(1)=−25/2, f", "f'=3x−8, C=−6")
R(7, U, "INTEG.INDEF.INTEGRAL_EQ_XF_RELATION", "∫f=xf−(다항식) 미분으로 f 결정", "부정적분;곱의 미분;항등식", "단일개념",
  "중하", "xf'=12x³+6x²." + E, S, "−6", "값", L, M, M, "", "∫f dx=xf−3x⁴−2x³, f(1)=2, f(−1)", "f=4x³+3x²−5 → −6")
R(8, U, "INTEG.INDEF.FUNCTIONAL_EQ_DERIVATIVE_DEF", "함수방정식+도함수 정의로 f' 구한 뒤 적분", "함수방정식;도함수의 정의;부정적분", "함수방정식+적분",
  "중", "lim f(h)/h=4, f'=4−x." + E, S, "6", "값", L, M, H, "f(0)=0 유도", "f(x+y)=f(x)+f(y)−xy, f'(1)=3, f(2)", "f=−x²/2+4x → 6")
R(9, U, "INTEG.INDEF.FUNCTIONAL_EQ_DERIVATIVE_DEF", "함수방정식+도함수 정의로 f' 구한 뒤 적분", "함수방정식;도함수의 정의;부정적분", "함수방정식+적분",
  "중", "f'=x²+1." + E, S, "f(x)=(1/3)x³+x", "식", L, M, H, "f(0)=0 유도", "f(x+y)=f(x)+f(y)+xy(x+y), lim f(h)/h=1, f", "f'=1+x², C=0")
R(10, U, "INTEG.INDEF.FUNCTIONAL_EQ_DERIVATIVE_DEF", "함수방정식+도함수 정의로 f' 구한 뒤 적분", "함수방정식;도함수의 정의;부정적분", "함수방정식+적분",
  "중", "f'=3x+2." + E, S, "7/2", "값", L, M, H, "f(0)=0 유도", "f(a+b)=f(a)+f(b)+3ab, f'(0)=2, f(1)", "f=(3/2)x²+2x → 7/2")
build("Batch292", ROWS, 11436)
