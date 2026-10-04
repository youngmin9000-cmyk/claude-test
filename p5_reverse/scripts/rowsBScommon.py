from cfgp2 import *
import hashlib, builder
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"; MC = "5지선다"; D = "서술형"
q = [0]
HOLDG = dict(ready="HOLD", status="판독 불가(원본 >10MB·그림 내용 텍스트층 부재)", trust="낮음(그림 조건 미확정)", review="HOLD-그림판독")
NUMG = "번호 배치 추정(2단 조판 텍스트층 순서 뒤섞임)"
def SBS(QID, SRC, TAG, SEC, EXAM, MID, UNIT, BIG, FNAME, NP):
    q[0] = 0
    setup(QID=QID, SRC=SRC, SHA="미산출(17MB·10MB 초과 다운로드 불가, Drive 텍스트층 판독)", TAG=TAG, NPAGES=NP, FNAME=FNAME, UNIT=UNIT, BIG=BIG, SEC=SEC, EXAM=EXAM, MID=MID, POFF=0,
          BOOK="비상 확률과 통계 교과서", SUBJ="확률과 통계", GRADE="고2",
          KEYNOTE="정답지 미연결 — 교과서 정답과 해설(141~155쪽 표기) 존재하나 Drive 텍스트층이 77쪽에서 절단되어 판독 불가",
          NOKEYNOTE="정답지 미연결(정답과 해설 부록 판독 불가: 텍스트층 절단·원본 10MB 초과) — 독립풀이 단독",
          VISUAL="Drive read_file_content 텍스트층 판독(원본 17MB로 렌더 불가); 지수 기호 치환(!@#$%^=¹~⁶, ?=계승) 문맥 복원",
          TEXTST="PARTIAL_TEXT(Drive 텍스트층 55,702자, 교과서 10~33·36~69·72~77·128~135쪽만 포함, 77쪽 이후 절단) — 그림 내용 없음",
          MEMO="비상 확률과 통계 교과서 전권 PDF; 판독 가능 범위 본문 문제·예제·수학 기르기·중단원/대단원·수학 익힘책 행 생성(개념 열기·준비·활동·문제 만들기 제외); ")
    builder.P = 'b' + hashlib.sha256(SRC.encode()).hexdigest()[:11]
def r(label, page, small, tid, tname, tags, combo, diff, why, fmt, ans, atype, c, d, i, trap, summ, chk, **kw):
    q[0] += 1
    R(q[0], label, page, small, tid, tname, tags, combo, diff, why + E, fmt, ans, atype, c, d, i, trap, summ, chk, **kw)
