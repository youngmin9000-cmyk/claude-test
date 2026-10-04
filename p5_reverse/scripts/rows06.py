from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h06/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h06/A.hwp','rb').read()).hexdigest()
setup(QID="A02571", SRC="1XAAWmj35Urm32fM0OR4hoFB0ms8lwN6J", SHA=SQ, TAG="DSM2D203N", N=10,
      FNAME="15개정_고등_수학Ⅱ_2-2-03_소단원평가_기본_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D203N", EXAM="Ⅱ-2-03 함수의 증가와 감소, 극대와 극소 소단원평가(기본)", MID="도함수의 활용",
      ANS_QID="A02606", ANS_SRC="1KIqvu-GPSOQzZMoIgPoaTR-LuDP2JYPI", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
ID, EX = "함수의 증가와 감소", "함수의 극대와 극소"
R(1, ID, "DERIV.MONO.DIFFERENCE_FUNCTION_SIGN", "f'>g' 와 f(0)=g(0)으로 대소 판정", "함수의 증가와 감소;차함수", "단조성+대소",
  "하", "h=f−g 증가." + E, MC, "②", "선택지번호", L, M, L, "", "f(0)=g(0), f'>g'일 때 옳은 것", "h(1)>h(0)=0 → f(1)>g(1) ②", final="②")
R(2, ID, "DERIV.MONO.CUBIC_BIJECTION_GENERAL_CONDITION", "삼차함수 일대일대응 일반 조건", "일대일대응;판별식;증가함수", "단조성+판별식",
  "하", "f'=3ax²+2bx+c, D/4≤0." + E, MC, "④", "선택지번호", L, M, L, "", "a>0인 삼차함수 일대일대응 조건", "b²−3ac≤0 ④", final="④ (b²−3ac≤0)")
R(3, EX, "DERIV.EXTREMA.DERIV_FROM_EXTREMA_ROOT_SUM", "극값 위치로 도함수 결정 → f'(x)=x 근의 합", "극대;극소;근과 계수의 관계", "극값+비에타",
  "중하", "f'=(x−2)(x−4)/8." + E, MC, "③", "선택지번호", L, M, L, "", "삼차 f: x=2 극대, x=4 극소, f'(0)=1일 때 f'(x)=x 두 근의 합", "x²−14x+8=0 → 14 ③", final="③ (14)")
R(4, ID, "DERIV.MONO.CUBIC_INCREASING_DISCRIMINANT", "삼차함수가 실수 전체에서 증가할 조건", "함수의 증가와 감소;판별식", "단조성+판별식",
  "하", "D/4≤0." + E, MC, "③", "선택지번호", L, M, L, "", "f=x³−ax²+(a+6)x+5가 증가하는 정수 a 최댓값", "(a+3)(a−6)≤0 → 6 ③", final="③ (6)")
R(5, ID, "DERIV.MONO.CUBIC_DECREASING_DISCRIMINANT", "삼차함수가 실수 전체에서 감소할 조건", "함수의 증가와 감소;판별식", "단조성+판별식",
  "하", "D/4≤0." + E, S, "−6≤a≤6", "범위", L, M, L, "등호 포함", "f=−x³+ax²−12x−1이 감소함수인 a", "a²−36≤0")
R(6, ID, "DERIV.MONO.CUBIC_INJECTIVE_DISCRIMINANT", "일대일함수 조건 → 판별식", "일대일함수;판별식;증가함수", "단조성+판별식",
  "하", "f'=3x²+4kx+4≥0." + E, MC, "③", "선택지번호", L, M, L, "", "f=x³+2kx²+4x가 일대일인 k", "4k²−12≤0 → −√3≤k≤√3 ③", final="③")
R(7, ID, "DERIV.MONO.INCREASING_INTERVAL_ONLY", "증가 구간이 (α,β)뿐일 때 α²+β²", "함수의 증가와 감소;이차부등식", "단일개념",
  "하", "f'=−x²+3>0." + E, MC, "②", "선택지번호", L, L, L, "", "f=−x³/3+3x가 α<x<β에서만 증가: α²+β²", "−√3<x<√3 → 6 ②", final="② (6)")
R(8, ID, "DERIV.MONO.DECREASING_INTERVAL_TO_COEFFS", "감소 구간 [−1,3]으로 계수 결정", "함수의 증가와 감소;이차부등식;계수 비교", "단조성+계수비교",
  "중하", "f'=3(x+1)(x−3)." + E, S, "−6", "값", L, M, L, "", "f=x³−ax²+bx가 감소하는 구간이 [−1,3]일 때 a+b", "a=3, b=−9 → −6")
R(9, ID, "DERIV.MONO.DECREASING_ON_INTERVAL_ENDPOINTS", "구간에서 감소할 조건(아래로 볼록 도함수 끝점)", "함수의 증가와 감소;이차함수;끝점 조건", "단조성+이차함수",
  "중하", "f'(−2)≤0, f'(1)≤0." + E, MC, "④", "선택지번호", L, M, M, "", "f=x³+kx²−8x+4가 −2<x<1에서 감소하는 k 최대+최소", "1≤k≤5/2 → 7/2 ④", final="④ (7/2)", fig="설명 그림(gso)")
R(10, EX, "DERIV.EXTREMA.MAX_VALUE_TO_MIN", "극댓값 조건으로 계수 결정 후 극솟값", "극대;극소;연립방정식", "극값+연립",
  "하", "f'(2)=0, f(2)=23." + E, MC, "⑤", "선택지번호", L, L, L, "", "f=x³+ax²+bx+3이 x=2 극댓값 23: 극솟값", "a=−9, b=24 → f(4)=19 ⑤", final="⑤ (19)")
build("Batch241", ROWS, 10989)
