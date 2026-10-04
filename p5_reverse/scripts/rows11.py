from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h11/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h11/A.hwp','rb').read()).hexdigest()
setup(QID="A02611", SRC="1jo8GM-3ASbBZfSxGl0uyOQUVwHIFVAK1", SHA=SQ, TAG="DSM2D2041A", N=5,
      FNAME="15개정_고등_수학Ⅱ_2-2-04-1_소단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D2041A", EXAM="Ⅱ-2-04-1 함수의 그래프의 개형 소단원평가(발전)", MID="도함수의 활용",
      ANS_QID="A02610", ANS_SRC="1tWUcYH0HAEo2AxFSiJP4Sqt6GBpi8KSj", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
GS, MX = "함수의 그래프의 개형", "함수의 최대와 최소"
G = dict(ready="REVIEW", status="논리검산(그림 시각확인 불가)", trust="중간(그림 미확인)", review="REVIEW-그래프시각확인")
R(1, GS, "DERIV.SKETCH.FROM_DERIV_GRAPH_WITH_VALUE_ORDER", "도함수 그래프 + 함숫값 대소로 개형 그리기", "그래프의 개형;도함수 그래프;극값", "개형+그래프",
  "중", "f' 근 −1,1,2 부호 + f(−1)<0<f(2)<f(1)." + E, "서술형(작도)", "풀이 참조(개형: x=−1 극소(음), x=1 극대, x=2 극소(양))", "작도", L, H, M, "",
  "f' 그래프와 f(−1)<0<f(2)<f(1)에서 f 개형", "그래프(gso) 시각확인 불가 — 해설 증감표(−1 극소, 1 극대, 2 극소)로 논리검산",
  fig="도함수 그래프(gso)", **G)
R(2, MX, "DERIV.MAXMIN.COMPOSITE_SUBSTITUTION_RANGE", "합성함수 최솟값 — 치환과 범위 제한", "최대최소;합성함수;치환", "최대최소+합성",
  "중하", "t=g(x)≥−1." + E, MC, "②", "선택지번호", L, M, M, "치환 범위", "f=x³−3x+4, g=x²−4x+3일 때 (f∘g)(x) 최솟값", "t≥−1에서 f(1)=2 ②", final="② (2)",
  memo_extra="유사중복: A02617 서술형 문항20과 동일 구조(g만 상이)")
R(3, MX, "DERIV.MAXMIN.BOX_FIXED_SURFACE_SQUARE_BASE", "겉넓이 일정 정사각기둥 부피 최대 비", "최대최소;부피;겉넓이", "최대최소+입체",
  "중", "y를 x로 표현 → V'=0." + E, MC, "①", "선택지번호", L, M, M, "", "겉넓이 일정 직육면체(그림: 밑면 x×x, 높이 y) 부피 최대일 때 x:y",
  "그림(gso) 시각확인 불가 — 해설 겉넓이식 2x²+4xy=a 기준 x=y=√(a/6) → 1:1 ①", fig="입체 그림(gso)", final="① (1:1)", **G)
R(4, MX, "DERIV.MAXMIN.OPEN_BOX_FROM_EQUILATERAL_SHEET", "정삼각형 판으로 만든 상자 부피 최대", "최대최소;부피;정삼각형", "최대최소+입체",
  "중", "V=x(8−x)²." + E, S, "8/3", "값", M, M, M, "모퉁이 사각형 치수(그림)", "한 변 16cm 정삼각형 세 모퉁이를 잘라 접은 상자 부피 최대 x",
  "그림(gso) 시각확인 불가 — 해설 모델(밑변 16−2x, 높이 x/√3)로 V'=(3x−8)(x−8)=0 → 8/3", fig="전개도 그림(gso)", **G)
R(5, MX, "DERIV.MAXMIN.PROFIT_CUBIC_EMPLOYEES", "수익 함수(삼차) 값과 최대 인원", "최대최소;실생활;삼차함수", "최대최소+실생활",
  "중하", "P'=−3n(n−400)." + E, S, "⑴ 1375000(천 원)=13억 7500만 원 ⑵ 400명", "값(소문항별)", L, L, L, "단위(천 원)", "P(n)=−n³+600n² (0<n<600): ⑴ P(50) ⑵ 최대 인원",
  "⑴ −125000+1500000=1375000 ⑵ n=400", nsub=2)
build("Batch237", ROWS, 10959)
