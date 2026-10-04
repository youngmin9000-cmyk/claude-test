from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h03/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h03/A.hwp','rb').read()).hexdigest()
setup(QID="A02603", SRC="1L3qKW55r-iGPyjk_rnFstaCxTILEm2Gt", SHA=SQ, TAG="DSM2D202N", N=10,
      FNAME="15개정_고등_수학Ⅱ_2-2-02_소단원평가_기본_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D202N", EXAM="Ⅱ-2-02 평균값 정리 소단원평가(기본)", MID="도함수의 활용",
      ANS_QID="A02568", ANS_SRC="1EaMg4U8e79fTVeZfYmvYHdqgMY7mEjXn", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
MV = "평균값 정리"
R(1, MV, "DERIV.MVT.ROLLE_FIND_C", "롤의 정리를 만족하는 c", "롤의 정리;미분계수", "단일개념",
  "하", "f(1)=f(3) → f'(c)=0." + E, S, "2", "값", L, L, L, "", "f=4x−x², [1,3] 롤의 정리 c", "4−2c=0")
R(2, MV, "DERIV.MVT.ROLLE_PARAM_FROM_C", "롤의 정리 c 값으로 상수 결정", "롤의 정리;미정계수", "롤+미정계수",
  "하", "f'(c)=0 대입." + E, S, "[원문 결함] 성립하는 상수 없음(롤 조건상 a=4, c=2)", "값", L, M, M, "c는 열린구간 내부",
  "f=ax−x², [1,3] 롤의 정리 상수값 3일 때 상수 k(원문 표기)",
  "롤의 정리는 f(1)=f(3) 필요 → a−1=3a−9 → a=4, 이때 c=2. c=3은 열린구간 (1,3) 밖이며 a=6이면 f(1)=5≠f(3)=9 — 원문 조건 모순; 해설은 f'(3)=0만으로 a=6",
  keymatch=False, key="6 (해설: f'(3)=a−6=0)", final="HOLD(원문 조건 모순 — c=3은 구간 끝점, 롤 조건 불충족; 해설 6)",
  conflict="원문 c=3(끝점)·문자 k/a 불일치 — 롤의 정리 적용 불가, 해설은 f'(3)=0으로 a=6 산출",
  ready="REVIEW", status="원문 오류(조건 모순)", trust="낮음(원문 결함)", review="REVIEW-원문오류")
R(3, MV, "DERIV.MVT.MEAN_VALUE_FIND_C", "평균값 정리를 만족하는 c", "평균값 정리;평균변화율", "단일개념",
  "하", "평균변화율=f'(c)." + E, S, "√21/3", "값", L, L, L, "구간 내부 c", "f=x³−2x, [1,2] 평균값 정리 c", "5=3c²−2 → c=√21/3")
R(4, MV, "DERIV.MVT.BOUND_SECANT_SLOPE_PROOF", "평균값 정리로 할선 기울기 범위 증명", "평균값 정리;도함수의 최대최소;부등식 증명", "평균값정리+부등식",
  "중", "f'=3(x−1)²−1 ∈[−1,11]." + E, "서술형(증명)", "풀이 참조(증명)", "증명", L, M, M, "등호 배제 근거",
  "f=x³−3x²+2x, 0≤x1<x2≤3에서 −1<(f(x2)−f(x1))/(x2−x1)<11 증명",
  "할선 기울기=구간 [x1,x2]에서 f'의 평균 → f'가 −1·11을 한 점에서만 취하므로 엄격 부등식 성립; 해설(MVT+f' 범위) 결론 일치")
R(5, MV, "DERIV.MVT.MEAN_VALUE_C_PRODUCT", "평균값 정리 c가 여러 개일 때 곱", "평균값 정리;평균변화율", "단일개념",
  "하", "3c²−4=−3." + E, MC, "②", "선택지번호", L, L, L, "c 두 개", "f=x³−4x, [−1,1] 평균값 정리 c 값의 곱", "c=±1/√3 → −1/3 ②", final="② (−1/3)")
R(6, MV, "DERIV.MVT.MEAN_VALUE_OF_DERIVATIVE", "도함수 g=f'에 평균값 정리", "평균값 정리;도함수", "단일개념",
  "하", "g=6x²−2x−1." + E, MC, "③", "선택지번호", L, L, L, "", "f=2x³−x²−x, g=f'의 [0,2] 평균값 정리 c", "(19+1)/2=10=12c−2 → 1 ③", final="③ (1)")
R(7, MV, "DERIV.MVT.INTERVAL_ENDPOINT_FROM_C", "c 값으로 구간 끝점 결정", "평균값 정리;미정계수", "평균값정리+방정식",
  "중하", "평균변화율=f'(0)=5." + E, MC, "②", "선택지번호", L, M, L, "a<0", "f=−x²+5x, [a,1] 평균값 정리 c=0일 때 a", "a²=1 → −1 ②", final="② (−1)")
R(8, MV, "DERIV.MVT.INTERVAL_ENDPOINT_FROM_C", "c 값으로 구간 끝점 결정", "평균값 정리;미정계수", "평균값정리+방정식",
  "중하", "평균변화율=f'(3)=0." + E, S, "5", "값", L, M, L, "a>3", "f=x²−6x−3, [1,a] 평균값 정리 c=3일 때 a", "(a−1)(a−5)=0 → 5")
R(9, MV, "DERIV.MVT.INTERVAL_ENDPOINT_FROM_C", "c 값으로 구간 끝점 결정", "평균값 정리;미정계수", "평균값정리+방정식",
  "중하", "평균변화율=f'(4)=−3." + E, S, "7", "값", L, M, L, "k>1", "f=−x²+5x+1, [1,k] 평균값 정리 c=4일 때 k", "(k−1)(k−7)=0 → 7")
R(10, MV, "DERIV.MVT.THETA_QUADRATIC", "평균값 정리의 θ 결정(이차함수)", "평균값 정리;이차함수", "단일개념",
  "하", "전개 비교." + E, S, "1/2", "값", L, L, L, "", "f=x²+ax+b, f(x+h)=f(x)+hf'(x+θh)의 θ", "h²=2θh² → 1/2",
  memo_extra="유사중복: A02617 서술형 문항10과 동일 구조(일반 이차식)")
build("Batch243", ROWS, 11009)
