# 비상교육 고등 대수(2022 개정) 계산력 강화 문제 HWP 다중 원본(소스당 2~3문항) — 문항+정답 동일 파일
import sys, os, re, json, hashlib
sys.path.insert(0, '/tmp/claude-0/-home-user-claude-test/b3c9c0b1-2d20-5f6f-a984-cabdebc0e83c/scratchpad')
import builder
from builder import COLS, save, validate
from cfgh import slim, OUT
ROWS = []; P = {}; SRCS = []
def setup(QID, SRC, FNAME, SEC, MID, UNIT):
    sha = hashlib.sha256(open(OUT + f'calc/{QID}.hwp', 'rb').read()).hexdigest()
    P.clear(); P.update(QID=QID, SRC=SRC, FNAME=FNAME, SHA=sha, SEC=SEC, MID=MID, UNIT=UNIT)
    builder.configure(SRC_ID=SRC, ZIP_SHA=sha, PDF_SHA=sha, TAG="BSDS" + QID[-3:], QID=QID, NPAGES=0, ANS_PAGES="파일 내 정답",
        FNAME=FNAME, UNIT_TITLE=UNIT, BIG="대수", SOL={0: (1, 99)}, QUICK=None)
    builder.SECTIONS[SEC] = ("[비상교육] 고등 대수 계산력 강화 문제", MID)
    SRCS.append(QID)
def R(q, small, tid, tname, tags, diff, fmt, ans, summ, chk, key=None, atype="값", nsub=1, fig="없음", final=None, combo="단일개념", c="낮음", d="낮음", i="낮음", trap="", **kw):
    if fig != "없음":
        kw.setdefault('ready', "REVIEW"); kw.setdefault('status', "독립풀이(그래프 작도 부분 시각확인 불가)"); kw.setdefault('trust', "중간(그림 미확인)"); kw.setdefault('review', "REVIEW-그래프시각확인")
    if str(kw.get('review', '')).startswith(('REVIEW', 'HOLD')) and 'ready' not in kw:
        kw['ready'] = "REVIEW"; kw.setdefault('status', "독립풀이·파일정답 대조(검토 필요)"); kw.setdefault('trust', "중간")
    kw.setdefault('trust', "높음(HWP 수식 전문+파일 정답+독립풀이 일치)"); kw.setdefault('status', "검산완료(독립풀이·파일 정답 일치)")
    r = builder.row(q, "", P['SEC'], "hwp", small, tid, tname, tags, combo, diff, tname + ". 계산량·조건해석·추론량 기준.", fmt, ans, atype, c, d, i, trap,
                    summ, chk, nsub, fig=fig, final=final,
                    visual="HWP5 렌더 불가 — olefile BodyText 파싱 텍스트+수식(EQEDIT) 스크립트 판독", key=key or ans, **kw)
    r.update({"원문항번호": f"{q:02d}", "상위원문항번호": f"{q:02d}",
        "학교/시험명": f"[비상교육] 고등 대수 계산력 강화 문제 — {P['MID']}", "출처대분류": "교과서 부교재(출판사 계산력 강화, hwp)",
        "주관기관": "비상교육", "학년": "고2", "교육과정": "2022 개정", "과목": "대수",
        "원본페이지": "hwp 1쪽(문항)+1쪽(정답)", "문항이미지/좌표": f"hwp 문항 {q:02d}",
        "해설파일 Drive ID": "", "정답표 Drive ID": P['SRC'], "해설페이지": "없음(정답만 수록)", "정답표페이지": "동일 hwp 정답 쪽",
        "해설연결상태": "동일 hwp 내 정답(해설 없음)", "텍스트추출상태": "HWP5(olefile+zlib) BodyText PARA_TEXT+EQEDIT 수식 전문",
        "중복대표여부": "원문항 1개=문항 1행(소문항은 소문항수)", "분석큐ID": P['QID'],
        "메모": f"{P['QID']} {P['FNAME']}: HWP5 원본(SHA256 {P['SHA'][:16]}…); 다중 원본 배치(소스당 2~3문항); "})
    r["_q"] = f"{P['QID']}-{q:02d}"; ROWS.append(r)
def build(name, rows, cum0):
    for r in rows:
        for c in COLS:
            v = r.get(c)
            if isinstance(v, str) and v and v[0] in '=+-@':
                r[c] = {'-': '−', '+': '＋'}.get(v[0], '(식) ' + v[0]) + v[1:]
    clean_ = [{c: r[c] for c in COLS} for r in rows]
    print(name, validate(clean_))
    p = OUT + f'Math_Question_DB_P5_Result_{name}_20261004.xlsx'
    rv = [r["_q"] for r in rows if r["production_ready"] != "YES"]
    qs = sorted({r["분석큐ID"] for r in rows})
    save(clean_, p, [("배치", name), ("방향", "P5→P4→P3→P2 역방향 신규 DB 구축(P2 구간)"), ("분석큐ID", ", ".join(qs)), ("원본파일", "[비상교육] 고등_대수 계산력 강화 문제 HWP(다중)"),
        ("원본 Drive ID", ", ".join(sorted({r['원본파일 Drive ID'] for r in rows}))), ("정답", "각 원본 hwp 내 정답"),
        ("처리범위", f"{rows[0]['_q']} ~ {rows[-1]['_q']}"), ("정규 문항행", len(rows)), ("하위문항 합계", sum(int(r['소문항수']) for r in rows)),
        ("REVIEW", ", ".join(rv) or "없음"), ("HOLD", sum(r['production_ready'] == 'HOLD' for r in rows)),
        ("역방향 누적(직전까지)", cum0), ("역방향 누적(본 배치 후)", cum0 + len(rows))])
    slim(p); os.system(f"base64 -w0 '{p}' > {OUT}{name}.b64; wc -c {OUT}{name}.b64")
