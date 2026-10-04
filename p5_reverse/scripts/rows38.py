from cfgp2 import *
import hashlib, builder
SRC = "1Z1IMjxTSPa3icBggYCzC2Nqna9qsnwWd"
setup(QID="A02438", SRC=SRC, SHA="미산출(10MB 초과·10MB 초과 다운로드 불가, Drive 텍스트층 판독)", TAG="CJPS100", NPAGES="교과서 8~41쪽(34쪽)",
      FNAME="천재이 확률과통계 교과서 1단원.pdf (10MB 초과)", UNIT="Ⅰ. 경우의 수", BIG="확률과 통계", SEC="CJ1A", EXAM="천재(이) 확률과 통계 교과서 Ⅰ. 경우의 수", MID="여러 가지 순열", POFF=0,
      BOOK="천재(이) 확률과 통계 교과서", SUBJ="확률과 통계", GRADE="고2",
      KEYNOTE="정답지 미연결 — 정답은 교과서 136~139쪽(본 파일 범위 밖)",
      NOKEYNOTE="정답지 미연결(정답 136~139쪽은 본 단원 PDF에 미포함) — 독립풀이 단독",
      VISUAL="Drive read_file_content 텍스트층 판독(원본 10MB 초과로 렌더 불가); 분수 글리프(;a\\b; 꼴) 문맥 복원",
      TEXTST="FULL_TEXT(Drive 텍스트층, 교과서 8~41쪽 전체; 그림 내용 없음, 분수 글리프 일부 손상)",
      MEMO="천재(이) 확률과 통계 Ⅰ단원 PDF; 문제·예제·소단원 확인·중단원 연습·대단원 종합·창의 탐구/함께 생각하는 탐구/수학 체험(정량 답 있는 것) 행 생성(생각 열기·탐구 활동·알고 있나요 제외); ")
builder.P = 'd' + hashlib.sha256(SRC.encode()).hexdigest()[:11]
SECS = {"1-1": ("CJ1A", "원순열"), "1-2": ("CJ1B", "중복순열"), "1-3": ("CJ1C", "같은 것이 있는 순열"), "1-4": ("CJ1D", "중복조합"),
        "1M": ("CJ1E", "순열과 조합(중단원 연습)"), "2-1": ("CJ1F", "이항정리"), "2M": ("CJ1G", "이항정리(중단원 연습)"), "T": ("CJ1H", "경우의 수(대단원 종합)")}
for k, (s_, m) in SECS.items(): builder.SECTIONS[s_] = ("천재(이) 확률과 통계 Ⅰ. 경우의 수", m)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, D, MC, ACT = "서술형(단답)", "서술형", "5지선다", "서술형(활동)"
CP, RP, IP, SP, BT = "원순열", "중복순열", "같은 것이 있는 순열", "중복조합", "이항정리"
HOLDG = dict(ready="HOLD", status="판독 불가(원본 >10MB·그림 내용 텍스트층 부재)", trust="낮음(그림 조건 미확정)", review="HOLD-그림판독")
GL = dict(review="REVIEW-기호글리프")
q = [0]
def r(sec, label, page, small, tid, tname, tags, diff, fmt, ans, summ, chk, atype="값", nsub=1, c=L, d=L, i=L, trap="", combo="단일개념", why="", **kw):
    q[0] += 1
    P['SEC'] = SECS[sec][0]
    R(q[0], label, page, small, tid, tname, tags, combo, diff, (why or tname + ".") + E, fmt, ans, atype, c, d, i, trap, summ, chk, nsub=nsub, **kw)
