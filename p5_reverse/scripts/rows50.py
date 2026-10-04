from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h50/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h50/A.hwp','rb').read()).hexdigest()
setup(QID="A02550", SRC="1ODO3RdCF_fdCgQjSkSIaa4OVow49Hh6T", SHA=SQ, TAG="DSM2I3MA", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-3_중단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I3MA", EXAM="Ⅲ-3 정적분의 활용 중단원평가(발전)", MID="정적분의 활용",
      ANS_QID="A02539", ANS_SRC="1QAw4F5w6pMa0KrLbISRtXAGtQ4vk8gW0", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
F = dict(fig="설명 그림(gso)")
A, V = "넓이", "속도와 거리"
R(1, A, "INTEG.AREA.LIMIT_OF_AREA_OVER_H", "넓이 함수 S(h)/h의 극한(미분계수 해석)", "정적분;넓이;미분계수", "적분+미분",
  "중하", "F' 이용 4f(1)." + E, MC, "④", "선택지번호", L, M, M, "구간 폭 4h", "y=3x²−1, x축, x=1±2h 넓이 S(h)일 때 lim S(h)/h", "4f(1)=8", final="④ (8)")
R(2, A, "INTEG.AREA.TANGENT_CURVE_MIN_AREA", "접선과 곡선 사이 넓이의 최솟값", "넓이;접선의 방정식;이차함수 최솟값", "넓이+최대최소",
  "중", "∫(x−t)²=t²−t+1/3." + E, MC, "①", "선택지번호", L, M, M, "", "y=x²−1과 (t,t²−1) 접선, y축, x=1로 둘러싸인 넓이 최솟값 (0<t<1)", "(t−1/2)²+1/12 → 1/12", final="① (1/12)")
R(3, A, "INTEG.AREA.FUNCTION_AND_INVERSE", "함수와 역함수 그래프로 둘러싸인 넓이", "넓이;역함수;대칭", "넓이+역함수",
  "중", "y=x 대칭 → 2배." + E, MC, "①", "선택지번호", L, M, M, "증가함수 확인", "f=x³−2x²+2x와 역함수 g로 둘러싸인 넓이", "2∫₀¹ x(x−1)² dx=1/6", final="① (1/6)")
R(4, A, "INTEG.AREA.ODD_ABS_FUNCTION_X_AXIS", "절댓값 포함 기함수와 x축 사이 넓이", "넓이;기함수;절댓값", "넓이+대칭",
  "중하", "원점대칭 2배." + E, S, "27/8", "값", L, M, M, "x<0 식 변형", "f=4x³−6x|x|와 x축으로 둘러싸인 넓이", "2∫₀^{3/2}(6x²−4x³)dx=27/8", **F)
R(5, V, "INTEG.MOTION.POSITION_PIECEWISE_VELOCITY", "구간별 속도에서 위치 계산", "속도;위치;정적분", "적분+운동",
  "중하", "구간 나눠 적분." + E, S, "35/6", "값", L, M, L, "위치 vs 거리", "v=2t−t²(0≤t<2), t²−5t+6(t≥2), t=5 위치", "4/3+9/2=35/6")
R(6, A, "INTEG.AREA.TWO_PARABOLAS_LIMIT", "두 포물선 사이 넓이의 극한", "넓이;수열의 극한", "넓이+극한",
  "중", "교점 ±√(1+1/n²)." + E, MC, "④", "선택지번호", L, M, M, "", "y=x²−2−2/n², y=−x² 사이 넓이 S_n의 극한", "→ ∫_{−1}^{1}(2−2x²)=8/3", final="④ (8/3)")
R(7, A, "INTEG.AREA.FUNCTION_PLUS_INVERSE_INTEGRAL", "∫f + ∫f⁻¹ 넓이 합(직사각형)", "정적분;역함수;넓이", "적분+역함수",
  "중", "bf(b)−af(a)." + E, S, "1", "값", L, M, H, "", "증가 f, f(0)=1/4, f(1)=1일 때 ∫₀¹f + ∫_{1/4}^{1} f⁻¹", "1·1−0·(1/4)=1 (그림 보조)", **F)
R(8, V, "INTEG.MOTION.FLOW_VOLUME_FROM_VELOCITY", "속도 적분으로 유출량(단면적×거리)", "속도;정적분;실생활 활용", "적분+실생활",
  "하", "정지 t=6." + E, S, "72 cm³", "값", L, L, L, "", "단면적 2cm², v=6t−t² 물이 멈출 때까지 유출량", "2×36=72")
R(9, V, "INTEG.MOTION.TWO_POINTS_MEET_MAX_DIST", "두 점이 만나는 시각과 최대 거리 시각", "속도;위치;정적분;최대최소", "적분+운동",
  "중하", "위치 비교." + E, S, "6", "값", L, M, M, "", "v_P=−3t+6, v_Q=3t−6: 다시 만나는 t1, 거리 최대 t2 (0<t<t1)의 합", "t1=4, t2=2 → 6")
R(10, V, "INTEG.MOTION.REVERSE_DIRECTION_DISTANCE_GRAPH", "속도 그래프로 역방향 이동 거리", "속도;이동 거리;정적분;그래프", "그래프+운동",
  "중하", "f'=(t−1)(t−2) 그래프 판독." + E, S, "1/6", "값", L, M, M, "방향 전환 구간", "이차 f'(t) 그래프(0,2),(1,0),(2,0)에서 반대 방향 이동 거리", "∫₁²|f'|=1/6 (그림 의존)", **G)
build("Batch263", ROWS, 11182)
