from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h00/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h00/A.hwp','rb').read()).hexdigest()
setup(QID="A02500", SRC="11U3kEhkwo9oDnNSmOzD7mhtTibBNAl1r", SHA=SQ, TAG="DSM2I102A", N=5,
      FNAME="15개정_고등_수학Ⅱ_3-1-02_소단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I102A", EXAM="Ⅲ-1-02 부정적분의 계산 소단원평가(발전)", MID="부정적분",
      ANS_QID="A02522", ANS_SRC="1N6tNWVjsnDWjaSpuXISzuGXWtDKKYBWu", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"; MC = "5지선다"
U = "부정적분의 계산"
R(1, U, "INTEG.INDEF.TANGENT_SLOPE_MIN_VALUE", "접선 기울기·최솟값으로 함수 복원 후 구간 최댓값", "부정적분;적분상수;최대최소", "적분+최대최소",
  "중하", "C=6." + E, S, "15", "값", L, M, M, "구간 끝점 최대", "f'=2x−8, f 최솟값 −10, [−1,3]에서 최댓값", "f=x²−8x+6 → f(−1)=15")
R(2, U, "INTEG.INDEF.DOUBLE_ANTIDERIVATIVE_REMAINDER", "도함수→함수→부정적분, 나머지정리", "부정적분;적분상수;나머지정리", "적분+나머지정리",
  "중하", "f=4x³−6x²+2." + E, S, "0", "값", L, M, M, "", "f'=12x(x−1), f(0)=2, F(1)=−3, F를 x−2로 나눈 나머지", "F=x⁴−2x³+2x−4 → F(2)=0")
R(3, U, "INTEG.INDEF.SAME_DERIVATIVE_CONSTANT", "도함수가 같은 함수의 적분상수 결정", "부정적분;적분상수", "단일개념",
  "하", "F=G+C." + E, MC, "②", "선택지번호", L, L, L, "", "G=5x²+2x, F'=G', F(2)=G(1), F(1)", "C=−17 → −10", final="② (−10)", fig="설명 그림(gso)")
R(4, U, "INTEG.INDEF.DIVISIBILITY_CONDITION", "부정적분 함수가 다항식으로 나누어떨어질 조건", "부정적분;인수정리;연립방정식", "적분+인수정리",
  "중", "f(−1)=f(2)=0." + E, S, "35/4", "값", M, M, M, "", "f'=g, g'=h, g=x³−(3/2)x²−6x+a, f(0)=b, h | f, a+b", "a=13/4, b=11/2")
R(5, U, "INTEG.INDEF.PRODUCT_RULE_REVERSE", "곱의 미분 역이용 부정적분과 극한", "곱의 미분;부정적분;극한", "적분+극한",
  "중", "{(x³−1)f}'=2x−3." + E, MC, "⑤", "선택지번호", M, M, H, "x=1 대입으로 C", "(x³−1)f'+3x²f=2x−3, lim_{x→2}(x−2)/f(x)", "f=(x−2)/(x²+x+1) → 7", final="⑤ (7)")
build("Batch286", ROWS, 11391)
