from cfgp import *
KN = "정답지 미연결 — 본 파일(10MB 초과)은 Drive 텍스트로 PDF 1~122쪽만 판독, 정답부(뒤쪽) 판독 불가"
MEMO = "미래엔 수학(상) 전체본; 판독 가능 범위 PDF 1~122쪽(교과서 10~131쪽)만 행 생성, PDF 123~341쪽 HOLD(접근 한계); Ⅲ-2 이후는 A02487~A02489 분할본과 중복 — "
def S86(tag, sec, exam, mid, unit, big):
    setup(QID="A02486", SRC="1rQ5Xzakn0Q6misoDr7Iboy0_du_dfeGo", SHA="미산출(10MB 초과·다운로드 불가, Drive 텍스트층 판독)", TAG=tag, NPAGES=341,
          FNAME="미래엔_고1-수학-교과서.pdf (미래엔 2015 개정 수학(상) 전체본, 341쪽)", UNIT=unit, BIG=big, SEC=sec, EXAM=exam, MID=mid,
          KEYNOTE=KN, MEMO=MEMO, POFF=9)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"; MC = "5지선다"; D = "서술형"
q = [0]
def r(label, page, small, tid, tname, tags, combo, diff, why, fmt, ans, atype, c, d, i, trap, summ, chk, **kw):
    q[0] += 1
    R(q[0], label, page, small, tid, tname, tags, combo, diff, why + E, fmt, ans, atype, c, d, i, trap, summ, chk, **kw)
