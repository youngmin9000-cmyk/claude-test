from cfgp2 import *
import hashlib, builder
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"; MC = "5지선다"; D = "서술형"
q = [0]
HOLDG = dict(ready="HOLD", status="판독 불가(원본 >10MB·첨자/그림 글리프 소실)", trust="낮음(원문 수치 미확정)", review="HOLD-그림판독")
def SPS(QID, SRC, TAG, SEC, EXAM, MID, UNIT, BIG, FNAME, NP, POFF):
    q[0] = 0
    setup(QID=QID, SRC=SRC, SHA="미산출(10MB 초과·다운로드 불가, Drive 텍스트층 판독)", TAG=TAG, NPAGES=NP, FNAME=FNAME, UNIT=UNIT, BIG=BIG, SEC=SEC, EXAM=EXAM, MID=MID, POFF=POFF,
          BOOK="미래엔 확률과 통계 교과서", SUBJ="확률과 통계", GRADE="고2",
          KEYNOTE="정답지 미연결 — 미래엔 확률과 통계 교과서 단원 분할 PDF(본문만, 정답·해설 부록 없음)",
          NOKEYNOTE="정답지 미연결(단원 분할 PDF에 정답 부록 없음) — 독립풀이 단독",
          VISUAL="Drive read_file_content 텍스트층 판독(원본 10MB 초과로 렌더 불가); 지수·첨자 평탄화(10³→103) 문맥 복원",
          TEXTST="FULL_TEXT(Drive 텍스트층) — 지수/첨자 글리프 일부 소실(Mac 기호 대체), 그림 내용 없음",
          MEMO="미래엔 확률과 통계 교과서 단원 분할본; 본문 문제·예제·중단원 마무리 행 생성(활동 제외); ")
    builder.P = 'd' + hashlib.sha256(SRC.encode()).hexdigest()[:11]
def r(label, page, small, tid, tname, tags, combo, diff, why, fmt, ans, atype, c, d, i, trap, summ, chk, **kw):
    q[0] += 1
    R(q[0], label, page, small, tid, tname, tags, combo, diff, why + E, fmt, ans, atype, c, d, i, trap, summ, chk, **kw)
