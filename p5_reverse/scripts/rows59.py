from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h59/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h59/A.hwp','rb').read()).hexdigest()
setup(QID="A02559", SRC="1uuoYkWQIo3XhgznvC3osrQCecUmTczaK", SHA=SQ, TAG="DSM2D102N", N=10,
      FNAME="15개정_고등_수학Ⅱ_2-1-02_소단원평가_기본_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D102N", EXAM="Ⅱ-1-02 미분가능성과 연속성 소단원평가(기본)", MID="미분계수와 도함수",
      ANS_QID="A02558", ANS_SRC="1UJZErvittdnU2EEVkqoGT-rNGipGZVOC", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
T = "미분가능성과 연속성"
R(1, T, "DERIV.DIFFABLE.SELECT_DIFFERENTIABLE_AT_POINT", "주어진 점에서 미분가능한 함수 보기 선택", "미분가능성;절댓값;분수함수", "보기판별",
  "하", "좌우 미분계수." + E, MC, "④", "선택지번호", L, M, L, "|x²−x| 첨점", "x=1 미분가능: ㄱ x² ㄴ |x²−x| ㄷ 1/x", "ㄱ 2, ㄴ ±1, ㄷ −1 → ㄱ,ㄷ", final="④ (ㄱ, ㄷ)")
R(2, T, "DERIV.DIFFABLE.CONT_NOT_DIFF_CHOICE", "x=0 연속이나 미분불가능한 함수 선택", "연속성;미분가능성;절댓값", "보기판별",
  "하", "√(x²)=|x|." + E, MC, "③", "선택지번호", L, M, L, "|x|/x 불연속", "① 5 ② x|x| ③ √(x²) ④ |x|/x ⑤ |x|² 중 연속·미분불가능", "③", final="③ (√(x²))")
R(3, T, "DERIV.DIFFABLE.GRAPH_COUNT_NONDIFF", "그래프에서 미분불가능 점 개수", "미분가능성;그래프", "그래프+미분가능성",
  "하", "그래프 판독." + E, S, "2", "값", L, M, L, "", "그래프의 미분가능하지 않은 점 개수", "해설: x=0 첨점, x=1 불연속 → 2 (그림 의존)", **G)
R(4, T, "DERIV.DIFFABLE.GRAPH_PROPERTY_CHOICE", "그래프에서 미분계수·극한·불연속·미분불가능 판단", "미분계수;극한;연속성;미분가능성;그래프", "그래프+보기판별",
  "중하", "그래프 판독." + E, MC, "⑤", "선택지번호", L, M, M, "", "(0,5)에서 ①f'(3)>0 ②lim_{x→2} 미존재 ③f'=0 점 존재 ④불연속 3개 ⑤미분불가능 3개 중 옳은 것", "해설: 미분불가능 x=1,2,4 → ⑤ (그림 의존)", final="⑤", **G)
R(5, T, "DERIV.DIFFABLE.PIECEWISE_QUADRATIC_LINEAR", "구간별 함수 미분가능 조건(이차·일차)", "미분가능성;연속성", "연속+미분계수",
  "하", "a+b=2, a=4." + E, S, "a=4, b=−2", "값", L, M, L, "", "f=2x²(x≤1), ax+b(x>1) x=1 미분가능", "a=4, b=−2")
R(6, T, "DERIV.DIFFABLE.ABS_LINEAR_PRODUCT_AT_ROOT", "|x−2|(x+a)의 x=2 미분가능 조건", "미분가능성;절댓값;좌우 미분계수", "절댓값+미분가능성",
  "중하", "2+a=−(2+a)." + E, MC, "②", "선택지번호", L, M, M, "", "f=|x−2|(x+a)가 x=2 미분가능일 때 a+f'(2)", "a=−2, f'(2)=0 → −2", final="② (−2)")
R(7, T, "DERIV.DIFFABLE.GRAPH_COUNT_DISCONT_NONDIFF", "그래프에서 불연속·미분불가능 점 개수", "연속성;미분가능성;그래프", "그래프+미분가능성",
  "중하", "그래프 판독." + E, S, "5", "값", L, M, M, "", "(0,d)에서 불연속 m개, 미분불가능 n개일 때 m+n", "해설: m=2(b,c), n=3(a,b,c) → 5 (그림 의존)", **G)
R(8, T, "DERIV.DIFFABLE.GRAPH_SELECT_DIFFERENTIABLE", "그래프 보기에서 x=a 미분가능 선택", "미분가능성;연속성;그래프", "그래프+보기판별",
  "하", "그래프 4종 판독." + E, S, "ㄹ", "보기", L, M, L, "", "그래프 ㄱ~ㄹ 중 x=a에서 미분가능한 것", "해설: ㄱ 함숫값 없음, ㄴ 극한 없음, ㄷ 첨점, ㄹ 매끄러움 → ㄹ (그림 의존)", **G)
R(9, T, "DERIV.DIFFABLE.GRAPH_SELECT_PROPERTIES", "그래프에서 미분계수 부호·극한·불연속 보기 판별", "미분계수;극한;연속성;미분가능성;그래프", "그래프+보기판별",
  "중하", "그래프 판독." + E, S, "ㄷ", "보기", L, M, M, "", "0<x<5 그래프: ㄱ f'(4)<0 ㄴ f'(3)=0 ㄷ lim_{x→1} 존재 ㄹ 불연속 3개·미분불가능 2개", "해설: ㄷ만 참 (그림 의존)", **G)
R(10, T, "DERIV.DIFFABLE.PIECEWISE_CONST_QUADRATIC", "상수·이차 구간별 함수 미분가능 조건", "미분가능성;연속성", "연속+미분계수",
  "하", "b=1+a, 2+a=0." + E, MC, "④", "선택지번호", L, M, L, "", "f=x²+ax(x≥1), b(x<1) x=1 미분가능일 때 ab", "a=−2, b=−1 → 2", final="④ (2)")
build("Batch260", ROWS, 11157)
