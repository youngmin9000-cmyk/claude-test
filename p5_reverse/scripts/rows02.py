from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h02/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h02/A.hwp','rb').read()).hexdigest()
setup(QID="A02502", SRC="1RPASoYsb6vFt8-ZllWZXv2iPMEK7quUs", SHA=SQ, TAG="DSM2I2MN", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-2_중단원평가_기본_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I2MN", EXAM="Ⅲ-2 정적분 중단원평가(기본)", MID="정적분",
      ANS_QID="A02524", ANS_SRC="18GZWpFtCAxS5L8KIJl0FNDfL9HnMZUBv", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"; MC = "5지선다"
DI = "정적분"; FI = "정적분으로 정의된 함수"
R(1, DI, "INTEG.DEF.PARAM_FROM_VALUE", "정적분 값으로 상수 결정", "정적분;일차방정식", "단일개념",
  "하", "3+a/3=0." + E, MC, "②", "선택지번호", L, L, L, "", "∫₀¹(4x³+ax²+2)dx=0, a", "a=−9", final="② (−9)")
R(2, DI, "INTEG.DEF.ADJACENT_INTERVALS_MERGE", "인접 구간 합치기 + 대칭", "정적분 성질;구간 합;우함수·기함수", "단일개념",
  "하", "∫₋₂²." + E, MC, "③", "선택지번호", L, L, L, "", "∫₋₂¹+∫₁²(−6x²+2x−1)dx", "2∫₀²(−6x²−1)=−36", final="③ (−36)")
R(3, FI, "INTEG.FUNC.DERIV_LIMIT_FORMS", "적분 정의 함수의 미분계수 극한", "미분계수 정의;적분과 미분", "단일개념",
  "하", "f'(3)." + E, MC, "①", "선택지번호", L, L, L, "", "f=∫₀ˣ(t³−5t²+3)dt, lim[f(x)−f(3)]/(x−3)", "27−45+3=−15", final="① (−15)")
R(4, FI, "INTEG.FUNC.LIMIT_OF_INTEGRAL_OVER_H", "정적분 극한 (1/h)∫ 꼴", "미분계수 정의;부정적분;극한", "극한+적분",
  "중하", "3f(1)." + E, MC, "①", "선택지번호", L, M, M, "구간 길이 3h", "lim (1/h)∫_{1−h}^{1+2h}(2x²−x+a)dx=4, a", "3(1+a)=4 → 1/3", final="① (1/3)")
R(5, FI, "INTEG.FUNC.CONSTANT_INTEGRAL_SELF", "정적분 상수 치환(자기 참조)", "정적분 상수;연립", "단일개념",
  "중하", "4+2a=a." + E, MC, "①", "선택지번호", L, M, M, "", "f=2x+∫₀²(4x−3)f(t)dt, ∫₀²f", "a=−4", final="① (−4)")
R(6, DI, "INTEG.DEF.DERIVATIVE_INTEGRAND_FTC", "f'의 정적분 → 함숫값 차", "미적분 기본정리;정적분", "단일개념",
  "하", "13−2f(3)=1." + E, MC, "④", "선택지번호", L, M, L, "", "∫₂³{3x²−2f'(x)}dx=1, f(2)=−3, f(3)", "6", final="④ (6)")
R(7, DI, "INTEG.DEF.ODD_EVEN_SYMMETRIC", "대칭 구간에서 짝수차항만 남기기", "우함수;기함수;대칭 구간", "적분+수열",
  "중하", "짝수차 50개." + E, MC, "⑤", "선택지번호", L, M, M, "", "∫₋₁¹(1+2x+3x²+…+100x⁹⁹)dx", "2×50=100", final="⑤ (100)")
R(8, DI, "INTEG.DEF.ABS_PARAM_MINIMIZE", "절댓값 정적분 매개변수 최소화", "절댓값;정적분;이차함수 최소", "적분+최대최소",
  "중하", "(a−3/2)²+9/4." + E, S, "3/2", "값", L, M, M, "", "f(a)=∫₀³|x−a|dx (0≤a≤3) 최소인 a", "a=3/2")
R(9, DI, "INTEG.DEF.QUADRATIC_COEFF_FROM_CONDITIONS", "대칭 구간 정적분 조건으로 계수 결정", "우함수·기함수;정적분", "대칭+방정식",
  "중하", "b=1/6, a=3." + E, MC, "⑤", "선택지번호", L, M, M, "", "f=x²+ax+b, ∫₋₁¹f=1, ∫₋₁¹xf=2, ab", "1/2", final="⑤ (1/2)")
R(10, FI, "INTEG.FUNC.EQUATION_DIFFERENTIATE_CONSTANT", "∫₁ˣf=다항식, x=1 대입 후 미분", "적분과 미분;항등식", "단일개념",
  "하", "a=1." + E, MC, "④", "선택지번호", L, M, L, "해설 미분식 표기 오타(최종 정상)", "∫₁ˣf(t)dt=x³−2ax²+a, f(2)", "f=3x²−4x → 4", final="④ (4)")
build("Batch283", ROWS, 11361)
