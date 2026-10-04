from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h31/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h31/A.hwp','rb').read()).hexdigest()
setup(QID="A02531", SRC="1u1QdQJt4t2srIfBd4vv6KTWtDJuQuftB", SHA=SQ, TAG="DSM2I201A", N=5,
      FNAME="15개정_고등_수학Ⅱ_3-2-01_소단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I201A", EXAM="Ⅲ-2-01 정적분 소단원평가(발전)", MID="정적분",
      ANS_QID="A02530", ANS_SRC="1d_MZTJCP7a0VwcZfzJxfz9iaz4L6iQWT", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"; MC = "5지선다"
DI = "정적분"; FI = "정적분으로 정의된 함수"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
R(1, DI, "INTEG.DEF.PIECEWISE_SHIFTED", "평행이동한 구간별 함수 곱의 정적분", "구간별 함수;평행이동;정적분", "단일개념",
  "중", "x=2 분할." + E, S, "139/12", "값", M, M, M, "x−1≤1 ⇔ x≤2", "f=4−x²(x≤1), 4−x(x>1), ∫₁³xf(x−1)dx", "65/12+37/6=139/12")
R(2, DI, "INTEG.DEF.DIFF_POLY_FROM_ROOTS", "두 삼차함수 차를 인수로 결정 후 정적분", "인수정리;정적분", "다항식+적분",
  "중", "F=4x³−4x." + E, MC, "④", "선택지번호", L, M, M, "", "f(0)=g(0), f(±1)=g(±1), f(2)=g(2)+24, ∫₋₁²(f−g)", "F(2)=6a=24 → [x⁴−2x²]₋₁²=9", final="④ (9)")
R(3, DI, "INTEG.DEF.SEQUENCE_TELESCOPING", "정적분으로 정의된 수열의 부분분수 합", "정적분;부분분수;Σ", "적분+수열",
  "중하", "f(n)=n(n+1)." + E, S, "61", "값", L, M, M, "", "f(n)=∫₀ⁿ(2x+1)dx, Σ₁³⁰1/f(n)=q/p, p+q", "30/31 → 61")
R(4, FI, "INTEG.FUNC.ROOT_COUNT_CUBIC", "적분 정의 삼차함수가 x축과 세 점에서 만날 조건", "적분과 미분;판별식;삼차방정식", "적분+방정식",
  "중", "a≠2, a<4." + E, MC, "①", "선택지번호", L, M, M, "근 0 중복 제외", "f(x)=∫₀ˣ(3t²−8t−4+2a)dt, x축과 서로 다른 세 점, 자연수 a의 합", "a=1,3 → 4", final="① (4)")
R(5, FI, "INTEG.FUNC.PROPERTIES_FROM_GRAPH_TFQ", "그래프로 주어진 f의 적분함수 성질 판정(ㄱㄴㄷ)", "적분과 미분;극값;실근", "그래프+판정",
  "중", "a<0(그림)." + E, MC, "①", "선택지번호", L, H, M, "a 부호 그림 의존", "f=ax(x−3) 그래프, g=∫₀ˣf, ㄱ g'(3)=0 ㄴ x=0 극대 ㄷ g=0 세 실근",
  "해설 기준 a<0: ㄱ참, ㄴ거짓(극소), ㄷ거짓(g=a x²(2x−9)/6 → 2개) → ① (a>0이면 ③; 그림 의존)", final="① (ㄱ)", **G)
build("Batch279", ROWS, 11326)
