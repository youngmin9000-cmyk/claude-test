from cfgex import *
MC, D = "객관식(5지선다)", "서술형"
M, H = "보통", "높음"
def a(q, pg, big, mid, small, tid, tname, tags, diff, ans, summ, chk, pts, fmt=MC, **kw):
    kw.setdefault("atype", "선택지" if fmt == MC else "값"); R(q, pg, big, mid, small, tid, tname, tags, diff, fmt, ans, summ, chk, pts=pts, **kw)
LC, DF = "함수의 극한과 연속", "미분"
G = dict(fig="그래프"); F = dict(fig="도형")
# ── A00845 영등포여고 2023 2-2 중간 수학Ⅱ — 정답표 A00844(jpg), 서답 채점기준 A00843(jpg); A00840('수정')은 동일 이미지 회전본 DUPLICATE
K45 = dict(enumerate("②②④⑤②③①⑤③①①③⑤④③①⑤④", 1)); K45.update({19: "−9", 20: "g(x)=4(x−2)²", 21: "4/3", 22: "2/3"})
setup("A00845", "1w5wvHvt1U8z7Xm-AvVaWKsg-XwNq1SyV", "2023년 2학기 중간고사.pdf", "p2/A00845.pdf", "영등포여고", "2023학년도", "2학기 중간고사", "고2", "수학Ⅱ",
      KEY=K45, KEYPAGE="A00844 정답/배점표 사진(1/2), A00843 서답형 채점기준표 사진", KEYSRC="1FhOcQxkfNk0mWGsaN13tVPQ4CIYFVA7a; 1-mgInm5aihyGZpujIFw9w20yOMBQ4j6s",
      VIS="스캔 PDF(텍스트층 없음) — 동일 이미지 정방향본 A00840으로 렌더 시각판독(6쪽)", TEXT="텍스트층 없음 — 렌더 판독")
