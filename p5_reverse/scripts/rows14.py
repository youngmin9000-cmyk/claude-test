from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h14/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h14/A.hwp','rb').read()).hexdigest()
setup(QID="A02514", SRC="1s_h7Uj__Caq74d1VR5rLt6q3vPP9mnLQ", SHA=SQ, TAG="DSM2I1MN", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-1_중단원평가_기본_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I1MN", EXAM="Ⅲ-1 부정적분 중단원평가(기본)", MID="부정적분",
      ANS_QID="A02513", ANS_SRC="1yQhJcsL4Iw6ybXnCPKYkqfCQp4OBpjdQ", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
MC = "5지선다"
U = "부정적분"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
R(1, U, "INTEG.INDEF.DERIVATIVE_OF_INDEFINITE", "부정적분 함수의 미분계수", "부정적분과 미분", "단일개념",
  "하", "f'=피적분함수." + E, MC, "③", "선택지번호", L, L, L, "", "f=∫(2x−1)⁴(x+2)dx, f'(1)", "1·3=3", final="③ (3)")
R(2, U, "INTEG.INDEF.COMBINE_RATIONAL_TO_POLY", "부정적분 결합 후 인수분해", "부정적분 선형성;인수분해", "단일개념",
  "하", "(x³−1)/(x−1)." + E, MC, "①", "선택지번호", L, L, L, "", "∫x³/(x−1)dx−∫1/(x−1)dx", "∫(x²+x+1)", final="① (⅓x³+½x²+x+C)")
R(3, U, "INTEG.INDEF.LINEAR_FROM_IDENTITY", "부정적분 관계와 항등식으로 일차함수 결정", "부정적분과 미분;항등식", "단일개념",
  "중하", "a=1, b=−4." + E, MC, "①", "선택지번호", L, M, M, "", "일차 f, g=∫xf(x+1)dx, f'+g'=x²−3x+1, f(2)", "f=x−4 → −2", final="① (−2)")
R(4, U, "INTEG.INDEF.F_AND_ANTIDERIVATIVE_RELATION", "f와 부정적분 F의 관계식 미분", "부정적분;미분;항등식", "단일개념",
  "중하", "f'=3x−4." + E, MC, "②", "선택지번호", L, M, M, "", "F=xf−x³+2x²−3, f(0)=1, f(2)", "f=(3/2)x²−4x+1 → −1 (검산 F'=f)", final="② (−1)")
R(5, U, "INTEG.INDEF.TANGENT_SLOPE_POINT", "접선 기울기와 통과점으로 함수 복원", "부정적분;적분상수", "단일개념",
  "하", "C=−13." + E, MC, "②", "선택지번호", L, L, L, "", "기울기 6x²−2x+2, (2,3) 통과, f(1)", "−10", final="② (−10)")
R(6, U, "INTEG.INDEF.EXTREMA_FROM_DERIVATIVE", "도함수와 극솟값으로 함수 복원, 극댓값", "부정적분;극값", "적분+극값",
  "중하", "C=17." + E, MC, "④", "선택지번호", L, M, M, "", "∫f'dx=x³−3x²−9x+C, 극솟값 −10, 극댓값", "f(−1)=22", final="④ (22)")
R(7, U, "INTEG.INDEF.CUBIC_FROM_DERIVATIVE_GRAPH", "도함수 그래프로 삼차함수 복원", "부정적분;그래프;적분상수", "그래프+적분",
  "중하", "f'=x(x−2)." + E, MC, "①", "선택지번호", L, M, M, "그래프 판독", "f' 그래프, f(0)=1, f(3)", "해설 판독 근 0,2, f'(1)=−1 → f(3)=1 (그림 의존)", final="① (1)", **G)
R(8, U, "INTEG.INDEF.DEFINITION_DERIVATIVE_OF_PRODUCT", "∫h=fg → h=(fg)'", "부정적분 정의;곱의 미분", "단일개념",
  "하", "h=6x²−2x+2." + E, MC, "③", "선택지번호", L, L, L, "", "f=x²+1, g=2x−1, ∫h dx=fg, h'(1)", "12−2=10", final="③ (10)")
R(9, U, "INTEG.INDEF.COMBINE_SQUARES_DIFF", "제곱 차 결합 후 부정적분 계수", "부정적분 선형성;곱셈공식", "단일개념",
  "하", "4x³+4x." + E, MC, "③", "선택지번호", L, L, L, "", "∫(x²+x+1)²−∫(x²−x+1)²=ax⁴+bx²+C, a+b", "1+2=3", final="③ (3)")
R(10, U, "INTEG.INDEF.ABS_DERIVATIVE_PIECEWISE", "절댓값 도함수의 구간별 부정적분", "절댓값;구간별 함수;연속", "절댓값+적분",
  "중하", "C₁=−1, C₂=1." + E, MC, "④", "선택지번호", L, M, M, "연속 조건", "f'=2|x−1|, f(1)=0, f(−1)+f(2)", "−4+1=−3", final="④ (−3)")
build("Batch289", ROWS, 11411)
