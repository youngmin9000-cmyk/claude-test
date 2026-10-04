from cfgy import *
import cfgy, builder
SQ = hashlib.sha256(open(OUT+'h83/Q.hwp','rb').read()).hexdigest()
IT = json.load(open(OUT+'y83m.json'))
setup(QID="A02483", SRC="1375CIRtowB3Qg0VFKzv6f3ioYkOd6UWj", SHA=SQ, TAG="YMCAL03", N=132, SUBJ="미적분", SEC="C03A",
      FNAME="3. 적분법 132제(미래엔-용문아).hwp", UNIT="Ⅲ. 적분법", BIG="Ⅲ. 적분법", EXAM="Ⅲ 적분법 132제", MID="여러 가지 적분법")
cfgy.P["MEMO_X"] = "파서가 70번 활동의 정답 2번째 줄((가)(나)(다) xₖ 정의)을 별도 항목으로 분리하여 70번에 병합함(132문항=빠른 정답 132개); "
for s, mid in (("C03A", "여러 가지 적분법"), ("C03B", "정적분의 활용"), ("C03C", "적분법 종합(대단원 평가)")):
    builder.SECTIONS[s] = ("Ⅲ 적분법 132제", mid)
L, M, H = "낮음", "보통", "높음"
S, MC, D, ACT, PRF = "서술형(단답)", "5지선다", "서술형", "서술형(활동)", "서술형(증명)"
I1, I2, I3 = "여러 가지 함수의 적분", "치환적분법", "부분적분법"
J1, J2, J3, J4 = "정적분과 급수의 합 사이의 관계", "넓이", "부피", "속도와 거리"
def secof(q): return "C03A" if q <= 62 else "C03B" if q <= 110 else "C03C"
def r(q, small, tid, tname, tags, diff, fmt, ans, atype="값", nsub=1, fig="없음", final=None, combo="단일개념", c=L, d=L, i=L, trap="", why="", chk="독립풀이 일치", **kw):
    cfgy.P['SEC'] = secof(q)
    R(q, IT[q-1], small, tid, tname, tags, combo, diff, why or tname + ".", fmt, ans, atype, c, d, i, trap, chk, nsub=nsub, fig=fig, final=final, **kw)
