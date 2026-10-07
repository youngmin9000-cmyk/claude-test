import json, cfgex
from cfgp5 import *
d=json.load(open('p5l/A00660/w/items.json'))
FILES=[('1','풍필유-수학(II) 01 함수의 극한.hwp','함수의 극한과 연속','함수의 극한','01 간단한 함수의 극한',73),
       ('2','풍필유-수학(II) 02 함수의 연속.hwp','함수의 극한과 연속','함수의 연속','01 함수의 연속의 의미',51),
       ('0','풍필유-수학(II) 03 미분계수와 도함수.hwp','미분','미분계수와 도함수','01 평균변화율과 그 의미',50)]
FIG={'1':{40,42,43,45,46,50,54,55,56,57,78,84},'0':{3,4,5,9,32,62},'2':{4,5,6,7,8,9,10,39,57}}
HOLD={('1',26):("1 (인쇄된 x⁵ 기준)","원문 지수 오기 의심: 문제 x⁵+5, 원문 풀이는 x²+5로 계산(−1/2). 인쇄 문제 기준 독립값 1"),
      ('1',37):("7","원문 풀이 오류: f=3x³+2x²+2x인데 풀이에서 3x³+x²+2x로 적어 f(1)=6. 독립값 7"),
      ('1',44):("−3 (①)","문제 x²−3x+a(x<1)와 원문 풀이 x²−4x+a 불일치. 인쇄 문제 기준 a=0, b=3 → a−b=−3(①); 키 ②(−2)는 풀이식 기준"),
      ('0',55):("① 51","원문 풀이는 51을 도출하나 정답표는 ⑤(55). 51은 보기 ①")}
REV={('2',45):"원문 전제 부정확: 10x¹⁰+10x=a는 짝수차라 실근 1개는 최솟값일 때뿐. 의도(−1<근<1 ⇔ 0<a<20) 해석 시 정수 19개=키 ③",
     ('2',31):"키 '풀이 참조' — 독립답: ⑴ 실수 전체에서 연속 ⑵ x≠1, 3인 모든 실수에서 연속(x=1, 3에서 불연속)"}
TYPO={('2',16):"조건 표기 오기 (x>0)→(x>1) 해석", ('2',18):"조건 표기 오기 (x<2)→(x<−2) 해석", ('2',54):"lim n→∞ 표기 오기(x→∞)", ('1',3):"lim n→∞ 표기 오기(x→∞)", ('0',19):""}
allrows=[]; cum=362
import re
def clean(s):
    s=re.sub(r'\s+',' ',s.replace('⟦','').replace('⟧',''))
    return s[:220]
for k,fn,big,mid,sec0,hard in FILES:
    pass
cfgex.ROWS.clear()
key={}
items=[]
for k,fn,big,mid,sec0,hard in FILES:
    for i,x in enumerate(d[k],1):
        items.append((k,fn,big,mid,sec0,hard,i,x))
for n,(k,fn,big,mid,sec0,hard,i,x) in enumerate(items,1): key[n]=x['ans']
setup("A00660","1aMPb_jPLvxVPVB4bHvZaW025kPetdMqw","수학2(1).zip [풍산자 필수유형 수학Ⅱ 01~03]","p5l/A00660/src.zip","풍산자 필수유형(시판 문제집)","2022 개정","수학Ⅱ 1~3장","고2","수학Ⅱ",CURR="2022 개정",KEY=key,KEYPAGE="각 HWP 후반 정답·풀이",KEYSRC="",VIS="HWP 본문·수식 추출(로컬 파서); 그림(gso)은 텍스트 미추출",TEXT="HWP 텍스트층(수식 스크립트 포함) — FULL_TEXT")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
for n,(k,fn,big,mid,sec0,hard,i,x) in enumerate(items,1):
    sec=x['sec'] or sec0
    sec=re.sub(r'[{}]','',sec).replace(' over ','/').replace('times0','×0')
    small=re.sub(r'^\d\d ','',sec)
    diff='상' if i>=hard else ('하' if i<=len(d[k])*0.3 else '중')
    fmt='객관식' if '①' in x['text'] else '서술형'
    tid=f"S2.{mid}.{sec[:2]}"
    kw={}; fig="없음"; ans=x['ans']; final=None
    note="원문 정답·풀이 동봉(동일 HWP) — 독립풀이(sympy/수기) 대조"
    if i in FIG[k]:
        fig="그림(HWP gso, 미추출)"; kw.update(status="원문 정답 기재 — 그림 조건 미판독으로 독립검증 보류", trust="중간(원문 정답 의존)")
    if (k,i) in HOLD:
        final,why=HOLD[(k,i)]; kw.update(ready="HOLD",review="HOLD-원문정답충돌",status="독립풀이 ≠ 원문 정답(원문 정답 보존)",trust="낮음(충돌)",conflict=why)
        note+="; 충돌: "+why
    if (k,i) in REV:
        kw.update(ready="REVIEW",review="REVIEW-원문조건검토",status="독립풀이·원문 정답 대조(원문 조건 검토 필요)",trust="중간"); note+="; "+REV[(k,i)]
    if TYPO.get((k,i)): note+="; "+TYPO[(k,i)]
    R(n,int(k)+1,big,mid,small,tid,f"{small} — {fn[11:]} {i}번",mid+";"+small,diff,fmt,ans+(f" | 독립: {final}" if final else ""),clean(x['text']),note,
      label=f"{fn[:-4].split(') ')[1]}-{i}",fig=fig,final=final,**kw)
    ROWS[-1].update({"출처대분류":"시판 문제집(풍산자 필수유형)","학교/시험명":f"풍산자 필수유형 수학Ⅱ {fn[11:-4]} {i}번","해설연결상태":"동일 파일 정답·풀이"})
build("A00660",list(ROWS),cum); print(len(ROWS))
