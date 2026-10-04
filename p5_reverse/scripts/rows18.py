from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h18/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h18/A.hwp','rb').read()).hexdigest()
setup(QID="A02588", SRC="1mOmILDoeowXwyJ5A36QKX_7CjLgMbwpd", SHA=SQ, TAG="DSM2D101B", N=10,
      FNAME="15개정_고등_수학Ⅱ_2-1-01_소단원평가_기초_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D101B", EXAM="Ⅱ-1-01 미분계수 소단원평가(기초)", MID="미분계수와 도함수",
      ANS_QID="A02618", ANS_SRC="1EhBRvceTDX6qW8N8lHg3VDVrL3xzkp_i", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"
SM = "미분계수"
R(1, SM, "DIFF.AVG_RATE.QUADRATIC_NUM_AND_SYMBOLIC", "평균변화율 — 수치 구간·문자 구간", "평균변화율;이차함수", "단일개념",
  "하", "정의 대입." + E, S, "⑴ 2 ⑵ 2a+Δx", "값(소문항별)", L, L, L, "", "f=x²: ⑴ −1→3 ⑵ a→a+Δx 평균변화율", "⑴ (9−1)/4=2 ⑵ 2a+Δx", nsub=2)
R(2, SM, "DIFF.AVG_RATE.QUADRATIC_NUM_AND_SYMBOLIC", "평균변화율 — 수치 구간·문자 구간", "평균변화율;이차함수", "단일개념",
  "하", "정의 대입." + E, S, "⑴ 4 ⑵ 4+Δx", "값(소문항별)", L, L, L, "", "f=x²−2x: ⑴ 1→5 ⑵ 3→3+Δx 평균변화율", "⑴ (15−(−1))/4=4 ⑵ (4Δx+Δx²)/Δx", nsub=2)
R(3, SM, "DIFF.DERIV_AT_POINT.BY_DEFINITION", "정의로 미분계수 계산", "미분계수;극한", "단일개념",
  "하", "정의식 극한." + E, S, "6", "값", L, L, L, "", "f=x²의 x=3 미분계수", "lim(6+Δx)=6")
R(4, SM, "DIFF.TANGENT_SLOPE.BY_DEFINITION", "접선의 기울기 = 미분계수(정의)", "미분계수;접선의 기울기", "단일개념",
  "하", "정의식 극한." + E, S, "2", "값", L, L, L, "", "y=x²+2 위 (1,3) 접선 기울기", "lim(2+Δx)=2")
R(5, SM, "DIFF.AVG_RATE.QUADRATIC_NUM_AND_SYMBOLIC", "평균변화율 — 수치 구간·문자 구간", "평균변화율;이차함수", "단일개념",
  "하", "정의 대입." + E, S, "[독립] ⑴ 1 ⑵ 3+2Δx", "값(소문항별)", L, L, L, "구간 시작점 1", "f=2x²−x+1: ⑴ −1→2 ⑵ 1→1+Δx 평균변화율",
  "⑴ (7−4)/3=1 일치. ⑵ (2(1+Δx)²−(1+Δx)+1−2)/Δx=3+2Δx; 동반 해설은 a→a+Δx로 풀어 4a+2Δx−1 (a=1 대입 시 3+2Δx와 동치) — 해설 표기 불일치",
  nsub=2, keymatch=False, key="⑴ 1 ⑵ 4a+2Δx−1", final="⑴ 1 ⑵ 3+2Δx (해설 4a+2Δx−1은 a=1에서 동치)",
  conflict="⑵ 원문 '1에서 1+Δx까지' vs 해설 일반 a 풀이 4a+2Δx−1 — 해설 표기 오류(수학적으로 a=1 대입 시 일치)",
  ready="REVIEW", status="독립풀이-정답 표기 불일치", trust="중간(해설 표기 오류)", review="REVIEW-해설표기불일치")
R(6, SM, "DIFF.DERIV_AT_POINT.BY_DEFINITION", "정의로 미분계수 계산", "미분계수;극한", "단일개념",
  "하", "정의식 극한." + E, S, "7", "값", L, L, L, "", "f=x²+3x의 x=2 미분계수", "lim(7+Δx)=7")
R(7, SM, "DIFF.TANGENT_SLOPE.BY_DEFINITION", "접선의 기울기 = 미분계수(정의)", "미분계수;접선의 기울기", "단일개념",
  "하", "정의식 극한." + E, S, "4", "값", L, L, L, "", "f=2x²−1 위 (1,1) 접선 기울기", "lim(4+2Δx)=4")
R(8, SM, "DIFF.AVG_RATE.LINEAR_AND_QUADRATIC", "같은 구간 평균변화율 — 일차·이차", "평균변화율;일차함수;이차함수", "단일개념",
  "하", "정의 대입." + E, S, "⑴ 1 ⑵ 5", "값(소문항별)", L, L, L, "", "x: −1→3, ⑴ f=x+2 ⑵ f=x²+3x 평균변화율", "⑴ 4/4=1 ⑵ (18−(−2))/4=5", nsub=2)
R(9, SM, "DIFF.DERIV_AT_POINT.BY_DEFINITION", "정의로 미분계수 계산", "미분계수;극한", "단일개념",
  "하", "정의식 극한." + E, S, "⑴ 1 ⑵ 5", "값(소문항별)", L, L, L, "", "x=1 미분계수: ⑴ f=x+1 ⑵ f=2x²+x", "⑴ 1 ⑵ lim(5+2Δx)=5", nsub=2)
R(10, SM, "DIFF.TANGENT_SLOPE.BY_DEFINITION", "접선의 기울기 = 미분계수(정의)", "미분계수;접선의 기울기;삼차함수", "단일개념",
  "하", "정의식 극한(삼차 전개)." + E, S, "⑴ −6 ⑵ −4", "값(소문항별)", L, L, L, "", "⑴ f=3x²+1, (−1,4) ⑵ f=−x³−x+7, (−1,9) 접선 기울기",
  "⑴ lim(−6+3Δx)=−6 ⑵ lim(−Δx²+3Δx−4)=−4; 점 좌표 검산 일치", nsub=2)
build("Batch228", ROWS, 10880)
