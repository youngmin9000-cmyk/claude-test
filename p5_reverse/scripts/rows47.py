from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h47/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h47/A.hwp','rb').read()).hexdigest()
setup(QID="A02547", SRC="1F1U3iZ_guGBwa3zMwrnQ4lwoUCtkuqUd", SHA=SQ, TAG="DSM2I3SV", N=20,
      FNAME="15개정_고등_수학Ⅱ_3-3서술형평가_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I3SV", EXAM="Ⅲ-3 정적분의 활용 서술형평가", MID="정적분의 활용",
      ANS_QID="A02511", ANS_SRC="1zpCYmOLZoKkTC6D9dlVUodzi0QG0BOq6", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
F = dict(fig="설명 그림(gso)")
A, V = "넓이", "속도와 거리"
R(1, A, "INTEG.AREA.TANGENT_FROM_EXTERNAL_POINT_AXES", "외부점 접선·곡선·좌표축으로 둘러싸인 넓이", "넓이;접선의 방정식;외부점 접선", "접선+넓이",
  "중", "t=2, y=12x−12." + E, S, "6", "값", M, M, M, "삼각형 부분 제외", "y=x³+4와 (1,0)에서 그은 접선, x축, y축으로 둘러싸인 넓이", "∫₀²(x³+4)−6=6", _pt="5")
R(2, A, "INTEG.AREA.SPLIT_RATIO_VERTICAL_LINE", "넓이를 주어진 비로 나누는 직선 x=k", "넓이;정적분;삼차방정식", "넓이+방정식",
  "중하", "S_B=2S_A." + E, S, "2", "값", L, M, M, "", "y=3x²−6x+4, x축, y축, x=3 넓이를 x=k가 B=2A로 나눌 때 k", "k³−3k²+4k−4=0 → 2", _pt="5", **F)
R(3, A, "INTEG.AREA.Y_AXIS_INTEGRATION_SQRT", "y에 대한 적분으로 넓이(무리함수)", "넓이;y축 기준 적분;절댓값", "넓이+역함수",
  "중", "x=y²−2y, |·| 적분." + E, S, "2", "값", L, M, M, "y=2에서 부호 변화", "y=√(x+1)+1, y=1, y=3, y축으로 둘러싸인 넓이", "∫₁³|y²−2y|dy=2/3+4/3=2", _pt="5")
R(4, A, "INTEG.AREA.MIN_DISTANCE_POINT_THEN_AREA", "최단거리 점 구한 뒤 넓이", "넓이;최대최소;두 점 사이의 거리", "미분+넓이",
  "중", "AP² 최소 a=2." + E, S, "104/3", "값", M, M, M, "", "A(18,0)에서 y=x²까지 최단 점 P, 곡선·x축·AP로 둘러싸인 넓이", "P(2,4) → 8/3+32", _pt="5")
R(5, A, "INTEG.AREA.BETWEEN_CUBIC_AND_PARABOLA", "삼차·이차 곡선 사이 넓이", "넓이;두 곡선 사이", "단일개념",
  "중하", "교점 0,1,2." + E, S, "1/2", "값", L, M, L, "", "y=−x²+2x, y=−x³+2x²으로 둘러싸인 넓이", "1/4+1/4", _pt="6")
R(6, A, "INTEG.AREA.POWER_CURVES_TELESCOPING_SUM", "xⁿ, xⁿ⁺¹ 사이 넓이의 합(망원급수)", "넓이;수열의 합;부분분수", "넓이+수열",
  "중", "S_n=1/(n+1)−1/(n+2)." + E, S, "76", "값", L, M, M, "", "y=xⁿ, y=xⁿ⁺¹, x=1 사이 넓이 S_n, Σ_{1}^{100}S_k=q/p일 때 p+q", "25/51 → 76", _pt="6")
R(7, A, "INTEG.AREA.ABS_CURVE_AND_LINE", "절댓값 포함 곡선과 직선 사이 넓이", "넓이;절댓값;두 곡선 사이", "넓이+절댓값",
  "중", "구간별 식." + E, S, "1/4", "값", M, M, M, "", "y=2x|x−1/2|와 y=x로 둘러싸인 넓이", "1/12+1/6=1/4", _pt="6")
R(8, A, "INTEG.AREA.TWO_TANGENTS_FROM_POINT", "외부점에서 그은 두 접선과 포물선 사이 넓이", "넓이;접선의 방정식;대칭", "접선+넓이",
  "중하", "y=±2x−1." + E, S, "5", "값", L, M, M, "", "y=x²과 (0,−1)에서 그은 두 접선으로 둘러싸인 넓이 a/b의 a+b", "2/3 → 5", _pt="6")
R(9, A, "INTEG.AREA.BISECT_Y_AXIS_REGION_BY_LINE", "y축 기준 영역을 직선이 이등분", "넓이;y축 기준 적분;세제곱근", "넓이+방정식",
  "중상", "S1=2S2." + E, S, "1−1/∛2", "값", M, H, M, "", "x=y²+y와 y축 영역을 x=ay(0<a<1)가 이등분할 때 a", "(a−1)³=−1/2 → 1−1/∛2", _pt="7", **F)
R(10, A, "INTEG.AREA.FUNCTION_PLUS_INVERSE_INTEGRAL", "∫f + ∫f⁻¹ 넓이 합(직사각형)", "정적분;역함수;넓이", "적분+역함수",
  "중", "bf(b)−af(a)." + E, S, "4", "값", L, M, H, "", "f=x³+2x+1, 역함수 g일 때 ∫₀¹f + ∫₁⁴g", "1·4−0·1=4", _pt="5")
R(11, A, "INTEG.AREA.EQUAL_AREAS_ZERO_INTEGRAL", "두 넓이가 같을 조건(정적분=0)", "넓이;정적분", "넓이+조건",
  "중", "∫₀^{√2}(−x²+2−mx)=0." + E, S, "4√2/3", "값", L, M, M, "", "y=−x²+2와 y=mx, y축 넓이 A, y=mx, x=√2 넓이 B가 같을 때 m", "4√2/3−m=0", _pt="5", **F)
R(12, A, "INTEG.AREA.EQUAL_AREAS_ZERO_INTEGRAL", "넓이 비 조건(정적분=0)으로 t", "넓이;정적분", "넓이+조건",
  "중하", "S1=S2 → ∫₀ᵗ=0." + E, S, "3/2", "값", L, M, M, "t>1", "y=x²−x와 x축 넓이가 곡선·x축·x=t 넓이의 1/2일 때 t", "t²(2t−3)/6=0 → 3/2", _pt="6")
R(13, "미분의 활용", "DERIV.TANGENT.MAX_TRIANGLE_AREA_PARALLEL_TANGENT", "평행 접선 접점에서 삼각형 넓이 최대", "접선의 기울기;넓이;최대", "접선+도형",
  "중하", "기울기 1 접선." + E, S, "(1/2, 1/4)", "좌표", L, M, M, "", "y=x² 위 O와 A(1,1) 사이 P, 삼각형 OAP 넓이 최대인 P", "2x=1", _pt="6", **F)
R(14, V, "INTEG.MOTION.MAX_HEIGHT_PROJECTILE", "속도 적분으로 최고 높이", "속도;위치;정적분", "적분+운동",
  "하", "v=0 at t=2." + E, S, "25 m", "값", L, L, L, "초기 높이", "높이 5m, v=20−10t일 때 최고 높이", "5+20=25", _pt="5")
R(15, V, "INTEG.MOTION.DISTANCE_AT_MAX_SPEED", "최대 속도 시각까지 이동 거리", "속도;최대최소;정적분", "미분+적분",
  "중하", "v'=0 at t=2." + E, S, "2 km", "값", L, M, M, "", "v=t²(3−t)/2 (km/분), 속도 최대 지점의 P역으로부터 거리", "∫₀²v=2", _pt="5")
R(16, V, "INTEG.MOTION.COUNT_RETURNS_TO_ORIGIN", "원점 통과 횟수(위치 함수의 근)", "속도;위치;정적분;인수분해", "적분+방정식",
  "중하", "a(a−1)(a−2)(a−4)=0." + E, S, "2회", "값", L, M, M, "t≤3 범위", "v=4t³−21t²+28t−8, t=3까지 원점 통과 횟수", "a=1,2 → 2회", _pt="5")
R(17, V, "INTEG.MOTION.TOTAL_DISTANCE_FROM_VT_GRAPH", "속도 그래프로 실제 이동 거리", "속도;이동 거리;그래프", "그래프+운동",
  "중하", "구간별 v 식 판독." + E, S, "8", "값", L, M, M, "부호 바뀌는 구간", "0≤t≤6 v-t 그래프에서 실제 이동 거리", "해설: v=t, 2, −2t+10 → ∫|v|=8 (그림 의존)", _pt="7", **G)
R(18, V, "INTEG.MOTION.FLOW_VOLUME_FROM_VELOCITY", "속도 적분으로 유출량(원 단면)", "속도;정적분;실생활 활용", "적분+실생활",
  "하", "4π×36." + E, S, "144π cm³", "값", L, L, L, "", "반지름 2cm 관, v=6t−t² 멈출 때까지 유출량", "144π", _pt="6")
R(19, V, "INTEG.MOTION.CATCH_UP_TIME", "두 물체 위치가 같아지는 시각(추월)", "속도;위치;정적분", "적분+방정식",
  "하", "t²=t²/2+t+24." + E, S, "8초 후", "값", L, M, L, "", "B가 A보다 24m 앞, v_A=2t, v_B=t+1일 때 위치가 같아지는 시각", "(t−8)(t+6)=0 → 8", _pt="6")
R(20, V, "INTEG.MOTION.PIECEWISE_DISTANCE_THEN_CONSTANT", "거리 조건 후 등속 구간 포함 총 이동거리", "속도;이동 거리;삼차방정식", "적분+방정식",
  "중", "4km 도달 x=2분." + E, S, "40 km", "값", M, M, M, "", "4km까지 v=3t²/4+t/2+1/2, 이후 등속, 10분 동안 거리", "x=2, v(2)=4.5 → 4+8×4.5=40", _pt="6")
build("Batch266", ROWS[:10], 11212)
build("Batch267", ROWS[10:], 11222)
