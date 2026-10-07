import cfgex
from cfgp5 import *
D = "서술형"
NOTE = "공식 빈칸 워크시트(정답지 없음) — 표준 공식으로 독립 작성"
def src(QID, SRC, FN, PATH, SUBJ, GRADE, VIS):
    cfgex.ROWS.clear()
    setup(QID, SRC, FN, PATH, "자체 제작(공식 정리지)", "2026", "공식 확인 워크시트", GRADE, SUBJ, CURR="2022 개정", VIS=VIS, TEXT=VIS)
    builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
def row(q, page, big, mid, small, tid, tname, ans, lab, nsub=1, diff="하"):
    R(q, page, big, mid, small, tid, tname, mid+";공식", diff, D, ans, "공식 빈칸", NOTE, label=lab, nsub=nsub, atype="식")
    r = ROWS[-1]; r.update({"출처대분류": "자체 제작 공식 정리 워크시트", "학교/시험명": f"{cfgex.P['QID']} 공식 확인 {lab}"})
EXP = [("(a+b)²","a²+2ab+b²"),("(a−b)²","a²−2ab+b²"),("(a+b)(a−b)","a²−b²"),("(x+a)(x+b)","x²+(a+b)x+ab"),("(ax+b)(cx+d)","acx²+(ad+bc)x+bd"),
       ("(a+b+c)²","a²+b²+c²+2ab+2bc+2ca"),("(a+b)³","a³+3a²b+3ab²+b³"),("(a−b)³","a³−3a²b+3ab²−b³"),("(a+b)(a²−ab+b²)","a³+b³"),("(a−b)(a²+ab+b²)","a³−b³"),
       ("(a+b+c)(a²+b²+c²−ab−bc−ca)","a³+b³+c³−3abc"),("(a²+ab+b²)(a²−ab+b²)","a⁴+a²b²+b⁴")]
VAR = [("a²+b²","① (a+b)²−2ab ② (a−b)²+2ab"),("(a+b)²","(a−b)²+4ab"),("(a−b)²","(a+b)²−4ab"),("a³+b³","(a+b)³−3ab(a+b)"),("a³−b³","(a−b)³+3ab(a−b)"),
       ("x²+1/x²","(x+1/x)²−2 = (x−1/x)²+2"),("x³+1/x³","(x+1/x)³−3(x+1/x)"),("x³−1/x³","(x−1/x)³+3(x−1/x)"),("a²+b²+c²","(a+b+c)²−2(ab+bc+ca)"),
       ("a²+b²+c²−ab−bc−ca","½{(a−b)²+(b−c)²+(c−a)²}"),("a²+b²+c²+ab+bc+ca","½{(a+b)²+(b+c)²+(c+a)²}"),("a³+b³+c³","(a+b+c)(a²+b²+c²−ab−bc−ca)+3abc")]
