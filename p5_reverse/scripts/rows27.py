from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h27/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h27/A.hwp','rb').read()).hexdigest()
setup(QID="A02527", SRC="129hlTL_BYO7QI6rtb5Z71JaiNU4q4xSJ", SHA=SQ, TAG="DSM2I201N", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-2-01_소단원평가_기본_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I201N", EXAM="Ⅲ-2-01 정적분 소단원평가(기본)", MID="정적분",
      ANS_QID="A02526", ANS_SRC="1S9n0G8EjVv5DxaPehAFdRY1Zun7ibbCU", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"; MC = "5지선다"
DI = "정적분"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
R(1, DI, "INTEG.DEF.POLY_BASIC_EVAL", "인수분해형 이차식 정적분", "정적분;(β−α)³/6", "단일개념",
  "하", "전개 또는 공식." + E, MC, "②", "선택지번호", L, L, L, "", "∫₋₃¹2(x−1)(x+3)dx", "−2·4³/6=−64/3", final="② (−64/3)")
R(2, DI, "INTEG.DEF.SAME_LIMITS_ZERO", "위끝=아래끝 정적분 0 활용", "정적분 성질;∫ₐᵃ=0", "단일개념",
  "하", "둘째 항 0." + E, MC, "①", "선택지번호", L, L, L, "∫₃³=0", "∫₋₁²(6t+5)(1−2t)dt+∫₃³(1−2t)(6t+5)dt", "−36−6+15=−27", final="① (−27)")
R(3, DI, "INTEG.DEF.PARAM_FROM_VALUE", "정적분 값으로 상수 결정", "정적분;일차방정식", "단일개념",
  "하", "3+4k=5." + E, S, "1/2", "값", L, L, L, "", "∫₀²(x²+2kx+1/6)dx=5, k", "k=1/2")
R(4, DI, "INTEG.DEF.DERIVATIVE_INTEGRAND_FTC", "f'의 정적분 → 함숫값 차", "미적분 기본정리;정적분", "단일개념",
  "하", "2(f(4)−f(1))−30." + E, MC, "⑤", "선택지번호", L, M, L, "", "∫₁⁴{2f'(x)−4x}dx=2, f(1)=−6, f(4)", "2f(4)−18=2 → 10", final="⑤ (10)")
R(5, DI, "INTEG.DEF.QUADRATIC_COEFF_FROM_CONDITIONS", "통과점·정적분 조건으로 이차함수 계수", "정적분;연립방정식;이차함수", "적분+방정식",
  "중하", "b=0, c=1−a." + E, MC, "⑤", "선택지번호", L, M, M, "", "f=ax²+bx+c가 (−1,1),(1,1) 지나고 ∫₀¹f=−1, a", "1−2a/3=−1 → 3", final="⑤ (3)")
R(6, DI, "INTEG.DEF.INEQUALITY_PARAM", "정적분 부등식 정수 최댓값", "정적분;일차부등식", "단일개념",
  "하", "−3k+8>5." + E, MC, "②", "선택지번호", L, M, L, "", "∫₁²(3x²−2kx+1)dx>5인 정수 k 최댓값", "k<1 → 0", final="② (0)")
R(7, DI, "INTEG.DEF.PARAM_FROM_VALUE", "정적분=함숫값 조건으로 상수", "정적분;일차방정식", "단일개념",
  "하", "1/2−2k=2−4k." + E, MC, "④", "선택지번호", L, L, L, "", "f=2x³−4kx, ∫₀¹f=f(1), k", "k=3/4", final="④ (3/4)")
R(8, DI, "INTEG.DEF.CONSTANT_FROM_INTEGRAL", "도함수와 정적분 값으로 함수 결정", "부정적분;적분상수;정적분", "단일개념",
  "하", "∫₀¹=C." + E, MC, "⑤", "선택지번호", L, L, L, "", "f'=6x−2, ∫₀¹f=1, f(x)", "f=3x²−2x+1", final="⑤ (3x²−2x+1)")
R(9, DI, "INTEG.DEF.CUBIC_FROM_GRAPH", "그래프로 삼차함수 결정 후 정적분", "삼차함수;극값;정적분;그래프", "그래프+적분",
  "중", "f'=3a(x²−1)." + E, MC, "②", "선택지번호", L, M, M, "그래프 판독", "삼차함수 y=f(x) 그래프, ∫₋₁¹f",
  "해설 판독: 극점 x=±1, f(0)=−1, f(1)=1 → f=−x³+3x−1 → −2 (그림 의존)", final="② (−2)", **G)
R(10, DI, "INTEG.DEF.PIECEWISE_CONTINUITY", "연속 조건 후 구간별 정적분", "연속;구간별 함수;정적분", "연속+적분",
  "하", "a=0." + E, S, "17/4", "값", L, M, L, "", "f=3x²−2x(x≥1), x³+a(x<1) 연속, ∫₀²f", "1/4+4=17/4")
build("Batch281", ROWS, 11341)
