from cfgp2 import *
import hashlib
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"; MC = "5지선다"; D = "서술형"
q = [0]
def SM2(QID, SRC, pdf, TAG, SEC, EXAM, MID, UNIT, BIG, FNAME, POFF):
    sha = hashlib.sha256(open(OUT + pdf, 'rb').read()).hexdigest()
    import pymupdf
    n = len(pymupdf.open(OUT + pdf))
    q[0] = 0
    setup(QID=QID, SRC=SRC, SHA=sha, TAG=TAG, NPAGES=n, FNAME=FNAME, UNIT=UNIT, BIG=BIG, SEC=SEC, EXAM=EXAM, MID=MID, POFF=POFF,
          BOOK="미래엔 수학Ⅱ 교과서", SUBJ="수학Ⅱ", GRADE="고2",
          KEYNOTE="정답지 미연결 — 미래엔 수학Ⅱ 교과서 단원 분할 PDF(본문만, 정답·해설 부록 없음)",
          NOKEYNOTE="정답지 미연결(단원 분할 PDF에 정답 부록 없음) — 독립풀이 단독",
          VISUAL="원본 PDF PyMuPDF 110dpi 렌더 시각판독(텍스트층 CID 폰트 깨짐·숫자 소실로 텍스트 불가)",
          TEXTST="NO_TEXT_RECHECK: PDF 텍스트층 CID 폰트 매핑 깨짐(라틴 문자 시프트·숫자 소실) → 원본 렌더 시각판독",
          MEMO=f"미래엔 수학Ⅱ 교과서 단원 분할본; 본문 문제·예제·중단원 마무리 행 생성(준비하기·생각열기·함께하기·생각넓히기 활동 제외, 기존 A02486 관례와 동일); ")
def r(label, page, small, tid, tname, tags, combo, diff, why, fmt, ans, atype, c, d, i, trap, summ, chk, **kw):
    q[0] += 1
    R(q[0], label, page, small, tid, tname, tags, combo, diff, why + E, fmt, ans, atype, c, d, i, trap, summ, chk, **kw)
