import sys, os, zipfile, re
sys.path.insert(0, '/tmp/claude-0/-home-user-claude-test/b3c9c0b1-2d20-5f6f-a984-cabdebc0e83c/scratchpad')
import builder
from builder import COLS, save, validate
OUT = '/tmp/claude-0/-home-user-claude-test/b3c9c0b1-2d20-5f6f-a984-cabdebc0e83c/scratchpad/'
ROWS = []
P = {}
def setup(**kw):
    P.clear(); P.update(kw); ROWS.clear()
    n = kw['N']
    builder.configure(SRC_ID=kw['SRC'], ZIP_SHA=kw['SHA'], PDF_SHA=kw['SHA'], TAG=kw['TAG'], QID=kw['QID'], NPAGES=0,
        ANS_PAGES="동반 정답 hwp", FNAME=kw['FNAME'], UNIT_TITLE=kw['UNIT'], BIG=kw['BIG'], SOL={0: (1, n)}, QUICK=None)
    builder.SECTIONS[kw['SEC']] = (kw['EXAM'], kw['MID'])
def R(q, small, tid, tname, tags, combo, diff, why, fmt, ans, atype, calc, cond, infer, trap, summary, check,
      nsub=1, keymatch=True, fig="없음", **kw):
    pt = kw.pop('_pt', "미표기")
    if keymatch: check = check + f"; 동반 정답 hwp({P['ANS_QID']}) 답 일치"
    r = builder.row(q, "", P['SEC'], "hwp", small, tid, tname, tags, combo, diff, why, fmt, ans, atype, calc, cond, infer, trap,
                    summary, check, nsub, fig=fig,
                    visual=kw.pop('visual', "HWP5 렌더 불가 — olefile BodyText 파싱 텍스트+수식(EQEDIT) 스크립트 판독" + ("; 그림(gso) 시각확인 불가" if fig != "없음" else "")), **kw)
    r.update({"원문항번호": str(q), "상위원문항번호": str(q),
        "학교/시험명": f"두산(동아) 15개정 수학Ⅱ 평가자료 — {P['EXAM']}",
        "출처대분류": "교과서 출판사 평가자료(hwp)", "주관기관": P.get('PUB', "두산동아 수학Ⅱ 교과서 출판사 문제 모음"),
        "학년": "고2", "교육과정": "2015 개정", "과목": "수학Ⅱ",
        "원본페이지": "hwp(쪽 정보 없음)", "문항이미지/좌표": "hwp 본문 문항 " + str(q),
        "해설파일 Drive ID": P['ANS_SRC'], "정답표 Drive ID": P['ANS_SRC'], "해설페이지": "동반 정답 hwp 문항 " + str(q), "정답표페이지": "동반 정답 hwp",
        "해설연결상태": f"동반 정답·해설 hwp {P['ANS_QID']}({P['ANS_SRC']}) 연결 — 동반파일은 독립 행 미생성",
        "텍스트추출상태": "HWP5(olefile+zlib) BodyText 레코드 파싱: PARA_TEXT + EQEDIT 수식 스크립트 순서 복원",
        "배점": pt, "중복대표여부": "원문항 1개=문항 1행"})
    r["_q"] = q; r["_extra"] = kw.get("memo_extra", "")
    ROWS.append(r)
def slim(p):
    zin = zipfile.ZipFile(p); t = p + '.tmp'; zout = zipfile.ZipFile(t, 'w', zipfile.ZIP_DEFLATED, compresslevel=9)
    for i in zin.infolist():
        n = i.filename
        if n.startswith('docProps/') or n.startswith('xl/theme/'): continue
        d = zin.read(n)
        if n == '[Content_Types].xml': d = re.sub(r'<Override PartName="/(docProps|xl/theme)[^>]*/>', '', d.decode()).encode()
        if n == '_rels/.rels': d = re.sub(r'<Relationship [^>]*Target="/?docProps[^>]*/>', '', d.decode()).encode()
        if n == 'xl/_rels/workbook.xml.rels': d = re.sub(r'<Relationship [^>]*Target="[^"]*theme[^"]*"[^>]*/>', '', d.decode()).encode()
        zout.writestr(n, d)
    zout.close(); zin.close(); os.replace(t, p)
def build(name, rows, cum0):
    for r in rows:
        r["메모"] = (f"{P['QID']} {name}: HWP5 원본(SHA256 {P['SHA'][:16]}…); 동반 정답 {P['ANS_QID']}({P['ANS_SRC']}, SHA {P['ANS_SHA'][:16]}…); " + r.get("_extra", ""))
    clean = [{c: r[c] for c in COLS} for r in rows]
    print(name, validate(clean))
    p = OUT + f'Math_Question_DB_P5_Result_{name}_20261004.xlsx'
    rv = [r["원문항번호"] for r in rows if r["production_ready"] != "YES"]
    save(clean, p, [("배치", name), ("방향", "P5→P4 역방향 신규 DB 구축"), ("분석큐ID", P['QID']), ("원본파일", P['FNAME']),
        ("원본 Drive ID", P['SRC']), ("원본 SHA256(hwp)", P['SHA']), ("동반 정답 hwp", f"{P['ANS_QID']} {P['ANS_SRC']}"),
        ("처리범위", f"문항 {rows[0]['_q']}~{rows[-1]['_q']}"), ("정규 문항행", len(rows)), ("하위문항 합계", sum(int(r['소문항수']) for r in rows)),
        ("REVIEW", ", ".join(rv) or "없음"), ("HOLD", sum(r['production_ready'] == 'HOLD' for r in rows)),
        ("역방향 누적(직전까지)", cum0), ("역방향 누적(본 배치 후)", cum0 + len(rows))])
    slim(p); os.system(f"base64 -w0 '{p}' > {OUT}{name}.b64; wc -c {OUT}{name}.b64")
