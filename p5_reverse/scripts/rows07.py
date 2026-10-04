from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h07/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h07/A.hwp','rb').read()).hexdigest()
setup(QID="A02574", SRC="1UcD38LKxHF-Zaq_HIKcpCOwYRyrw4i5u", SHA=SQ, TAG="DSM2D203A", N=5,
      FNAME="15개정_고등_수학Ⅱ_2-2-03_소단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D203A", EXAM="Ⅱ-2-03 함수의 증가와 감소, 극대와 극소 소단원평가(발전)", MID="도함수의 활용",
      ANS_QID="A02607", ANS_SRC="1OrQcfqOFjglRuWmIlhdK_KpoZQDBHC8M", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
ID, EX = "함수의 증가와 감소", "함수의 극대와 극소"
R(1, ID, "DERIV.MONO.TANGENT_SLOPE_INCREASING_FROM_GRAPH", "접선 기울기가 증가하는 구간(그래프)", "도함수;접선의 기울기;이차함수;그래프", "단조성+그래프",
  "중", "f' 이차함수의 꼭짓점 (a+b)/2." + E, MC, "③", "선택지번호", L, H, M, "f 증가 vs f' 증가", "삼차 f 그래프(극값 x=a, b)에서 접선 기울기가 증가하는 구간",
  "그래프(gso) 시각확인 불가 — 해설(f'(a)=f'(b)=0, 최고차 양수)로 x>(a+b)/2 ③", fig="함수 그래프(gso)", final="③",
  ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
R(2, ID, "DERIV.MONO.INCREASING_ON_INTERVAL_CASEWORK", "닫힌구간에서 증가할 조건(축 위치 경우 나누기)", "함수의 증가와 감소;이차함수의 최솟값;경우 나누기", "단조성+이차함수",
  "중상", "f'≥0 on [0,1], 꼭짓점 위치 3경우." + E, S, "−2≤a≤3", "범위", M, H, M, "경우 누락", "f=x³/3−ax²+(a+2)x가 [0,1]에서 증가하는 a",
  "a<0: a+2≥0; 0≤a≤1: −a²+a+2≥0(항상); a>1: 3−a≥0 → −2≤a≤3")
R(3, EX, "DERIV.EXTREMA.CONDITIONS_TO_LOCAL_MAX", "극소 위치·접선 조건으로 극댓값", "극대;극소;접선의 기울기", "극값+연립",
  "중하", "f'(3)=0, f(0)=4, f'(0)=−9." + E, S, "9", "값", L, M, L, "", "f=x³+ax²+bx+c, x=3 극소, (0,4) 접선 기울기 −9: 극댓값", "a=−3,b=−9,c=4 → f(−1)=9")
R(4, ID, "DERIV.MONO.DEC_INC_INTERVAL_ROOT_LOCATION", "감소·증가 구간 조건 → 도함수 근 위치", "함수의 증가와 감소;도함수의 근", "단조성+근의 위치",
  "중", "f'=x(3x+2a), 근 −2a/3 ∈ [2,3]." + E, S, "−9/2≤a≤−3", "범위", L, M, M, "등호 포함", "f=x³+ax²+3이 (1,2)에서 감소, (3,∞)에서 증가하는 a", "2≤−2a/3≤3")
R(5, EX, "DERIV.EXTREMA.CUBIC_FROM_MAX_AND_TANGENT", "극댓값·접선 조건으로 삼차함수 결정 후 극솟값", "극대;극소;접선의 방정식", "극값+연립",
  "중하", "d=0, c=−12, f'(−1)=0, f(−1)=7." + E, S, "−20", "값", L, M, L, "", "삼차 f: x=−1 극댓값 7, (0,0) 접선 y=−12x일 때 극솟값", "f=2x³−3x²−12x → f(2)=−20")
build("Batch240", ROWS, 10984)
