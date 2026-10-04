# P1 학교 내신 기출(스캔 PDF/HWP) — 정답지 동봉 여부는 소스별(KEY 매개변수)
import sys, os, re, json, hashlib
sys.path.insert(0, '/tmp/claude-0/-home-user-claude-test/b3c9c0b1-2d20-5f6f-a984-cabdebc0e83c/scratchpad')
import builder
from builder import COLS, save, validate
from cfgh import slim, OUT
ROWS = []; P = {}
def setup(QID, SRC, FNAME, PATH, SCHOOL, YEAR, TERM, GRADE, SUBJ, CURR="2015 개정", KEY=None, KEYPAGE="", KEYSRC="", VIS="PDF 100dpi 렌더 시각판독(스캔 원안지)", TEXT="스캔 PDF(OCR 텍스트층 불완전) — 렌더 판독 확정"):
    sha = hashlib.sha256(open(OUT + PATH, 'rb').read()).hexdigest()
    P.clear(); P.update(QID=QID, SRC=SRC, FNAME=FNAME, SHA=sha, SCHOOL=SCHOOL, YEAR=YEAR, TERM=TERM, GRADE=GRADE, SUBJ=SUBJ, CURR=CURR, KEY=KEY, KEYPAGE=KEYPAGE, KEYSRC=KEYSRC, VIS=VIS, TEXT=TEXT)
    builder.configure(SRC_ID=SRC, ZIP_SHA=sha, PDF_SHA=sha, TAG="SCH" + QID[-4:], QID=QID, NPAGES=0, ANS_PAGES=KEYPAGE or "없음",
        FNAME=FNAME, UNIT_TITLE=SUBJ, BIG=SUBJ, SOL={0: (1, 99)}, QUICK=None)
    P['SEC'] = "EX" + QID[-4:]
    builder.SECTIONS[P['SEC']] = (f"{SCHOOL} {YEAR} {TERM} {GRADE} {SUBJ}", SUBJ)
NOKEY = dict(ready="REVIEW", status="독립풀이(정답지 미연결)", trust="중간(원문 렌더 판독+독립풀이; 정답지 미확보)", review="REVIEW-정답지미연결")
def R(q, page, big, mid, small, tid, tname, tags, diff, fmt, ans, summ, chk, label=None, pts="", atype="값", nsub=1, fig="없음", final=None, combo="단일개념", c="낮음", d="낮음", i="낮음", trap="", **kw):
    if not P['KEY']:
        for k, v in NOKEY.items(): kw.setdefault(k, v)
        chk = chk + "; 정답지 미연결(원안지만 수록) — 독립풀이 단독"
    if fig != "없음":
        kw['review'] = (kw.get('review', '') + ";REVIEW-그림판독").strip(';'); kw.setdefault('ready', "REVIEW")
    kw.setdefault('trust', "높음(렌더 판독+정답지+독립풀이 일치)"); kw.setdefault('status', "검산완료(독립풀이·정답지 일치)")
    r = builder.row(q, "", P['SEC'], page, small, tid, tname, tags, combo, diff, tname + ". 계산량·조건해석·추론량 기준.", fmt, ans, atype, c, d, i, trap,
                    summ, chk, nsub, fig=fig, final=final, visual=P['VIS'], key=(P['KEY'] or {}).get(q, ""), **kw)
    lab = label or f"{q}"
    r.update({"원문항번호": lab, "상위원문항번호": lab, "대단원": big, "중단원": mid, "소단원": small,
        "학교/시험명": f"{P['SCHOOL']} {P['YEAR']} {P['TERM']} {P['GRADE']} {P['SUBJ']}", "학교명": P['SCHOOL'], "출처대분류": "학교 내신 기출",
        "주관기관": P['SCHOOL'], "시행연도": P['YEAR'][:4], "학년도": P['YEAR'], "시행월": P['TERM'], "학년": P['GRADE'], "교육과정": P['CURR'], "과목": P['SUBJ'],
        "배점": pts or "미표기", "원본페이지": f"p{page}", "문항이미지/좌표": f"p{page} 문항 {lab}",
        "해설파일 Drive ID": "", "정답표 Drive ID": (P['KEYSRC'] or P['SRC']) if P['KEY'] else "", "해설페이지": "없음", "정답표페이지": P['KEYPAGE'] or "없음",
        "해설연결상태": (("동반 정답자료 연결: " + P['KEYSRC']) if P['KEYSRC'] else "동일 파일 정답표") if P['KEY'] else "정답지 미연결(원안지만)", "텍스트추출상태": P['TEXT'],
        "중복대표여부": "원문항 1개=문항 1행", "분석큐ID": P['QID'],
        "메모": f"{P['QID']} {P['FNAME']}: 원본 SHA256 {P['SHA'][:16]}…; P1 학교기출(P5REV 스트림 P1 구간); "})
    r["_q"] = f"{P['QID']}-{lab}"; ROWS.append(r)
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
    save(clean_, p, [("배치", name), ("방향", "P5→P4→P3→P2→P1 역방향 신규 DB 구축(P1 구간)"), ("분석큐ID", ", ".join(qs)), ("원본파일", " / ".join(sorted({r['원본파일명'] for r in rows}))),
        ("원본 Drive ID", ", ".join(sorted({r['원본파일 Drive ID'] for r in rows}))), ("정답", "소스별(학교 원안지는 정답 미수록 다수)"),
        ("처리범위", f"{rows[0]['_q']} ~ {rows[-1]['_q']}"), ("정규 문항행", len(rows)), ("하위문항 합계", sum(int(r['소문항수']) for r in rows)),
        ("REVIEW", ", ".join(rv) or "없음"), ("HOLD", sum(r['production_ready'] == 'HOLD' for r in rows)),
        ("역방향 누적(직전까지)", cum0), ("역방향 누적(본 배치 후)", cum0 + len(rows))])
    slim(p); os.system(f"base64 -w0 '{p}' > {OUT}{name}.b64; wc -c {OUT}{name}.b64")
