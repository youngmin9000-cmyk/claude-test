"""공통 도우미: 문항 정의와 sympy 기반 독립 검산."""
from sympy import (symbols, sqrt, Rational as R, simplify, solve, Eq, expand,
                   Interval, Union, oo, S, Abs, nsimplify, Poly, solveset, FiniteSet)

x, y, k, a, b, m, r, t = symbols('x y k a b m r t', real=True)


def dist(P, Q):
    return sqrt((P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2)


def div(P, Q, mm, nn):
    """선분 PQ를 mm:nn으로 내분하는 점"""
    return tuple(simplify((mm * q + nn * p) / (mm + nn)) for p, q in zip(P, Q))


def cen(A, B, C):
    return tuple(simplify((A[i] + B[i] + C[i]) / 3) for i in range(2))


def pl_dist(P, A, B, C):
    """점 P와 직선 Ax+By+C=0 사이 거리"""
    return simplify(Abs(A * P[0] + B * P[1] + C) / sqrt(A ** 2 + B ** 2))


def circle_from(expr):
    """x^2+y^2+Dx+Ey+F (=0) -> (중심, 반지름^2)"""
    p = Poly(expand(expr), x, y)
    D = p.coeff_monomial(x)
    E = p.coeff_monomial(y)
    F = p.coeff_monomial(1)
    c = (-D / 2, -E / 2)
    return c, simplify(c[0] ** 2 + c[1] ** 2 - F)


class EQ:
    """방정식 f(x,y)=0 (상수배 동치 비교)"""

    def __init__(self, lhs, rhs=0):
        self.e = expand(lhs - rhs)

    def __eq__(self, o):
        if not isinstance(o, EQ):
            return False
        q = simplify(self.e / o.e)
        return q != 0 and not q.free_symbols

    def __repr__(self):
        return f"EQ({self.e})"

    def __hash__(self):
        return 0


def same(u, v):
    from sympy import Set
    if isinstance(u, Set) or isinstance(v, Set):
        return u == v
    if isinstance(u, EQ) or isinstance(v, EQ):
        return isinstance(u, EQ) and isinstance(v, EQ) and u == v
    if isinstance(u, (tuple, list)) and isinstance(v, (tuple, list)):
        return len(u) == len(v) and all(same(p, q) for p, q in zip(u, v))
    if isinstance(u, (set, frozenset)) and isinstance(v, (set, frozenset)):
        if len(u) != len(v):
            return False
        vv = list(v)
        for p in u:
            hit = [q for q in vv if same(p, q)]
            if not hit:
                return False
            vv.remove(hit[0])
        return True
    if isinstance(u, str) or isinstance(v, str):
        return u == v
    try:
        if hasattr(u, 'is_Interval') or hasattr(u, 'is_Union'):
            if u.is_Set or v.is_Set:
                return u == v
    except AttributeError:
        pass
    try:
        return simplify(S(u) - S(v)) == 0
    except Exception:
        return u == v


ITEMS = {}


def Q(exam, no, *, src, typ, mode, diff, q, ans, calc, sol, choices=None,
      cv=None, pts=None, fig=None, ccols=None, ansval=None):
    it = dict(exam=exam, no=no, src=src, typ=typ, mode=mode, diff=diff, q=q,
              choices=choices, cv=cv, ans=ans, calc=calc, sol=sol, pts=pts,
              fig=fig, ccols=ccols, ansval=ansval)
    ITEMS.setdefault(exam, []).append(it)
    return it


def S_(concept, why, steps, caution, final):
    return dict(concept=concept, why=why, steps=steps, caution=caution,
                final=final)


def verify(exam):
    errs = []
    items = ITEMS[exam]
    assert len(items) == 20, (exam, len(items))
    for it in items:
        c = it['calc']() if callable(it['calc']) else it['calc']
        if it['choices'] is not None:
            assert len(it['choices']) == 5 and len(it['cv']) == 5, (exam, it['no'])
            hits = [i + 1 for i, v in enumerate(it['cv']) if same(v, c)]
            if hits != [it['ans']]:
                errs.append((exam, it['no'], 'calc', c, 'hits', hits, 'declared', it['ans']))
            # 선지끼리 중복 금지
            for i in range(5):
                for j in range(i + 1, 5):
                    if same(it['cv'][i], it['cv'][j]):
                        errs.append((exam, it['no'], 'dup choice', i + 1, j + 1))
        else:
            if not same(c, it['ansval']):
                errs.append((exam, it['no'], 'calc', c, 'declared', it['ansval']))
    return errs
