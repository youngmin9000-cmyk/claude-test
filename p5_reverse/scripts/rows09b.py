from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h09b/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h09b/A.hwp','rb').read()).hexdigest()
setup(QID="A02509", SRC="10Kp8pHh6S_1BBDHOw20h_EBxU4825N5Z", SHA=SQ, TAG="DSM2I302F", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-3-02_소단원평가_기초_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I302F", EXAM="Ⅲ-3-02 속도와 거리 소단원평가(기초)", MID="정적분의 활용",
      ANS_QID="A02545", ANS_SRC="1Z_SJ9Lw6Sx7Q2bw7S1zI3qHMPl7usnv9", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
V = "속도와 거리"
IT = "원문 수식 'it −8t+2' 등의 'it'은 이탤릭 서식 토큰(v(t)=−8t+2), 해설과 일치."
R(1, V, "INTEG.MOTION.POSITION_DISPLACEMENT_DISTANCE", "위치·위치 변화량·이동 거리 구분 계산", "속도;위치;이동 거리;정적분", "적분+운동",
  "하", "3문항." + E, S, "⑴ t³/3−3t²/2+2t+3 ⑵ 2/3 ⑶ 1", "식/값", L, M, L, "변화량 vs 거리", "좌표 3 출발, v=t²−3t+2: ⑴ 위치 ⑵ 0→2 변화량 ⑶ 0→2 이동 거리", "⑶ 5/6+1/6=1", nsub=3)
R(2, V, "INTEG.MOTION.DIRECTION_CHANGE_POSITION", "운동 방향 바뀌는 시각과 위치", "속도;위치;정적분", "단일개념",
  "하", "v=0." + E, S, "t=1/4, 위치 49/4", "값", L, L, L, "", "좌표 12 출발, v=−8t+2일 때 방향 바뀌는 시각과 위치", "12+1/4=49/4", memo_extra=IT)
R(3, V, "INTEG.MOTION.HEIGHT_AT_TIME", "속도 적분으로 시각 t의 높이", "속도;위치;정적분", "단일개념",
  "하", "∫₀³." + E, S, "15 m", "값", L, L, L, "", "지면에서 v=20−10t로 던진 물체의 3초 후 높이", "60−45=15")
R(4, V, "INTEG.MOTION.AREA_MEANING_DISPLACEMENT_DISTANCE", "속도 그래프 넓이의 의미(변화량·거리)", "속도;이동 거리;위치 변화량;그래프", "그래프+개념",
  "하", "부호 있는 넓이 vs 절댓값." + E, S, "⑴ t=0~b 위치 변화량 ⑵ t=0~c 이동 거리", "서술", L, M, M, "", "v-t 그래프 넓이 S1,S2,S3: ⑴ S1−S2 ⑵ S1+S2+S3의 의미", "해설: b, c는 그래프 표기점 (그림 의존)", nsub=2, **G)
R(5, V, "INTEG.MOTION.POSITION_AND_DISTANCE_AT_TIME", "시각 t의 위치와 이동 거리", "속도;위치;이동 거리;정적분", "단일개념",
  "하", "t=3/2 분할." + E, S, "위치 2, 거리 5/2", "값", L, M, L, "", "원점 출발, v=−2t+3일 때 2초 후 위치와 이동 거리", "9/4+1/4=5/2", memo_extra=IT)
R(6, V, "INTEG.MOTION.BRAKING_DISTANCE", "제동 후 정지까지 이동 거리", "속도;이동 거리;정적분;실생활 활용", "적분+실생활",
  "하", "정지 t=10." + E, S, "100 m", "값", L, L, L, "", "v=−2t+20으로 제동, 정지까지 거리", "∫₀¹⁰(−2t+20)=100", memo_extra=IT)
R(7, "속도와 가속도", "DERIV.MOTION.VELOCITY_ACCEL_DIRECTION_QUADRATIC", "이차 위치함수의 속도·가속도·방향 전환", "속도;가속도;운동 방향", "단일개념",
  "하", "미분." + E, S, "⑴ 속도 −1, 가속도 2 ⑵ 3/2", "값", L, L, L, "", "x=t²−3t: ⑴ t=1 속도·가속도 ⑵ 방향 바뀌는 시각", "v=2t−3, a=2", nsub=2)
R(8, "속도와 가속도", "DERIV.MOTION.VELOCITY_ACCEL_DIRECTION_CUBIC", "삼차 위치함수의 속도·가속도·방향 전환", "속도;가속도;운동 방향", "단일개념",
  "하", "미분, t>0." + E, S, "⑴ 속도 −27, 가속도 0 ⑵ 5", "값", L, L, L, "t>0", "x=t³−6t²−15t: ⑴ t=2 속도·가속도 ⑵ 방향 바뀌는 시각", "v=3(t+1)(t−5)", nsub=2)
R(9, V, "INTEG.MOTION.DISTANCE_WITH_SIGN_CHANGE", "부호 바뀌는 속도의 이동 거리", "속도;이동 거리;정적분", "단일개념",
  "하", "t=2 분할." + E, S, "1", "값", L, L, L, "", "v=−t+2, t=1→3 이동 거리", "1/2+1/2=1")
R(10, V, "INTEG.MOTION.DISTANCE_WITH_SIGN_CHANGE", "부호 바뀌는 이차 속도의 이동 거리", "속도;이동 거리;정적분", "단일개념",
  "하", "t=1 분할." + E, S, "3", "값", L, M, L, "", "v=−t²−t+2, t=0→2 이동 거리", "7/6+11/6=3")
build("Batch269", ROWS, 11237)
