# P5 lane wrapper over cfgex (local-only results; no Drive upload)
import cfgex
from cfgex import *
def build(name, rows, cum0):
    for r in rows:
        r["메모"] = r["메모"].replace("P1 학교기출(P5REV 스트림 P1 구간)", "P5 lane 신규 구축(P5 전담 세션)")
        r["출처대분류"] = r.get("출처대분류") if r.get("출처대분류") not in ("학교 내신 기출",) else r["출처대분류"]
    for r in rows:
        for c in COLS:
            v = r.get(c)
            if isinstance(v, str) and v and v[0] in '=+-@':
                r[c] = {'-': '−', '+': '＋'}.get(v[0], '(식) ' + v[0]) + v[1:]
    clean_ = [{c: r[c] for c in COLS} for r in rows]
    print(name, validate(clean_))
    p = OUT + f'Math_Question_DB_P5LANE_Result_{name}_20261006.xlsx'
    rv = [r["_q"] for r in rows if r["production_ready"] != "YES"]
    qs = sorted({r["분석큐ID"] for r in rows})
    save(clean_, p, [("배치", name), ("방향", "P5 lane 신규 DB 구축 (P1_P5_FINAL_READY_MASTER lane=P5 고정순서)"), ("분석큐ID", ", ".join(qs)),
        ("원본파일", " / ".join(sorted({r['원본파일명'] for r in rows}))), ("원본 Drive ID", ", ".join(sorted({r['원본파일 Drive ID'] for r in rows}))),
        ("처리범위", f"{rows[0]['_q']} ~ {rows[-1]['_q']}"), ("정규 문항행", len(rows)), ("하위문항 합계", sum(int(r['소문항수']) for r in rows)),
        ("REVIEW", ", ".join(rv) or "없음"), ("HOLD", sum(r['production_ready'] == 'HOLD' for r in rows)),
        ("P5 lane 누적(직전까지)", cum0), ("P5 lane 누적(본 배치 후)", cum0 + len(rows)), ("업로드", "LOCAL_RESULT_READY / READY_FOR_UPLOAD (Drive 미업로드)")])
    slim(p)
