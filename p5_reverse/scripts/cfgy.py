# 용문아 수학방 미래엔 교과서 편집본 HWP (문항+빠른정답+해설 동일 파일)
import sys, os, re, json, hashlib
sys.path.insert(0, '/tmp/claude-0/-home-user-claude-test/b3c9c0b1-2d20-5f6f-a984-cabdebc0e83c/scratchpad')
import builder
from builder import COLS, save, validate
from cfgh import slim, OUT
ROWS = []; P = {}
def clean(s):
    s = s.replace('⟦','').replace('⟧','').replace('[gso]','').replace('lim_{n →  inf}','lim').replace('lim  _{n →  inf}','lim')
    s = re.sub(r'\s+',' ', s).strip()
    return s
def setup(**kw):
    P.clear(); P.update(kw); ROWS.clear()
    builder.configure(SRC_ID=kw['SRC'], ZIP_SHA=kw['SHA'], PDF_SHA=kw['SHA'], TAG=kw['TAG'], QID=kw['QID'], NPAGES=0,
        ANS_PAGES="파일 내 빠른 정답", FNAME=kw['FNAME'], UNIT_TITLE=kw['UNIT'], BIG=kw['BIG'], SOL={0: (1, 999)}, QUICK=None)
    builder.SECTIONS[kw['SEC']] = (kw['EXAM'], kw['MID'])
def R(q, it, small, tid, tname, tags, combo, diff, why, fmt, ans, atype, calc, cond, infer, trap, check, nsub=1, fig="없음", final=None, **kw):
    label = f"{q}" + (f"({it['act']})" if it.get('act') else "")
    summ = clean(it['stmt'])[:220]
    if fig != "없음":
        kw.setdefault('ready', "REVIEW"); kw.setdefault('status', "논리검산(그림 시각확인 불가)"); kw.setdefault('trust', "중간(그림 미확인)"); kw.setdefault('review', "REVIEW-그래프시각확인")
    r = builder.row(q, "", P['SEC'], "hwp", small, tid, tname, tags, combo, diff, why + " 계산량·조건해석·추론량 기준.", fmt, ans, atype, calc, cond, infer, trap,
                    summ, check + "; 파일 내 빠른 정답·해설과 일치", nsub, fig=fig, final=final,
                    visual="HWP5 렌더 불가 — olefile BodyText 파싱 텍스트+수식(EQEDIT) 스크립트 판독" + ("; 그림(gso) 시각확인 불가" if fig != "없음" else ""), key=clean(it['ans']), **kw)
    r.update({"원문항번호": label, "상위원문항번호": str(q),
        "학교/시험명": f"미래엔 {P['SUBJ']} 교과서 편집본(용문아 수학방) — {P['EXAM']} / {it['sec']}",
        "출처대분류": "교과서/교과서편집본(학원편집, hwp)", "주관기관": f"미래엔 {P['SUBJ']} 교과서 기반 · 용문아 수학방 편집",
        "학년": P.get('GRADE', "고2"), "교육과정": "2015 개정", "과목": P['SUBJ'],
        "원본페이지": "hwp(쪽 정보 없음)", "문항이미지/좌표": f"hwp 본문 {it['sec']} 문항 {q}",
        "해설파일 Drive ID": P['SRC'], "정답표 Drive ID": P['SRC'], "해설페이지": "동일 hwp 정답 및 해설", "정답표페이지": "동일 hwp 빠른 정답",
        "해설연결상태": "동일 hwp 내 빠른 정답+정답 및 해설 연결",
        "텍스트추출상태": "HWP5(olefile+zlib) BodyText 레코드 파싱: PARA_TEXT + EQEDIT 수식 스크립트 순서 복원",
        "중복대표여부": "원문항 1개=문항 1행(편집본 순번 기준)"})
    r["_q"] = q; ROWS.append(r)
def build(name, rows, cum0):
    for r in rows:
        r["메모"] = f"{P['QID']} {name}: HWP5 원본(SHA256 {P['SHA'][:16]}…); 문항 순번은 편집본 내 출현 순서(빠른 정답 목록 {P['N']}개와 일치); " + P.get('MEMO_X', '')
    for r in rows:
        for c in COLS:
            v = r.get(c)
            if isinstance(v, str) and v and v[0] in '=+-@':
                r[c] = {'-': '−', '+': '＋'}.get(v[0], '(식) ' + v[0]) + v[1:]
    clean_ = [{c: r[c] for c in COLS} for r in rows]
    print(name, validate(clean_))
    p = OUT + f'Math_Question_DB_P5_Result_{name}_20261004.xlsx'
    rv = [r["원문항번호"] for r in rows if r["production_ready"] != "YES"]
    save(clean_, p, [("배치", name), ("방향", "P5→P4 역방향 신규 DB 구축"), ("분석큐ID", P['QID']), ("원본파일", P['FNAME']),
        ("원본 Drive ID", P['SRC']), ("원본 SHA256(hwp)", P['SHA']), ("정답", "동일 파일 빠른 정답·해설"),
        ("처리범위", f"문항 {rows[0]['_q']}~{rows[-1]['_q']}"), ("정규 문항행", len(rows)), ("하위문항 합계", sum(int(r['소문항수']) for r in rows)),
        ("REVIEW", ", ".join(rv) or "없음"), ("HOLD", sum(r['production_ready'] == 'HOLD' for r in rows)),
        ("역방향 누적(직전까지)", cum0), ("역방향 누적(본 배치 후)", cum0 + len(rows))])
    slim(p); os.system(f"base64 -w0 '{p}' > {OUT}{name}.b64; wc -c {OUT}{name}.b64")
