from cfgex import *
MC, D, S = "객관식(5지선다)", "서술형", "서술형(단답)"
M, H = "보통", "높음"
def a(q, pg, big, mid, small, tid, tname, tags, diff, ans, summ, chk, pts, fmt=MC, **kw):
    kw.setdefault("atype", "선택지" if fmt == MC else "값"); R(q, pg, big, mid, small, tid, tname, tags, diff, fmt, ans, summ, chk, pts=pts, **kw)
SQ, DF = "수열의 극한", "미분법"
setup("A01823", "10Gzf04qXkXRh9gJhI-esGKe7uyY7lses", "[2020년+기출]+화정고등학교+(경기+고양시+덕양구)+3-1+중간+미적분.hwp", "p1/A01823.hwp", "화정고(경기 고양)", "2020학년도", "1학기 1차 지필평가(중간)", "고3", "미적분",
      KEY={18:"32/15(4π−3√3)", 19:"1/2", 20:"1/ln3"}, KEYPAGE="서술형 3문항만 정답 인라인(객관식 정답 미수록)", KEYSRC="동일 hwp(족보닷컴 재편집본)",
      VIS="HWP5 렌더 불가 — olefile BodyText 파싱(족보닷컴 워터마크 수식 내 삽입분 제거) 텍스트+수식 판독", TEXT="HWP5 BodyText+EQEDIT(족보닷컴 재편집; 머리글 '수학1 고2'는 템플릿 오기, 파일명·내용은 3-1 미적분)")
