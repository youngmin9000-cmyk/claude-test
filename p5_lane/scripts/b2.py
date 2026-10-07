from itertools import product as P, combinations as C
c=lambda f,it: sum(1 for x in it if f(x))
print(61,c(lambda n:any(d in str(n) for d in '369'),range(1,1000)))
X=[n for n in range(10,201) if str(n)[-1]=='0' or (n>=100 and str(n)[-2]=='0')]
print(66,c(lambda p:p[0]!=p[1] and (p[0]+p[1])%10==0,P(X,repeat=2)))
# subsets via labels: each element assigned membership
def cnt(n,k,f): return c(f,P(range(k),repeat=n))
# 69: A∩B=∅, n(A)=2, n(B)>=1 ; labels 0 none,1 A,2 B
print(69,cnt(5,3,lambda t:t.count(1)==2 and t.count(2)>=1))
print(70,cnt(5,4,lambda t:True) if False else None)
U=[1,3,5,7,9]
def subs(u):
    for r in range(len(u)+1):
        for s in C(u,r): yield frozenset(s)
S=list(subs(U));print(70,c(lambda ab:ab[0]&ab[1]=={9} and len(ab[0]|ab[1])==4,P(S,repeat=2)))
print(71,c(lambda ab:ab[0] and ab[0]<=ab[1],P(S,repeat=2)))
S6=list(subs(range(6)));print(72,c(lambda ab:not(ab[0]&ab[1]),P(S6,repeat=2)))
S10=None
# 73: labels per element for 10: in A only, B only, both, none; both must be exactly {2,4,6,8}
# elements 2,4,6,8 both; others (6 elements) in A-only/B-only/none, need A-only nonempty and B-only nonempty
print(73,cnt(6,3,lambda t:1 in t and 2 in t))
S3=list(subs([1,2,3]));print(74,c(lambda x:x[0]<=(x[1]&x[2]),P(S3,repeat=3)))
print(75,c(lambda ab:ab[0] and ab[1] and ab[0]<=ab[1],P(S,repeat=2)))
S4=list(subs([1,2,3,4]));print(76,c(lambda ab:ab[0] and ab[0]<=ab[1],P(S4,repeat=2)))
print(77,c(lambda ab:ab[0]<=ab[1],P(S,repeat=2)))
print(78,c(lambda x:len(x[0]&x[1])==2 and x[0]-x[1] and not((x[0]|x[1])&x[2]),P(S,repeat=3)))
print(81,'3^20/9=3^18')
print(82,c(lambda ab:ab[0]<=ab[1],P(S,repeat=2)),c(lambda ab:ab[0]<ab[1],P(S,repeat=2)))
S6b=list(subs(range(1,7)))
print(83,c(lambda ab:len(ab[0]-ab[1])==1 and len(ab[0]&ab[1])==2 and 3 not in (ab[0]&ab[1]),P(S6b,repeat=2)))
print(84,cnt(7,3,lambda t:t.count(2)==1))  # 0 A-only,1 B-only,2 both
print(85,2**8)
print(87,cnt(4,3,lambda t:1 in t and 2 in t))
print(88,cnt(6,3,lambda t:t.count(1)>=1 and t.count(2)==1))
print(89,2**7-2**3)
print(90,c(lambda x:x[0]<=x[1],P(S3,repeat=3)))
print(93,3**4)
for n in [3,4]:
    Sn=list(subs(range(n)));print(94,n,c(lambda ab:ab[0] and ab[1] and ab[0]<ab[1],P(Sn,repeat=2)),3**n-2**(n+1)+1)
print(96,3**11-2**12,'a=3 m=?')
print(97,c(lambda d:True,P(range(2,6),repeat=7)), 4**7, 2**14)
