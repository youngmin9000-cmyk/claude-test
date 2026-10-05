from cfgex import *
MC, S_, D = "객관식(5지선다)", "단답형", "서술형"
M, H = "보통", "높음"
setup("A00596", "1lDTUPaPOins7b0Mp5InOiioblEbijw6Z", "2023년 고1 중간고사.pdf", "p4/A00596.pdf", "장훈고등학교", "2024학년도", "1학기 중간고사", "고1", "수학(상)", CURR="2015 개정",
      VIS="재조판 PDF(7쪽) 110dpi 렌더 시각판독; 머리글 '2024년 1-1 중간고사 장훈고등학교 서울시 영등포구 수학(상)' — 파일명 '2023년'과 불일치(머리글 우선 기록)", TEXT="텍스트층 일부(수식 누락) — 렌더 판독 확정")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
POLY, EQ = "다항식", "방정식과 부등식"
def r(q, page, big, mid, small, tid, tname, tags, diff, fmt, ans, chk, pts, **kw):
    kw.setdefault("atype", "선택지" if fmt == MC else "값")
    lab = str(q) if q <= 18 else f"{q}(서답{q-18})"
    R(q, page, big, mid, small, tid, tname, tags, diff, fmt, ans, f"장훈고 2024 1-1 중간 수학(상) {q}번", chk, label=lab, pts=pts, **kw)
    ROWS[-1]["메모"] += "파일명 연도(2023)와 머리글(2024) 불일치 — 머리글 기준; "
