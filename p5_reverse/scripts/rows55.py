from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h55/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h55/A.hwp','rb').read()).hexdigest()
setup(QID="A02555", SRC="1TcGXxlqxnc_CkMeuUrp9kvLUXZFm2R27", SHA=SQ, TAG="DSM2D101N", N=10,
      FNAME="15개정_고등_수학Ⅱ_2-1-01_소단원평가_기본_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D101N", EXAM="Ⅱ-1-01 미분계수 소단원평가(기본)", MID="미분계수와 도함수",
      ANS_QID="A02587", ANS_SRC="1oCpUlGqPcoJEX8WiSlmmuWQkCwNyeckx", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
AV, DC = "평균변화율", "미분계수"
R(1, AV, "DERIV.AVGRATE.PRODUCT_OF_ENDPOINTS_VIETA", "평균변화율 조건의 모든 끝점 곱(근과 계수)", "평균변화율;인수분해;근과 계수의 관계", "평균변화율+방정식",
  "하", "a²+a−1=3." + E, S, "−4", "값", L, M, L, "", "f=x³−2x+5, 1→a 평균변화율 3인 모든 a의 곱", "a²+a−4=0 → −4")
R(2, AV, "DERIV.AVGRATE.GIVEN_VALUE_FIND_INTERVAL", "평균변화율 값으로 구간 끝 결정", "평균변화율", "단일개념",
  "하", "평균변화율=h." + E, S, "3", "값", L, L, L, "", "f=x²−2x, 1→1+h 평균변화율 3일 때 h", "h=3")
R(3, AV, "DERIV.AVGRATE.FROM_DIFFERENCE_IDENTITY", "f(x)−f(1) 항등식으로 평균변화율", "평균변화율;항등식", "단일개념",
  "하", "f(2)−f(1)=7." + E, S, "7", "값", L, L, L, "", "f(x)−f(1)=x³−1일 때 1→2 평균변화율", "8−1=7")
R(4, DC, "DERIV.DERIVCOEF.DEFINITION_DIRECT", "정의에 따른 미분계수 계산", "미분계수의 정의", "단일개념",
  "하", "h+4→4." + E, S, "4", "값", L, L, L, "", "f=x²−2, lim (f(2+h)−f(2))/h", "4")
R(5, DC, "DERIV.DERIVCOEF.SYMMETRIC_INCREMENT_COMBO", "서로 다른 증분 결합 극한의 미분계수 변형", "미분계수의 정의;극한 변형", "극한+미분계수",
  "하", "(1/2+1)f'(0)." + E, MC, "①", "선택지번호", L, M, M, "", "lim (f(h)−f(−2h))/(2h)=3일 때 f'(0)", "3/2 f'(0)=3 → 2", final="① (2)")
R(6, DC, "DERIV.DERIVCOEF.SUBSTITUTION_T_EQ_X2", "치환으로 미분계수 인식", "미분계수의 정의;치환", "극한+미분계수",
  "하", "t=x² → f'(4)." + E, MC, "②", "선택지번호", L, L, L, "", "f=x²+5, lim (f(x²)−f(4))/(x²−4), x→2", "f'(4)=8", final="② (8)")
R(7, DC, "DERIV.DERIVCOEF.COMPOSITE_ARGUMENT_LIMIT", "f(x³) 형태 극한의 미분계수 변형", "미분계수의 정의;극한 변형", "극한+미분계수",
  "하", "×(x²+x+1)." + E, MC, "③", "선택지번호", L, M, M, "", "f'(1)=2일 때 lim (f(x³)−f(1))/(x−1)", "3f'(1)=6", final="③ (6)")
R(8, DC, "DERIV.DERIVCOEF.SYMMETRIC_INCREMENT_COMBO", "a+2h, a−3h 결합 극한", "미분계수의 정의;극한 변형", "극한+미분계수",
  "하", "2f'+3f'." + E, MC, "⑤", "선택지번호", L, M, M, "부호", "lim (f(a+2h)−f(a−3h))/h를 f'(a)로", "5f'(a)", final="⑤ (5f'(a))")
R(9, DC, "DERIV.DERIVCOEF.SEQUENCE_LIMIT_AS_DERIV", "수열 극한을 미분계수로 변형", "미분계수의 정의;수열의 극한;치환", "극한+미분계수",
  "중하", "h=3/n." + E, MC, "②", "선택지번호", L, M, M, "", "f'(1)=2일 때 lim n{f(1+3/n)−f(1−3/n)}", "6f'(1)=12", final="② (12)")
R(10, DC, "DERIV.DERIVCOEF.ADD_SUBTRACT_FA_TRICK", "f(1)을 더하고 빼는 극한 변형", "미분계수의 정의;극한 변형", "극한+미분계수",
  "중하", "2f(1)−f'(1)." + E, MC, "③", "선택지번호", L, M, M, "", "f(1)=3, f'(1)=1일 때 lim (x²f(1)−f(x))/(x−1)", "6−1=5", final="③ (5)")
build("Batch255", ROWS, 11107)
