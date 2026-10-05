from cfgex import *
MC, S_, D = "객관식(5지선다)", "단답형", "서술형"
M, H = "보통", "높음"
setup("A00580", "1LZJtwLnLvaIBe46MYPxw96NYX9hJ-O-z", "운암고등학교_1학년_2025_1학기중간_공통수학1_공통_문제.pdf", "p4/A00580.pdf", "운암고등학교", "2025학년도", "1학기 중간고사", "고1", "공통수학1", CURR="2022 개정",
      VIS="재조판(복원) PDF 3쪽 100dpi 렌더 + 200dpi 확대 시각판독; 조판 오타 존재(2번 'a+v')", TEXT="텍스트층 일부 — 렌더 판독 확정")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
POLY, EQ = "다항식", "방정식과 부등식"
def r(q, page, big, mid, small, tid, tname, tags, diff, fmt, ans, chk, pts, **kw):
    kw.setdefault("atype", "선택지" if fmt == MC else "값")
    lab = str(q) if q <= 22 else f"{q}(논술{q-22})"
    R(q, page, big, mid, small, tid, tname, tags, diff, fmt, ans, f"운암고 2025 1-1 중간 공통수학1 {q}번", chk, label=lab, pts=pts, **kw)
r(1,1,POLY,"다항식의 연산","다항식의 덧셈","POLY.ADD.BASIC","(x²+2xy)+(x²−xy)","다항식","하",MC,"③ (2x²+xy)","","3.2")
r(2,1,POLY,"다항식의 연산","곱셈 공식","POLY.CUBE_EXPANSION.EVAL","a+b=3, a³+3a²b+3ab²+b³","곱셈공식","하",MC,"④ (27)","조판 오타 'a+v=3'(=a+b) 해석","3.3",review="REVIEW-정답지미연결;REVIEW-원문오타(a+v)")
r(3,1,POLY,"다항식의 나눗셈","다항식의 나눗셈","POLY.DIVISION.LINEAR","(x²+3x+4)÷(x+1) 몫·나머지","나눗셈","하",MC,"③ (몫 x+2, 나머지 2)","","3.3")
r(4,1,EQ,"이차방정식","판별식","EQ.QUADRATIC.DOUBLE_ROOT","x²−6x+k+1=0 중근 k","판별식","하",MC,"④ (8)","","3.4")
r(5,1,POLY,"인수분해","인수분해 공식","POLY.FACTOR.TRINOMIAL_SQUARE","x²+y²+4z²+2xy+4yz+4zx 인수분해","인수분해","하",MC,"③ ((x+y+2z)²)","","3.5")
r(6,1,EQ,"이차방정식","판별식","EQ.DISCRIMINANT.NATURAL_PAIR","x²+ax+2b=0 중근, x²+5x+a=0 서로 다른 두 실근, a+b (자연수)","판별식","중하",MC,"① (6)","a²=8b, a<25/4 → a=4, b=2","3.5",c=M)
r(7,1,EQ,"이차방정식","근과 계수의 관계","EQ.VIETA.SUM","2x²+6x−3=0, α+β","근과 계수","하",MC,"① (−3)","","3.6")
r(8,1,POLY,"다항식의 연산","다항식의 덧셈과 뺄셈","POLY.LINEAR_SYSTEM.SUM","3A−B, A−3B 주어짐, A+B","다항식;연립","하",MC,"③ (2x³−3x+2)","2(A+B)=P−Q","3.6")
r(9,1,EQ,"이차방정식과 이차함수","제한된 범위의 최대·최소","QUADF.RESTRICTED.MAX","1≤x≤4, (x−2)²+3 최댓값","이차함수","하",MC,"⑤ (7)","x=4","3.7")
r(10,1,EQ,"이차방정식","근과 계수의 관계","EQ.VIETA.ROOT_DIFFERENCE","x²−kx+2k+4=0 두 근 차 2, k 합","근과 계수","중하",MC,"④ (8)","k²−8k−20=0","3.7",c=M)
r(11,2,EQ,"이차방정식과 이차함수","이차함수와 x축","QUADF.X_AXIS.TANGENT","2x²−2x−k가 x축과 한 점, k","판별식","하",MC,"① (−1/2)","","3.8")
r(12,2,EQ,"이차방정식과 이차함수","이차함수와 x축","QUADF.TANGENT_X_AXIS.IDENTITY_IN_K","x²−2(2a−k)x+k²+2k+b 항상 x축 접함, 2a×b","판별식;항등식","중하",MC,"② (−1)","a=−1/2, b=1","3.8",c=M)
r(13,2,POLY,"항등식","항등식의 성질","POLY.IDENTITY.COEFF_COMPARE","ax²+b(x−2)+4=−2x²+x+c 항등식, abc","항등식","하",MC,"③ (−4)","a=−2, b=1, c=2","3.9")
r(14,2,EQ,"복소수","복소수의 뜻과 연산","COMPLEX.BASIC.STATEMENTS","z=2−3i 보기","복소수","하",MC,"③ (ㄱ, ㄷ)","허수부분은 −3 (−3i 아님)","3.9",trap=M)
r(15,2,POLY,"나머지정리","인수정리와 조립제법","POLY.DIVISIBLE.QUOTIENT_REMAINDER","2x³−3x²+10x+k가 x²+5로 나누어떨어짐, x−2로 나눈 몫·나머지, k+a+b+R","인수정리;조립제법","중하",MC,"② (7)","k=−15, 몫 2x²+x+12, R=9","4",c=M)
r(16,2,POLY,"인수분해","인수정리를 이용한 인수분해","POLY.FACTOR.QUARTIC_FILL_BLANK","x⁴+5x³+x²−21x−18 인수분해 과정 빈칸, α−β","인수정리;빈칸","중하",MC,"② (±(18의 약수), P(2)=0, −2)","(x−2)(x+1)(x+3)²","4.1",c=M)
r(17,2,EQ,"복소수","복소수의 연산","COMPLEX.UNIT_CIRCLE.STATEMENTS","z=√3/2+i/2, w=1/2+√3i/2 보기","복소수;켤레","중하",MC,"⑤ (ㄱ, ㄴ, ㄷ)","극형식 확인","4.2",c=M)
r(18,2,EQ,"이차방정식과 이차함수","이차함수와 x축","QUADF.NO_X_INTERCEPT.STATEMENTS","x²+ax+b x축과 만나지 않음, 보기 ㄱ a²−4b<0 ㄴ f(a)>0 ㄷ b<0","판별식;보기","중하",MC,"독립풀이 ㄱ, ㄴ (선택지 부재)","f(a)=2a²+b>0 (b>a²/4≥0) 참, ㄷ 거짓 → {ㄱ,ㄴ}이 선택지에 없음; 200dpi 확대 확인 — 원문 오류","4.3",c=M,trap=M,review="HOLD-원문오류(정답 선택지 부재)",ready="HOLD",status="독립풀이 결과가 선택지에 없음 — 원문/복원 오류 의심",trust="낮음",conflict="원문조건충돌: 정답 {ㄱ,ㄴ} ∉ 선택지(①ㄱ ②ㄴ ③ㄷ ④ㄱ,ㄷ ⑤ㄱ,ㄴ,ㄷ)",final="ㄱ, ㄴ (선택지 부재)")
r(19,3,EQ,"이차방정식과 이차함수","이차함수의 최대·최소","QUADF.MIN_AS_FUNCTION.RANGE","x²−4ax+3a²−2a 최솟값 f(a), 0≤a≤2 최대+최소","이차함수;최대최소","중하",MC,"⑤ (−8)","f(a)=−a²−2a: 0, −8","4.4",c=M)
r(20,3,EQ,"이차방정식과 이차함수","두 그래프의 교점","QUADF.TWO_PARABOLAS.CHORD_LENGTH","−(x−1)²+a와 2(x−1)² 교점 AB=3, a","이차함수;교점","하",MC,"② (27/4)","2√(a/3)=3","4.5")
r(21,3,POLY,"다항식의 나눗셈","다항식의 나눗셈","POLY.DIVISION.DEGREE_ARGUMENT","4PQ÷(P+Q) 몫 P+Q 나머지 R, R(1)=0, P(0)=1, Q(0)","나눗셈;차수","중",MC,"④ (1)","R=−(P−Q)², 차수 조건 → P=Q","4.6",c=M,i=M)
r(22,3,EQ,"이차방정식","근과 계수의 관계","EQ.VIETA.SQUARE_ROOTS_CONDITION","x²−4x+1=0 두 근, f(α²)=4β, f(β²)=4α, q−p","근과 계수","중",MC,"⑤ (31)","p=−15, q=16 (기호 계산)","4.7",c=M)
r(23,3,POLY,"인수분해","치환을 이용한 인수분해","POLY.FACTOR.SUBSTITUTION_PERFECT_SQUARE","{(x+1)(x+4)+8}(x+2)(x+3)+k (1) X²+aX+b (2) 완전제곱 k와 P (3) 48×42+k","인수분해;치환;서술","중",D,"(1) X=x²+5x, X²+18X+72+k (2) k=9, P=(x²+5x+9)² (3) 2025","x=4 대입: 45²","7",nsub=3,c=M)
r(24,3,EQ,"이차방정식","근과 계수의 관계","EQ.VIETA.RECIPROCAL_SUBSTITUTION","x²+3x+4=0 두 근, 1/(2α²+4α+4)+1/(2β²+4β+4)","근과 계수;서술","중하",D,"−1/4","2α²+4α+4=−2(α+2) → −(α+β+4)/(2(αβ+2(α+β)+4))","8",c=M)
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{846+i}", ROWS[i*10:(i+1)*10], 16619+i*10)
