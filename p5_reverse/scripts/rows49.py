from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h49/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h49/A.hwp','rb').read()).hexdigest()
setup(QID="A02549", SRC="1V1FD_oVO6UFdXTBFH3g8wpDysrEiZbW4", SHA=SQ, TAG="DSM2I202N", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-2-02_소단원평가_기본_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I202N", EXAM="Ⅲ-2-02 정적분의 성질 소단원평가(기본)", MID="정적분",
      ANS_QID="A02532", ANS_SRC="1udvUKaL4L5jHiF1GjieWOd_nx6Tit8js", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
T, D = "정적분의 성질", "정적분으로 정의된 함수"
R(1, T, "INTEG.DEFINITE.LINEARITY_COMBINE_INTEGRANDS", "같은 구간 정적분 차를 피적분함수로 합침", "정적분의 성질;선형성", "단일개념",
  "하", "4kx 적분." + E, MC, "④", "선택지번호", L, L, L, "", "∫₀²(x+k)²dx−∫₀²(x−k)²dx=16일 때 k", "8k=16 → 2", final="④ (2)")
R(2, T, "INTEG.DEFINITE.INTERVAL_ADDITIVITY", "구간 가법성으로 정적분 정리", "정적분의 성질;구간 분할", "단일개념",
  "하", "∫₁³로 정리." + E, S, "2/3", "값", L, L, L, "", "f=x²−2x, ∫₂⁵f−∫₃⁵f+∫₁²f", "∫₁³f=2/3")
R(3, T, "INTEG.DEFINITE.INTERVAL_ADDITIVITY_GIVEN_VALUES", "주어진 정적분 값들의 구간 연결", "정적분의 성질;구간 분할", "단일개념",
  "하", "(2−8)+4." + E, S, "−2", "값", L, M, L, "", "∫_{−1}^{2}f=2, ∫₁³f=4, ∫₁²f=8일 때 ∫_{−1}^{3}f", "−2")
R(4, T, "INTEG.DEFINITE.ABS_PARAM_MIN", "|x−k| 정적분의 최솟값", "정적분;절댓값;이차함수 최솟값", "적분+최대최소",
  "중하", "k²−3k+9/2." + E, MC, "①", "선택지번호", L, M, M, "", "f(k)=∫₀³|x−k|dx (0<k<3) 최솟값", "(k−3/2)²+9/4 → 9/4", final="① (9/4)")
R(5, T, "INTEG.DEFINITE.ABS_POLYNOMIAL_SPLIT", "절댓값 다항식 정적분(구간 분할)", "정적분;절댓값", "단일개념",
  "하", "x=2에서 분할." + E, MC, "②", "선택지번호", L, M, L, "", "∫₁³|3x²−6x|dx", "2+4=6", final="② (6)")
R(6, T, "INTEG.DEFINITE.REVERSE_LIMITS_ABS", "적분 구간 뒤집기와 절댓값 적분", "정적분의 성질;절댓값", "단일개념",
  "중하", "3∫₀²|x²−1|." + E, MC, "③", "선택지번호", L, M, M, "부호", "∫₀²|x²−1|dx−2∫₂⁰|1−x²|dx", "3×2=6", final="③ (6)")
R(7, T, "INTEG.DEFINITE.SUM_OF_ABS_MIN_THEN_INTEGRATE", "절댓값 합 함수의 최솟값과 정적분", "절댓값;최솟값;정적분", "절댓값+적분",
  "중하", "a=f(0)=4, x≥2에서 3x." + E, S, "18", "값", L, M, M, "", "f=|x+2|+|x|+|x−2| 최솟값 a일 때 ∫₂^a f", "a=4, ∫₂⁴3x=18", fig="설명 그림(gso)")
R(8, D, "INTEG.FUNC.SQUARE_EQUATION_DERIVATIVE", "∫₁ˣf=f² 미분으로 f' 구하기", "정적분으로 정의된 함수;미분", "적분+미분",
  "중하", "f=2ff'." + E, S, "f'(x)=1/2", "식", L, M, M, "f≠0 가정", "∫₁ˣf(t)dt={f(x)}²일 때 f'(x)", "f=2ff' → 1/2 (f=(x−1)/2 확인). 자명해 f≡0(f'=0) 배제가 원문에 미명시",
  ready="REVIEW", status="원문 조건 불충분(자명해 f≡0 배제 미명시) — 해설 의도 답 1/2 일치", trust="중간(원문 모호)", review="REVIEW-원문모호",
  memo_extra="f≡0도 조건 만족 → 원문에 f≠0 또는 비상수 조건 필요.")
R(9, D, "INTEG.FUNC.FIND_F_AND_LOWER_LIMIT", "정적분 항등식에서 f와 아래끝 결정", "정적분으로 정의된 함수;미분", "적분+미분",
  "하", "미분 + x=a 대입." + E, S, "f(x)=2x−3, a=4", "식", L, M, L, "a>0", "∫ₐˣf(t)dt=x²−3x−4 (a>0)일 때 f, a", "f=2x−3, (a+1)(a−4)=0 → 4")
R(10, D, "INTEG.FUNC.FIND_F_AND_COEFF", "정적분 항등식에서 f와 계수 결정", "정적분으로 정의된 함수;미분", "적분+미분",
  "하", "미분 + x=1 대입." + E, S, "f(x)=2x−2, a=−2", "식", L, L, L, "", "∫₁ˣf(t)dt=x²+ax+1일 때 f, a", "a=−2, f=2x−2")
build("Batch264", ROWS, 11192)
