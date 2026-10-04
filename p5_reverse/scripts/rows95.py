from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h95/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h95/A.hwp','rb').read()).hexdigest()
setup(QID="A02495", SRC="15rBvpoWO6DNa-ETluH5Tfx2j8dZVMNS4", SHA=SQ, TAG="DSM2I0BU", N=10,
      FNAME="15개정_고등_수학Ⅱ_3_대단원평가_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I0BU", EXAM="Ⅲ 다항함수의 적분 대단원평가", MID="적분 종합(대단원)",
      ANS_QID="A02512", ANS_SRC="1Zrox-9p6vXfwOuQBKEfAUeuMuPjljnpj", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
MC = "5지선다"
S = "서술형(단답)"
R(1, "부정적분", "INTEG.INDEF.INTEGRAND_FROM_ANTIDERIVATIVE_SHIFTED", "∫{f−3}dx 결과 미분으로 f 구하기", "부정적분의 정의;미분", "단일개념",
  "하", "f−3=3x²−2x+2." + E, MC, "④", "선택지번호", L, L, L, "상수 3 보정", "∫{f(x)−3}dx=x³−x²+2x+C일 때 f(1)", "f=3x²−2x+5 → 6", final="④ (6)")
R(2, "부정적분", "INTEG.INDEF.FUNCTIONAL_EQ_DERIVATIVE_DEF", "함수방정식+도함수 정의로 f' 결정", "함수방정식;도함수의 정의", "함수방정식+미분",
  "중하", "f'(x)=f'(0)−3x." + E, MC, "②", "선택지번호", L, M, M, "f(0)=0 유도", "f(x+y)=f(x)+f(y)−3xy, f'(0)=−1일 때 f'(x)", "f'=−3x−1", final="② (f'(x)=−3x−1)")
R(3, "정적분", "INTEG.DEF.LINEARITY_INTERVAL_REVERSAL", "구간 뒤집기와 선형성으로 정적분 합치기", "정적분의 성질;구간 반전", "단일개념",
  "하", "∫₂⁻¹=−∫₋₁²." + E, MC, "③", "선택지번호", L, M, L, "부호(구간 반전)", "2∫₋₁²(2x²+1)dx−∫₂⁻¹(2x−x²)dx", "∫₋₁²(3x²+2x+2)dx=[x³+x²+2x]=18", final="③ (18)")
R(4, "정적분", "INTEG.DEF.INTERVAL_ADDITIVITY", "구간 가법성으로 정적분 값 조합", "정적분의 성질;구간 분할", "단일개념",
  "하", "∫₀⁵=∫₀³−∫₁³+∫₁⁵." + E, S, "6", "값", L, M, L, "", "∫₀³f=5, ∫₁⁵f=4, ∫₁³f=3일 때 ∫₀⁵f", "5−3+4=6")
R(5, "정적분", "INTEG.DEF.PIECEWISE_SHIFTED_TIMES_X", "평행이동한 구간별 함수와 x의 곱의 정적분", "정적분;구간별 함수;평행이동", "구간분할+치환식 정리",
  "중", "f(x−1) 경계 x=3." + E, S, "29/2", "값", M, M, M, "경계 이동(2→3)", "f=4−x²(x≤2), 4−x(x>2), ∫₁⁴x f(x−1)dx", "∫₁³(−x³+2x²+3x)=28/3, ∫₃⁴(5x−x²)=31/6 → 29/2")
R(6, "정적분의 활용", "INTEG.AREA.LINE_BISECTS_PARABOLA_REGION", "직선이 포물선-x축 넓이를 이등분", "넓이;정적분;이등분", "넓이+방정식",
  "중", "(6−m)³/6=18." + E, MC, "④", "선택지번호", M, M, M, "", "y=−x²+6x와 x축 넓이를 y=mx가 이등분, (6−m)³", "전체 36, 부분 (6−m)³/6 → 108", final="④ (108)")
R(7, "정적분의 활용", "INTEG.MOTION.PIECEWISE_VELOCITY_DISTANCE", "구간별 속도함수로 이동 거리(실생활)", "속도와 거리;정적분;구간별 함수", "적분+실생활",
  "하", "6+36+9." + E, MC, "④", "선택지번호", L, M, L, "정지 시각 t=11", "엘리베이터 v=3t(0~2), 6(2~8), −2t+22(8~11) 이동 거리", "6+36+9=51m", final="④ (51 m)")
R(8, "부정적분", "INTEG.INDEF.MISTAKEN_DERIVATIVE_RECOVER", "잘못 미분한 결과로 f 복원 후 부정적분", "부정적분;적분상수;미분", "적분 2회",
  "중하", "f=x³−x²+5x+2." + E, S, "(1/4)x⁴−(1/3)x³+(5/2)x²+2x+C", "식", L, M, M, "적분상수 2종 구분", "f'=3x²−2x+5, f(0)=2일 때 ∫f dx", "f 복원 후 재적분")
R(9, "정적분", "INTEG.FUNC.LOWER_LIMIT_CONSTANT_THEN_DIFFERENTIATE", "정적분 함수에서 상수 결정(x=하한 대입) 후 미분", "정적분으로 정의된 함수;미분", "단일개념",
  "중하", "x=2 대입 → a=−2." + E, MC, "②", "선택지번호", L, M, M, "하한 대입", "∫₂ˣf(t)dt=x³−x²+ax, f(1)", "f=3x²−2x−2 → −1", final="② (−1)")
R(10, "정적분의 활용", "INTEG.AREA.POWER_CURVES_TELESCOPING_LIMIT", "xⁿ과 xⁿ⁺² 사이 넓이의 급수 극한(망원합)", "넓이;대칭;부분분수;급수의 극한", "넓이+급수",
  "중상", "S_n=2(1/(n+1)−1/(n+3))." + E, S, "5/3", "값", M, M, H, "대칭(홀짝 n) 처리", "y=xⁿ, y=xⁿ⁺²로 둘러싸인 넓이 S_n, lim ΣS_k", "망원합 2(1/2+1/3)=5/3")
build("Batch294", ROWS, 11456)
