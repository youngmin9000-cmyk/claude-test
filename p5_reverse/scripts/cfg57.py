import sys, os, zipfile; sys.path.insert(0, '/tmp/claude-0/-home-user-claude-test/b3c9c0b1-2d20-5f6f-a984-cabdebc0e83c/scratchpad')
import builder
from builder import COLS, save, validate
PDF_SHA = "f1ab7e02b9769c3803b8618adf8b0aaf2c3cdf7e874b4fc791e823e99fa61526"
SOL58={34:(1,18),35:(19,33),36:(34,61),37:(62,90),38:(91,114),39:(115,116)}
builder.configure(SRC_ID="1e7eJqaJyLigKBM8m4iw5_klIoku4ARIy", ZIP_SHA=PDF_SHA, PDF_SHA=PDF_SHA,
    TAG="CJGEOB", QID="A02657", NPAGES=39, ANS_PAGES="34~39",
    FNAME="[100발100중 고등수학 기출] 천재교과서(교과서)_3. 도형의 방정식 예제, 연습, 단원평가문제.pdf",
    UNIT_TITLE="Ⅲ. 도형의 방정식", BIG="Ⅲ. 도형의 방정식",
    SOL=SOL58, QUICK=None)
SRC_ID = builder.SRC_ID
S = {"S1": ("1. 두 점 사이의 거리", "두 점 사이의 거리"), "S1C": ("1. 스스로 확인하기", "두 점 사이의 거리"), "S2": ("2. 선분의 내분과 외분", "선분의 내분과 외분"), "S2C": ("2. 스스로 확인하기", "선분의 내분과 외분"), "S3": ("3. 직선의 방정식", "직선의 방정식"), "S3C": ("3. 스스로 확인하기", "직선의 방정식"), "S4": ("4. 두 직선의 평행과 수직", "두 직선의 평행과 수직"), "S4C": ("4. 스스로 확인하기", "두 직선의 평행과 수직"), "S5": ("5. 원의 방정식", "원의 방정식"), "S5C": ("5. 스스로 확인하기", "원의 방정식"), "S6": ("6. 원과 직선의 위치 관계", "원과 직선의 위치 관계"), "S6C": ("6. 스스로 확인하기", "원과 직선의 위치 관계"), "S7": ("7. 평행이동", "평행이동"), "S7C": ("7. 스스로 확인하기", "평행이동"), "S8": ("8. 대칭이동", "대칭이동"), "S8C": ("8. 스스로 확인하기", "대칭이동"), "MIX": ("스스로 마무리하기(대단원)", "대단원 종합평가")}
UNITNO = {"S1": 1, "S2": 2, "S3": 3, "S4": 4, "S5": 5, "S6": 6, "S7": 7, "S8": 8}
builder.SECTIONS.update(S)
OUT = '/tmp/claude-0/-home-user-claude-test/b3c9c0b1-2d20-5f6f-a984-cabdebc0e83c/scratchpad/'
ROWS = []

def R(q, sec, page, label, small, tid, tname, tags, combo, diff, why, fmt, ans, atype, calc, cond, infer, trap,
      summary, check, nsub=1, keymatch=True, **kw):
    sp = builder.SOL_PAGE[q]
    if keymatch: check = check + f"; 동일 PDF {sp}쪽 정답 일치"
    r = builder.row(q, "", sec, page, small, tid, tname, tags, combo, diff, why, fmt, ans, atype, calc, cond, infer, trap,
                    summary, check, nsub, **kw)
    base = sec.rstrip("C")
    lab = (f"{UNITNO[base]}단원 " if base in UNITNO else "") + label
    exam_sfx = S[sec][0]
    r.update({
        "원문항번호": lab, "상위원문항번호": lab,
        "학교/시험명": f"백발백중 천재교과서 교과서문제풀이(고1 1학기 기말대비) Ⅲ. 도형의 방정식 — {exam_sfx}",
        "주관기관": "천재교육 수학(상) 교과서 기반 · (주)백발백중(100bal) 재편집",
        "과목": "수학(상)",
        "해설페이지": f"{sp}(정답·풀이)", "해설연결상태": "동일 PDF 정답편(34~39쪽) 연결", "정답표페이지": str(sp),
        "텍스트추출상태": "PyMuPDF 본문 추출(수식객체 텍스트 소실) → 원본 130dpi 렌더 시각판독으로 수식 확정",
        "중복대표여부": "원문항 1개=문항 1행(따라하기는 예제의 소문항으로 병합)",
        "유사문항그룹ID": tid,
    })
    r["_q"] = q
    r["_extra"] = kw.get("memo_extra", "")
    ROWS.append(r)

def memo_fix(r, batch):
    r["메모"] = (f"A02657 {batch}: 단일 PDF(SHA256 {PDF_SHA[:16]}…) 39쪽; 순번 Q{r['_q']:03d}; "
                 "근사중복 검토후보: A02667(03 도형의 방정식 천재-류 137제, 동일 교과서 문항 재편집) — 자동 병합 금지; "
                                  f"" + r.get("_extra", ""))

def slim(p):
    import re
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
    for r in rows: memo_fix(r, name)
    clean = [{c: r[c] for c in COLS} for r in rows]
    print(name, validate(clean))
    qs = [r["_q"] for r in rows]
    p = OUT + f'Math_Question_DB_P5_Result_{name}_20261004.xlsx'
    rv = [r["원문항번호"] for r in rows if r["production_ready"] != "YES"]
    save(clean, p, [("배치", name), ("방향", "P5→P4 역방향 신규 DB 구축"), ("분석큐ID", "A02657"), ("원본파일", builder.CFG["FNAME"]),
        ("원본 Drive ID", SRC_ID), ("원본 SHA256(pdf)", PDF_SHA), ("처리범위", f"순번 Q{min(qs):03d}~Q{max(qs):03d} / PDF {rows[0]['원본페이지']}~{rows[-1]['원본페이지']}쪽"),
        ("정규 문항행", len(rows)), ("하위문항 합계", sum(int(r['소문항수']) for r in rows)), ("정답 연결", "동일 PDF 34~39쪽 정답·풀이"),
        ("REVIEW", ", ".join(rv) or "없음"), ("HOLD", sum(r['production_ready'] == 'HOLD' for r in rows)),
        ("역방향 누적(직전까지)", cum0), ("역방향 누적(본 배치 후)", cum0 + len(rows))])
    slim(p); os.system(f"base64 -w0 '{p}' > {OUT}{name}.b64; wc -c {OUT}{name}.b64")
    import openpyxl; wb = openpyxl.load_workbook(p); print('reload', [(ws.title, ws.max_row) for ws in wb])
