from cfgex import *
MC, S_, D = "객관식(5지선다)", "단답형", "서술형"
M, H = "보통", "높음"
KEYQ=True
setup("A00595", "1PRooVJS-T0mDLuyMaW2TFBXLUzrB6Sx9", "2025년 고1 2학기 기말고사.pdf", "p4/A00595.pdf", "장훈고등학교", "2025학년도", "2학기 기말고사", "고1", "공통수학2", CURR="2022 개정", KEY={1: '② (5)', 2: '④ (필요충분, 충분)', 3: '② (유리수, 3m², 3k²)', 4: '④ (ㄱ, ㄴ, ㄹ)', 5: '③ (5/4)', 6: '① (1)', 7: '② (2)', 8: '① (5)', 9: '① (25)', 10: '③ (6)', 11: '④ (√22)', 12: '⑤ (5)', 13: '③ (0)', 14: '① (10)', 15: '④ (63/4)', 16: '③ (−2)', 17: '⑤ (−2/3)', 18: '⑤ (9)', 19: '6', 20: '3', 21: '−1', 22: '17', 23: '12'}, KEYPAGE="A00593 정답/배점표(선택형)·A00594 서답형 채점기준표", KEYSRC="15wv3f8SbZzGLE485K1qa-EstZeITaXci + 1zAhK-V2O-wINmpfokl2wgrg-JcNdy2mf",
      VIS="스캔 PDF(7쪽, 텍스트층 없음) 70dpi 렌더 + 130~160dpi 확대 시각판독", TEXT="텍스트층 없음 — 렌더 판독 확정")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
SET, FN = "집합과 명제", "함수와 그래프"
def r(q, page, big, mid, small, tid, tname, tags, diff, fmt, ans, chk, pts, **kw):
    kw.setdefault("atype", "선택지" if fmt == MC else "값")
    lab = str(q) if q <= 18 else f"서답{q-18}"
    R(q, page, big, mid, small, tid, tname, tags, diff, fmt, ans, f"장훈고 2025 1-2 기말 공통수학2 {lab}", chk, label=lab, pts=pts, **kw)
    ROWS[-1]["메모"] += "KEYLINK v2 (append-only 수리본): Batch834-836 동일 문항ID 대체 — 동반 정답지 A00593(선택형·서답1~5)/A00594(서답 채점기준) 연결; A00592 0바이트 txt; "
