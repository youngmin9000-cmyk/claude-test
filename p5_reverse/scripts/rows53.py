from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h53/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h53/A.hwp','rb').read()).hexdigest()
setup(QID="A02553", SRC="1Aokl0-AFFyxKIE4VFRH7FySOW4bTty5l", SHA=SQ, TAG="DSM2D1MB", N=20,
      FNAME="15개정_고등_수학Ⅱ_2-1_중단원평가_기본_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D1MB", EXAM="Ⅱ-1 미분계수와 도함수 중단원평가(기본) — 1. 미분계수 / 2. 도함수 2부 구성", MID="미분계수와 도함수",
      ANS_QID="A02585", ANS_SRC="1hl16QPlwUkmuWN-W6NSzpPVBpHzTDydI", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
AV, DC, DF, DR = "평균변화율", "미분계수", "미분가능성과 연속성", "도함수"
R(1, AV, "DERIV.AVGRATE.BASIC_INTERVAL", "주어진 구간의 평균변화율 계산", "평균변화율", "단일개념",
  "하", "2문항 대입." + E, S, "⑴ 2 ⑵ 3", "값", L, L, L, "", "1→3 평균변화율: ⑴ 2x+1 ⑵ x²−x", "⑴ 4/2 ⑵ 6/2", nsub=2)
R(2, DC, "DERIV.DERIVCOEF.DEFINITION_DIRECT", "정의에 따른 미분계수 계산", "미분계수의 정의", "단일개념",
  "하", "2문항 정의 적용." + E, S, "⑴ 1 ⑵ 4", "값", L, L, L, "", "x=1 미분계수: ⑴ x+2 ⑵ x²+2x", "⑴ 1 ⑵ Δx+4→4", nsub=2)
R(3, DC, "DERIV.DERIVCOEF.TANGENT_SLOPE_AT_POINT", "곡선 위 점에서의 접선 기울기(미분계수)", "미분계수;접선의 기울기", "단일개념",
  "하", "4문항 정의 적용." + E, S, "⑴ 3 ⑵ 2 ⑶ −4 ⑷ 1", "값", L, L, L, "", "⑴ 3x+1,(0,1) ⑵ 2x−3,(1,−1) ⑶ 2x²+1,(−1,3) ⑷ x²−3x,(2,−2) 접선 기울기", "f'(a) 계산", nsub=4)
R(4, AV, "DERIV.AVGRATE.GIVEN_VALUE_FIND_INTERVAL", "평균변화율 값으로 구간 끝 결정", "평균변화율", "단일개념",
  "하", "h+4=10." + E, S, "6", "값", L, L, L, "h>0", "f=x², 2→2+h 평균변화율 10일 때 h", "6", memo_extra="원문 근사중복 후보: A02595 Q1.")
R(5, DC, "DERIV.DERIVCOEF.INSTANT_RATE_APPLIED", "실생활 순간변화율(전하량)", "미분계수;순간변화율;실생활 활용", "실생활+미분계수",
  "하", "Q'(3)." + E, S, "6 C/s", "값", L, L, L, "", "Q(t)=t³/3−t²+3t+3 (C), t=3 순간변화율 (원문 '전화량'은 '전하량' 오기)", "Q'=t²−2t+3 → 6")
R(6, DF, "DERIV.DIFFABLE.REMOVABLE_POINT_VALUE", "한 점 값만 다른 함수의 미분가능 조건", "미분가능성;연속성", "단일개념",
  "하", "미분가능 → 연속." + E, S, "5", "값", L, L, L, "", "f=x²+1(x≠2), a(x=2) x=2 미분가능일 때 a", "5")
R(7, DF, "DERIV.DIFFABLE.PIECEWISE_QUADRATIC_LINEAR", "구간별 함수 미분가능 조건(이차·일차)", "미분가능성;연속성", "연속+미분계수",
  "하", "a+b=1, a=2." + E, MC, "⑤", "선택지번호", L, M, L, "", "f=x²(x≥1), ax+b(x<1) x=1 미분가능일 때 a−b", "a=2, b=−1 → 3", final="⑤ (3)")
R(8, DF, "DERIV.DIFFABLE.PIECEWISE_LINEAR_QUADRATIC", "구간별 함수가 미분가능할 조건(계수 결정)", "미분가능성;연속성;좌우 미분계수", "연속+미분계수",
  "중하", "연속+좌우미분계수." + E, S, "−4", "값", L, M, M, "", "f=ax+b(x≥2), x²−4x(x<2) 미분가능, f(3)", "a=0, b=−4 → −4")
R(9, DF, "DERIV.DIFFABLE.ABS_CONTINUITY_DIFFERENTIABILITY", "절댓값 함수의 x=0 연속성·미분가능성 조사", "연속성;미분가능성;절댓값", "연속+미분가능성",
  "중하", "좌우 미분계수 비교." + E, S, "⑴ 연속, 미분가능 ⑵ 연속, 미분가능하지 않음", "서술", L, M, M, "", "⑴ 2x|x| ⑵ x²−3|x|+2의 x=0 연속성·미분가능성", "⑴ 0=0 ⑵ −3 vs 3", nsub=2)
R(10, DF, "DERIV.DIFFABLE.CONT_NOT_DIFF_SELECT_BASIC", "연속이나 미분불가능한 함수 보기 선택", "연속성;미분가능성;절댓값;분수함수", "보기판별",
  "하", "불연속 배제 후 첨점." + E, S, "ㄷ", "보기", L, M, L, "1/|x| 불연속", "x=0 연속·미분불가능: ㄱ 1/x ㄴ 1/|x| ㄷ −|x| ㄹ x²−1", "ㄱ,ㄴ 불연속, ㄷ 첨점, ㄹ 미분가능 → ㄷ")
R(11, DR, "DERIV.RULES.POWER_RULE_BASIC", "상수·거듭제곱 함수 미분", "도함수;거듭제곱 미분", "단일개념",
  "하", "4문항 공식." + E, S, "⑴ 0 ⑵ 2 ⑶ −7x⁶ ⑷ 2nx^{2n−1}", "식", L, L, L, "", "미분: ⑴ 3 ⑵ 2x ⑶ −x⁷ ⑷ x^{2n}", "공식 적용 (해설 ⑷ 풀이 x^{n−1}은 x^{2n−1} 오기, 답란 정확)", nsub=4)
R(12, DR, "DERIV.RULES.POLYNOMIAL_TERMWISE", "다항함수 항별 미분", "도함수;미분법(합·실수배)", "단일개념",
  "하", "3문항." + E, S, "⑴ 5 ⑵ −2x+3 ⑶ x²+x−6", "식", L, L, L, "", "미분: ⑴ 5x−2 ⑵ −x²+3x+2 ⑶ x³/3+x²/2−6x−3", "항별 미분", nsub=3)
R(13, DR, "DERIV.RULES.PRODUCT_RULE_POLY", "곱의 미분법(다항식 곱)", "곱의 미분법", "단일개념",
  "하", "3문항." + E, S, "⑴ 4x+1 ⑵ 6x−4 ⑶ 9x²+22x+7", "식", L, M, L, "", "미분: ⑴ x(2x+1) ⑵ (x−2)(3x+2) ⑶ (x²+2x−1)(3x+5)", "곱의 미분법", nsub=3)
R(14, DR, "DERIV.RULES.LINEARITY_AT_POINT", "미분계수의 선형성(합·실수배)", "미분법;미분계수", "단일개념",
  "하", "2문항." + E, S, "⑴ −1 ⑵ 10", "값", L, L, L, "", "f'(0)=3, g'(0)=4일 때 ⑴ f−g ⑵ 2f+g의 x=0 미분계수", "3−4, 6+4", nsub=2, memo_extra="원문 근사중복 후보: A02595 Q18.")
R(15, DR, "DERIV.RULES.POWER_SUM_ODD", "홀수 거듭제곱 합의 미분계수", "도함수;거듭제곱 미분;등차수열의 합", "미분+수열",
  "하", "1+3+…+19." + E, S, "100", "값", L, L, L, "", "f=Σ_{k=1}^{10} x^{2k−1}일 때 f'(1)", "100", memo_extra="원문 근사중복 후보: A02595 Q19.")
R(16, DR, "DERIV.DERIVFN.QUADRATIC_FROM_VALUE_AND_DERIV", "함숫값·미분계수로 이차함수 계수", "도함수;미정계수", "단일개념",
  "하", "연립." + E, S, "4", "값", L, L, L, "", "f=ax²+bx, f(1)=5, f'(−1)=2일 때 ab", "a=1, b=4 → 4")
R(17, DC, "DERIV.DERIVCOEF.LIMIT_AS_DERIVATIVE_POLY", "다항식 극한을 미분계수로 해석", "미분계수의 정의;도함수", "극한+미분",
  "하", "f(2)=4 인식." + E, S, "22", "값", L, M, L, "", "lim (x⁴−2x²−2x−4)/(x−2), x→2", "f'(2)=22", memo_extra="원문 근사중복 후보: A02595 Q20.")
R(18, DC, "DERIV.DERIVCOEF.LIMIT_AS_DERIV_FIND_EXPONENT", "극한을 미분계수로 보고 지수 결정", "미분계수의 정의;거듭제곱 미분", "극한+미분",
  "하", "6n=12." + E, S, "2", "값", L, M, L, "", "lim (x^{3n}+x^{2n}+xⁿ−3)/(x−1)=12인 자연수 n", "f'(1)=6n → 2")
R(19, DR, "DERIV.RULES.TRIPLE_PRODUCT_FIND_PARAM", "세 함수 곱의 미분계수로 상수 결정", "곱의 미분법", "곱의미분+방정식",
  "중하", "17a−46=56." + E, S, "6", "값", L, M, L, "", "f=(2x²+1)(3x−1)(−2x+a), f'(1)=56일 때 a", "8(a−2)+9(a−2)−12=56 → 6")
R(20, DR, "DERIV.RULES.PRODUCT_RULE_FROM_LIMITS", "극한 조건에서 함숫값·미분계수 후 곱의 미분", "곱의 미분법;미분계수;접선의 기울기", "극한+곱의미분",
  "중하", "f(3)=2, f'(3)=1, g(3)=−3, g'(3)=7." + E, S, "11", "값", L, M, M, "", "lim (f−2)/(x−3)=1, lim (g+3)/(x−3)=7, h=fg의 x=3 접선 기울기", "−3+14=11", memo_extra="원문 근사중복 후보: A02595 Q22.")
for r in ROWS:
    q = r["_q"]; part, k = ("1. 미분계수", q) if q <= 10 else ("2. 도함수", q - 10)
    lab = f"[{part}] {k}"
    r["원문항번호"] = lab; r["상위원문항번호"] = lab; r["문항이미지/좌표"] = "hwp 본문 " + lab; r["해설페이지"] = "동반 정답 hwp " + lab
build("Batch258", ROWS[:10], 11137)
build("Batch259", ROWS[10:], 11147)
