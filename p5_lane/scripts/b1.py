from itertools import product as P
c=lambda f,it: sum(1 for x in it if f(x))
print(42,c(lambda t: 1 in [t.count(b) for b in range(4)] and 0 in [t.count(b) for b in range(4)], P(range(4),repeat=4)))
print(45,c(lambda s:'ABC' not in ''.join(s),P('ABC',repeat=6)))
def ok48(s):
    d=[ch for ch in s if ch in '123']; return len(d)>=1 and len(d)==len(set(d))
print(48,c(ok48,P('xy123',repeat=5)))
print(49,c(lambda s: not any({s[i],s[i+1]}=={'a','b'} for i in range(3)),P('abcd',repeat=4)))
def ok52(s):
    l=[ch for ch in s if ch in 'abc']; return len(l)>=1 and len(l)==len(set(l))
print(52,c(ok52,P('012abc',repeat=4)))
def ok54(s):
    v=[i for i,ch in enumerate(s) if ch in 'ae']; return len(v)>=2 and all(v[i+1]-v[i]>1 for i in range(len(v)-1))
n=c(ok54,P('abcde',repeat=7));print(54,n,n/36)
print(55,sum(int(''.join(s)) for s in P('0123',repeat=3) if s[0]!='0'))
print(56,sum(int(''.join(s)) for s in P('1234',repeat=3)))
