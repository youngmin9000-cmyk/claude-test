from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h34/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h34/A.hwp','rb').read()).hexdigest()
setup(QID="A02534", SRC="1zIdabdb4ZlYAYvKlddoKRSawRMN5n9O4", SHA=SQ, TAG="DSM2I202F", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-2-02_소단원평가_기초_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I202F", EXAM="Ⅲ-2-02 정적분의 성질 소단원평가(기초)", MID="정적분",
      ANS_QID="A02533", ANS_SRC="1L2z7wW91F90nAWCen1BBxdmihDsb8430", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"
DI = "정적분"; FI = "정적분으로 정의된 함수"
R(1, DI, "INTEG.DEF.LINEARITY_COMBINE_SAME_INTERVAL", "같은 구간 정적분 합·차 결합", "정적분 성질;선형성", "단일개념",
  "하", "∫₀²4x." + E, S, "8", "값", L, L, L, "", "∫₀²(x+1)²dx−∫₀²(x−1)²dx", "8")
R(2, DI, "INTEG.DEF.LINEARITY_COMBINE_SAME_INTERVAL", "같은 구간 정적분 결합(대칭·전개)", "정적분 성질;선형성;우함수·기함수", "단일개념",
  "하", "2문항." + E, S, "⑴ 46/3 ⑵ 368", "값", M, L, L, "", "⑴ ∫₋₁¹(x²+4)−2∫₋₁¹(x²−x−2) ⑵ ∫₁³(2x+1)³+∫₁³(2x−1)³", "⑴ −2/3+16 ⑵ ∫(16x³+12x)=320+48", nsub=2)
R(3, DI, "INTEG.DEF.ADJACENT_INTERVALS_MERGE", "인접 구간 정적분 합치기", "정적분 성질;구간 합", "단일개념",
  "하", "2문항." + E, S, "⑴ 6 ⑵ 21", "값", L, L, L, "", "⑴ ∫₋₁¹(2x+1)+∫₁²(2x+1) ⑵ ∫₂³+∫₀²(3x²−2x+1)", "⑴ ∫₋₁² ⑵ ∫₀³=27−9+3", nsub=2)
R(4, DI, "INTEG.DEF.ABS_LINEAR", "일차식 절댓값 정적분", "절댓값;구간 분할", "단일개념",
  "하", "x=1 분할." + E, S, "5/2", "값", L, M, L, "", "∫₀³|x−1|dx", "1/2+2=5/2")
R(5, DI, "INTEG.DEF.ABS_LINEAR_QUADRATIC", "일차·이차식 절댓값 정적분", "절댓값;구간 분할", "단일개념",
  "하", "2문항." + E, S, "⑴ 13/2 ⑵ 8/3", "값", L, M, L, "", "⑴ ∫₋₂¹|2x−1| ⑵ ∫₀³|x(x−2)|", "⑴ 25/4+1/4 ⑵ 4/3+4/3", nsub=2)
R(6, DI, "INTEG.DEF.LINEARITY_COMBINE_SAME_INTERVAL", "같은 구간 정적분 차 결합", "정적분 성질;선형성", "단일개념",
  "하", "∫₁³(3x²+2)." + E, S, "30", "값", L, L, L, "", "∫₁³(3x²+x)dx−∫₁³(x−2)dx", "26+4=30")
R(7, DI, "INTEG.DEF.LINEARITY_COMBINE_SAME_INTERVAL", "같은 구간 정적분 합 결합", "정적분 성질;선형성", "단일개념",
  "하", "∫₁²(3x²+2x+3)." + E, S, "13", "값", L, L, L, "", "∫₁²(3x²−2x)dx+∫₁²(4x+3)dx", "7+3+3=13")
R(8, DI, "INTEG.DEF.LINEARITY_COMBINE_SAME_INTERVAL", "같은 구간 정적분 합·차(전개)", "정적분 성질;선형성", "단일개념",
  "하", "2문항." + E, S, "⑴ 16/3 ⑵ 24", "값", L, L, L, "", "⑴ ∫₀²(x²−1)+∫₀²(x²+1) ⑵ ∫₋₂¹(x+1)³−∫₋₂¹(x−1)³", "⑴ ∫2x² ⑵ ∫(6x²+2)=24", nsub=2)
R(9, DI, "INTEG.DEF.ABS_AND_MERGE_SYMMETRIC", "절댓값 정적분·구간 합치기(대칭)", "절댓값;구간 합;기함수", "단일개념",
  "하", "2문항." + E, S, "⑴ 29/6 ⑵ 16", "값", L, M, L, "", "⑴ ∫₋₁²|x(x+1)| ⑵ ∫₋₂¹+∫₁²(x³+3x²)", "⑴ 1/6+14/3 ⑵ 0+2·8", nsub=2)
R(10, FI, "INTEG.FUNC.DERIVATIVE_OF_INTEGRAL_BASIC", "위끝이 x인 정적분의 미분", "적분과 미분의 관계", "단일개념",
  "하", "피적분함수 그대로." + E, S, "⑴ 5x³−2x² ⑵ 3−2x+3x²", "식", L, L, L, "", "⑴ d/dx∫₁ˣ(5t³−2t²)dt ⑵ d/dx∫₋₁ˣ(3−2t+3t²)dt", "피적분함수의 t→x", nsub=2)
build("Batch278", ROWS, 11316)
