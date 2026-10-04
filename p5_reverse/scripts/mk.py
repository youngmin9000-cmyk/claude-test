import sys, os, zipfile; sys.path.insert(0,'/tmp/claude-0/-home-user-claude-test/b3c9c0b1-2d20-5f6f-a984-cabdebc0e83c/scratchpad')
from cfg68 import *
def repack(p):
    t=p+'.tmp'; zin=zipfile.ZipFile(p); zout=zipfile.ZipFile(t,'w',zipfile.ZIP_DEFLATED,compresslevel=9)
    for i in zin.infolist(): zout.writestr(i.filename, zin.read(i.filename))
    zout.close(); zin.close(); os.replace(t,p)
def build(name, rows, rng, cum0, review="없음", key_pages="", extra=()):
    print(name, validate(rows))
    p=OUT+f'Math_Question_DB_P5_Result_{name}_20261004.xlsx'
    save(rows,p,[("배치",name),("방향","P5→P4 역방향 신규 DB 구축"),("분석큐ID",CFG["QID"]),("원본파일",CFG["FNAME"]),("원본 Drive ID",SRC_ID),
      ("원본 SHA256(zip)",ZIP_SHA),("내부 PDF SHA256",PDF_SHA),("처리범위",rng),("정규 문항행",len(rows)),("하위문항 합계",sum(int(r['소문항수']) for r in rows)),
      ("정답 연결",key_pages),("REVIEW",review),("HOLD",sum(r['production_ready']=='HOLD' for r in rows)),
      ("역방향 누적(직전까지)",cum0),("역방향 누적(본 배치 후)",cum0+len(rows))]+list(extra))
    repack(p); os.system(f"base64 -w0 '{p}' > {OUT}{name}.b64; wc -c {OUT}{name}.b64")