r("1-1", "1-1-예제1", 12, CP, "PERM.CIRCULAR.FAMILY", "가족 원탁(예제)", "원순열", "하", S, "(1) 120 (2) 48 (3) 24", "부모 포함 6명", "5!; 4!·2!; 4!", nsub=3, worked=True)
r("1-1", "1-1-문제1", 12, CP, "PERM.CIRCULAR.ADJ_OPPOSITE", "8명 원형 안무 이웃·마주 보기", "원순열", "하", S, "(1) 5040 (2) 1440 (3) 720", "A, B 포함 8명", "7!; 6!·2; 6!", nsub=3, trap="마주 보기=한 명 고정 후 6!")
r("1-1", "1-1-확인1", 13, CP, "PERM.CIRCULAR.MATCH", "원순열 값 찾기", "원순열", "하", S, "(1) 24 (2) 144", "의자 5개; 여4 남3 남자끼리 이웃", "4!; 4!·3!(보기 24, 72, 48, 144)", nsub=2)
r("1-1", "1-1-확인2", 13, CP, "PERM.CIRCULAR.CENTER_PLATE", "가운데 칸 있는 접시 담기", "원순열", "중하", S, "840", "가운데 1칸+둘레 6칸, 음식 7가지", "7×5!", c=M, trap="가운데 칸은 회전 불변")
r("1-1", "1-1-확인3", 13, CP, "PERM.CIRCULAR.TRIANGLE_TABLE", "정삼각형 탁자 6명", "원순열", "중하", D, "㈎ 720 ㈏ 3 ㈐ 240", "변마다 2석", "6!/3", nsub=3, fig="그림", i=M, review="REVIEW-그림판독")
r("1-2", "1-2-문제1", 15, RP, "PERM.REPETITION.EVAL", "중복순열의 수", "중복순열", "하", S, "(1) 36 (2) 243 (3) 256", "6Π2, 3Π5, 4Π4", "nʳ", nsub=3)
r("1-2", "1-2-문제2", 15, RP, "PERM.REPETITION.CHOICE", "3명이 4기관 중 택하기", "중복순열", "하", S, "64", "학생 3, 기관 4", "4³")
r("1-2", "1-2-문제3", 15, RP, "PERM.REPETITION.DIGITS_ZERO", "0 포함 중복 네 자리 수·짝수", "중복순열", "하", S, "(1) 500 (2) 300", "0~4", "4·5³; 4·5²·3", nsub=2, trap="맨 앞 0 불가")
r("1-2", "1-2-예제1", 15, RP, "PERM.REPETITION.MAILBOX", "느린 우체통(예제)", "중복순열", "하", S, "81", "편지 4, 우체통 3", "3⁴", worked=True)
r("1-2", "1-2-확인1", 16, RP, "PERM.REPETITION.SOLVE_EQ", "중복순열 등식 n, r", "중복순열", "하", S, "(1) n=4 (2) r=6", "nΠ4=256, 3Πr=729", "지수", nsub=2)
r("1-2", "1-2-확인2", 16, RP, "PERM.REPETITION.FUNCTION_COUNT", "함수의 개수", "중복순열;함수", "하", S, "125", "X 3원소→Y 5원소", "5³")
r("1-2", "1-2-확인3", 16, RP, "PERM.REPETITION.ORDER_POSITION", "3000보다 큰 수·2543의 순서", "중복순열", "중", S, "(1) 375 (2) 383번째", "1~5 중복 네 자리", "2543보다 큰 수 375+5+2=382", nsub=2, c=M, i=M)
r("1-2", "1-2-확인4", 16, RP, "PERM.REPETITION.ERROR_ANALYSIS", "야구공 나누기 풀이 오류", "중복순열", "중하", D, "81 (공마다 학생 3명 중 1명: 3⁴; 한석·현진 모두 오류)", "서로 다른 공 4, 학생 3", "3Π4", atype="값+서술", i=M, trap="nΠr에서 n·r 역할")
r("1-3", "1-3-문제1", 18, IP, "PERM.IDENTICAL.WORD_VOWEL_ENDS", "같은 문자 포함 단어 배열", "같은 것이 있는 순열", "하", S, "(1) 15120 (2) 1260", "a,l,l,i,s,w,e,l,l", "9!/4!; 3·2·7!/4!", nsub=2)
r("1-3", "1-3-예제1", 19, IP, "PERM.IDENTICAL.SHORTEST_PATH", "최단 경로(예제)", "같은 것이 있는 순열", "하", S, "35", "오른쪽 4, 위 3", "7!/(4!3!)", worked=True, fig="도로망")
r("1-3", "1-3-문제2", 19, IP, "PERM.IDENTICAL.SHORTEST_PATH_VIA", "P 경유 최단 경로", "같은 것이 있는 순열;곱의 법칙", "하", S, "미산출(도로망 그림 판독 불가)", "A→P→B", "그림 의존", fig="도로망", final="미산출", **HOLDG)
r("1-3", "1-3-창의탐구", 19, IP, "PERM.IDENTICAL.AS_COMBINATION", "같은 것이 있는 순열을 조합으로", "같은 것이 있는 순열;조합", "하", ACT, "(1) ₇C₄×₃C₃ (2) ₇C₃×₄C₂×₂C₂(=210)", "A4B3; A3B2C2", "자리 선택", nsub=2)
r("1-3", "1-3-확인1", 20, IP, "PERM.IDENTICAL.CARDS_MATCH", "글자 카드 배열 수 찾기", "같은 것이 있는 순열", "하", S, "미산출(카드 글자 배치 텍스트층 판독 불가)", "보기 140, 1260, 1680, 2520", "카드 구성 미확정", nsub=4, final="미산출", **HOLDG)
r("1-3", "1-3-확인2", 20, IP, "PERM.IDENTICAL.FLAGS", "깃발 신호·양 끝 파란 깃발", "같은 것이 있는 순열", "하", S, "(1) 210 (2) 10", "빨3 파2 초2", "7!/(3!2!2!); 5!/(3!2!)", nsub=2)
r("1-3", "1-3-확인3", 20, IP, "PERM.IDENTICAL.MATCH_SEVEN_SETS", "7세트에서 A 승리 확정", "같은 것이 있는 순열", "중하", S, "20", "먼저 4세트, 7세트까지", "6세트 3:3 → ₆C₃", c=M, trap="7세트는 A 승")
r("1-3", "1-3-확인4", 20, IP, "PERM.IDENTICAL.PATH_VIA_AVOID", "P 지나고 Q 지나지 않는 경로", "같은 것이 있는 순열", "중하", D, "미산출(도로망 그림 판독 불가)", "A→B, P 경유·Q 회피", "그림 의존", fig="도로망", final="미산출", **HOLDG)
r("1-4", "1-4-문제1", 22, SP, "COMB.REPETITION.BASIC", "골프공 3종 중 7개", "중복조합", "하", S, "36", "3H7", "₉C₇")
r("1-4", "1-4-예제1", 22, SP, "COMB.REPETITION.EXPANSION_TERMS", "(a+b+c)⁶ 항의 개수(예제)", "중복조합", "하", S, "28", "3H6", "₈C₆", worked=True)
r("1-4", "1-4-문제2", 22, SP, "COMB.REPETITION.EXPANSION_TERMS", "(a+b+c+d)³ 항의 개수", "중복조합", "하", S, "20", "4H3", "₆C₃")
r("1-4", "1-4-예제2", 23, SP, "COMB.REPETITION.EQUATION_SOLUTIONS", "x+y+z=8 정수해(예제)", "중복조합", "하", S, "(1) 45 (2) 21", "3H8; 3H5", "치환", nsub=2, worked=True)
r("1-4", "1-4-창의탐구", 23, SP, "COMB.REPETITION.TERMS_PITFALL", "(x²+x+1)³ 항의 개수 오류", "중복조합;다항식의 전개", "중하", D, "선미가 잘못(다른 선택이 같은 차수의 항을 만듦) — 항의 개수 7", "선미 3H3=10 vs 수훈 7", "차수 0~6", atype="서술+값", i=M, trap="같은 문자 거듭제곱 항 중복")
r("1-4", "1-4-문제3", 24, SP, "COMB.REPETITION.EQUATION_SOLUTIONS", "x+y+z+w=6 정수해", "중복조합", "하", S, "(1) 84 (2) 10", "4H6; 4H2", "₉C₆; ₅C₂", nsub=2)
r("1-4", "1-4-확인1", 24, SP, "COMB.REPETITION.IDENTITY", "중복조합 등식 n, r", "중복조합", "하", S, "(1) n=9 (2) r=6", "6H4=nC4, 3Hr=8C6", "nHr=n+r−1Cr", nsub=2)
r("1-4", "1-4-확인2", 24, SP, "COMB.REPETITION.EQUATION_BOUNDS", "x+y+z=9 정수해(하한 조건)", "중복조합", "하", S, "(1) 55 (2) 28 (3) 10", "음이 아닌, 양의, x≥1·y≥2·z≥3", "3H9; 3H6; 3H3('\\>'를 ≥로 판독)", nsub=3, **GL)
r("1-4", "1-4-확인3", 24, SP, "COMB.VS_REPETITION.MILK", "우유 3개 구입(서로 다른/중복)", "조합;중복조합", "하", S, "(1) 10 (2) 35", "5종", "₅C₃; 5H3", nsub=2)
r("1-4", "1-4-확인4", 24, SP, "COMB.REPETITION.ANONYMOUS_VOTE", "무기명 투표 결과 경우의 수", "중복조합", "중하", D, "496", "유권자 30, 후보 3", "3H30=₃₂C₂", c=M)
r("1-4", "1-4-확인5", 24, SP, "COMB.FUNCTIONS.INCREASING_NONDECREASING", "증가·비감소 함수 개수", "조합;중복조합;함수", "중하", D, "(1) 20 (2) 56", "X 3원소→Y 6원소", "₆C₃; 6H3", nsub=2, **GL)
r("1-4", "1-4-함께탐구", 25, SP, "COMB.REPETITION.BIJECTION_PROOF", "일대일대응으로 중복조합 수", "중복조합", "중하", ACT, "2H4=₅C₄=5, 3H3=₅C₃=10", "자리별 0,1,2,3 더하기", "일대일대응", nsub=2, i=M)
r("1M", "1중-01", 26, CP, "PERM.CIRCULAR.HEXAGON_TABLE", "정육각형 탁자 6명", "원순열", "하", S, "120", "변마다 1명", "5!", fig="그림")
r("1M", "1중-02", 26, RP, "PERM.REPETITION.DIGITS_ZERO", "0,1,2로 네 자리 수", "중복순열", "하", S, "54", "맨 앞 1,2", "2·3³")
r("1M", "1중-03", 26, IP, "PERM.IDENTICAL.LETTERS", "A,A,B,B,B,C 배열", "같은 것이 있는 순열", "하", S, "60", "6글자", "6!/(2!3!)")
r("1M", "1중-04", 26, SP, "COMB.REPETITION.AT_LEAST_ONE", "과일 바구니 각 종류 1개 이상", "중복조합", "하", S, "21", "3종 8개", "3H5")
r("1M", "1중-05", 27, CP, "PERM.CIRCULAR.COUPLES_ADJACENT", "세 쌍 부부 이웃하여 원탁", "원순열", "중하", S, "16", "부부 3쌍", "2!·2³", c=M)
r("1M", "1중-06", 27, CP, "PERM.CIRCULAR.COLORING_FIGURE", "5영역 도형 색칠", "원순열", "중하", S, "미산출(영역 그림 판독 불가)", "5색 모두", "그림 의존", fig="그림", final="미산출", **HOLDG)
r("1M", "1중-07", 27, IP, "PERM.IDENTICAL.ORDER_CONSTRAINT", "b, d, f 순서 고정 배열", "같은 것이 있는 순열", "하", S, "120", "6문자", "6!/3!", trap="순서 고정=같은 것 취급")
r("1M", "1중-08", 27, SP, "COMB.REPETITION.ODD_SOLUTIONS", "x+y+z=11 홀수 양의 정수해", "중복조합", "중하", S, "15", "x=2a+1 치환", "a+b+c=4 → 3H4", c=M)
r("1M", "1중-09", 27, RP, "PERM.REPETITION.FUNCTION_CONDITION", "f(1)+f(2)=3인 함수 개수", "중복순열;함수", "중하", S, "250", "X→X, 5원소", "2·5³")
r("1M", "1중-10", 27, IP, "PERM.IDENTICAL.PATHS_NOT_MEET", "두 사람이 만나지 않는 최단 경로", "같은 것이 있는 순열", "중상", D, "미산출(도로망 그림 판독 불가)", "동시 출발 같은 속력", "그림 의존", fig="도로망", final="미산출", **HOLDG)
r("2-1", "2-1-예제1", 30, BT, "BINOM.EXPAND.SIGNED", "(x−2y)³ 전개(예제)", "이항정리", "하", S, "x³−6x²y+12xy²−8y³", "이항정리", "공식", worked=True)
r("2-1", "2-1-문제1", 30, BT, "BINOM.EXPAND.COEFF_POWER", "이항정리로 전개", "이항정리", "하", S, "(1) 81a⁴+108a³b+54a²b²+12ab³+b⁴ (2) a⁵−10a⁴b+40a³b²−80a²b³+80ab⁴−32b⁵", "(3a+b)⁴, (a−2b)⁵", "이항계수", atype="식", nsub=2, c=M)
r("2-1", "2-1-예제2", 30, BT, "BINOM.COEFF.RECIPROCAL_TERM", "(3x−2/x)⁶의 x⁴ 계수(예제)", "이항정리", "하", S, "−2916", "일반항", "r=1", worked=True)
r("2-1", "2-1-문제2", 31, BT, "BINOM.COEFF.RECIPROCAL_TERM", "x³ 계수·상수항", "이항정리", "하", S, "(1) 240 (2) −160", "(2x+3/x)⁵, (x−2/x)⁶로 판독", "r=1: ₅C₁·2⁴·3; r=3: ₆C₃(−2)³", nsub=2, **GL)
r("2-1", "2-1-문제3", 32, BT, "BINOM.PASCAL.EXPAND", "파스칼 삼각형으로 전개", "파스칼 삼각형", "하", S, "(1) a⁶+6a⁵b+15a⁴b²+20a³b³+15a²b⁴+6ab⁵+b⁶ (2) x⁷−7x⁶y+21x⁵y²−35x⁴y³+35x³y⁴−21x²y⁵+7xy⁶−y⁷", "(a+b)⁶, (x−y)⁷", "계수 행", atype="식", nsub=2)
r("2-1", "2-1-문제4", 32, BT, "BINOM.COEFF_SUM.POWER_OF_TWO", "이항계수의 합", "이항계수의 성질", "하", S, "(1) 512 (2) 1024", "₉Cᵣ 합, ₁₀Cᵣ 합", "2ⁿ", nsub=2)
r("2-1", "2-1-예제3", 32, BT, "BINOM.COEFF_SUM.PROOF", "이항계수 합 2ⁿ 증명(예제)", "이항계수의 성질", "하", "서술형(증명)", "(1+x)ⁿ에 x=1 대입", "증명", "대입", atype="증명", worked=True)
r("2-1", "2-1-문제5", 32, BT, "BINOM.ALTERNATING_EVEN_ODD.PROOF", "교대합 0·짝수항 합=홀수항 합 증명", "이항계수의 성질", "중하", "서술형(증명)", "(1) x=−1 대입 (2) x=±1 대입한 두 식을 더하고 빼면 각각 2²ⁿ⁻¹", "증명", "대입", atype="증명", nsub=2, i=M)
r("2-1", "2-1-확인1", 33, BT, "BINOM.COEFF.MATCH", "항의 계수 연결", "이항정리", "하", S, "(1) ㉢ 60 (2) ㉠ 24 (3) ㉡ 36", "(a+2)⁶ a⁴, (a+2b)⁴ a²b², (3a+2b)³ ab²", "₆C₂·4; ₄C₂·4; ₃C₂·3·4", nsub=3)
r("2-1", "2-1-확인2", 33, BT, "BINOM.PASCAL.IDENTITY", "nCr+nCr+1=8C4인 n, r", "파스칼 삼각형", "하", S, "n=7, r=3", "파스칼 성질", "ₙ₊₁Cᵣ₊₁")
r("2-1", "2-1-확인3", 33, BT, "BINOM.COEFF_SUM.FIND_N", "이항계수 합 조건 n", "이항계수의 성질", "하", S, "(1) 6 (2) 10", "합=2ⁿ, 1000<2ⁿ<2000", "2¹⁰=1024", nsub=2)
r("2-1", "2-1-확인4", 33, BT, "BINOM.COEFF.RECIPROCAL_TERM", "(x²−2/x)⁷ 계수", "이항정리", "중하", S, "(1) −280 (2) 448", "x⁵, 1/x⁴", "x¹⁴⁻³ʳ: r=3, r=6", nsub=2, c=M, **GL)
r("2-1", "2-1-확인5", 33, BT, "BINOM.PASCAL.CASE_SPLIT", "회장 포함 여부로 대표 뽑기", "조합;파스칼 삼각형", "하", D, "252 (₉C₄+₉C₅=126+126=₁₀C₅)", "10명 중 5명", "합의 법칙", atype="값+서술", i=M)
r("2-1", "2-1-함께탐구", 34, BT, "BINOM.PASCAL.HOCKEY_STICK", "하키 스틱 성질", "파스칼 삼각형", "중하", ACT, "(1) ₃C₃+₄C₃+₅C₃=₆C₄, ₆C₀+₇C₁+₈C₂+₉C₃=₁₀C₃ (2) ① ₇C₃ ② ₁₁C₆", "파스칼 삼각형 대각선 합", "ₙCᵣ 누적", nsub=3, i=M)
r("2M", "2중-01", 35, BT, "BINOM.COEFF.SPECIFIC_TERM", "(x+2)⁷의 x⁵ 계수", "이항정리", "하", S, "84", "일반항", "₇C₂·4")
r("2M", "2중-02", 35, BT, "BINOM.ALTERNATING_ODD_SUM", "교대합·홀수항 합", "이항계수의 성질", "하", S, "(1) 0 (2) 2048", "₆Cᵣ 교대합; ₁₂C 홀수항", "0; 2¹¹", nsub=2)
r("2M", "2중-03", 35, BT, "BINOM.CONSTANT_TERM.FIND_A", "상수항 24인 양수 a", "이항정리", "하", S, "2", "(x−a/x)⁴", "₄C₂a²=24", **GL)
r("2M", "2중-04", 35, BT, "BINOM.ODD_SUM.FIND_N", "홀수항 합=512인 n", "이항계수의 성질", "하", S, "5", "2²ⁿ⁻¹=512", "2n−1=9")
r("2M", "2중-05", 35, BT, "BINOM.PRODUCT_COEFF.FIND_N", "(1+x)⁴(1+x²)ⁿ의 x² 계수", "이항정리", "중하", S, "6", "x² 계수 12", "₄C₂+n=12", c=M)
r("2M", "2중-06", 35, BT, "BINOM.COEFF_RATIO.FIND_A", "x⁴ 계수가 x⁵ 계수의 10배", "이항정리", "중하", S, "4", "(x+a)⁶", "15a²=10·6a")
r("T", "대단원-01", 38, RP, "PERM.REPETITION.RPS", "4명 가위바위보(객관식)", "중복순열", "하", MC, "⑤ (81)", "4명", "3⁴", atype="선택지")
r("T", "대단원-02", 38, CP, "PERM.CIRCULAR.SQUARE_COLORING", "정사각형 4등분 색칠(객관식)", "원순열;조합", "하", MC, "④ (210)", "7색 중 4색", "₇C₄·3!", atype="선택지", fig="그림")
r("T", "대단원-03", 38, IP, "PERM.IDENTICAL.MULTIPLE_OF_6", "6의 배수 여섯 자리 수(객관식)", "같은 것이 있는 순열", "중하", MC, "② (30)", "1,1,2,2,3,3", "합 12 → 일의 자리 2: 5!/(2!2!)", atype="선택지", c=M)
r("T", "대단원-04", 38, SP, "COMB.REPETITION.CRAYONS", "색연필 7개 선택(객관식)", "중복조합", "하", MC, "① (120)", "4색 각 7개", "4H7=₁₀C₇", atype="선택지")
r("T", "대단원-05", 38, BT, "BINOM.COEFF.FIND_A", "x³ 계수 70인 a(객관식)", "이항정리", "하", MC, "③ (1/2)", "(ax+2)⁷", "560a³=70", atype="선택지")
r("T", "대단원-06", 38, BT, "BINOM.PRODUCT.XY_COEFF", "(x+y)⁶(1+1/(xy))⁶의 xy 계수(객관식)", "이항정리", "중", MC, "① (300)", "두 일반항 곱", "i=3, j=2: 20·15", atype="선택지", c=M, i=M, **GL)
r("T", "대단원-07", 38, BT, "BINOM.SUM_TO_POWER.DIVISORS", "N=4¹⁰의 약수 개수(객관식)", "이항정리;약수", "중하", MC, "④ (21)", "Σ₁₀Cᵣ3ʳ", "(1+3)¹⁰=2²⁰", atype="선택지", i=M)
r("T", "대단원-08", 39, CP, "PERM.CIRCULAR.TRIANGLE_INCIRCLE", "정삼각형·내접원 7영역 색칠(객관식)", "원순열", "중", MC, "⑤ (1680)", "가운데 원 1+대칭 6영역 판독", "7×6!/3", atype="선택지", fig="그림", c=M, i=M, review="REVIEW-그림판독")
r("T", "대단원-09", 39, IP, "PERM.IDENTICAL.SHORTEST_PATH_FIGURE", "도로망 최단 경로(객관식)", "같은 것이 있는 순열", "중하", MC, "미산출(도로망 그림 판독 불가)", "A→B", "그림 의존", atype="선택지", fig="도로망", final="미산출", **HOLDG)
r("T", "대단원-10", 39, RP, "PERM.REPETITION.SET_PAIRS", "A∩B 고정 두 집합 정하기(객관식)", "중복순열;집합", "중하", MC, "④ (81)", "나머지 4원소 3가지씩", "3⁴", atype="선택지", c=M)
r("T", "대단원-11", 39, SP, "COMB.COMPOSITION.ORDERED_COLORS", "8칸 4색 순서대로 칠하기(객관식)", "중복조합", "중하", MC, "① (35)", "각 색 1칸 이상", "4H4=₇C₃", atype="선택지")
r("T", "대단원-12", 39, RP, "PERM.REPETITION.FUNCTION_EXCLUDE", "f(a)≠1 함수 개수(객관식)", "중복순열;함수", "하", MC, "③ (100)", "A 3원소→B 5원소", "4·5·5", atype="선택지", **GL)
r("T", "대단원-13", 39, SP, "COMB.REPETITION.PARITY_SOLUTIONS", "짝·홀 조건 정수해(객관식)", "중복조합", "중", MC, "② (56)", "x,y 짝수, z,w 홀수", "a+b+c+d=5 → 4H5", atype="선택지", c=M)
r("T", "대단원-14", 40, IP, "PERM.IDENTICAL.ORDERED_DIGITS", "숫자 오름차순 배열(서술형)", "같은 것이 있는 순열", "하", D, "210", "1,2,3,4,a,b,c", "7!/4!")
r("T", "대단원-15", 40, BT, "BINOM.HOCKEY_STICK.COEFF", "합의 x² 계수 a₂(서술형)", "이항정리;파스칼 삼각형", "중하", D, "165", "(1+x)²~(1+x)¹⁰", "Σ₂¹⁰ₖC₂=₁₁C₃", c=M)
r("T", "대단원-16", 40, SP, "COMB.REPETITION.FUNCTION_CONDITIONS", "조건 만족 비감소 함수 개수(서술형)", "중복조합;함수", "중", D, "87", "f(2)f(3)=6, f(n)≤f(n+1)", "(1,6): 1·6H... =15, (2,3): 2·₉C₂=72", c=M, i=H, **GL)
r("T", "대단원-17", 40, RP, "PERM.REPETITION.SUBSET_PAIRS", "A⊂B 공집합 아닌 부분집합 쌍(서술형)", "중복순열;집합", "중하", D, "211", "U 5원소", "3⁵−2⁵(A=∅ 제외)", c=M, **GL)
n = len(ROWS)
for i in range((n + 9) // 10): build(f"Batch{576+i}", ROWS[i*10:(i+1)*10], 14130+i*10)
print(n)
