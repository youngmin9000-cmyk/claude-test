from mpmath import mp, mpf, sin, cos, tan, atan, exp, log, sqrt, pi, findroot, quad
mp.dps=40
def tri(P,Q,R): return abs((Q[0]-P[0])*(R[1]-P[1])-(R[0]-P[0])*(Q[1]-P[1]))/2
# 32
def p32(t):
    P=(cos(t),sin(t)); Q=(1/cos(t),0); R=(1/cos(t),tan(t))
    # tangent from R to arc (other than through P): S on circle with OS ⟂ RS, angle of S = 2*atan2... R polar angle t, dist 1/cos? |OR|=sqrt(1/cos^2+tan^2)
    import mpmath
    r=mpmath.sqrt((1/cos(t))**2+tan(t)**2); phi=mpmath.atan2(tan(t),1/cos(t)); a=mpmath.acos(1/r)
    S=(cos(phi+a),sin(phi+a))
    f=tri((0,0),S,R); g=tri(P,Q,R); return g/(t*f*f)
print('32',[p32(mpf(10)**-k) for k in (3,5)])
# 33: AB=2, center O(0,0), A(-1,0),B(1,0). angle BAP=t: P angle 2t from B? P = (cos(pi-2*(pi/2 - t))...) inscribed: central angle BOP = 2t
def p33(t):
    P=(cos(2*t),sin(2*t)); # arc PB = arc PQ -> Q at central angle 4t
    Q=(cos(4*t),sin(4*t)); A=(-1,0);B=(1,0)
    # R = AP ∩ BQ
    import mpmath
    def inter(P1,P2,P3,P4):
        x1,y1=P1;x2,y2=P2;x3,y3=P3;x4,y4=P4
        d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        px=((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d
        py=((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d
        return (px,py)
    R=inter(A,P,B,Q); S=(1,2*tan(t))
    seg=lambda th: (th-sin(th))/2  # circular segment area r=1
    f=tri(P,Q,R)+seg(2*t)  # region PR,QR, arc PQ
    g=tri(P,B,S)-seg(2*t)  # region PS,BS, arc BP (triangle minus segment)
    return (f+g)/t**3
print('33',[p33(mpf(10)**-k) for k in (3,5)])
# 34
def p34(t):
    P=(cos(t),sin(t)); qx=log(1+sin(t)); T=(qx,qx*tan(t)); return tri((0,0),(qx,0),T)/t**3
print('34',[60*p34(mpf(10)**-k) for k in (3,5)])
# 35
def p35(t):
    # P on arc, angle APH = t; A(0,1), H=(0,yP). Let P=(cos s, sin s); tan(angle APH)= (1-sin s)/cos s = t-> solve
    import mpmath
    s=mpmath.findroot(lambda s:(1-sin(s))/cos(s)-tan(t),mpf(1.4))
    P=(cos(s),sin(s)); H=(0,sin(s)); A=(0,1); O=(0,0)
    # bisector of angle OAP from A: direction = unit(AO)+unit(AP)
    u1=(0,-1); v=(P[0],P[1]-1); n=mpmath.sqrt(v[0]**2+v[1]**2); u2=(v[0]/n,v[1]/n); d=(u1[0]+u2[0],u1[1]+u2[1])
    def on(y): k=(y-1)/d[1]; return (k*d[0],y)
    Q=on(sin(s)); S=on(0)
    # R = bisector ∩ OP
    import mpmath
    k=mpmath.findroot(lambda k:(k*d[0])*P[1]-(1+k*d[1])*P[0],mpf(0.5)); R=(k*d[0],1+k*d[1])
    f=tri(A,Q,H); g=tri(P,S,R); return t**3*g/f
print('35',[100*p35(mpf(10)**-k) for k in (2,3,4)])
