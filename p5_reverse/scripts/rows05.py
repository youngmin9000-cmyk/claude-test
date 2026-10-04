from cfgh import *
import hashlib
SQ = hashlib.sha256(open(OUT+'h05/Q.hwp','rb').read()).hexdigest(); SA = hashlib.sha256(open(OUT+'h05/A.hwp','rb').read()).hexdigest()
setup(QID="A02605", SRC="1L1xClwKqShxwHGUqW04eqKA3-xoWPm_W", SHA=SQ, TAG="DSM2D202B", N=10,
      FNAME="15개정_고등_수학Ⅱ_2-2-02_소단원평가_기초_Q.hwp (두산-수학II- 출판사 문제 모음.vol1)",
      UNIT="Ⅱ. 미분", BIG="Ⅱ. 미분", SEC="D202B", EXAM="Ⅱ-2-02 평균값 정리 소단원평가(기초)", MID="도함수의 활용",
      ANS_QID="A02604", ANS_SRC="1EjZzTy37uFEIqBEK6zSiLBaPtxbiqsBC", ANS_SHA=SA)
E = " 계산량·조건해석·추론량 기준."
L, M, H = "낮음", "보통", "높음"
S = "서술형(단답)"
MV = "평균값 정리"
def RO(q, desc, ans, chk, nsub=1):
    R(q, MV, "DERIV.MVT.ROLLE_FIND_C", "롤의 정리를 만족하는 c", "롤의 정리;미분계수", "단일개념",
      "하", "f(a)=f(b) 확인 → f'(c)=0." + E, S, ans, "값" if nsub == 1 else "값(소문항별)", L, L, L, "구간 내부 c 선택", desc, chk, nsub=nsub)
def MVT(q, desc, ans, chk, nsub=1):
    R(q, MV, "DERIV.MVT.MEAN_VALUE_FIND_C", "평균값 정리를 만족하는 c", "평균값 정리;평균변화율;미분계수", "단일개념",
      "하", "평균변화율=f'(c)." + E, S, ans, "값" if nsub == 1 else "값(소문항별)", L, L, L, "구간 내부 c 선택", desc, chk, nsub=nsub)
RO(1, "f=x²−2x−3, [−1,3] 롤의 정리 c", "1", "f(−1)=f(3)=0, 2c−2=0")
RO(2, "⑴ x²−3x+2 [1,2] ⑵ x³−x [0,1] 롤의 정리 c", "⑴ 3/2 ⑵ √3/3", "⑴ 2c−3=0 ⑵ 3c²=1, 0<c<1", nsub=2)
MVT(3, "f=−x²+2x, [0,3] 평균값 정리 c", "3/2", "평균변화율 −1 = −2c+2")
MVT(4, "⑴ x²−6x [2,5] ⑵ x³−2 [0,2] 평균값 정리 c", "⑴ 7/2 ⑵ 2√3/3", "⑴ 1=2c−6 ⑵ 4=3c²", nsub=2)
MVT(5, "f=x³+6, [0,3] 평균값 정리 c", "√3", "9=3c²")
RO(6, "⑴ x²−4x [1,3] ⑵ −x²+2x+3 [0,2] 롤의 정리 c", "⑴ 2 ⑵ 1", "⑴ 2c−4=0 ⑵ −2c+2=0", nsub=2)
RO(7, "⑴ (x−a)(x−b) [a,b] ⑵ x²−8x [0,8] ⑶ x³−x²−5x−3 [−1,3] 롤의 정리 c", "⑴ (a+b)/2 ⑵ 4 ⑶ 5/3", "⑶ (c+1)(3c−5)=0, −1<c<3", nsub=3)
RO(8, "⑴ (x−1)(x−3) [1,3] ⑵ x²−2x [0,2] 롤의 정리 c", "⑴ 2 ⑵ 1", "대칭축", nsub=2)
MVT(9, "f=3x²+2x+1, [−1,1] 평균값 정리 c", "0", "(6−2)/2=2=6c+2")
MVT(10, "f=2x²−4x+3, [−2,1] 평균값 정리 c", "−1/2", "(1−19)/3=−6=4c−4")
build("Batch242", ROWS, 10999)
