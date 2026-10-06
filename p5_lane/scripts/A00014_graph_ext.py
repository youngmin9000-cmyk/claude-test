import sympy as sp, re, json
x=sp.symbols('x')
C="""2x3 −18x2 + 54x −51|−x3 + x2 + x + 2|3x3 −9x2 + 9x −3|−2x3 −10x2 −14x −11|−x3 −5x2 −8x −4|−2x3 + 6x + 6|x3 + 7x2 + 16x + 11|−2x3 + 2x2 −1|2x3 + 18x2 + 48x + 27|3x3 −15x2 + 21x −4|3x3 −21x2 + 48x −35|2x3 −6x2 + 3|−x3 + 4x2 −5x −1|3x3 + 6x2 −3|−x3 −x2 + 1|−x3 −4x2 −4x −2|−3x3 −9x2 + 14|x3 + 3x2 −2|x3 −3x|−3x3 + 21x2 −45x + 30|3x3 + 18x2 + 36x + 24|3x3 + 6x2 + 1|x3 −7x2 + 16x −11|3x3 −9x2|x3 −2x2 + x|−x3 + x2 + 1|−x3 + 4x2 −5x|−3x3 −12x2 −15x −8|x3 −3x2 + 3x −5|2x3 −10x2 + 14x −6"""
Q="""x4 −8x3 + 18x2 −28|x4 −10x3 + 36x2 −54x + 29|x4 + 2x3 −3x2 −4x + 7|x4 + 4x3 + 4x2 −1|x4 −6x3 + 12x2 −8x −1|x4 + 6x3 + 12x2 + 8x + 1|x4 −8x3 + 16x2 −1|x4 + 12x3 + 52x2 + 96x + 61|x4 + 4x3 −16x −14|x4 −2x3 + x2 + 1|x4 −8x3 + 18x2 −26|x4 −2x3 −3x2 + 4x + 5|x4 −12x3 + 48x2 −64x −1|x4 + 6x3 + 13x2 + 12x + 2|x4 + 2x3 −2x −1|x4 + 4x3 + 4x2|x4 −6x2 + 8x −6|x4 + 4x3 −2x2 −12x + 8|x4 −8x3 + 22x2 −24x + 10|x4 + 8x3 + 18x2 −24|x4 −4x3 −2x2 + 12x + 11|x4 −2x3 + x2 −3|x4 + 2x3 −2x + 1|x4 −2x3 + 2|x4 −12x3 + 46x2 −60x + 23|x4 + 16x3 + 90x2 + 200x + 123|x4 −8x3 + 18x2 −28|x4 + 12x3 + 46x2 + 60x + 23|x4 + 2x3 −3|x4 −8x3 + 22x2 −24x + 6"""
def parse(s):
    s=s.replace('−','-').replace(' ','')
    s=re.sub(r'x(\d)',r'x**\1',s); s=re.sub(r'(\d)x',r'\1*x',s)
    return sp.sympify(s)
def feat(f):
    d=sp.diff(f,x); out=[]
    for r in sorted(set(sp.real_roots(sp.Poly(d,x))), key=lambda t: float(t)):
        dd=sp.diff(f,x,2).subs(x,r)
        # classify by sign change
        lf=d.subs(x,r-sp.Rational(1,1000)); rt=d.subs(x,r+sp.Rational(1,1000))
        kind='극대' if lf>0>rt else ('극소' if lf<0<rt else '정류(극값X)')
        out.append(f"x={sp.nsimplify(r)}:{kind} {sp.nsimplify(f.subs(x,r))}")
    return f"y절편 {f.subs(x,0)}; "+", ".join(out)
res={'cubic':[feat(parse(s)) for s in C.split('|')],'quartic':[feat(parse(s)) for s in Q.split('|')]}
json.dump(res,open(__import__('sys').argv[1],'w'),ensure_ascii=False,indent=0)
for k in res:
    for i,v in enumerate(res[k],1): print(k,i,v)