a(1, 1, LC, "함수의 극한", "극한의 성질", "LIMIT.LINEARITY", "lim f=2, lim g=4, lim(3f−g)", "함수의 극한의 성질", "하", "② (2)", "", "6−4", "3.6")
a(2, 1, LC, "함수의 극한", "0/0 꼴", "LIMIT.SQRT.RATIONALIZE", "(√(x+2)−2)/(x−2)", "함수의 극한", "하", "② (1/4)", "", "유리화", "3.6")
a(3, 1, DF, "미분계수", "미분계수", "DERIV.POLY.VALUE", "2x³+x의 x=1 미분계수", "미분계수", "하", "④ (7)", "", "6+1", "3.8")
a(4, 1, LC, "함수의 극한", "그래프 극한", "LIMIT.GRAPH.ORDER", "그래프 a=lim₀₊f, b=lim₁f, c=f(−1) 대소", "함수의 극한", "하", "⑤ (a<b≤c)", "", "a=0, b=1, c=1", "3.8", **G)
a(5, 1, DF, "도함수의 활용", "접선", "TANGENT.SLOPE.POINT", "x²+x+1 위 (1,a) 접선 기울기 b, a+b", "접선의 기울기", "하", "② (6)", "", "3+3", "4")
a(6, 2, DF, "도함수", "곱의 미분", "DERIV.PRODUCT.VALUE", "x(x−1)+(x−1)²(x−3) f'(1)", "도함수", "하", "③ (1)", "", "", "4")
a(7, 2, LC, "함수의 극한", "미정계수", "LIMIT.CUBIC.UNDETERMINED", "(x³+ax²+bx+2)/(x−2)→1, a+b", "함수의 극한;미분계수", "중하", "① (−2)", "", "a=−3, b=1", "4", c=M)
a(8, 2, DF, "도함수", "절댓값 함수 미분", "DERIV.ABS_POWER.VALUES", "x|x|+|x−2|³ f'(2)−f'(0)", "도함수", "중하", "⑤ (16)", "", "4−(−12)", "4.1", c=M)
a(9, 2, LC, "함수의 극한", "x→−∞ 무리식", "LIMIT.SQRT.NEG_INFINITY", "(√(x²−x+3)+x)/(√(x²−2x+4)+x) x→−∞", "함수의 극한", "중하", "③ (1/2)", "", "x=−t 치환", "4.1", c=M, trap=M)
a(10, 2, LC, "함수의 극한", "극한의 성질", "LIMIT.PROPERTIES.STATEMENTS", "극한 존재 명제 보기", "함수의 극한의 성질", "중", "① (ㄱ)", "", "ㄴ 우극한만, ㄷ f(2) 미정", "4.3", trap=H)
a(11, 3, LC, "함수의 극한", "가우스 기호 극한", "LIMIT.GAUSS.RIGHT_LIMIT", "(2x+[−x])/(x−n)=k (x→n⁺), n+k", "함수의 극한", "중", "① (3)", "", "[−x]=−n−1 → n=1, k=2", "4.3", c=M, trap=M)
a(12, 3, LC, "함수의 연속", "사잇값 정리", "IVT.ROOT_COUNT.TABLE", "(x−1)f(x)=x (0,5) 실근 최소 개수 최대", "사잇값의 정리", "중하", "③ (2)", "", "h부호 +,−,−,−,+", "4.4", c=M)
a(13, 3, DF, "미분계수", "다항식 나눗셈과 미분", "DERIV.DIVISION_SQUARE.REMAINDER", "xⁿ+x⁴+2x³+x−1을 (x−1)²로 나눈 Q(2)=23, R(−1)", "미분;나머지정리", "중", "⑤ (−24)", "", "2ⁿ=n+5 → n=3, R=14x−10", "4.5", c=M, i=M)
a(14, 3, DF, "미분계수", "미분계수의 정의", "DERIV.LIMIT_FORMS.SQRT_COMPOSITE", "f(1+h²)−f(1−2h) 극한 10, f(√(x−2)) 극한 q/p", "미분계수", "중", "④ (7)", "", "f'(1)=5, 5/2", "4.5", c=M)
a(15, 4, LC, "함수의 극한", "극한의 대소", "LIMIT.SQUEEZE.RATIONAL", "2x²−4x+1≤f≤2x²+2, (f+2x+1)/(f+x²−x)", "함수의 극한의 대소 관계", "하", "③ (2/3)", "", "f~2x²", "4.7")
a(16, 4, LC, "함수의 연속", "곱함수 연속", "CONTINUITY.PRODUCT.PARAM_SUM", "f·g 연속 모든 a 합", "함수의 연속", "중", "① (−4)", "", "a=3, −2, −5", "4.7", c=M, trap=M)
a(17, 4, DF, "미분계수", "극한 조건", "DERIV.SQRT_DIFF.QUADRATIC", "√f−√(4x²−8x+5)→3, x{f((x+2)/x)−f(1)}=k", "미분계수;함수의 극한", "중", "⑤ (24)", "", "f=4x²+4x+c, 2f'(1)", "4.8", c=M, i=M)
a(18, 4, DF, "미분가능성", "좌·우미분계수", "DERIV.ONE_SIDED.SYMMETRIC_LIMIT", "연속 구간함수, (f(2−h²)−f(2+h²))/h²=−2, f(3)", "미분계수", "중", "④ (3)", "", "f'₋+f'₊=2 → a=0, b=12", "4.8", c=M, i=M)
a(19, 5, LC, "함수의 극한", "극한 조건과 다항식", "LIMIT.POLY_CONDITIONS.COMPOSITE_RATIO", "두 극한 조건 f, x→−1 복합 극한(서답1)", "함수의 극한;미분계수", "중", "−9", "", "f(0)=3, f'(0)=1/2, f(2)=0, f'(2)=4", "5", fmt=D, label="서답1", c=M, i=M)
a(20, 5, LC, "함수의 연속", "곱함수 연속", "CONTINUITY.RATIONAL_TIMES_QUADRATIC", "(x−2)²f=x²−x+a, g(3)=4, fg 연속 g(서답2)", "함수의 연속", "중", "g(x)=4(x−2)²", "", "a≠−2 가정 시 유일(a=−2이면 g=(x−2)(px+q) 다수) — 원채점기준 4(x−2)²", "5", fmt=D, label="서답2", c=M, trap=M)
a(21, 6, LC, "함수의 극한", "극한의 성질", "LIMIT.RATIO_FROM_CONDITION", "f,g>0, f→0, 2/f−1/g→2, (f+2g)/(f+g)(서답3)", "함수의 극한의 성질", "중", "4/3", "", "f/g→2", "7", fmt=D, label="서답3", c=M, i=M)
a(22, 6, LC, "함수의 극한", "도형과 극한", "LIMIT.CIRCLE_CHORD.SLOPE_1_OVER_R", "원 x²+y²=r², A(−r,0) 기울기 1/r 현 AB/(3r−1)(서답4)", "함수의 극한;원", "중", "2/3", "", "AB=2r²/√(r²+1)", "7", fmt=D, label="서답4", c=M, **F)
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{715+i}", ROWS[i*10:(i+1)*10], 15427+i*10)
