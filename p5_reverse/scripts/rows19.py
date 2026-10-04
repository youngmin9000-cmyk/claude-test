from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h19/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h19/A.hwp','rb').read()).hexdigest()
setup(QID="A02519", SRC="1r5X3VtVsv4yKgB03E9c45iFUhZuf5CMf", SHA=SQ, TAG="DSM2I101A", N=5,
      FNAME="15개정_고등_수학Ⅱ_3-1-01_소단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I101A", EXAM="Ⅲ-1-01 부정적분 소단원평가(발전)", MID="부정적분",
      ANS_QID="A02518", ANS_SRC="1DX_ZUz9B5S520nsRpDoguxTFxyyb5ZTP", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"; MC = "5지선다"
U = "부정적분"
R(1, U, "INTEG.INDEF.DEFINITION_DIFFERENTIATE_FACTOR", "∫(3−x)f dx 미분 후 인수분해로 f", "부정적분 정의;미분;인수분해", "단일개념",
  "중하", "(3−x)(4x²+2)." + E, S, "f(x)=4x²+2", "식", L, M, M, "", "∫(3−x)f(x)dx=6x−x²+4x³−x⁴+C", "6−2x+12x²−4x³=(3−x)(4x²+2)")
R(2, U, "INTEG.INDEF.FUNCTIONAL_EQUATION", "가법 함수방정식에서 도함수 → 함수", "함수방정식;도함수 정의;부정적분", "함수방정식+적분",
  "중", "f'(x)=f'(0)=3." + E, S, "f(x)=3x", "식", L, M, M, "f(0)=0", "f(x+y)=f(x)+f(y), f'(0)=3", "f=3x")
R(3, U, "INTEG.INDEF.DERIV_INTEGRAL_ORDER_TFQ", "d/dx∫ 와 ∫d/dx 차이 판정", "부정적분과 미분;적분상수", "단일개념",
  "중", "f=g−g(0)." + E, MC, "①", "선택지번호", L, H, M, "적분상수 처리", "d/dx∫f dx−∫(d/dx g)dx=1, f(0)=0, 옳은 것", "f=g+C, C=−g(0) → ①", final="① (g(0)=0이면 f=g)")
R(4, U, "INTEG.INDEF.CONSTANT_FUNCTION_DERIVATIVE_ZERO", "도함수 0 → 상수함수(f²−g²)", "미분;상수함수;초기조건", "단일개념",
  "중", "F'=0." + E, MC, "①", "선택지번호", L, M, M, "", "f'=g, g'=f, f(0)=1, g(0)=0, f²−g²", "1", final="① (1)")
R(5, U, "INTEG.INDEF.QUADRATIC_FROM_IDENTITY_MAX", "항등식으로 이차함수 결정 후 최댓값", "항등식;d/dx∫f=f;최댓값", "단일개념",
  "중하", "f=−x²−2x−2." + E, MC, "③", "선택지번호", L, M, L, "", "이차 f=f'−x², d/dx∫f dx 최댓값", "−(x+1)²−1 → −1", final="③ (−1)")
build("Batch288", ROWS, 11406)
