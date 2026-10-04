from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h21/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h21/A.hwp','rb').read()).hexdigest()
setup(QID="A02521", SRC="1_HseI0rUt8wFki9cLXXwxNn13cJ_bfP5", SHA=SQ, TAG="DSM2I102F", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-1-02_소단원평가_기초_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I102F", EXAM="Ⅲ-1-02 부정적분의 계산 소단원평가(기초)", MID="부정적분",
      ANS_QID="A02520", ANS_SRC="1AbUXxy-qYVCRanoThjSJaWzxFbPAKNuy", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"
U = "부정적분의 계산"
P = "INTEG.INDEF.POLY_BASIC"; PN = "다항함수 부정적분 기본"
F = "INTEG.INDEF.FROM_DERIVATIVE_CONSTANT"; FN = "도함수와 함숫값으로 함수 복원"
N = "해설 'C는 부정적분' 표기(→적분상수)"
R(1, U, P, PN, "부정적분;선형성", "단일개념", "하", "2문항." + E, S, "⑴ 2x²−x+C ⑵ −x³+x²+C", "식", L, L, L, N, "⑴ ∫(4x−1)dx ⑵ ∫(−3x²+2x)dx", "기본", nsub=2)
R(2, U, P, PN, "부정적분;선형성", "단일개념", "하", "기본." + E, S, "x³−2x²+2x+C", "식", L, L, L, N, "∫(3x²−4x+2)dx", "기본")
R(3, U, P, PN, "부정적분;선형성;전개", "단일개념", "하", "4문항." + E, S, "⑴ 2x²−5x+C ⑵ −⅓x³+4x²+C ⑶ x⁴−x³+x²+C ⑷ ⅓x³+3x²−7x+C", "식", L, L, L, N,
  "⑴ ∫(4x−5) ⑵ ∫(−x²+8x) ⑶ ∫(4x³−3x²+2x) ⑷ ∫(x−1)(x+7)", "⑷ 전개 후 적분", nsub=4)
R(4, U, F, FN, "부정적분;적분상수", "단일개념", "하", "C=2." + E, S, "f(x)=x³+x²−x+2", "식", L, L, L, N, "f'=3x²+2x−1, f(0)=2", "C=2")
R(5, U, F, FN, "부정적분;적분상수", "단일개념", "하", "2문항." + E, S, "⑴ f=3x²+x−1 ⑵ f=−x³+4x²−5x+2", "식", L, L, L, N, "⑴ f'=6x+1, f(0)=−1 ⑵ f'=−3x²+8x−5, f(1)=0", "⑵ C=2", nsub=2)
R(6, U, P, PN, "부정적분;선형성", "단일개념", "하", "기본." + E, S, "¼x⁴−2x³+x²−5x+C", "식", L, L, L, N, "∫(x³−6x²+2x−5)dx", "기본")
R(7, U, P, PN, "부정적분;전개", "단일개념", "하", "전개." + E, S, "(4/3)x³+6x²+9x+C", "식", L, L, L, N, "∫(2x+3)²dx", "4x²+12x+9 적분")
R(8, U, P, PN, "부정적분;전개", "단일개념", "하", "2문항." + E, S, "⑴ x³−x²+4x+C ⑵ ⅔x³−(5/2)x²−3x+C", "식", L, L, L, N, "⑴ ∫(3x²−2x+4) ⑵ ∫(2x+1)(x−3)", "⑵ 전개", nsub=2)
R(9, U, F, FN, "부정적분;적분상수", "단일개념", "하", "C=−3." + E, S, "f(x)=¼x⁴−x³−3", "식", L, L, L, N, "f'=x³−3x², f(0)=−3", "C=−3")
R(10, U, "INTEG.INDEF.TANGENT_SLOPE_POINT", "접선 기울기와 통과점으로 함수 복원", "부정적분;접선 기울기;적분상수", "단일개념",
  "하", "C=−1." + E, S, "f(x)=x²+2x−1", "식", L, L, L, N, "기울기 2x+2, (1,2) 통과", "C=−1")
build("Batch287", ROWS, 11396)
