from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h57/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h57/A.hwp','rb').read()).hexdigest()
setup(QID="A02557", SRC="1QBO9aRUZuy0kNvwIvHTAI6efYgqhK6-U", SHA=SQ, TAG="DSM2D101A", N=5,
      FNAME="15개정_고등_수학Ⅱ_2-1-01_소단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D101A", EXAM="Ⅱ-1-01 미분계수 소단원평가(발전)", MID="미분계수와 도함수",
      ANS_QID="A02556", ANS_SRC="1eTc11rK32lZtTu4tcahsM5whm3RpcRug", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"
F = dict(fig="설명 그림(gso)")
AV, DC = "평균변화율", "미분계수"
R(1, DC, "DERIV.DERIVCOEF.SECANT_LIMIT_IS_TANGENT", "할선 기울기의 극한 = 접선 기울기", "미분계수;접선의 기울기;할선", "단일개념",
  "하", "f'(1)." + E, S, "1", "값", L, L, L, "", "f=x³−2x+1 위 A(1,0), B(t,f(t))에서 B→A일 때 AB 기울기", "f'(1)=3−2=1")
R(2, DC, "DERIV.DERIVCOEF.LIMIT_WITH_UNKNOWN_FUNCTION_G", "미지 함수 g를 포함한 극한식에서 lim g(h)/h", "미분계수의 정의;극한의 성질", "극한+미분계수",
  "중하", "3f'(a)−lim g/h=0." + E, S, "9", "값", L, M, M, "", "f'(a)=3, lim (f(a+2h)−f(a−h)−g(h))/h=0일 때 lim g(h)/h", "3·3=9")
R(3, DC, "DERIV.DERIVCOEF.RATIONALIZE_SQRT_F", "√f(x) 극한의 유리화 후 미분계수", "미분계수의 정의;유리화", "극한+미분계수",
  "중하", "×(√f+1)." + E, S, "1", "값", L, M, M, "", "f(1)=1, f'(1)=2일 때 lim (√f(x)−1)/(x−1)", "f'(1)/(√f(1)+1)=1")
R(4, AV, "DERIV.AVGRATE.MVT_STYLE_EQUAL_RATES", "평균변화율=순간변화율인 점", "평균변화율;순간변화율;미분계수", "평균변화율+미분계수",
  "중하", "3a²+1=5." + E, S, "2√3/3", "값", L, M, L, "0<a<2", "f=x³+x, 0→2 평균변화율과 x=a 순간변화율이 같을 때 a", "a²=4/3 → 2√3/3")
R(5, AV, "DERIV.AVGRATE.CONCAVE_SECANT_SLOPE_ORDER", "위로 볼록 곡선(√x) 할선 기울기 대소", "평균변화율;할선의 기울기;볼록성", "평균변화율+그래프",
  "중하", "g(i,j)=1/(√a_i+√a_j)." + E, S, "g(1,2)>g(1,3)>g(2,3)", "부등식", L, M, M, "볼록 방향", "f=√x, a1<a2<a3에서 g(1,2), g(1,3), g(2,3) 대소 (원문 'a_i에서 a_i (i, i=…)'는 a_j·(i,j) 오기)", "(√a_j−√a_i)/(a_j−a_i)=1/(√a_i+√a_j) (그림 불필요)", **F)
build("Batch261", ROWS, 11167)
