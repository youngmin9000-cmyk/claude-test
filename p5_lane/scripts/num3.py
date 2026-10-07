from mpmath import mp, mpf, sin, cos, tan, sqrt, findroot, pi, atan2, acos
mp.dps=40
def tri(P,Q,R): return abs((Q[0]-P[0])*(R[1]-P[1])-(R[0]-P[0])*(Q[1]-P[1]))/2
# 36: AB=1 semicircle center (1/2,0) r=1/2, A(0,0), C on arc with angle BAC=t. circle tangent to AB, AC, internally tangent to arc BC.
def p36(t):
    # center on bisector at angle t/2: (d cos(t/2), d sin(t/2)), radius r = d sin(t/2); internal tangency: dist to (1/2,0) = 1/2 - r
    f=lambda d: sqrt((d*cos(t/2)-mpf(1)/2)**2+(d*sin(t/2))**2)-(mpf(1)/2-d*sin(t/2))
    d=findroot(f,mpf('0.9')); r=d*sin(t/2); return (tan(t/2)-r)/t**2
print('36',[100*p36(mpf(10)**-k) for k in (3,5)])
# 37: circle center O radius 2, A(-2,0),B(2,0). P on circle with angle PAB=t -> P at central angle 2t: (2cos2t,2sin2t)
def p37(t):
    P=(2*cos(2*t),2*sin(2*t)); A=(-2,0); B=(2,0)
    # Q on AB with angle APQ = 2t. direction PA angle
    import mpmath
    ang_PA=mpmath.atan2(A[1]-P[1],A[0]-P[0])
    # rotate towards AB (clockwise? ) try both, pick Q on segment AB
    for sgn in (1,-1):
        a=ang_PA+sgn*2*t
        k=-P[1]/sin(a); Qx=P[0]+k*cos(a)
        if k>0 and -2<Qx<2: Q=(Qx,0); dirv=(cos(a),sin(a)); break
    # R second intersection of line PQ with circle
    # param P + s*dir: |P+s d|^2=4 -> s = -2 P·d
    s=-2*(P[0]*dirv[0]+P[1]*dirv[1]); R=(P[0]+s*dirv[0],P[1]+s*dirv[1])
    S=tri(B,Q,R)
    # circle C' tangent to PA and PR, passing O, center on bisector of angle APR inside triangle AQP
    import mpmath
    u1=(A[0]-P[0],A[1]-P[1]); n1=sqrt(u1[0]**2+u1[1]**2); u1=(u1[0]/n1,u1[1]/n1)
    u2=dirv; bis=(u1[0]+u2[0],u1[1]+u2[1]); nb=sqrt(bis[0]**2+bis[1]**2); bis=(bis[0]/nb,bis[1]/nb)
    half=acos(u1[0]*u2[0]+u1[1]*u2[1])/2
    g=lambda L: sqrt((P[0]+L*bis[0])**2+(P[1]+L*bis[1])**2)-L*sin(half)
    L=findroot(g,mpf(1.5)); r=L*sin(half)
    return S/r
print('37',[45*p37(mpf(10)**-k) for k in (3,4,5)])
# 38: B(0,0), C(2,0), A=(cos t, sin t), M(1,0). H foot from M to AB: (cos^2 t, cos t sin t). circle center M radius MH=sin t meets AM at D. E = HC ∩ DM.
def p38(t):
    import mpmath
    A=(cos(t),sin(t)); M=(1,0); C=(2,0); H=(cos(t)**2,cos(t)*sin(t)); r=sin(t)
    v=(A[0]-1,A[1]); nv=sqrt(v[0]**2+v[1]**2); D=(1+r*v[0]/nv, r*v[1]/nv)
    def inter(P1,P2,P3,P4):
        x1,y1=P1;x2,y2=P2;x3,y3=P3;x4,y4=P4
        d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        return (((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d, ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d)
    E=inter(H,C,D,M)
    return (tri(C,D,E)-tri(M,E,H))/t**2
print('38',[80*p38(mpf(10)**-k) for k in (3,5)])
