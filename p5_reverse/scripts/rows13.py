from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h13/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h13/A.hwp','rb').read()).hexdigest()
setup(QID="A02613", SRC="1kkhZME5I4sKxZfHGgLji0WlkPQgZw4xo", SHA=SQ, TAG="DSM2D2042B", N=15,
      FNAME="15개정_고등_수학Ⅱ_2-2-04-2_소단원평가_기초_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D2042B", EXAM="Ⅱ-2-04-2 방정식과 부등식의 활용 소단원평가(기초)", MID="도함수의 활용",
      ANS_QID="A02612", ANS_SRC="1UEBsCW--KAJjsJDgVS7AecgAgIqgLg9u", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, PF = "서술형(단답)", "서술형(증명)"
EQ = "방정식과 부등식에의 활용"
def NR(q, eq, n, deg="삼차", nsub=1, ans=None, chk=""):
    R(q, EQ, f"DERIV.EQ.ROOT_COUNT_{'CUBIC' if deg=='삼차' else 'QUARTIC'}_BY_EXTREMA", f"{deg}방정식 실근 개수(극값 부호)", "방정식의 실근;극값;증가와 감소", "방정식+극값",
      "하", "극값 부호로 x축 교점 개수." + E, S, ans or str(n), "개수" if nsub == 1 else "개수(소문항별)", L, L, L, "중근(극값=0) 개수", f"{eq}의 서로 다른 실근 개수", chk, nsub=nsub)
def PRF(q, ineq, dom, fac, tid, tname, nsub=1, summ=None):
    R(q, EQ, tid, tname, "부등식의 증명;최솟값;증가와 감소", "부등식+최소",
      "하" if nsub == 1 else "중하", "차함수 최솟값 ≥ 0." + E, PF, "풀이 참조(증명)", "증명", L, M, M, "구간 x≥0 제한", summ or f"{dom} {ineq} 증명",
      f"차함수 인수분해 {fac} ≥ 0 확인 — 해설(최솟값 0) 일치", nsub=nsub)
NR(1, "⑴ x³−3x+6=0 ⑵ x⁴−2x²−4=0", None, nsub=2, ans="⑴ 1 ⑵ 2", chk="⑴ 극대 8, 극소 4 >0 → 1 ⑵ 극소 −5, 극대 −4 → 2")
NR(2, "x³+3x²−9x−12=0", 3, chk="극대 15, 극소 −17 → 3")
NR(3, "2x⁴−4x²−1=0", 2, deg="사차", chk="극소 −3, 극대 −1 → 2")
PRF(4, "x³ ≥ 3x²−4", "x≥0에서", "(x−2)²(x+1)", "DERIV.INEQ.PROOF_CUBIC_NONNEG_DOMAIN", "x≥0에서 삼차부등식 증명")
PRF(5, "", "", "⑴ (x−1)²(x+2) ⑵ (x−2)²(3x²−4x+2)", "DERIV.INEQ.PROOF_CUBIC_AND_QUARTIC", "삼차(x≥0)·사차(전체) 부등식 증명", nsub=2,
    summ="⑴ x≥0에서 x³≥3x−2 ⑵ 모든 실수에서 3x⁴+30x²+8≥16x³+24x 증명")
NR(6, "x³−3x²+3=0", 3, chk="극대 3, 극소 −1 → 3")
NR(7, "x³−3x²−9x+24=0", 3, chk="극대 29, 극소 −3 → 3")
R(8, EQ, "DERIV.EQ.THREE_ROOTS_PARAM_RANGE", "서로 다른 세 실근 조건(상수 분리)", "방정식의 실근;극값;상수 분리", "방정식+극값",
  "중하", "극솟값<a<극댓값." + E, S, "0<a<1", "범위", L, M, L, "", "2x³+3x²=a가 서로 다른 세 실근", "극대 f(−1)=1, 극소 f(0)=0 → 0<a<1")
R(9, EQ, "DERIV.EQ.THREE_ROOTS_PARAM_RANGE", "서로 다른 세 실근 조건(상수 분리)", "방정식의 실근;극값;상수 분리", "방정식+극값",
  "중하", "극솟값<a<극댓값." + E, S, "−4<a<0", "범위", L, M, L, "", "x³+6x²+9x−a=0이 서로 다른 세 실근", "극대 f(−3)=0, 극소 f(−1)=−4 → −4<a<0")
PRF(10, "x⁴+2x² ≥ 8x−5", "모든 실수에서", "(x−1)²(x²+2x+5)", "DERIV.INEQ.PROOF_QUARTIC_ALL_REAL", "모든 실수에서 사차부등식 증명")
NR(11, "x³+3x²−9x+3=0", 3, chk="극대 30, 극소 −2 → 3")
NR(12, "x³−3x−2=0", 2, chk="극대 f(−1)=0(중근), 극소 −4 → 2")
NR(13, "x⁴−2x²−1=0", 2, deg="사차", chk="극소 −2, 극대 −1 → 2")
PRF(14, "1−3x² ≥ −2x³", "x≥0에서", "(x−1)²(2x+1)", "DERIV.INEQ.PROOF_CUBIC_NONNEG_DOMAIN", "x≥0에서 삼차부등식 증명")
PRF(15, "x⁴+4x+3 ≥ 0", "모든 실수에서", "(x+1)²(x²−2x+3)", "DERIV.INEQ.PROOF_QUARTIC_ALL_REAL", "모든 실수에서 사차부등식 증명")
build("Batch235", ROWS[:10], 10944)
build("Batch236", ROWS[10:], 10954)
