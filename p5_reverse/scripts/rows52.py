from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h52/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h52/A.hwp','rb').read()).hexdigest()
setup(QID="A02552", SRC="18othbOW5JDnXD53O4kAFt-TUcxOqK1Vw", SHA=SQ, TAG="DSM2D0BU", N=10,
      FNAME="15개정_고등_수학Ⅱ_2_대단원평가_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D0BU", EXAM="Ⅱ 다항함수의 미분 대단원평가", MID="미분 종합(대단원)",
      ANS_QID="A02551", ANS_SRC="1EN1RTipMkNtRWpuJMziWXk8q1hETEhmx", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
R(1, "평균변화율", "DERIV.AVGRATE.COMPOSITE_FROM_GRAPH", "그래프 판독 합성함수의 평균변화율", "평균변화율;합성함수;그래프", "평균변화율+합성",
  "중하", "그래프에서 f값 판독." + E, MC, "⑤", "선택지번호", L, M, M, "합성 순서", "y=f(x) 그래프, g=f∘f의 [0,2] 평균변화율", "해설: f(0)=1,f(1)=0,f(2)=−1,f(−1)=0 → g(2)=g(0)=0 → 0 (그림 의존)", final="⑤ (0)", **G)
R(2, "도함수", "DERIV.DERIVFN.FUNCTIONAL_EQ_ADDITIVE_CORRECTION", "f(x+y)=f(x)+f(y)−5xy 형 함수의 도함수", "도함수의 정의;함수방정식", "정의+함수방정식",
  "중", "f(0)=0, f'=f'(0)−5x." + E, MC, "④", "선택지번호", L, M, H, "f(0)=0 도출", "f(x+y)=f(x)+f(y)−5xy, f'(0)=−1일 때 f'(x)", "−5x−1", final="④ (−5x−1)")
R(3, "도함수", "DERIV.RULES.REMAINDER_BY_SQUARE_FROM_LIMIT", "극한 조건으로 (x−1)² 나눈 나머지", "미분계수;나머지정리;극한 존재 조건", "극한+나머지정리",
  "중하", "f(1)=2, f'(1)=3." + E, MC, "④", "선택지번호", L, M, M, "", "lim (f(x)−2)/(x−1)=3일 때 f를 (x−1)²으로 나눈 나머지", "a=3, b=−1 → 3x−1", final="④ (3x−1)")
R(4, "도함수", "DERIV.RULES.PRODUCT_RULE_PROOF_FILL_BLANK", "정의로 xf(x) 도함수 유도 빈칸", "도함수의 정의;곱의 미분법", "증명+빈칸",
  "하", "hf(x) 보정항." + E, MC, "④", "선택지번호", L, M, L, "", "y=xf(x) 도함수 유도 과정 ㈎, ㈏", "㈎ hf(x), ㈏ xf'(x)+f(x)", final="④")
R(5, "접선의 방정식", "DERIV.TANGENT.ODD_CUBIC_FROM_TANGENT", "기함수 삼차함수의 접선 조건으로 결정", "기함수;접선의 기울기;미정계수", "대칭+접선",
  "중하", "f=ax³+bx." + E, MC, "①", "선택지번호", L, M, M, "", "f(−x)=−f(x) 삼차, (2,2) 접선 기울기 −7일 때 x=1 접선 기울기", "a=−1, b=5 → f'(1)=2", final="① (2)")
R(6, "방정식에의 활용", "DERIV.EQROOTS.ABS_ODD_CUBIC_ROOT_COUNT", "|f(x)|=k 실근 개수로 기함수 삼차 결정", "극값;실근의 개수;기함수;절댓값", "극값+방정식",
  "중", "극댓값=2." + E, MC, "③", "선택지번호", M, H, M, "a≤0이면 근 2개", "최고차 1 기함수 삼차 f, |f(x)|=2 실근 4개일 때 f(√2)", "f=x³−ax, 극댓값 (2a/3)√(a/3)=2 → a=3 → −√2", final="③ (−√2)", fig="설명 그림(gso)")
R(7, "미분계수", "DERIV.DERIVCOEF.SEQUENCE_LIMIT_FROM_TANGENT_LINE", "접선 방정식에서 미분계수 후 수열 극한", "미분계수;접선의 방정식;수열의 극한", "극한+접선",
  "하", "f'(2)=3." + E, S, "3", "값", L, L, L, "", "(2,1) 접선 y=3x−5일 때 lim n{f(2+1/n)−f(2)}", "f'(2)=3")
R(8, "도함수", "DERIV.RULES.TRIPLE_PRODUCT_FIND_PARAM", "세 함수 곱의 미분계수로 상수 결정", "곱의 미분법", "곱의미분+방정식",
  "중하", "11a−26=62." + E, S, "8", "값", L, M, L, "", "f=(2x²−1)(3x−1)(−2x+a), f'(1)=62일 때 a", "8(a−2)+3(a−2)−4=62 → 8")
R(9, "함수의 증가와 감소", "DERIV.MONO.ONE_TO_ONE_CUBIC_DISCRIMINANT", "일대일함수 조건(감소)과 판별식", "증가와 감소;일대일함수;판별식", "증감+판별식",
  "중", "f'≤0, D/4≤0." + E, S, "−6", "값", L, M, M, "최고차 음수 → 감소", "f=−x³−3(a+1)x²+4ax+5가 일대일일 때 모든 정수 a의 합", "(a+3)(3a+1)≤0 → −3,−2,−1 → −6")
R(10, "함수의 최대와 최소", "DERIV.MAXMIN.COMPOSITE_RANGE_RESTRICTED", "합성함수 최댓값(치환 범위 제한)", "최대최소;합성함수;치환", "합성+최대최소",
  "중", "t=g(x)≥−3." + E, S, "6", "값", L, M, M, "치역 제한", "f=−x³−3x²+9x+1, g=x²−4x+1일 때 f∘g 최댓값", "t≥−3에서 t=1 극대·최대 → 6")
build("Batch262", ROWS, 11172)
