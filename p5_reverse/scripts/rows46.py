from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h46/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h46/A.hwp','rb').read()).hexdigest()
setup(QID="A02546", SRC="1PuOtqAYbvWccR9uNvtTfXNJ5nAHK89ST", SHA=SQ, TAG="DSM2I302A", N=5,
      FNAME="15개정_고등_수학Ⅱ_3-3-02_소단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I302A", EXAM="Ⅲ-3-02 속도와 거리 소단원평가(발전)", MID="정적분의 활용",
      ANS_QID="A02510", ANS_SRC="1kJB2CBjLbMOzqiPW2WBIVMojMKxPUpKA", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
V = "속도와 거리"
R(1, V, "INTEG.MOTION.TWO_POINTS_MEET_AGAIN", "두 점이 다시 만나는 시각", "속도;위치;정적분", "적분+방정식",
  "하", "위치 같음." + E, MC, "②", "선택지번호", L, M, L, "", "v=3t(4−t), u=2t로 원점 동시 출발, 다시 만나는 시각", "6t²−t³=t² → 5", final="② (5초)")
R(2, V, "INTEG.MOTION.REVERSE_DIRECTION_DISTANCE", "처음 방향과 반대로 움직인 거리", "속도;이동 거리;정적분", "미분+적분",
  "중하", "1<t<3에서 v<0." + E, MC, "④", "선택지번호", L, M, M, "", "x=t³/3−2t²+3t일 때 t=0 방향과 반대로 움직인 거리", "∫₁³(−t²+4t−3)=4/3", final="④ (4/3)")
R(3, V, "INTEG.MOTION.POSITION_AND_DISTANCE_FROM_VT_GRAPH", "속도 그래프로 위치 함수와 경과 거리", "속도;위치;이동 거리;그래프", "그래프+운동",
  "중하", "v=t, −t+2 판독." + E, S, "⑴ s=t²/2+1 (0≤t≤1), −t²/2+2t (1≤t≤3) ⑵ 3/2", "식/값", L, M, M, "위치 vs 거리", "0≤t≤3 v-t 그래프, s(0)=1: ⑴ s(t) ⑵ 경과 거리", "해설 그래프 판독 v=t, −t+2 → ⑵ 1/2×3 (그림 의존)", nsub=2, **G)
R(4, V, "INTEG.MOTION.SECOND_MEETING_TIME", "두 번째로 만나는 시각(삼차 속도)", "속도;위치;정적분;인수분해", "적분+방정식",
  "중", "t²(3t−4)(t−6)=0." + E, S, "6초 후", "값", M, M, M, "첫 만남 4/3초", "v_P=7t(4−t), v_Q=2t(3−t)(6−t) 같은 방향 출발, 두 번째 만나는 시각", "4/3, 6 → 6")
R(5, V, "INTEG.MOTION.TWO_POINTS_MEET_AGAIN", "두 점이 다시 만나는 시각", "속도;위치;정적분", "적분+방정식",
  "하", "t²−3t=6t−2t²." + E, MC, "⑤", "선택지번호", L, L, L, "", "v_P=2t−3, v_Q=6−4t로 원점 동시 출발, 다시 만나는 시각", "3t(t−3)=0 → 3", final="⑤ (3초)")
build("Batch268", ROWS, 11232)
