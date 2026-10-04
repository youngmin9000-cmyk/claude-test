from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h44/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h44/A.hwp','rb').read()).hexdigest()
setup(QID="A02544", SRC="1wQNctLO_iF9aFc-GOcbV-tCvo2V6hYHa", SHA=SQ, TAG="DSM2I302N", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-3-02_소단원평가_기본_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I302N", EXAM="Ⅲ-3-02 속도와 거리 소단원평가(기본)", MID="정적분의 활용",
      ANS_QID="A02543", ANS_SRC="1Jkq_uHrivVbhVYpZZ5LfJ4xF-_1dYtul", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
V = "속도와 거리"
R(1, V, "INTEG.MOTION.DISTANCE_WITH_SIGN_CHANGE", "방향 전환 포함 구간 이동 거리(연직 운동)", "속도;이동 거리;정적분", "적분+운동",
  "중하", "t=5 분할." + E, S, "166.6 m", "값", M, M, L, "", "v=49−9.8t, 2초 후~10초 후 움직인 거리", "44.1+122.5=166.6")
R(2, V, "INTEG.MOTION.RETURN_TO_ORIGIN_TIME", "원점으로 돌아오는 시각", "속도;위치;정적분;인수분해", "적분+방정식",
  "하", "−a(a+4)(a−3)=0." + E, MC, "③", "선택지번호", L, M, L, "", "v=−3t²−2t+12, 원점 출발 후 다시 돌아오는 시각", "3", final="③ (3)")
R(3, V, "INTEG.MOTION.BRAKING_DISTANCE", "제동 후 정지까지 이동 거리", "속도;이동 거리;정적분;실생활 활용", "적분+실생활",
  "하", "정지 t=10." + E, MC, "②", "선택지번호", L, L, L, "", "v=30−3t 제동 후 정지까지 거리", "150", final="② (150 m)")
R(4, V, "INTEG.MOTION.PIECEWISE_DISTANCE_THEN_CONSTANT", "거리 조건 후 등속 구간 포함 총 이동거리", "속도;이동 거리;삼차방정식", "적분+방정식",
  "중", "4km 도달 x=2분." + E, S, "40 km", "값", M, M, M, "", "4km까지 v=3t²/4+t/2+1/2, 이후 등속, 10분 동안 거리", "4+8×4.5=40", memo_extra="원문 근사중복 후보: A02547 Q20.")
R(5, V, "INTEG.MOTION.TOTAL_DISTANCE_FROM_VT_GRAPH", "속도 그래프로 실제 이동 거리", "속도;이동 거리;그래프", "그래프+운동",
  "하", "넓이 합." + E, MC, "④", "선택지번호", L, M, L, "", "v-t 그래프, t=0~3 실제 이동 거리", "해설: 1+2+1=4 (그림 의존)", final="④ (4)", **G)
R(6, V, "INTEG.MOTION.POSITION_FROM_VT_GRAPH", "속도 그래프로 시각별 위치", "속도;위치;그래프", "그래프+운동",
  "중하", "부호 있는 넓이." + E, S, "t=2: 1, t=4: 0", "값", L, M, M, "", "0≤t≤4 v-t 그래프, t=2와 t=4의 위치", "해설: v=t, −t+2, t−4 판독 → 1, 0 (그림 의존)", **G)
R(7, V, "INTEG.MOTION.DISTANCE_AT_MAX_SPEED", "최대 속도 시각까지 이동 거리", "속도;최대최소;정적분", "미분+적분",
  "중하", "v'=0 at t=30." + E, S, "180 m", "값", L, M, M, "", "v=−t²/100+3t/5 (0≤t≤60), 속도 최대 지점의 A로부터 거리", "∫₀³⁰v=180")
R(8, V, "INTEG.MOTION.DISTANCE_UNTIL_RETURN", "원점 복귀까지 이동 거리", "속도;위치;이동 거리;정적분", "적분+운동",
  "하", "복귀 t=4, 분할 t=2." + E, S, "12", "값", L, M, L, "변화량 0이지만 거리 ≠ 0", "v=6−3t, 원점 복귀까지 움직인 거리", "6+6=12")
R(9, V, "INTEG.MOTION.DISTANCE_UNTIL_FIRST_TURN_GRAPH", "처음 방향 전환까지 이동 거리(그래프)", "속도;이동 거리;그래프", "그래프+운동",
  "하", "삼각형 넓이." + E, S, "3/2", "값", L, M, L, "", "v-t 그래프, 처음 방향 바꿀 때까지 실제 거리", "해설: ½×3×1 (그림 의존)", **G)
R(10, V, "INTEG.MOTION.DISTANCE_FROM_ORIGIN_PLUS_PATH_GRAPH", "원점과의 거리 + 이동 거리(그래프)", "속도;위치;이동 거리;그래프", "그래프+운동",
  "중하", "S1−S2, S1+S2." + E, S, "16 (해설 8)", "값", L, M, M, "'원점 사이의 거리'는 |위치|",
  "v-t 그래프, t=10에서 물체와 원점 사이 거리 a, 0~10 이동 거리 b일 때 a+b",
  "해설 판독값 S1=4, S2=8 → 위치 −4, '원점 사이의 거리' a=|−4|=4, b=12 → a+b=16. 해설은 a=−4(위치)를 그대로 써서 8",
  keymatch=False, key="8 (해설: a=−4로 처리)", final="HOLD (독립 16 — 거리는 |−4|=4; 해설 8)",
  conflict="문항은 '원점 사이의 거리 a'인데 해설은 a=위치(−4)로 계산 → 8. 거리 정의상 a=4, a+b=16",
  fig="그래프(gso)", ready="REVIEW", status="해설 오류 의심(정의 불일치)+그래프 시각확인 불가", trust="낮음(해설 오류·그래프)", review="REVIEW-정답충돌")
build("Batch270", ROWS, 11247)
