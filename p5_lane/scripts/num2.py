import math
from mpmath import mp, mpf, sqrt, atan, asin, acos, pi, quad, sin, cos, findroot, identify, log
mp.dps=30
def tri(P,Q,R): return abs((Q[0]-P[0])*(R[1]-P[1])-(R[0]-P[0])*(Q[1]-P[1]))/2
seg=lambda th: (th-sin(th))/2
# 16
s6=2*sqrt(6); al=asin(mpf(1)/5)
B2=(cos(al),sin(al)); G1=(B2[0]/2,B2[1]/2); A1=(0,1); E1=(1,0)
r1=tri(A1,G1,B2)+seg(pi/2-al)
# shape2 congruent (central symmetry) to region bounded by B2G1? no: D2H1, H1F1, arc F1D2 ~ image of (B2,G1,E1, arc E1B2)
r2=tri(B2,G1,E1)+seg(al)
S1=r1+r2; L16=S1*25/16
print('16',S1,L16, identify(L16,['pi','sqrt(6)']))
# 20
def inC(x,y,c,r): return (x-c[0])**2+(y-c[1])**2<r*r
N=3000; h=mpf(2)/N; a=0
import itertools
cnt1=0;cnt2=0
for i in range(N):
  for j in range(int(N*1.2)):
    x=(i+0.5)*2/N; y=(j+0.5)*2/N
    c1=inC(x,y,(1,1),1); c2=inC(x,y,(1,2),math.sqrt(2))
    if c1 and not c2: cnt1+=1
    if (not c1) and c2 and y<=2: cnt2+=1
S1=(cnt1+cnt2)*(2/N)**2
print('20 S1~',S1,'lim~',S1*5/3)