r(1,1,SET,"명제","명제와 진리집합","PROP.TRUTH_SET.INCLUSION_PARAM","p: −3<x≤2, q: |x−2|≤a, p→q 참 a 최솟값","명제;진리집합","하",MC,"② (5)","2−a≤−3","3.2")
r(2,1,SET,"명제","필요조건과 충분조건","PROP.NEC_SUFF.SET_EQUATIONS","p: A∩Bᶜ=Aᶜ∩B, q: 둘 다 ∅, r: A=B=∅","필요충분;집합 연산","중하",MC,"④ (필요충분, 충분)","p⟺A=B⟺q; r⇒q, 역 불성립","3.3",c=M,trap=M)
r(3,1,SET,"명제","귀류법","PROP.CONTRADICTION.SQRT3_FILL","√3 무리수 귀류법 (가)(나)(다)","귀류법;빈칸","하",MC,"② (유리수, 3m², 3k²)","","3.3")
r(4,2,SET,"명제","명제의 대우","PROP.CHAIN.CONTRAPOSITIVE_STATEMENTS","p⇒~q, ~q⇒r, q⇒~r 보기","대우;삼단논법","중하",MC,"④ (ㄱ, ㄴ, ㄹ)","ㄷ 불확정","3.4",c=M)
r(5,2,FN,"합성함수","합성함수","FUNC.COMPOSITE.SOLVE","f=4x+1, g=3x−3, (g∘f)(a)=15","합성함수","하",MC,"③ (5/4)","12a=15","3.5")
r(6,2,FN,"역함수","역함수","FUNC.INVERSE.LINEAR_PARAM","f=ax+b, f⁻¹(4)=3, f⁻¹(7)=5, f(1)","역함수","하",MC,"① (1)","a=3/2, b=−1/2","3.5")
r(7,2,FN,"무리함수","무리함수의 평행이동","FUNC.SQRT.TRANSLATE_POINT","y=√2x를 (−3, k) 이동, (5,6) 통과 k","무리함수;평행이동","하",MC,"② (2)","√16+k=6","3.6")
r(8,3,SET,"명제","명제의 참거짓","PROP.BOTH_FALSE.PARAM_SUM","p: |x−1|≤k, q: x²−4x−5<0, p→q, q→p 모두 거짓 자연수 k 합","명제;진리집합","중하",MC,"① (5)","k≥2 이고 k<4","3.7",c=M,trap=M)
r(9,3,SET,"명제","절대부등식","INEQ.AMGM.RIGHT_TRIANGLE_AREA","빗변 10 직각삼각형 넓이 최댓값","산술기하;절대부등식","하",MC,"① (25)","ab≤(a²+b²)/2=50","3.8")
r(10,3,FN,"합성함수","합성함수와 역함수","FUNC.FINITE.COMPOSITE_INVERSE_GRAPH","f, f∘g 그래프(A→A), g(4)+(g∘f)⁻¹(2)","합성함수;역함수;대응","중하",MC,"③ (6)","g=(1,5,2,3,4), g(4)=3, (g∘f)⁻¹(2)=3 (130dpi 확대 판독)","3.9",c=M,fig="그래프")
r(11,3,FN,"무리함수","무리함수의 역함수","FUNC.SQRT.INVERSE_INTERSECT_DISTANCE","f=√(3x−7)+5/2, 역함수 g, 두 교점 거리","무리함수;역함수","중",MC,"독립풀이: 교점 1개 (출제의도 ④ √22)","y=x 위 x²−8x+53/4=0 → x=(8±√11)/2, 작은 근 2.34<5/2로 치역 조건 위배 → 교점 1개; '두 교점'이 성립하지 않음 — 출제오류 의심(조건 무시 시 √2·√11=√22). 160dpi 확대로 식 확인","4",c=M,trap=H,review="HOLD-원문오류(교점 1개)",ready="HOLD",status="독립풀이로 문제 조건 불성립 — 원문 오류 의심",trust="낮음",conflict="원문조건충돌: f와 역함수 교점은 1개(작은 근 x=(8−√11)/2<5/2 치역 밖); 학교 정답 ④(√22)=조건 무시 계산 — 정답지 값 보존",final="교점 1개(문항 성립 불가; 출제의도 ④ √22)")
r(12,4,FN,"합성함수","합성함수의 방정식","FUNC.PIECEWISE.COMPOSITE_LEVEL_COUNT","X→X 구간별 일차 f, (f∘f)(a)=3 실수 a 개수","합성함수;그래프","중",MC,"⑤ (5)","f(a)∈{3/2, 3, 13/3} → 1+3+1","4.1",c=M,fig="그래프")
r(13,4,SET,"명제","절대부등식","INEQ.AMGM.SHIFTED_RECIPROCAL","x²+2x−a=0 서로 다른 실근, 4a+1/(a+1) 최솟값","산술기하","중하",MC,"③ (0)","a>−1, 4(a+1)+1/(a+1)−4≥0","4.2",c=M)
r(14,4,FN,"함수","함수의 치역","FUNC.SMALLEST_PRIME_FACTOR.RANGE","A={2..30}, f(n)=1 제외 최소 약수, 치역 원소 수","함수;소수","하",MC,"① (10)","30 이하 소수 10개","4.3")
r(15,4,FN,"합성함수","합성함수의 방정식","FUNC.PIECEWISE.FIXED_POINT_PREIMAGE","f 구간별(일차/이차), (f∘f)(a)=f(a) a 합","합성함수;고정점","중",MC,"④ (63/4)","f(a)∈{1/4, 4} → a=1/4, 13/2, 4, 5","4.4",c=M,trap=M)
r(16,5,FN,"무리함수","무리함수와 이차함수","FUNC.PIECEWISE_SQRT_QUAD.LEVEL_COUNT","f 구간별(−(x−a)²+b / −√(x−a)+b), 조건 (가)(나), α+β+γ=26, f(10β)","무리함수;방정식 실근 개수","중상",MC,"③ (−2)","β=a=b, α=a−2, γ=a+16 → a=4; f(40)=−6+4","4.5",c=M,i=M)
r(17,5,FN,"역함수","역함수의 존재 조건","FUNC.BIJECTION.PIECEWISE_QUAD","g 구간별, 역함수 존재·치역 R, h=−f(−x) 일대일 t 최솟값 −5, f(0)","역함수;일대일대응;이차함수","중상",MC,"⑤ (−2/3)","f(−1)=3, f(2)=−6, 꼭짓점 x=5 → f=(x−5)²/3−9","4.6",c=M,i=M)
r(18,5,FN,"역함수","일대일대응","FUNC.BIJECTION.PIECEWISE_PARAM_SET","h=f(x<a)/g(x+b)(x≥a) 일대일대응 (a,b) 집합 A, m 정수 m+b 합 p+q√3","일대일대응;이차함수","상",MC,"⑤ (9)","a∈[−3,−1], b=2−a+√(4−(a+1)²) → m=−3,−2,−1: 2, 2+√3, 4","4.7",c=H,i=H)
r(19,6,SET,"명제","반례","PROP.COUNTEREXAMPLE.COUNT","U=1..10, p 소수, q 3의 배수, p→q·q→p 반례 수 m, n, mn","반례;진리집합","하",S_,"6","m=3 {2,5,7}, n=2 {6,9}","4")
r(20,6,FN,"함수","일대일대응","FUNC.BIJECTION.QUAD_DOMAIN_PARAM","x²−3x: X={x≥k}→Y={y≥k−3} 일대일대응 k","일대일대응;이차함수","중하",S_,"3","k≥3/2, k²−3k=k−3","4",c=M,trap=M)
r(21,6,FN,"유리함수","유리함수의 평행이동","FUNC.RATIONAL.TRANSLATE_MATCH","(ax+b)/(x−2) = 3/x를 (2,4) 이동, a+b","유리함수;평행이동","하",S_,"−1","(4x−5)/(x−2)","4")
r(22,6,FN,"유리함수","유리함수와 정수 조건","FUNC.RATIONAL.INTEGER_VALUE_SUM","f=(5x+22)/(x+2), g=정수 판별, (g∘f)(x)=1 자연수 x 합","유리함수;약수","중하",S_,"17","x+2|12 → x=1,2,4,10","5",c=M)
r(23,7,FN,"합성함수","합성함수와 최솟값","FUNC.COMPOSITE.WINDOW_MIN_QUAD_SQRT","f 이차(양수), g=−√(x−1)+3, h(t)=[t−1,t]에서 f∘g 최솟값, 조건 (가)(나), f(4)","합성함수;무리함수;최솟값","상",S_,"12","꼭짓점 2, f=2(x−2)²+4 (h(6)=f(1)=6)","5",c=H,i=H)
r(24,7,FN,"무리함수","무리함수의 그래프","FUNC.SQRT_PIECEWISE.LEVEL_COUNT_PARAM","f=√(−x+a)−b, g 구간별, h(α)h(β)=4, 해 최소 −45 최대 15, g(172)","무리함수;교점 개수","상",D,"−13+4√3","b>0: α=b, β=2b, a−4b²=−45, a+b²=15 → a=3, b=2√3","8",c=H,i=H,review="REVIEW-정답지값잘림(A00594 채점기준 풀이 중간까지만 촬영)",ready="REVIEW",status="독립풀이; 채점기준 b>0 경우 분석까지 일치, 최종값 이미지 잘림",trust="중간")
n = len(ROWS); print(n)
for i in range((n + 9) // 10): build(f"Batch{837+i}", ROWS[i*10:(i+1)*10], 16546+i*10)
