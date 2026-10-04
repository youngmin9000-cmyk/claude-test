from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h08/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h08/A.hwp','rb').read()).hexdigest()
setup(QID="A02508", SRC="1oB-Q2r0eRYczfaHVG5a2cBiWkKCLWN3t", SHA=SQ, TAG="DSM2I301A", N=5,
      FNAME="15개정_고등_수학Ⅱ_3-3-01_소단원평가_발전_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅲ. 적분", BIG="Ⅲ. 적분", SEC="I301A", EXAM="Ⅲ-3-01 넓이 소단원평가(발전)", MID="정적분의 활용",
      ANS_QID="A02507", ANS_SRC="1nu1IstjRBWg8I03eZBZ2GSYFCdVGh7tr", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"; MC = "5지선다"
A = "넓이"
G = dict(fig="그래프(gso)", ready="REVIEW", status="논리검산(그래프 시각확인 불가)", trust="중간(그래프 미확인)", review="REVIEW-그래프시각확인")
F = dict(fig="설명 그림(gso)")
R(1, A, "INTEG.AREA.EQUAL_AREAS_ZERO_INTEGRAL", "두 넓이 같음 → 정적분 0", "넓이;정적분=0;이차함수", "넓이+방정식",
  "중", "∫₀²f=0." + E, MC, "③", "선택지번호", L, M, M, "", "y=x²−(k+2)x+2k, x축·y축 넓이 S₁ = x축 넓이 S₂, 0<k<2", "2k−4/3=0 → 2/3", final="③ (2/3)")
R(2, A, "INTEG.AREA.PARABOLIC_SEGMENT_FORMULA", "포물선 도형 넓이 공식 유도(⅔bh)", "넓이;좌표 설정;정적분", "넓이+모델링",
  "중하", "y=−4h/b²x²+h." + E, MC, "②", "선택지번호", L, M, M, "", "밑변 b, 높이 h인 포물선 도형 넓이", "2∫₀^{b/2}=⅔bh", final="② (⅔bh)", **F)
R(3, A, "INTEG.AREA.RATIO_SYMMETRY_PARABOLA", "대칭축 이용 넓이 비 조건", "넓이;대칭;정적분=0", "넓이+대칭",
  "중", "∫₋ₐ⁰=0." + E, S, "3", "값", M, M, M, "A·B 영역 해석(그림)", "y=x²+2ax+6 (a>0), x축·y축 두 도형 A:B=2:1, a", "−⅔a³+6a=0 → 3 (영역 배치는 그림 의존)", **G)
R(4, A, "INTEG.AREA.INVERSE_FUNCTION_TILE", "역함수 대칭으로 타일 색칠 넓이 비", "역함수;y=x 대칭;넓이 비", "역함수+넓이",
  "중", "2S+T=225, T=3S." + E, S, "45", "값", L, M, M, "그림 판독(정사각형 15×15)", "정사각형 타일, f·역함수 g 경계, 파랑:노랑=2:3, ∫₀¹⁵f", "S=45 (타일 크기·배치 그림 의존)", **G)
R(5, A, "INTEG.AREA.BISECT_BY_X_AXIS", "곡선·직선 넓이를 x축이 이등분", "넓이;이등분;(β−α)³/6", "넓이+방정식",
  "중", "(k+2)³/6=8/3." + E, S, "2^(4/3)−2", "값", M, M, M, "", "y=x²−2x, y=kx 넓이를 x축이 이등분, k", "(k+2)³=16 → 2^{4/3}−2", **F)
build("Batch290", ROWS, 11421)