out = []
# A00382
src("A00382","1OISyXf9thytxQREahWMKFhQVHpnfyHMt","곱셉공식.pdf","p5l/A00382/src.pdf","공통수학1","고1","텍스트층 PDF 2쪽 (FULL_TEXT_SAFE, 수식은 렌더 확인)")
for i,(e,a) in enumerate(EXP,1): row(i,1,"다항식","다항식의 연산","곱셈 공식","POLY.EXPANSION_FORMULA.RECALL",f"곱셈공식 {e} 전개",a,f"곱셈공식-{i}")
for i,(e,a) in enumerate(VAR,1): row(12+i,2,"다항식","다항식의 연산","곱셈 공식의 변형","POLY.FORMULA_VARIANT.RECALL",f"곱셈공식 변형 {e}",a,f"변형-{i}",nsub=2 if i==1 else 1)
build("A00382", list(ROWS), 115); out.append(len(ROWS)); n382=len(ROWS)
# A00380
src("A00380","1sqtE-2QSooD6JQZH4YI2s8XALY9uIcs3","곱셉공식(중3).hwp","p5l/A00380/src.hwp","중3 수학","중3","HWP 본문·수식 추출(로컬 파서)")
for i,(e,a) in enumerate(EXP[:5],1): row(i,1,"다항식의 곱셈","곱셈 공식","곱셈 공식","POLY.EXPANSION_FORMULA.RECALL",f"곱셈공식 {e} 전개",a,f"곱셈공식-{i}")
V6=[("a²+b²","① (a+b)²−2ab ② (a−b)²+2ab"),("(a+b)²","(a−b)²+4ab"),("(a−b)²","(a+b)²−4ab"),("x²+1/x²","① (x+1/x)²−2 ② (x−1/x)²+2"),("(x+1/x)²","(x−1/x)²+4"),("(x−1/x)²","(x+1/x)²−4")]
for i,(e,a) in enumerate(V6,1): row(5+i,1,"다항식의 곱셈","곱셈 공식","곱셈 공식의 변형","POLY.FORMULA_VARIANT.RECALL",f"곱셈공식 변형 {e}",a,f"변형-{i}",nsub=2 if i in (1,4) else 1)
sq = "; ".join(f"{k}²={k*k}" for k in range(2,20)); pw = "; ".join(f"{b}^{e}={b**e}" for b,e in [(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(3,3),(3,4),(3,5),(3,6),(5,3),(5,4),(6,3)])
row(12,2,"수와 연산","거듭제곱","제곱수·거듭제곱 암기","NUM.POWERS.TABLE_RECALL","제곱수(2²~19²)·거듭제곱(2³~2¹⁰, 3³~3⁶, 5³, 5⁴, 6³) 값",sq+"; "+pw,"거듭제곱표",nsub=33)
build("A00380", list(ROWS), 115+n382); n380=len(ROWS)
# A00381
src("A00381","1nqcRIvXX6-njQDNNm4rCw9Y11NK_E-uX","복소수.pdf","p5l/A00381/src.pdf","공통수학1","고1","텍스트층 PDF 2쪽 (FULL_TEXT_SAFE, 수식은 렌더 확인)")
C=("방정식과 부등식","복소수와 이차방정식")
L=[(1,"복소수","COMPLEX.DEF.POWERS_CONJUGATE","i, i², i³, i⁴, z=a+bi의 켤레","i=√−1, i²=−1, i³=−i, i⁴=1, z̄=a−bi",6),
   (1,"켤레복소수","COMPLEX.CONJUGATE.PROPERTIES","켤레복소수의 성질 7가지","z̿=z; z+z̄=2a(실수); zz̄=a²+b²(실수); conj(z₁+z₂)=z̄₁+z̄₂; conj(z₁−z₂)=z̄₁−z̄₂; conj(z₁z₂)=z̄₁z̄₂; conj(z₁/z₂)=z̄₁/z̄₂",7),
   (1,"음수의 제곱근","COMPLEX.NEG_SQRT.SIGN_COND","√−a, √a√b=−√(ab)·√a/√b=−√(a/b)일 때 a, b 부호","√−a=√a i (a>0); √a√b=−√ab ⇔ a<0, b<0; √a/√b=−√(a/b) ⇔ a>0, b<0",3),
   (1,"복소수의 제곱","COMPLEX.SQUARE.REAL_IMAG_COND","z=a+bi, z²이 양의 실수/음의 실수/순허수 조건","양의 실수: b=0, a≠0; 음의 실수: a=0, b≠0; 순허수: a=±b, ab≠0 (a²=b²)",3),
   (2,"이차방정식","EQ.QUADRATIC.FORMULA_VIETA_DISC","근의 공식, 근과 계수의 관계, 판별식","x=(−b±√(b²−4ac))/(2a); α+β=−b/a, αβ=c/a; D=b²−4ac (D>0 서로 다른 두 실근, D=0 중근, D<0 서로 다른 두 허근)",3),
   (2,"이차방정식","EQ.QUADRATIC.CONJUGATE_ROOT","켤레근의 성질(유리계수 p+q√m, 실계수 p+qi)","유리계수: p−q√m; 실계수: p−qi",2),
   (2,"이차함수","QUADF.COEFF_ROLE.LINE_POSITION","a의 부호, 대칭축, c, 직선 y=mx+n과 위치관계","a>0 아래로 볼록, a<0 위로 볼록; x=−b/(2a); c는 y절편; ax²+(b−m)x+(c−n)=0의 D>0 두 점, D=0 접함, D<0 만나지 않음",4)]
for i,(pg,sm,tid,tn,a,ns) in enumerate(L,1): row(i,pg,C[0],C[1],sm,tid,tn,a,f"항목{i}",nsub=ns)
build("A00381", list(ROWS), 115+n382+n380); n381=len(ROWS)
print(n382,n380,n381)