r(1,1,POLY,"나머지정리","나머지정리","POLY.REMAINDER_THEOREM.CONCEPT","P(α)=R 내용의 명칭","나머지정리;개념","하",MC,"① (나머지정리)","","3.4")
r(2,1,POLY,"다항식의 연산","다항식의 덧셈과 뺄셈","POLY.LINEAR_EQ.SOLVE_X","A−2(X−B)=5A 만족 X","다항식;연산","하",MC,"② (−x²+5xy−3y²)","X=B−2A","3.4")
r(3,1,POLY,"항등식","항등식의 성질","POLY.IDENTITY.CONSTANT_RATIO","(3x−a)/(5x−b) 일정, b/a","항등식","하",MC,"⑤ (5/3)","3:5=a:b","3.5")
r(4,1,POLY,"다항식의 연산","곱셈 공식의 변형","POLY.POWER_SUM.RECURRENCE","x+y=2, x²+y²=8, x⁵+y⁵","곱셈공식;대칭식","하",MC,"② (152)","xy=−2; p₃=20, p₄=56, p₅=152","3.5")
r(5,1,EQ,"이차방정식과 이차함수","직선과 포물선의 위치 관계","QUADF.LINE.NO_INTERSECT_MIN_INT","y=x²−x+3a와 y=−4x+a−2 만나지 않는 정수 a 최소","판별식;위치 관계","하",MC,"④ (1)","9−8(a+1)<0 → a>1/8","3.6")
r(6,1,POLY,"다항식의 연산","곱셈 공식의 활용","POLY.PRODUCT_PLUS_CONST.SQRT","√(11×14×15×18+36)","곱셈공식;치환","하",MC,"② (204)","198·210+36=204²","3.6")
r(7,2,POLY,"인수분해","복이차식의 인수분해","POLY.FACTOR.BIQUADRATIC_CONDITIONS","x⁴−13x²+4=f·g, f 최댓값, f(3)>g(3), f(0)+g(4)","인수분해;이차함수","중하",MC,"① (−24)","(x²−3x−2)(x²+3x−2), f=−(x²−3x−2), g=−(x²+3x−2)","3.7",c=M,trap=M)
r(8,2,EQ,"이차방정식","근과 계수의 관계","EQ.VIETA.ROOT_SUBSTITUTION","x²+2x+k=0, 1/(α²−α+k)+1/(β²−β+k)=2/21, k","근과 계수","중하",MC,"① (7)","α²−α+k=−3α → 2/(3k)","3.7",c=M)
r(9,2,EQ,"이차방정식과 이차함수","직선과 포물선의 위치 관계","QUADF.TANGENT.IDENTITY_IN_K","x²−2kx+k²+3k와 y=2ax+b 항상 접함, |a+b|=p/q, p+q","판별식;항등식","중하",MC,"③ (7)","a=3/2, b=−9/4","3.8",c=M)
r(10,2,EQ,"복소수","ω의 성질","EQ.OMEGA.PERIODIC_SUM","f(n)=2ωⁿ/(1+ω²ⁿ), |Σf(1..100)|","ω;주기","중하",MC,"① (101)","주기 3: −2, −2, 1","3.8",c=M)
r(11,3,POLY,"인수분해","인수분해의 활용","POLY.FACTOR.ROOT_COUNT_PARAM","f(n)=(n−1)(n−k)(n+k), 자연수 근 1개 k 개수 A, 근 ≤5 k 개수 B","인수분해;경우 분석","중",MC,"④ (14)","A=3 (k=0,±1), B=11 (|k|≤5)","3.9",c=M,trap=M)
r(12,3,EQ,"이차방정식과 이차함수","직선과 포물선의 위치 관계","QUADF.APPLIED.TANGENT_FROM_POINT","폭 5, 높이 25/4 포물선, 9m 조명 접선 D, AD","이차함수;접선;실생활","중하",MC,"③ (3√5)","y=x(5−x), 접선 y=−x+9 → D(3,6)","4.0",c=M,fig="그림")
r(13,3,EQ,"복소수","복소수의 거듭제곱","COMPLEX.POWER.UNIT_ROOTS_COUNT","(√2/(1+i))ⁿ+(−2i/(1−√3i))ⁿ=2, n≤100 개수","복소수;주기","중",MC,"④ (4)","주기 8·12 → n≡0 mod 24 (수치 확인)","4.1",c=M)
r(14,4,EQ,"이차방정식","근과 계수의 관계","EQ.VIETA.DIVISOR_COUNT_MAX","α, β≤30 약수 4개, p, q≤100 서로 다름, q 최대 p+q","근과 계수;약수","중",MC,"⑤ (111)","α=6, β=15 (전수 확인)","4.2",c=M)
r(15,4,POLY,"다항식의 나눗셈","다항식의 나눗셈","POLY.DIVISION.STRUCTURE_DEGREE","(x−1)P−x²=(P−x)Q+P−2x, P÷Q 나머지 10, P(20)","다항식의 나눗셈;차수","중",MC,"② (46)","Q=x−2, 차수 조건 P=2x+6","4.3",c=M,i=M,trap=M)
r(16,4,EQ,"이차방정식","근과 계수의 관계","EQ.VIETA.SHIFTED_ROOTS.POWER_EQ","x²+ax+b, x²+3ax+3b 근 이동 2, αⁿ+βⁿ=αⁿ⁺¹+βⁿ⁺¹ n 합","근과 계수;복소수 거듭제곱","중",MC,"⑤ (63)","a=−2, b=4, α=2e^{iπ/3} → 3의 배수 (수치 확인)","4.4",c=M,i=M)
r(17,5,POLY,"나머지정리","인수정리","POLY.FUNCTIONAL_EQ.REMAINDER","Q²+Q(x−1)²=(x²−3x+2)P, P÷Q 나머지 R, R(5)","인수정리;나머지","중상",MC,"③ (108)","Q=x(x−1)(x−2), R=9x²−27x+18 (기호 계산)","4.5",c=M,i=M)
r(18,5,EQ,"사차방정식","복이차방정식","EQ.QUARTIC.INTEGER_ROOTS.FILL_BLANK","9x⁴−6(n+3)x²+(n−3)²=0 정수해 4개 과정 빈칸, f(k+1)","복이차;빈칸추론","중",MC,"④ (480)","f(n)=12n, k=12+27=39 (n=3 중복근 제외)","4.7",c=M,trap=M)
r(19,6,EQ,"복소수","복소수의 뜻","COMPLEX.DEFINITION.IMAGINARY","z=a+bi, b≠0이면 □","복소수;개념","하",S_,"허수","","4")
r(20,6,EQ,"이차방정식과 이차함수","제한된 범위의 최대·최소","QUADF.RESTRICTED.MAX_FROM_MIN","−4≤x≤4, (2−x)(6+x)+k 최솟값 −4, 최댓값","이차함수;최대최소","하",S_,"32","x=4에서 최소 → k=16, x=−2 최대","4")
r(21,6,EQ,"연립이차방정식","연립이차방정식","EQ.SYSTEM.FACTORABLE.SUM_EXTREMES","x²+2xy−3y²+x−y=0, x²+xy+3y²−3x−2y=0, α+β 최대×최소","연립이차방정식;인수분해","중",D,"0","(x−y)(x+3y+1)=0: (0,0),(1,1),(1,−2/3) → 합 0, 2, 1/3","5",c=M,trap=M)
r(22,6,POLY,"인수분해","인수분해의 활용","POLY.FACTOR.BIQUADRATIC_THREE_FACTORS","x⁴−260x²+b, x−a 인수, 서로 다른 세 정수계수 다항식 곱, q/(p−1)²","인수분해;조건 해석","중상",S_,"139","(x−a)(x+a)(x²−(260−a²)); 260−a² 제곱수(a=2,8,14,16) 제외 → p=12, q=121·139","5",c=M,i=M,trap=H,review="REVIEW-정답지미연결;REVIEW-조건해석(제곱수 경우 제외 해석)")
r(23,7,EQ,"이차방정식과 이차함수","이차함수의 최대·최소","QUADF.SUM_CONST.PRODUCT_MAX","x+y=c, xy (1) x 내림차순 (2) 최대와 x, y","이차함수;최대최소","하",D,"(1) xy=−x²+cx (2) 최댓값 c²/4, x=y=c/2","","6",nsub=2)
r(24,7,EQ,"이차방정식과 이차함수","이차함수의 최대·최소","QUADF.VERTICAL_SEGMENT.QUAD_AREA_MIN","x=t와 두 포물선 P, Q, A(1,1), B(4,1), PAQB 넓이 최솟값","이차함수;도형 넓이","중하",D,"9","P(t,2t²−4t+3), Q(t,−(t−4)²+1), 넓이 (3/2)(3(t−2)²+6)","6",c=M)
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{831+i}", ROWS[i*10:(i+1)*10], 16522+i*10)
