from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h97/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h97/A.hwp','rb').read()).hexdigest()
setup(QID="A02497", SRC="18N1TwxaOZrAlqGMDPRD5Z8h9cllLdwJX", SHA=SQ, TAG="DSM2I101F", N=10,
      FNAME="15개정_고등_수학Ⅱ_3-1-01_소단원평가_기초_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I101F", EXAM="Ⅲ-1-01 부정적분 소단원평가(기초)", MID="부정적분",
      ANS_QID="A02517", ANS_SRC="1TGTkvB5tfFWVXfay3K9vuMg5259s5GyC", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"
U = "부정적분"
V = "값(소문항별)"
R(1, U, "INTEG.INDEF.INTEGRAND_FROM_ANTIDERIVATIVE", "부정적분 결과 미분으로 피적분함수 구하기", "부정적분의 정의;미분", "단일개념",
  "하", "양변 미분." + E, S, "(1) 4x (2) 3x²−2", V, L, L, L, "", "∫f dx=2x²+C / x³−2x+C일 때 f", "(2x²)'=4x, (x³−2x)'=3x²−2", nsub=2)
R(2, U, "INTEG.INDEF.POWER_RULE_BASIC", "상수·거듭제곱 함수의 부정적분", "부정적분;xⁿ의 부정적분", "단일개념",
  "하", "∫xⁿ=xⁿ⁺¹/(n+1)+C." + E, S, "(1) 5x+C (2) 3x²+C (3) x⁵/5+C (4) x⁸/8+C", V, L, L, L, "", "∫5, ∫6x, ∫x⁴, ∫x⁷", "거듭제곱 공식", nsub=4)
R(3, U, "INTEG.INDEF.INTEGRAND_FROM_ANTIDERIVATIVE", "부정적분 결과 미분으로 피적분함수 구하기", "부정적분의 정의;미분", "단일개념",
  "하", "양변 미분." + E, S, "(1) 2x−3 (2) x²+x", V, L, L, L, "", "∫f dx=x²−3x+C / x³/3+x²/2+C일 때 f", "미분", nsub=2)
R(4, U, "INTEG.INDEF.INTEGRAND_FROM_ANTIDERIVATIVE", "부정적분 결과 미분으로 피적분함수 구하기", "부정적분의 정의;미분", "단일개념",
  "하", "양변 미분." + E, S, "f(x)=6x+4", "식", L, L, L, "", "∫f dx=3x²+4x+C일 때 f", "6x+4")
R(5, U, "INTEG.INDEF.INTEGRAND_FROM_ANTIDERIVATIVE", "부정적분 결과 미분으로 피적분함수 구하기", "부정적분의 정의;미분", "단일개념",
  "하", "양변 미분." + E, S, "f(x)=3x²−2x", "식", L, L, L, "", "∫f dx=x³−x²+C일 때 f", "3x²−2x")
R(6, U, "INTEG.INDEF.INTEGRAND_FROM_ANTIDERIVATIVE", "부정적분 결과 미분으로 피적분함수 구하기", "부정적분의 정의;미분", "단일개념",
  "하", "양변 미분." + E, S, "f(x)=x³+x²+x", "식", L, L, L, "", "∫f dx=x⁴/4+x³/3+x²/2+C일 때 f", "x³+x²+x")
R(7, U, "INTEG.INDEF.INTEGRAL_OF_DERIVATIVE", "∫(d/dx f)dx = f+C", "부정적분과 미분의 관계;적분상수", "단일개념",
  "하", "적분상수 유무 구분." + E, S, "x²+C", "식", L, M, L, "적분상수 C 누락", "∫(d/dx x²)dx", "f+C 성질")
R(8, U, "INTEG.INDEF.DERIVATIVE_OF_INTEGRAL", "d/dx∫f dx = f", "부정적분과 미분의 관계", "단일개념",
  "하", "C 소거." + E, S, "x²", "식", L, M, L, "C 붙이는 실수", "d/dx ∫x² dx", "f 성질")
R(9, U, "INTEG.INDEF.INTEGRAND_FROM_ANTIDERIVATIVE", "부정적분 결과 미분으로 피적분함수 구하기", "부정적분의 정의;미분", "단일개념",
  "하", "양변 미분." + E, S, "(1) 2x² (2) 6x−2", V, L, L, L, "", "∫f dx=(2/3)x³+C / 3x²−2x+C일 때 f", "미분", nsub=2)
R(10, U, "INTEG.INDEF.DIFF_INTEGRAL_ORDER_CONTRAST", "∫(d/dx f)dx 와 d/dx∫f dx 비교", "부정적분과 미분의 관계;적분상수", "단일개념",
  "하", "연산 순서 구분." + E, S, "(1) 6x⁵+C (2) 6x⁵", V, L, M, L, "연산 순서·C 유무",
  "f(x)=6x⁵일 때 (1) ∫{d/dx f}dx (2) d/dx∫f dx",
  "(1) ∫f'dx=f+C=6x⁵+C (2) d/dx∫f dx=f=6x⁵. 해설은 (1) x⁶+C (2) x⁶ — 해설 본문 스스로 'f(x)+C', 'f(x)'라 쓰고도 f를 적분한 x⁶을 대입한 오류",
  nsub=2, keymatch=False, key="(1) x⁶+C (2) x⁶", final="(1) 6x⁵+C (2) 6x⁵ (독립풀이; 해설 x⁶ 계열은 오류)",
  conflict="해설 답 (1) x⁶+C (2) x⁶ 은 f=6x⁵의 부정적분을 대입한 오류. 성질 ∫f'dx=f+C, d/dx∫f=f에 따르면 6x⁵+C, 6x⁵",
  ready="REVIEW", status="독립풀이-해설 불일치(해설 오류)", trust="중간(해설 오류 판정, 원문 정상)", review="REVIEW-정답충돌")
build("Batch293", ROWS, 11446)
