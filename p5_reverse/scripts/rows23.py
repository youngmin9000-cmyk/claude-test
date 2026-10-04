from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h23/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h23/A.hwp','rb').read()).hexdigest()
setup(QID="A02623", SRC="1Ym67fCAHuL40gBONrpIXgFCCPtcuNMnN", SHA=SQ, TAG="DSM2C11D", N=10,
      FNAME="15개정_고등_수학Ⅱ_1-1_중단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅰ. 함수의 극한과 연속", BIG="Ⅰ. 함수의 극한과 연속", SEC="C11D", EXAM="Ⅰ-1 함수의 극한 중단원평가(발전)", MID="함수의 극한",
      ANS_QID="A02622", ANS_SRC="1b7lUs-K6LLE1grUNQMHMoGmBxPWyZ8zu", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
R(1, "함수의 극한(미정계수)", "LIM.UNDET.POLY_DEGREE_FROM_TWO_LIMITS", "두 극한 존재 조건으로 다항식 차수·계수 결정", "미정계수;다항함수;∞/∞꼴;0/0꼴", "극한+다항식",
  "중하", "차수 1, 상수항 0." + E, MC, "③", "선택지번호", L, M, M, "", "다항 f: lim f/x (x→0), lim f/x (x→∞) 모두 존재, lim_{x→0} f/x=3일 때 lim_{x→∞} 2f/(3x−4)", "f=3x → 2 ③", final="③ (2)")
R(2, "함수의 극한에 대한 성질", "LIM.PROP.SHIFTED_ARGUMENT_SUBST", "치환으로 평행이동된 극한 조건 활용", "극한의 성질;치환", "극한+치환",
  "중하", "t=x−3 치환." + E, MC, "④", "선택지번호", L, M, M, "", "lim_{x→0} f/x=24일 때 lim_{x→3} f(x−3)/(x²−9)", "24·1/6=4 ④", final="④ (4)")
R(3, "함수의 극한에 대한 성질", "LIM.PROP.GIVEN_RATIO_SUBSTITUTE", "주어진 극한 f(x)/x 이용 — 분모·분자 x로 나누기", "극한의 성질;0/0꼴", "단일개념",
  "하", "x로 나눔." + E, MC, "③", "선택지번호", L, L, L, "", "lim f/x=α≠0일 때 lim (3f−x²)/(f+5x²)", "3α/α=3 ③", final="③ (3)")
R(4, "함수의 극한(미정계수)", "LIM.UNDET.TWO_ROOT_CONDITIONS_TF", "두 0/0 극한 조건 → 근·합성 성질 참거짓", "미정계수;다항함수;인수정리;반례", "극한+논리",
  "중상", "반례 x(x−2) 구성." + E, MC, "①", "선택지번호", M, M, H, "일차라고 단정 금지", "lim f/x (x→0) + lim f/(x−a) (x→a) = 0 (a>0)일 때 옳지 않은 것",
  "f(0)=f(a)=0; ① 반례 x(x−2) → 옳지 않은 것 ①", final="① (f는 일차함수 — 거짓)")
R(5, "함수의 극한에 대한 성질", "LIM.PROP.SQUEEZE_INF", "함수의 극한 대소 관계(조임)", "극한의 대소 관계;∞/∞꼴", "단일개념",
  "하", "x로 나눠 양쪽 극한." + E, MC, "④", "선택지번호", L, M, L, "x>0 나누기", "4x+3 ≤ xf(x) < (4x²−5x+3)/x (x>0)일 때 lim_{x→∞} f", "양쪽 → 4 ④", final="④ (4)")
R(6, "∞꼴 극한", "LIM.INF.SQRT_PRODUCT_MINUS_X", "√(x−a)√(x−b)−x의 ∞ 극한(유리화)", "∞−∞꼴;유리화", "극한+유리화",
  "중하", "유리화." + E, S, "−(a+b)/2", "식", L, M, L, "", "lim_{x→∞}(√(x−a)√(x−b)−x) (a,b>0)", "(−(a+b)x+ab)/(√…+x) → −(a+b)/2")
R(7, "우극한과 좌극한", "LIM.ONESIDED.FRACTIONAL_PART_RIGHT", "소수부분 함수의 우극한 대입", "우극한;소수부분;가우스 함수", "극한+특수함수",
  "중하", "구간에서 f=x−3." + E, S, "[독립] −1 (원문 분모 x²−4x+5 기준)", "값", L, M, M, "분모 부호", "x=n+α일 때 f=α; lim_{x→3+}(f(x)−2)/(x²−4x+5)",
  "f→0, 분자→−2, 분모→2 → −1. 동반 해설은 분모를 x²−4x−5로 풀어 1/4 — 원문/해설 분모 부호 불일치",
  keymatch=False, key="1/4", final="HOLD(원문 기준 −1 / 해설 1/4)", conflict="원문 분모 x²−4x+5(독립풀이 −1) vs 해설 분모 x²−4x−5(1/4)",
  ready="REVIEW", status="독립풀이-정답 불일치", trust="낮음(원문·해설 식 불일치)", review="REVIEW-원문해설불일치",
  memo_extra="유사중복: A02634 서술형 문항10과 동일 문항·동일 불일치(재사용 문항)")
R(8, "∞꼴 극한", "LIM.GEO.INTERSECTION_X_LIMIT_INF", "선분과 포물선 교점 좌표의 t→∞ 극한", "∞−∞꼴;유리화;이차방정식의 근", "극한+도형+유리화",
  "중", "근의 공식→유리화." + E, S, "1", "값", M, M, M, "x>0 근 선택", "(1,0)과 (0,t)를 잇는 선분과 y=x²의 교점 x좌표 f(t), lim_{t→∞} f(t)",
  "(√(t²+4t)−t)/2 → 1", fig="그래프(gso, 본문 조건으로 완결)", memo_extra="유사중복: A02634 서술형 문항11과 동일 문항(재사용)")
R(9, "우극한과 좌극한", "LIM.ONESIDED.FLOOR_ABS_COMPARE", "가우스·절댓값 한쪽 극한 대소 비교", "좌극한;우극한;가우스 함수;절댓값", "극한+특수함수",
  "중하", "3극한 계산." + E, MC, "④", "선택지번호", L, M, M, "x→−1+에서 [x]=−1", "a=lim_{x→−1+} x/[x], b=lim_{x→−1} x/|x|, c=lim_{x→1+}(x+1)/[x] 대소", "a=1, b=−1, c=2 → b<a<c ④", final="④ (b<a<c)")
R(10, "함수의 극한(미정계수)", "LIM.UNDET.DOUBLE_ROOT_DENOM", "(x−a)² 분모 0/0 극한 — 이중근 조건", "미정계수;이중근;인수분해", "극한+미정계수",
  "중", "분자 0 조건 2회." + E, S, "3", "값", M, M, M, "2단계 조건", "lim_{x→2}(3x²+ax+b)/(x−2)²=c일 때 a+b+c", "a=−12, b=12, c=3 → 3")
build("Batch225", ROWS, 10850)
