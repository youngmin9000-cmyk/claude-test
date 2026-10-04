from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h15/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h15/A.hwp','rb').read()).hexdigest()
setup(QID="A02515", SRC="1SY0WFSOS9OEfAYnB8YX54FdOatMRriUN", SHA=SQ, TAG="DSM2I1MA", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-1_중단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I1MA", EXAM="Ⅲ-1 부정적분 중단원평가(발전)", MID="부정적분",
      ANS_QID="(LOCK 범위 밖 companion A, read-only)", ANS_SRC="1Z3N2xElXH3S-qpEe-IpMTyOLL-LGVDwi", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
MC = "5지선다"
U = "부정적분"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
R(1, U, "INTEG.INDEF.QUARTIC_FROM_DERIVATIVE_CONDITIONS", "도함수 조건으로 사차함수 복원", "부정적분;적분상수;항등식", "적분+조건",
  "중", "f'=x³−3x²+2." + E, MC, "⑤", "선택지번호", M, M, M, "", "도함수 조건으로 f 결정 후 함숫값", "f=¼x⁴−x³+2x+1 → 9/4", final="⑤ (9/4)")
R(2, U, "INTEG.INDEF.F_AND_ANTIDERIVATIVE_RELATION", "부정적분 관계식으로 삼차함수 결정", "부정적분;미분;항등식", "단일개념",
  "중하", "f=x³−1." + E, MC, "②", "선택지번호", L, M, M, "", "관계식 미분 → f 결정, 함숫값", "f=x³−1 → −9", final="② (−9)")
R(3, U, "INTEG.INDEF.TWO_FUNCS_SUM_DIFF_CONDITIONS", "두 함수의 합·차 부정적분 조건", "부정적분 선형성;연립", "적분+연립",
  "중", "f=2x²−3x+1, g=−x²+2x+2." + E, "서술형(단답)", "9", "값", M, M, M, "", "(f+g)', (f−g)' 조건과 함숫값으로 f,g 결정", "f=2x²−3x+1, g=−x²+2x+2 → 9", fig="조건 상자(gso)")
R(4, U, "INTEG.INDEF.CONSTANT_FROM_EXTREMUM_CASES", "극값 조건으로 적분상수 두 경우", "부정적분;극값;적분상수", "적분+극값",
  "중", "C=−7 또는 20." + E, MC, "⑤", "선택지번호", M, M, M, "경우 누락", "도함수와 극값 조건, 적분상수 후보", "C=−7, 20 → 13", final="⑤ (13)")
R(5, U, "INTEG.INDEF.TRUTH_SET_FROM_DEFINITION", "부정적분 정의 기반 ㄱㄴㄷ 판정", "부정적분 정의;미분", "보기판정",
  "중", "f=x²+x." + E, MC, "③", "선택지번호", L, M, M, "ㄷ 함정", "보기 ㄱ,ㄴ,ㄷ 참거짓", "f=x²+x, f(1)=2 → ㄷ 거짓", final="③ (ㄱ,ㄴ)")
R(6, U, "INTEG.INDEF.PIECEWISE_DERIVATIVE_ROOT_COUNT", "구간별 도함수로 연속함수 복원 후 근의 개수", "부정적분;연속성;방정식 실근", "적분+연속+그래프",
  "중상", "f=x+2/x²/−x+2." + E, "서술형(단답)", "4", "개수", M, H, M, "연속 조건", "구간별 f' 와 연속성으로 f 복원, 방정식 실근 개수", "구간별 f 결정 → 4개", fig="해설 설명 그래프(gso)")
R(7, U, "INTEG.INDEF.APPLIED_PROFIT_MAX", "한계이익 적분→이익 함수 최댓값(실생활)", "부정적분;최대최소;실생활", "적분+최대",
  "중", "x=10에서 최대." + E, "서술형(단답)", "115/3 만원", "값", M, M, M, "단위", "변화율 적분으로 이익함수 복원, 최댓값", "f=−x³/15+x²+5, x=10 → 115/3")
R(8, U, "INTEG.INDEF.CUBIC_FROM_DERIVATIVE_CONDITIONS", "도함수 조건으로 삼차함수 결정", "부정적분;적분상수", "단일개념",
  "중하", "f=x³+2x²+4." + E, MC, "②", "선택지번호", L, M, M, "", "조건으로 f 결정 후 값", "f=x³+2x²+4 → 7", final="② (7)")
R(9, U, "INTEG.INDEF.PIECEWISE_FROM_DERIVATIVE_GRAPH", "도함수 그래프(구간별)로 연속함수 복원", "부정적분;연속성;그래프", "그래프+적분",
  "중상", "f'=2/−2/2x−4." + E, MC, "③", "선택지번호", M, H, M, "그래프 판독", "f' 그래프와 연속성, 함숫값", "해설 판독 f'=2/−2/2x−4 → 0 (그림 의존)", final="③ (0)", **G)
R(10, U, "INTEG.INDEF.CUBIC_FROM_FUNCTIONAL_IDENTITY", "항등식 조건으로 삼차함수 결정", "부정적분;항등식", "적분+항등식",
  "중", "f=x³/3+x+2." + E, MC, "④", "선택지번호", M, M, M, "", "부정적분 항등식에서 f 결정 후 값", "f=x³/3+x+2 → 14", final="④ (14)")
build("Batch291", ROWS, 11426)