NK = dict(ready="REVIEW", status="독립풀이(객관식 정답 미수록)", trust="중간(독립풀이 단독)", review="REVIEW-정답지미연결")
a(1, 1, SQ, "수열의 극한", "∞−∞ 꼴", "SEQLIM.RADICAL_DIFF", "√(n²+n+1)−n 극한", "수열의 극한", "하", "③ (1/2)", "", "유리화", "", **NK)
a(2, 1, DF, "여러 가지 미분법", "음함수 미분", "IMPLICIT.DERIV.FIND_COEFF", "음함수 dy/dx=3에서 ab", "음함수의 미분법", "중하", "② (6)", "x²+axy+y²+b=0, (−3,0)", "b=−9, −3a·y'=6 → a=−2/3", "", c=M, **NK)
a(3, 1, DF, "삼각함수의 미분", "두 직선이 이루는 각", "TRIG.LINES_ANGLE.COS", "두 직선 예각 cosθ", "삼각함수의 덧셈정리", "하", "③ (√2/2)", "3x−y+1=0, x−2y+2=0", "법선벡터 내적 5/√50", "", **NK)
a(4, 1, DF, "여러 가지 함수의 미분", "미분가능성", "DIFFERENTIABLE.LN_PIECEWISE", "ln ax / bx²+1 미분가능 a+b", "로그함수의 미분;미분가능성", "중하", "① (1/2+e√e)", "x=1", "b=1/2, ln a=3/2", "", c=M, **NK)
a(5, 1, SQ, "급수", "급수의 수렴", "SERIES.CONVERGENCE.STATEMENTS", "급수 수렴 보기", "급수", "하", "② (ㄴ)", "Σ(−1)ⁿ, 망원급수, aₙ→0", "ㄷ 역 불성립", "", **NK)
a(6, 1, SQ, "등비급수", "등비급수의 합", "SERIES.GEOMETRIC.NESTED_SUM", "Σ(3+…+3ⁿ⁺¹)/5ⁿ", "등비급수", "중하", "⑤ (51/8)", "분자 3^{n+1}까지", "(27/2−3/4)/2", "", c=M, **NK)
a(7, 1, SQ, "수열의 극한", "극한의 성질", "SEQLIM.RATIO_FROM_LIMIT", "7ⁿaₙ/(3ⁿ+1) 수렴 시 aₙ/aₙ₊₁", "수열의 극한", "중하", "⑤ (7/3)", "0 아닌 정수", "aₙ~k(3/7)ⁿ", "", i=M, **NK)
a(8, 1, SQ, "수열의 극한", "그래프와 극한", "SEQLIM.ABS_PARAM.GRAPH_COUNT", "그래프로 a 개수", "수열의 극한", "중", "미산출(그래프 미추출)", "[−2,5] 그래프, lim(|nf(a)−2|−nf(a))/(n+4)=1", "그래프 gso 미추출", "", final="미산출", fig="그래프", ready="HOLD", status="판독 불가(그래프 미추출)", trust="낮음", review="HOLD-그림판독")
a(9, 1, SQ, "등비수열의 극한", "수렴 조건", "SEQLIM.GEOMETRIC.CONVERGENCE_RANGE", "r²ⁿ 수렴 시 수렴 수열", "등비수열의 수렴", "중하", "③ (ㄱ, ㄷ)", "−1≤r≤1", "ㄴ r=−1에서 (−1)ⁿ", "", i=M, **NK)
a(10, 1, SQ, "급수", "망원급수", "SERIES.TELESCOPING.REMAINDER", "나머지 조건 aₙ 급수 합", "급수;나머지정리", "중하", "① (6)", "aₙx²+2aₙx−3을 x−n으로 나눈 나머지 5", "aₙ=8/(n(n+2))", "", c=M, combo="복합(나머지정리+급수)", **NK)
a(11, 1, DF, "여러 가지 함수의 미분", "미분계수 극한", "DERIV.LIMIT_DEFINED.EXP_TRIG", "g(x) 정의 후 (g−4eˣ)/x² 극한", "지수·삼각함수의 미분", "중", "① (−2)", "f=eˣ(sinx+cosx)", "g=2f'=4eˣcosx", "", c=M, i=M, **NK)
a(12, 1, DF, "여러 가지 미분법", "몫의 미분", "DERIV.QUOTIENT.EVAL", "g=4/(2−x²f) g'(1)", "함수의 몫의 미분법", "하", "⑤ (10)", "f(1)=1, f'(1)=1/2", "4(2+1/2)/1", "", **NK)
a(13, 1, DF, "여러 가지 미분법", "합성함수의 미분", "DERIV.CHAIN.LIMIT", "f(f(x))/(x−3) 극한", "합성함수의 미분법", "중하", "① (18)", "f(0)=0, f'(0)=3, lim f/(x−3)=6", "f'(0)·f'(3)", "", c=M, **NK)
a(14, 1, DF, "여러 가지 함수의 미분", "지수함수 극한", "LIMIT.EXP.DIFFERENCE_QUOTIENT", "(e^{1−sinx}−e^{1−tanx})/(tanx−sinx)", "지수함수의 극한", "중하", "④ (e)", "x→0", "평균변화율 → e¹", "", i=M, **NK)
a(15, 1, DF, "여러 가지 미분법", "로그·삼각 이계도함수", "DERIV.SECOND.LOG_COT", "e^f=√((1+cos)/(1−cos))에서 f''(π/6)", "로그함수의 미분;이계도함수", "중", "④ (2√3)", "", "f=ln cot(x/2), f'=−1/sinx", "", c=M, i=M, **NK)
a(16, 1, DF, "여러 가지 미분법", "역함수의 미분", "DERIV.INVERSE.COMPOSITE", "(g∘f)⁻¹의 G'(8)", "역함수의 미분법;합성함수의 미분법", "중하", "③ (1/4)", "f(4)=2, g(2)=8, f'(4)=1/4, g'(2)=16", "1/(16·1/4)", "", c=M, **NK)
a(17, 1, DF, "삼각함수의 미분", "도형과 미분", "DERIV.CIRCLE_SEGMENT.AREA_RATE", "원과 직선 활꼴 넓이 f'(√3)", "삼각함수의 미분;도형", "중", "③ (3/8)", "중심 (0,1) 반지름 1, y=tx", "f=φ−sin2φ/2, φ=arctan t", "", c=M, i=M, fig="도형", **NK)
a(18, 1, SQ, "등비급수", "도형과 등비급수", "SERIES.GEOMETRIC.FRACTAL_AREA", "프랙탈 넓이 극한(서술1)", "등비급수;도형", "상", "32/15(4π−3√3)", "AB=8 원, 정사각형·원 반복", "파일 정답(그림 미추출로 독립검증 불완전)", "", fmt=D, label="서술1", c=H, i=H, fig="도형", ready="REVIEW", status="파일 정답(그림 미추출)", trust="중간", review="REVIEW-그림판독")
a(19, 1, DF, "삼각함수의 극한", "도형과 극한", "TRIGLIM.SEMICIRCLE.AREA_RATIO", "T(θ)/S(θ) 극한(서술2)", "삼각함수의 극한;사인법칙", "중", "1/2", "AB=2 반원, ∠PAB=θ, ∠APO=∠OPC", "OC=sinθ/sin3θ→1/3, CB/AC=1/2", "", fmt=D, label="서술2", c=M, i=M, fig="도형", ready="YES", status="검산완료(본문 조건으로 독립풀이·정답 일치)", trust="높음(텍스트 조건 완결+정답 일치)", review="분석완료")
a(20, 1, DF, "지수함수의 극한", "도형과 극한", "EXPLIM.SEGMENT_RATIO", "AB/BC 극한(서술3)", "지수·로그함수의 극한", "중", "1/ln3", "y=k와 (1/3)ˣ−1, 3ˣ−1", "AB=2log₃(1+k), BC=k(2+k)/(1+k)", "", fmt=D, label="서술3", c=M, i=M, fig="그래프", ready="YES", status="검산완료(본문 조건으로 독립풀이·정답 일치)", trust="높음(텍스트 조건 완결+정답 일치)", review="분석완료")
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{673+i}", ROWS[i*10:(i+1)*10], 15051+i*10)
