from cfgy import *
import cfgy, builder
SQ = hashlib.sha256(open(OUT+'h84/Q.hwp','rb').read()).hexdigest()
IT = json.load(open(OUT+'y84.json'))
setup(QID="A02484", SRC="1bRTtMlwWdxQqg4tgHQxyDDe552v0DVgz", SHA=SQ, TAG="YMCAL02", N=224, SUBJ="미적분", SEC="C02A",
      FNAME="2. 미분법 224제(미래엔-용문아).hwp", UNIT="Ⅱ. 미분법", BIG="Ⅱ. 미분법", EXAM="Ⅱ 미분법 224제", MID="여러 가지 함수의 미분")
cfgy.P["MEMO_X"] = "빠른 정답 목록은 29번 답이 2줄로 분할되고 40번(반각 공식) 항목이 누락되어 있어, 각 문항 정답은 본문 직후 정답줄로 연결함; "
for s, mid in (("C02A", "여러 가지 함수의 미분"), ("C02B", "여러 가지 미분법"), ("C02C", "도함수의 활용"), ("C02D", "미분법 종합(대단원 평가)")):
    builder.SECTIONS[s] = ("Ⅱ 미분법 224제", mid)
L, M, H = "낮음", "보통", "높음"
S, MC, D, ACT, PRF = "서술형(단답)", "5지선다", "서술형", "서술형(활동)", "서술형(증명)"
E1, E2, T1, T2, T3 = "지수함수와 로그함수의 극한", "지수함수와 로그함수의 미분", "삼각함수의 덧셈정리", "삼각함수의 극한", "삼각함수의 미분"
Q1, Q2, Q3, Q4, Q5 = "함수의 몫의 미분법", "합성함수의 미분법", "매개변수로 나타낸 함수의 미분법", "음함수와 역함수의 미분법", "이계도함수"
U1, U2, U3, U4 = "접선의 방정식", "함수의 그래프", "방정식과 부등식에의 활용", "속도와 가속도"
def secof(q): return "C02A" if q <= 74 else "C02B" if q <= 136 else "C02C" if q <= 202 else "C02D"
def r(q, small, tid, tname, tags, diff, fmt, ans, atype="값", nsub=1, fig="없음", final=None, combo="단일개념", c=L, d=L, i=L, trap="", why="", chk="독립풀이 일치", **kw):
    cfgy.P['SEC'] = secof(q)
    R(q, IT[q-1], small, tid, tname, tags, combo, diff, why or tname + ".", fmt, ans, atype, c, d, i, trap, chk, nsub=nsub, fig=fig, final=final, **kw)
