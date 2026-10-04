from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h90/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h90/A.hwp','rb').read()).hexdigest()
setup(QID="A02590", SRC="1xOLuWedM6QwFOKy2xgvAb3m1YymuIvs5", SHA=SQ, TAG="DSM2D102A", N=4,
      FNAME="15개정_고등_수학Ⅱ_2-1-02_소단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D102A", EXAM="Ⅱ-1-02 미분가능성과 연속성 소단원평가(발전)", MID="미분계수와 도함수",
      ANS_QID="A02561", ANS_SRC="1a6MFaRdKsS8XGnfXk8x9_xPxUFiZb7f3", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
F = dict(fig="설명 그림(gso)")
T = "미분가능성과 연속성"
R(1, T, "DERIV.DIFFABLE.GRAPH_COUNT_DISCONT_NONDIFF", "그래프에서 불연속·미분불가능 점 개수", "연속성;미분가능성;그래프", "그래프+미분가능성",
  "중하", "그래프 판독." + E, MC, "②", "선택지번호", L, M, M, "첨점·불연속점 중복 계산", "(−1,5)에서 불연속 m개, 미분불가능 n개일 때 m+n", "해설: 불연속 x=1,2, 미분불가능 x=1,2,3 → 5 (그림 의존)", final="② (5)", **G)
R(2, T, "DERIV.DIFFABLE.ABS_FLOOR_CONT_NOT_DIFF_SELECT", "절댓값·가우스 함수의 연속이나 미분불가능 판별", "연속성;미분가능성;절댓값;가우스 기호", "보기판별",
  "중", "좌우 미분계수." + E, MC, "③", "선택지번호", L, M, M, "x|x|는 미분가능", "x=0에서 연속이지만 미분불가능: ㄱ |x| ㄴ x|x| ㄷ x[x]", "ㄱ ±1, ㄴ 0=0, ㄷ −1 vs 0 → ㄱ,ㄷ", final="③ (ㄱ, ㄷ)")
R(3, T, "DERIV.DIFFABLE.PIECEWISE_THREE_PART_SELECT", "세 구간 함수의 연속·미분가능 보기 판별", "연속성;미분가능성;좌우 미분계수", "보기판별",
  "중하", "x=0, 1 좌우 비교." + E, MC, "③", "선택지번호", L, M, M, "x=1 좌 2 우 1", "f=−x²(x<0), x²(0≤x<1), x(x≥1): ㄱ x=0 연속 ㄴ x=0 미분가능 ㄷ x=1 미분가능", "ㄱ 참, ㄴ 0=0 참, ㄷ 2≠1 거짓", final="③ (ㄱ, ㄴ)")
R(4, T, "DERIV.DIFFABLE.QUADRATIC_BRIDGE_TWO_LINES", "두 직선 사이를 이차함수로 매끄럽게 연결", "미분가능성;연속성;연립방정식", "연속+미분계수",
  "중", "양 끝 연속·접선 4식." + E, S, "14", "값", M, M, M, "", "y=x+3(x≤−3), ax²+bx+c(−3<x<1), y=−x+1(x≥1) 전체 미분가능, 16(a²+b²+c²)", "a=−1/4, b=−1/2, c=3/4 → 1+4+9=14", **F)
build("Batch253", ROWS, 11093)
