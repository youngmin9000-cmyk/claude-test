# PDF textbook variant v2 (generic subject; original bytes downloaded → SHA prefix; visual render reading)
import sys, os
sys.path.insert(0, '/tmp/claude-0/-home-user-claude-test/b3c9c0b1-2d20-5f6f-a984-cabdebc0e83c/scratchpad')
import builder
from builder import COLS, save, validate
from cfgh import slim, OUT
ROWS = []
P = {}
NOKEY = dict(ready="REVIEW", status="독립풀이(정답지 미연결)", trust="중간(독립풀이 단독; 정답지 미확보)", review="REVIEW-정답지미연결")
def setup(**kw):
    P.clear(); P.update(kw); ROWS.clear()
    builder.configure(SRC_ID=kw['SRC'], ZIP_SHA=kw['SHA'], PDF_SHA=kw['SHA'], TAG=kw['TAG'], QID=kw['QID'], NPAGES=kw['NPAGES'],
        ANS_PAGES="없음", FNAME=kw['FNAME'], UNIT_TITLE=kw['UNIT'], BIG=kw['BIG'], SOL={0: (1, 200)}, QUICK=None)
    builder.SECTIONS[kw['SEC']] = (kw['EXAM'], kw['MID'])
def R(q, label, page, small, tid, tname, tags, combo, diff, why, fmt, ans, atype, calc, cond, infer, trap, summary, check,
      nsub=1, worked=False, fig="없음", **kw):
    if worked:
        check = check + "; 교과서 본문 예제 풀이·답과 일치"
    else:
        for k, v in NOKEY.items(): kw.setdefault(k, v)
        check = check + "; " + P.get("NOKEYNOTE", "정답지 미연결(교과서 본문 PDF에 정답 부록 없음)")
    r = builder.row(q, "", P['SEC'], page, small, tid, tname, tags, combo, diff, why, fmt, ans, atype, calc, cond, infer, trap,
                    summary, check, nsub, fig=fig,
                    visual=kw.pop('visual', P.get("VISUAL", "원본 PDF PyMuPDF 110dpi 렌더 시각판독") + ("; 그림·그래프 렌더로 확인" if fig != "없음" else "")), **kw)
    r.update({"원문항번호": label, "상위원문항번호": label,
        "학교/시험명": f"{P['BOOK']} — {P['EXAM']}",
        "출처대분류": "교과서 본문(pdf)", "주관기관": P['BOOK'],
        "학년": P.get("GRADE", "고2"), "교육과정": "2015 개정", "과목": P["SUBJ"],
        "원본페이지": f"교과서 {page}쪽" + (f" (PDF {page-P['POFF']}쪽)" if P.get("POFF") else ""), "문항이미지/좌표": f"교과서 {page}쪽 {label}",
        "해설파일 Drive ID": P['SRC'] if worked else "", "정답표 Drive ID": "",
        "해설페이지": f"교과서 {page}쪽 본문 풀이" if worked else "없음", "정답표페이지": "없음",
        "해설연결상태": "본문 예제 풀이 동일 파일" if worked else P.get("KEYNOTE", "정답지 미연결"),
        "텍스트추출상태": P.get("TEXTST", "PDF 텍스트층 판독"),
        "중복대표여부": "원문항 1개=문항 1행(교과서 번호는 절마다 재시작 → 절 접두 표기)"})
    r["_q"] = q; r["_label"] = label; r["_extra"] = kw.get("memo_extra", "")
    ROWS.append(r)
def build(name, rows, cum0):
    name = name + os.environ.get('RSUF', '')
    for r in rows:
        r["메모"] = (f"{P['QID']} {name}: 교과서 PDF(SHA256 {P['SHA'][:16]}…) {P['NPAGES']}쪽; " + P.get("MEMO", "") + r.get("_extra", "") + ("; R1: 문항ID·시험ID 접두를 Drive ID 해시(d+sha256(DriveID)[:11])로 교정 — 이전판(접두=SHA 자리표시 문자열) 대체" if os.environ.get("RSUF") else ""))
    for r in rows:
        for c in COLS:
            v = r.get(c)
            if isinstance(v, str) and v and v[0] in '=+-@':
                r[c] = {'-': '−', '+': '＋'}.get(v[0], '(식) ' + v[0]) + v[1:]
    clean = [{c: r[c] for c in COLS} for r in rows]
    print(name, validate(clean))
    p = OUT + f'Math_Question_DB_P5_Result_{name}_20261004.xlsx'
    rv = [r["원문항번호"] for r in rows if r["production_ready"] != "YES"]
    save(clean, p, [("배치", name), ("방향", "P5→P4 역방향 신규 DB 구축"), ("분석큐ID", P['QID']), ("원본파일", P['FNAME']),
        ("원본 Drive ID", P['SRC']), ("원본 SHA256(pdf)", P['SHA']), ("정답지", "미연결(교과서 본문 PDF; 예제만 본문 풀이 검산)"),
        ("처리범위", f"{rows[0]['_label']} ~ {rows[-1]['_label']}"), ("정규 문항행", len(rows)), ("하위문항 합계", sum(int(r['소문항수']) for r in rows)),
        ("REVIEW", ", ".join(rv) or "없음"), ("HOLD", sum(r['production_ready'] == 'HOLD' for r in rows)),
        ("역방향 누적(직전까지)", cum0), ("역방향 누적(본 배치 후)", cum0 + len(rows))])
    slim(p); os.system(f"base64 -w0 '{p}' > {OUT}{name}.b64; wc -c {OUT}{name}.b64")
