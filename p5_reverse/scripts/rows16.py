from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h16/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h16/A.hwp','rb').read()).hexdigest()
setup(QID="A02516", SRC="19M7LIdZBPulOlH1A4a36-fuS-lZiFV2y", SHA=SQ, TAG="DSM2I101N", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-1-01_소단원평가_기본_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I101N", EXAM="Ⅲ-1-01 부정적분 소단원평가(기본)", MID="부정적분",
      ANS_QID="A02548", ANS_SRC="1uXZ622NAtHokaFePOStSxRLDb6nI4rlO", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
T = "부정적분"
R(1, T, "INTEG.INDEF.COEFF_MATCH_BY_DIFFERENTIATION", "부정적분 결과에서 계수 비교", "부정적분;미분;계수비교", "단일개념",
  "하", "양변 미분." + E, MC, "③", "선택지번호", L, L, L, "", "∫(9x²+ax+1)dx=bx³+9x²+cx+C일 때 a+b+c", "b=3, a=18, c=1 → 22", final="③ (22)")
R(2, T, "INTEG.INDEF.DERIVE_F_THEN_MAX", "부정적분에서 f 구한 뒤 최댓값", "부정적분;미분;이차함수 최댓값", "적분+최대최소",
  "하", "f=−6(x−1)²+7." + E, MC, "④", "선택지번호", L, L, L, "", "∫f dx=−2x³+6x²+x+C일 때 f 최댓값", "7", final="④ (7)")
R(3, T, "INTEG.INDEF.FACTOR_PRODUCT_INTEGRAND", "(x−1)f(x) 부정적분에서 f 결정", "부정적분;미분;인수분해", "단일개념",
  "하", "6x(x−1)=(x−1)f." + E, MC, "⑤", "선택지번호", L, L, L, "", "∫(x−1)f(x)dx=2x³−3x²+2일 때 f(2)", "f=6x → 12", final="⑤ (12)")
R(4, T, "INTEG.INDEF.FACTOR_PRODUCT_INTEGRAND", "(x−3)f(x) 부정적분에서 f 결정", "부정적분;미분;인수분해", "단일개념",
  "하", "3(x+3)(x−3)." + E, MC, "④", "선택지번호", L, L, L, "", "∫(x−3)f(x)dx=x³−27x일 때 f(−1)", "f=3(x+3) → 6", final="④ (6)")
R(5, T, "INTEG.INDEF.ANTIDERIVATIVE_TO_F", "부정적분 하나로 f 구하기", "부정적분;미분", "단일개념",
  "하", "F'=f." + E, MC, "②", "선택지번호", L, L, L, "", "f의 부정적분 중 하나가 x³+x²+1일 때 f", "3x²+2x", final="② (3x²+2x)")
R(6, T, "INTEG.INDEF.INTEGRAND_FROM_PRODUCT", "∫F=fg에서 곱의 미분으로 F(0)", "부정적분;곱의 미분법", "적분+곱의미분",
  "하", "F=(fg)'." + E, S, "−4", "값", L, L, L, "", "f=2x²−1, g=4x+3, ∫F dx=f·g일 때 F(0)", "f'(0)g(0)+f(0)g'(0)=0−4")
R(7, T, "INTEG.INDEF.ANTIDERIVATIVE_CONDITIONS_COEFF", "부정적분 조건으로 계수·함숫값", "부정적분;미분계수", "단일개념",
  "하", "f=3x²+2ax+2." + E, S, "3", "값", L, L, L, "", "F=x³+ax²+2x가 f의 부정적분, f(0)=b, f'(0)=3일 때 ab", "b=2, a=3/2 → 3")
R(8, T, "INTEG.INDEF.FUNCTIONAL_EQ_DEGREE_ANALYSIS", "부정적분 항등식에서 차수 분석으로 f 결정", "부정적분;다항식의 차수;계수비교", "적분+차수",
  "중", "f−g=f'+g', f 이차." + E, MC, "⑤", "선택지번호", L, M, H, "차수 판단", "g=x²+x−2, ∫(f−g)dx=f+g+C일 때 f(1) (원문 '다항함수 F(x)'는 f(x) 오기)", "f=x²+5x+4 → 10", final="⑤ (10)")
R(9, T, "INTEG.INDEF.LIMIT_AS_DERIVATIVE_OF_INTEGRAL", "부정적분 정의 함수의 극한(미분계수)", "부정적분;미분계수;극한 변형", "적분+극한",
  "하", "f'(2)/4." + E, MC, "③", "선택지번호", L, M, L, "", "f=∫(4x²−3x+2)dx일 때 lim (f(x)−f(2))/(x²−4), x→2", "12/4=3", final="③ (3)")
R(10, T, "INTEG.INDEF.DOUBLE_DIFFERENTIATION_PRODUCT", "F=x∫g² 두 번 미분으로 f'(0)", "부정적분;곱의 미분법", "적분+곱의미분",
  "중", "f'=2g²+2xgg'." + E, MC, "③", "선택지번호", L, M, M, "", "F(x)=x∫{g(x)}²dx, g(0)=5일 때 f'(0)", "2·25=50", final="③ (50)")
build("Batch265", ROWS, 11202)
