from itertools import product as P, combinations_with_replacement as CR
c=lambda f,it: sum(1 for x in it if f(x))
print(108,c(lambda s:s.count('B')<=2 and s.count('Y')<=2,P('RBY',repeat=4)))
print(113,c(lambda s:s[1]+s[2]==6,CR(range(1,10),5)))
def nums(digs,maxlen):
    out=set()
    for L in range(1,maxlen+1):
        for s in P(digs,repeat=L):
            if s[0]!='0' or L==1:
                v=int(''.join(s))
                if v>0: out.add(v)
    return sorted(out)
def rank(digs,v,ml=5): return nums(digs,ml).index(v)+1
print(114,rank('012345',3200,4))
print(115,nums('01234',4)[128])
print(116,rank('012345',2300,4))
print(117,rank('01234',3000,4))
print(118,rank('0345',4000,4))
print(119,rank('01356',3500,4))
print(120,rank('01234',1000,4))
ev=[x for x in nums('01234',4) if x%2==0];print(121,ev.index(2000)+1)
print(122,nums('1234',4)[90])
f4=[x for x in nums('0123',4) if x>=1000];print(123,f4.index(2200)+1)
print(124,len([x for x in nums('01357',3) if x>=100]),rank('01357',700,3))
print(125,rank('012345',13400,5))
