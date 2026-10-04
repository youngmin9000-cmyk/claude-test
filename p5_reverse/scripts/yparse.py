import re,sys,json
def parse(path):
    L=open(path).read().split('\n')
    items=[]; sec=''; act=None; i=0; mid=False
    while i<len(L):
        s=L[i]
        m=re.match(r'^\s{4}(\d-\d-\d\.\s*.+|중단원 마무리하기|대단원 마무리하기|대단원 평가.*)$',s)
        if m and L[i-1].strip()=='[tbl]': sec=m.group(1).strip(); i+=1; continue
        if re.match(r'^\[(.+)\]\s*$',s) and not s.startswith('[tbl]') and not s.startswith('[gso]'):
            act=s.strip('[] '); i+=1; continue
        if s.startswith(' ') and not s.startswith('  ') and i+1<len(L) and L[i+1].startswith('     '):
            stmt=[s.strip()]; ans=L[i+1].strip(); j=i+2; sol=[]; extra=[]
            while j<len(L) and not (L[j].startswith(' ') and not L[j].startswith('  ') and j+1<len(L) and L[j+1].startswith('     ')) and not re.match(r'^\[(.+)\]\s*$',L[j]) and L[j].strip()!='[tbl]':
                (sol if L[j].startswith('    ') else extra).append(L[j].strip()); j+=1
            items.append(dict(sec=sec,act=act,stmt=' '.join(stmt+extra),ans=ans.replace('[gso]',''),sol=' / '.join(sol)))
            act=None; i=j; continue
        i+=1
    return items
if __name__=='__main__':
    it=parse(sys.argv[1]); json.dump(it,open(sys.argv[2],'w'),ensure_ascii=False)
    for k,x in enumerate(it): print(k+1,'|',x['sec'][:14],'|',x['act'] or '-','|',x['stmt'][:230],'| ANS:',x['ans'][:120])
