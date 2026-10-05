from cfgex import *
MC, S_, D = "객관식(5지선다)", "단답형", "서술형"
M, H = "보통", "높음"
setup("A00591", "1Dpt0QVw-45ubhidjJ6pnGhbtUAhaJkQ5", "장훈고등학교_2학년_2025_1학기중간_수학1_공통_문제.pdf", "p4/A00591.pdf", "장훈고등학교", "2025학년도", "1학기 중간고사", "고2", "수학1", CURR="2015 개정",
      VIS="재조판 PDF(8쪽) 100dpi 렌더 시각판독", TEXT="텍스트층 일부 — 렌더 판독 확정")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
EL, TR = "지수함수와 로그함수", "삼각함수"
def r(q, page, big, mid, small, tid, tname, tags, diff, fmt, ans, chk, pts, **kw):
    kw.setdefault("atype", "선택지" if fmt == MC else "값")
    lab = str(q) if q <= 18 else f"{q}(서답{q-18})"
    R(q, page, big, mid, small, tid, tname, tags, diff, fmt, ans, f"장훈고 2025 2-1 중간 수학1 {q}번", chk, label=lab, pts=pts, **kw)
r(1,1,EL,"지수","지수의 확장","EXP.INTEGER_EXPONENT.EVAL","3⁻²","지수","하",MC,"③ (1/9)","","3.4")
r(2,1,TR,"삼각방정식","삼각방정식","TRIGEQ.SIN.BASIC","0≤x<3π/2, sin x=−1/2","삼각방정식","하",MC,"⑤ (7π/6)","11π/6은 범위 밖","3.4",trap=M)
r(3,1,EL,"로그","로그의 정의","LOG.NESTED.SOLVE","log₂{log₃(log₄x)}=1","로그","하",MC,"④ (2¹⁸)","log₄x=9","3.5")
r(4,1,TR,"삼각함수","삼각함수 사이의 관계","TRIG.IDENTITY.FROM_RATIO","3π/2<θ<2π, 4sinθ=−cosθ, sinθ","삼각함수","하",MC,"③ (−√17/17)","tanθ=−1/4","3.5")
r(5,2,EL,"상용로그","상용로그표","LOG.COMMON.TABLE_QUOTIENT","log(√3.35/0.0316) 상용로그표","상용로그","하",MC,"④ (1.7628)","0.2625−(0.4997−2)","3.6",fig="표")
r(6,2,TR,"호도법과 부채꼴","부채꼴","TRIG.SEMICIRCLE.SECTOR_SPLIT","반원 호 AC=π, 부채꼴 OBC=28π, OA","부채꼴","하",MC,"④ (8)","r²−r−56=0","3.6",fig="도형")
r(7,2,TR,"삼각함수","삼각함수 사이의 관계","TRIG.SUM_SQRT2.FIFTH_POWER","sinθ+cosθ=√2, sin⁵θ+cos⁵θ","삼각함수","하",MC,"② (√2/4)","sinθcosθ=1/2 → sin=cos=√2/2","3.7")
r(8,2,TR,"삼각함수","삼각함수의 성질","TRIG.ANGLE_REDUCTION.POINT","P(−4,3), 10sin(π+θ)−15cos(π−θ)+5sin(π/2+θ)","각변환","하",MC,"① (−22)","−10s+20c, s=3/5, c=−4/5","3.7")
r(9,3,EL,"지수","거듭제곱근","ROOT.REAL_COUNT.CONSECUTIVE_EQ","n²−15n+54의 n제곱근 중 실수 개수 f(n)=f(n+1), 4≤n≤12, n 합","거듭제곱근;실수 개수","중하",MC,"① (11)","n=5, 6","3.8",c=M,trap=M)
r(10,3,EL,"로그","로그의 성질","LOG.CONDITION.NATURAL_TRIPLE","log a+log b−log c=0, a+b=c/2, a²+b²","로그;정수 조건","중하",MC,"③ (45)","(a−2)(b−2)=4 → {3,6}","3.8",c=M)
r(11,3,EL,"로그함수","로그함수의 그래프","LOGF.TRIANGLE_AREA.CONSTANT","log₂(x−3)²+n과 x축 A, B, y=2^{n/2} 교점 C, ABC 넓이","로그함수;넓이","중하",MC,"① (1)","AB=2^{1−n/2}, 높이 2^{n/2}","3.9",c=M)
r(12,3,EL,"로그","로그의 성질","LOG.CONDITION.SOLVE","log₃(m²+2/9)=−1, log₃m=5+3log₃n, m+n","로그","하",MC,"② (4/9)","m=1/3, n=1/9","3.9")
r(13,4,EL,"지수","지수법칙","EXP.ROOT_EQUATION.QUAD_COUNT","2≤a,b,c,d≤50, a^{1/b}c^{1/d}=28^{1/5} (a,b,c,d) 개수","지수법칙;정수 조건","중상",MC,"③ (21)","전수 확인","4.1",c=M,i=M)
r(14,4,EL,"로그함수","로그함수와 이차함수","LOGF.PIECEWISE.ROOT_DISTANCE","a(x−3)(x+2)/−blog₂(x/5)+14a, AB=7, f(b)=−2b, 7a+b","로그함수;구간별 함수","중",MC,"⑤ (60)","B x=10 → b=14a, b=40","4.2",c=M)
r(15,5,EL,"지수함수의 활용","지수부등식","EXPINEQ.PIECEWISE_LINEAR.INTEGER_SUM","(1/3)^{f(x)}≥27^{(|x|−9)/3}, f 꺾은선, 정수 x 합","지수부등식;절댓값","중하",MC,"② (15)","f(x)+|x|≤9 → x=0~5","4.3",c=M,fig="그래프")
r(16,5,EL,"지수함수와 로그함수의 관계","역함수와 교점","EXPLOG.INVERSE.LARGER_ROOT_CEIL","5ˣ−n와 역함수 큰 교점 g(n), h(n)=⌈g⌉, h(n)<h(n+1) n≤200 합","역함수;지수함수","중상",MC,"④ (149)","5ᵏ−k=n → n=4, 23, 122 (수치 확인)","4.4",c=M,i=M)
r(17,6,TR,"삼각함수의 그래프","삼각함수의 그래프 활용","TRIGF.MAX_FUNC.ROOT_COUNT_RANGE","h=max(acos x+b, −2sin x), 최솟값 −1, h=√3 실근 3개, h=k 네 실근 c<k<d, a+b+c+d","삼각함수 그래프;실근 개수","상",MC,"⑤ (2√3−1)","a=−2, b=√3−1 (최소 x=π/6), c=√3, d=2 (수치 확인)","4.5",c=H,i=H)
r(18,6,EL,"로그함수","로그함수와 정수 조건","LOGF.DIVIDE_POINT.SET_SUM_COUNT","A(a,0), B(4,log₂b) 1:3 내분점이 3log₁₆((x−1)/3)+3/2 위, {n|b<3ⁿa≤81b} 합 26, (a,b) 개수","로그함수;내분점;부등식","중상",MC,"① (7)","b=a³, n=5~8 → 81≤a²<243 → a=9~15","4.7",c=M,i=M)
r(19,7,TR,"삼각부등식","삼각부등식","TRIGINEQ.SIN2X.SYMMETRIC","0≤x<π, 3sin2x−1>0 해 α<x<β, sin(α+β)","삼각부등식;대칭","하",S_,"1","α+β=π/2","4")
r(20,7,EL,"지수함수와 로그함수의 활용","실생활 활용","EXP.APPLIED.NEWTON_COOLING","뉴턴 냉각법칙 2.7^{−kt}, 15℃ at 18시, 꺼낸 시각","지수;로그;실생활","중하",D,"11시","2.7^{−0.1t}=1/2 → t=0.301/0.043=7","5",c=M)
r(21,7,TR,"삼각방정식","삼각방정식","TRIGEQ.QUADRATIC_SUB.ROOT_COUNT","cos²x+sin x−a=0 서로 다른 실근 3개 a","삼각방정식;실근 개수","중하",S_,"1","s²−s+a−1=0, s=1·0","5",c=M,trap=M)
r(22,7,EL,"로그","로그의 성질","LOG.SET_PRODUCT.COUNT_MAX_M","A_m={ab | log₃a+log₂₇b 자연수 ≤100, 1≤a≤m, b=3ᵏ}, n(A_m)=302, m 최댓값","로그;집합;정수 조건","상",S_,"80","a=3ᵉ, ab=3^{3j−2e}; e≤3 → 302 → 27≤m≤80 (전수 확인)","6",c=H,i=H)
r(23,8,TR,"삼각함수의 그래프","삼각함수의 그래프","TRIGF.COS.RIGHT_ISOSCELES_AREA","acos(bx+c), A 최댓점, B 영점, ∠OAB=π/2, 넓이 1, a+b+c","삼각함수 그래프;넓이","중",S_,"1","c=−π/2, a=π/(2b), b=π/2, a=1","5",c=M,fig="그래프")
r(24,8,EL,"로그함수","로그함수의 그래프","LOGF.ABS.TRAPEZOID_AREA","|log₂x−n|과 y=1, y=2 사다리꼴 Sₙ, 42≤S_k≤168 k 합","로그함수;넓이","중하",S_,"15","Sₙ=21·2^{n−3} → k=4,5,6","5",c=M,fig="그래프")
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{840+i}", ROWS[i*10:(i+1)*10], 16570+i*10)
