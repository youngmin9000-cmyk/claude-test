from itertools import product as P, combinations_with_replacement as CR
import sys; sys.path.insert(0,'.')
c=lambda f,it: sum(1 for x in it if f(x))
def nums(digs,maxlen):
    out=set()
    for L in range(1,maxlen+1):
        for s in P(digs,repeat=L):
            if s[0]!='0' or L==1:
                v=int(''.join(s))
                if v>0: out.add(v)
    return sorted(out)
def rank(digs,v,ml): return nums(digs,ml).index(v)+1
def fixed(digs,L): return [int(''.join(s)) for s in P(digs,repeat=L) if s[0]!='0']
print(126,rank('012345',2013,4));print(127,rank('01234',3000,4));print(128,rank('012345',3000,4));print(129,rank('01234',2000,4))
print(130,c(lambda n:n%2==0 and n<=50 and str(n)[0]!=str(n)[1] and '0' not in str(n),range(10,100)))
print(131,rank('012345',10000,5));print(132,sorted(fixed('0123',4))[161])
print(133,c(lambda n:n%2,fixed('01234',3)));print(134,c(lambda n:n%4==0,fixed('12345',4)))
print(135,c(lambda n:sum(map(int,str(n)))%2,fixed('34567',3)));print(136,c(lambda n:n>2300,fixed('1234',4)))
print(137,c(lambda n:sum(map(int,str(n)))%2,fixed('12345',4)))
f=sorted(fixed('01234',4),reverse=True);print(140,f.index(2133)+1)
print(143,c(lambda n:n%2==0,fixed('01234',3)));print(144,c(lambda n:sum(map(int,str(n)))%2==0,fixed('12345',3)))
print(145,nums('01234',4)[199]);print(146,len(fixed('01234',3)))
def ok147(s):
    if '5' not in s: return False
    k=s.count('2')
    if k>=2: return '2'*k in ''.join(s)
    return True
print(147,c(ok147,P('23456',repeat=4)))
print(148,c(lambda n:n%2==0,fixed('0123',4)))
import math
print(149,len({math.prod(t) for t in CR([3,7,11,13,19],7)}))
print(150,c(lambda n:n%2,fixed('0123',3)))
def ok152(s):
    if sum(map(int,s))%2==0: return False
    ev=[x for x in s if int(x)%2==0]; return len(ev)==len(set(ev))
print(152,c(ok152,P('234567',repeat=3)))
print(153,c(lambda n:n%2==0,fixed('01234',5)))
def ok156(s): o=[x for x in s if x in '345']; return len(o)==len(set(o))
print(156,c(ok156,P('12345',repeat=4)))
print(158,c(lambda n:n%2,fixed('012345',4)));print(159,c(lambda n:n%2==0,fixed('01234',4)))
print(161,c(lambda n:n%4==0 and n<3400,fixed('01234',4)))
a=fixed('123',3);print(162,sum(a)/len(a))
print(163,c(lambda s:'11' not in ''.join(s),P('123',repeat=5)))
print(164,c(lambda n:'3' in str(n),fixed('01234',3)))
print(165,c(ok156,P('12345',repeat=5)))
print(168,sorted(fixed('0123',4))[126]);print(169,c(lambda n:n%2,fixed('01234',5)))
def ok170(s): o=[x for x in s if x in '45']; return len(o)==len(set(o))
print(170,c(ok170,P('12345',repeat=4)))
print(171,c(lambda s:'2' in s and '3' in s,P('234',repeat=4)))
print(172,c(lambda s:len(set(s))>=2 and all(s[i]!=s[i+1] for i in range(3)),P('567',repeat=4)))
print(173,c(lambda n:n%2,fixed('01234',4)))
def ok174(s):
    return s[0]!='0' and s.count('0')<=1 and s.count('1')<=1
print(174,c(ok174,P('01234',repeat=4)))
n=c(lambda s:s.count('3') in (1,2),P('0123456789',repeat=4));print(175,n,n/243)
print(176,c(lambda n:n%3==0,fixed('123456789',3)))
n=c(lambda s:s.count('7') in (1,2),P('123456789',repeat=4));print(177,n,n/128)
print(178,'k(n)=3^n -> 3^(2n+1)/3^3=3^20 -> n=11')
print(180,c(lambda n:n%2==0,fixed('01234',3)));print(181,len(fixed('012345',3)));print(182,c(lambda n:n%2==0,fixed('01234',4)))
print(184,c(lambda n:n%3,fixed('123',3)));print(185,c(lambda s:'00' not in ''.join(s),[s for s in P('012',repeat=5) if s[0]!='0']))
