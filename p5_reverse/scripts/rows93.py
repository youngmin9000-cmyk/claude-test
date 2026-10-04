from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h93/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h93/A.hwp','rb').read()).hexdigest()
setup(QID="A02593", SRC="1MZC4Xc7mCEfJkGp7vOz41tPe1VUCSCh7", SHA=SQ, TAG="DSM2D103A", N=5,
      FNAME="15개정_고등_수학Ⅱ_2-1-03_소단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D103A", EXAM="Ⅱ-1-03 도함수 소단원평가(발전)", MID="미분계수와 도함수",
      ANS_QID="A02592", ANS_SRC="1GFhj67aj_mj3CLzhSNhZE41PMLmnSca6", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S, MC = "서술형(단답)", "5지선다"
F = dict(fig="설명 그림(gso)")
T = "도함수"
R(1, T, "DERIV.DERIVFN.IDENTITY_WITH_DERIVATIVE_QUADRATIC", "f와 f'의 항등식으로 이차함수 결정", "도함수;항등식;미정계수", "도함수+항등식",
  "중하", "계수비교 연립." + E, MC, "③", "선택지번호", L, M, M, "", "이차 f, f(−1)=1, (2x+1)f'(x)−4f(x)+3=0일 때 f'(1)", "a=b, b−4c+3=0, a−b+c=1 → f=x²+x+1 → 3", final="③ (3)")
R(2, T, "DERIV.DERIVFN.FUNCTIONAL_INEQUALITY_SQUEEZE", "함수 부등식에서 증분 조임으로 도함수", "도함수의 정의;함수방정식;부등식", "정의+부등식",
  "중상", "양방향 부등식 → f(x+h)−f(x)=h." + E, MC, "②", "선택지번호", L, H, H, "f(−h)≥−h 활용", "f(x+y)≥f(x)+f(y), f(x)≥x일 때 f'(x)", "h≤f(x+h)−f(x)≤h → f'=1", final="② (1)")
R(3, T, "DERIV.DIFFABLE.PIECEWISE_THEN_DERIV_LIMIT", "구간별 함수 미분가능 조건 후 미분계수 극한", "미분가능성;연속성;미분계수의 정의", "미분가능성+극한",
  "중", "b(b−2)=0, a=b, a≠0." + E, S, "18", "값", M, M, M, "a≠0으로 b=0 배제", "f=ax³+b²(x≥1), bx²+ax+b(x<1) x=1 미분가능, lim (f(1+2h)−f(1−h))/h", "a=b=2, f'(1)=6 → 3·6=18")
R(4, T, "DERIV.DERIVFN.DEGREE_ANALYSIS_F_FPRIME", "f·f' 차수 비교로 다항함수 결정", "도함수;다항식의 차수;계수비교", "차수+계수비교",
  "중하", "2n−1=1." + E, S, "35", "값", L, M, M, "복부호", "다항 f, f(x)f'(x)=4x+6일 때 f(1)f(2)", "f=±(2x+3) → (±5)(±7)=35")
R(5, T, "DERIV.DERIVFN.PROJECTILE_PARABOLA_TANGENT_ANGLE", "접선 각도와 착지점으로 포물선 최고점", "접선의 기울기;이차함수;실생활 활용", "실생활+도함수",
  "중하", "f'(0)=tan45°." + E, MC, "④", "선택지번호", L, M, M, "", "A에서 45° 발사, 200m 지점 B 착지 포물선의 최고 높이", "y=−x²/200+x → 꼭짓점 50", final="④ (50 m)", **F)
build("Batch251", ROWS, 11078)
