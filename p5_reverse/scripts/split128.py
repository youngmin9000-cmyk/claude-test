import sys; sys.path.insert(0,'.')
import b128
from cfg68 import *
import zipfile, os
A=[r for r in b128.rows if int(r['원문항번호'])<=63]; Bq=[r for r in b128.rows if int(r['원문항번호'])>=64]
for r in Bq: r['메모']=r['메모'].replace('Batch128','Batch129')
def repack(p):
    t=p+'.tmp'; zin=zipfile.ZipFile(p); zout=zipfile.ZipFile(t,'w',zipfile.ZIP_DEFLATED,compresslevel=9)
    for i in zin.infolist(): zout.writestr(i.filename, zin.read(i.filename))
    zout.close(); zin.close(); os.replace(t,p)
for name,rows,rng,cum0,note in [("Batch128",A,"PDF 9~10쪽 / Q51~Q63 (2-4 이차방정식과 이차함수의 관계 + 스스로 확인하기)",9940,"Q53 (정답 충돌: (4) 원문식 기준 '만나지 않는다' vs 원답지 '서로 다른 두 점')"),
                                ("Batch129",Bq,"PDF 11~12쪽 / Q64~Q75 (2-5 이차함수의 최대·최소 + 스스로 확인하기)",9940+len(A),"없음")]:
    print(name, validate(rows))
    p=OUT+f'Math_Question_DB_P5_Result_{name}_20261004.xlsx'
    save(rows,p,[("배치",name),("방향","P5→P4 역방향 신규 DB 구축"),("분석큐ID","A02668"),("원본파일",CFG["FNAME"]),("원본 Drive ID",SRC_ID),
      ("원본 SHA256(zip)",ZIP_SHA),("내부 PDF SHA256",PDF_SHA),("처리범위",rng),("정규 문항행",len(rows)),("하위문항 합계",sum(int(r['소문항수']) for r in rows)),
      ("정답 연결","동일 PDF 27~28쪽 빠른정답 + 33~34쪽 풀이"),("REVIEW",note),("HOLD",0),
      (f"역방향 누적(직전까지)",cum0),("역방향 누적(본 배치 후)",cum0+len(rows))])
    repack(p)
    os.system(f"base64 -w0 {p} > {name}.b64; wc -c {name}.b64")
