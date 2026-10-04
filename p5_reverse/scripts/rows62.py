from cfgy2 import *
import cfgy2, builder
SQ = hashlib.sha256(open(OUT+'h62/Q.hwp','rb').read()).hexdigest()
setup(QID="A02462", SRC="1wKFGDRkT10-9iytWfVtvXK6cmGs3LSj9", SHA=SQ, TAG="SSM1E1", N=24, SUBJ="수학Ⅰ", SEC="SM1E",
      FNAME="[대단원평가문제] Ⅰ 지수함수+로그함수 (1).hwp", UNIT="Ⅰ. 지수함수와 로그함수", BIG="Ⅰ. 지수함수와 로그함수", EXAM="Ⅰ 지수함수와 로그함수 대단원 평가 문제", MID="지수함수와 로그함수 종합(대단원 평가)")
cfgy2.P.update(BOOK="신사고 수학Ⅰ", GRADE="고2", MEMO_X="대단원 평가 문제지(1~17 선택형, 18~24 서답형) — 같은 파일 내 '정답 및 풀이' 답표(24개)와 대조; 용문아 편집본 아님(학교 배포형 평가지 hwp); ")
L, M, H = "낮음", "보통", "높음"
S, D, MC = "서술형(단답)", "서술형", "5지선다"
E1, E2, E3, E4 = "지수", "로그", "지수함수", "로그함수"
def r(q, stmt, ans, small, tid, tname, tags, diff, fmt, a2, atype="값", fig="없음", final=None, c=L, d=L, i=L, trap="", combo="단일개념", chk="독립풀이 일치", **kw):
    it = dict(sec="대단원 평가 문제", act=None, stmt=stmt, ans=ans)
    R(q, it, small, tid, tname, tags, combo, diff, tname + ".", fmt, a2, atype, c, d, i, trap, chk, fig=fig, final=final, **kw)
r(1, "a>0, √(a³)=2일 때 ∜(a√(a²√(a⁴)))의 값 (3점)", "③", E1, "EXPONENT.NESTED_RADICAL.VALUE", "중첩 거듭제곱근 값", "거듭제곱근;지수법칙", "하", MC, "③", "선택지번호", final="③ (√2)")
r(2, "∛(√243)×(√3)^(−1/3)÷(1/3)^(−1/3)을 간단히 (3점)", "②", E1, "EXPONENT.RATIONAL.SIMPLIFY", "유리수 지수 간단히", "지수법칙", "하", MC, "②", "선택지번호", final="② (∛3)")
r(3, "3ˣ=2ʸ=20일 때 20^(1/x−1/y) (4점)", "③", E1, "EXPONENT.COMMON_VALUE.RECIPROCAL", "3ˣ=2ʸ=20 역수 지수", "지수법칙", "중하", MC, "③", "선택지번호", final="③ (3/2)", i=M)
r(4, "log₂(3/8)+2log₂(1/√12)의 값 (3점)", "①", E2, "LOG.PROPERTIES.EVALUATE", "로그 성질로 값 계산", "로그의 성질", "하", MC, "①", "선택지번호", final="① (−5)")
r(5, "28ˣ=32, 49ʸ=64일 때 5/x−3/y (5점)", "②", E2, "LOG.EXPONENT_TO_LOG.COMBINE", "지수식을 로그로 바꿔 결합", "로그의 정의;로그의 성질", "중", MC, "②", "선택지번호", final="② (2)", c=M, i=M)
r(6, "a>1, b>1, ab=36일 때 √(log₂a·log₂b) 최댓값 (5점)", "①", E2, "LOG.AM_GM.MAX", "산술·기하평균으로 로그곱 최대", "로그의 성질;산술평균과 기하평균", "중", MC, "①", "선택지번호", final="① (1+log₂3)", combo="로그+부등식", i=M)
r(7, "log₂3=a, log₂5=b일 때 log₁₂80을 a, b로 (3점)", "④", E2, "LOG.CHANGE_OF_BASE.EXPRESS", "밑변환으로 문자 표현", "로그의 밑의 변환", "하", MC, "④", "선택지번호", final="④ ((4+b)/(2+a))")
r(8, "log a의 정수 부분 3, 소수 부분 0.4일 때 a (4점)", "⑤", E2, "LOG.COMMON.CHARACTERISTIC_MANTISSA", "상용로그 정수·소수 부분으로 진수", "상용로그", "중하", MC, "⑤", "선택지번호", final="⑤ (1000·⁵√100)")
r(9, "x²−4x+2=0의 두 근 α, β에 대해 log_(α+β)4α+log_(α+β)β (3점)", "②", E2, "LOG.VIETA.COMBINE", "근과 계수의 관계+로그", "로그의 성질;근과 계수의 관계", "하", MC, "②", "선택지번호", final="② (3/2)", combo="로그+방정식")
r(10, "y=2^(x−1)−5 그래프 보기 판정 (4점)", "④", E3, "EXP_FUNC.GRAPH.STATEMENTS", "지수함수 그래프 성질 보기", "지수함수의 그래프;평행이동", "중하", MC, "④", "선택지번호", final="④ (ㄱ, ㄴ, ㄹ)", trap="제2사분면 통과 여부", d=M)
r(11, "y=2ˣ, y=4ˣ 그래프에서 AB=12일 때 a (5점)", "④", E3, "EXP_FUNC.TWO_GRAPHS.SEGMENT", "두 지수함수 그래프 사이 선분", "지수함수의 그래프;지수방정식", "중", MC, "④", "선택지번호", fig="그래프", final="④ (2)", c=M, chk="독립풀이 일치(x=a에서 4ᵃ−2ᵃ=12 해석, 그림 배치)")
r(12, "y=log_(1/2)(−3x+1)+2 설명 중 옳은 것 (4점)", "⑤", E4, "LOG_FUNC.PROPERTIES.CORRECT_STATEMENT", "로그함수 성질 판정", "로그함수의 그래프", "중하", MC, "⑤", "선택지번호", final="⑤", d=M, trap="밑<1과 −3x 합성 → 증가")
r(13, "y=log₂x 그래프에서 x₁+x₃ (점선 축 평행) (4점)", "⑤", E4, "LOG_FUNC.GRAPH.READ_CHAIN", "로그 그래프 점선 따라 좌표 읽기", "로그함수의 그래프", "중하", MC, "⑤", "선택지번호", fig="그래프", final="⑤ (18)", review="REVIEW-그림판독", chk="그림 객체 미추출 — 해설(x₁=2, x₃=16) 기준")
r(14, "4^(2x)+a·4^(x+1)+8=0의 두 근의 비 1:2일 때 a (5점)", "②", E3, "EXP_EQ.SUBSTITUTION.ROOT_RATIO", "치환 지수방정식 근의 비", "지수방정식;근과 계수의 관계", "중상", MC, "②", "선택지번호", final="② (−3/2)", c=M, i=H, combo="지수+방정식")
r(15, "모든 x>0에서 (log x)²+log 100x−k≥0인 k 범위 (4점)", "⑤", E4, "LOG_INEQ.QUADRATIC.ALWAYS", "로그 치환 이차부등식 항상 성립", "로그부등식;판별식", "중", MC, "⑤", "선택지번호", final="⑤ (k≤7/4)", combo="로그+부등식", i=M)
r(16, "x=1600000·0.75ᵗ, 처음 90만 원 이하 (4점)", "①", E3, "EXP_INEQ.CONTEXT.DEPRECIATION", "감가 지수부등식", "지수부등식", "하", MC, "①", "선택지번호", final="① (2년)")
r(17, "매년 5% 상승, 처음 2배 이상 (log2=0.3010, log1.05=0.0212) (5점)", "②", E2, "LOG.COMMON.GROWTH_DOUBLING", "상용로그 성장 배가 시간", "상용로그;지수부등식", "중하", MC, "②", "선택지번호", final="② (15년)")
r(18, "(⁶√7−⁶√5)(⁶√7+⁶√5)(∛49+∛35+∛25) 계산 (3점)", "2", E1, "EXPONENT.RADICAL.FACTOR_IDENTITY", "곱셈공식으로 거듭제곱근 계산", "거듭제곱근;곱셈공식", "중하", S, "2", trap="a³−b³ 인수분해")
r(19, "(aˣ+a⁻ˣ)/(aˣ−a⁻ˣ)=2일 때 (a³ˣ+a⁻ˣ)/(a³ˣ−a⁻ˣ) (서술형 5점)", "5/4", E1, "EXPONENT.RATIO_EXPRESSION", "지수 분수식 값", "지수법칙", "중", D, "5/4", i=M)
r(20, "log2.871=0.458, log3=0.4771로 (1/3)²⁰ (서술형 5점)", "2.871×10⁻¹⁰", E2, "LOG.COMMON.LARGE_POWER_VALUE", "상용로그로 거듭제곱 값", "상용로그", "중하", D, "2.871×10⁻¹⁰", trap="음의 지표 처리")
r(21, "벽 통과마다 25% 감소, 2% 이하 되는 최소 횟수 (서술형 5점)", "14번", E2, "LOG.COMMON.DECAY_THRESHOLD", "상용로그 감쇠 최소 횟수", "상용로그;지수부등식", "중하", D, "14번", trap="음수로 나눌 때 부등호 방향")
r(22, "y=a^(x²−4x+7)의 최댓값 1/27일 때 a (5점)", "1/3", E3, "EXP_FUNC.MAX.QUADRATIC_EXPONENT", "이차식 지수 최대", "지수함수의 최대·최소", "중하", S, "1/3", trap="밑 0<a<1", combo="지수+이차함수")
r(23, "(1/5)^(2x)<(1/25)^(x²−2) 정수 x 개수 (서술형 5점)", "2", E3, "EXP_INEQ.SAME_BASE.INTEGER_COUNT", "같은 밑 지수부등식 정수 개수", "지수부등식", "중하", D, "2")
r(24, "(log₃x)²+k·log₃x−8=0 두 근 곱 9일 때 k (4점)", "−2", E4, "LOG_EQ.QUADRATIC.ROOT_PRODUCT", "로그 치환 이차방정식 근의 곱", "로그방정식;근과 계수의 관계", "중하", S, "−2", combo="로그+방정식")
for i in range(3): build(f"Batch{493+i}", ROWS[i*10:(i+1)*10], 13344+i*10)
print(len(ROWS))
