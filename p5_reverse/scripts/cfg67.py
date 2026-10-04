import sys; sys.path.insert(0, '/tmp/claude-0/-home-user-claude-test/b3c9c0b1-2d20-5f6f-a984-cabdebc0e83c/scratchpad')
import builder
from builder import *
builder.configure(SRC_ID="1PejrDfgTJ2ly49mKOR03XkpicMTnmBqE",
    ZIP_SHA="71cececaabfc76a4fc71eee628577b4934fb6a0b027ea72ea612944048ba5282",
    PDF_SHA="6d5649aa839d48821e8c7a972e76064ad0d4e786b5ed478167e44366759ce214",
    TAG="CJGEO", QID="A02667", NPAGES=39, ANS_PAGES="27~29",
    FNAME="03 도형의 방정식(천재-류) 137제.zip > 03 도형의 방정식(천재-류) 137제.pdf",
    UNIT_TITLE="3. 도형의 방정식", BIG="Ⅲ. 도형의 방정식",
    SOL={30:(1,14),31:(15,28),32:(29,41),33:(42,57),34:(58,71),35:(72,86),36:(87,105),37:(106,120),38:(121,135),39:(136,137)},
    QUICK={27:(1,62),28:(63,117),29:(118,137)})
_S=[("G31","3-1 두 점 사이의 거리"),("G32","3-2 선분의 내분과 외분"),("G33","3-3 직선의 방정식"),("G34","3-4 두 직선의 평행과 수직"),
    ("G35","3-5 원의 방정식"),("G36","3-6 원과 직선의 위치관계"),("G37","3-7 평행이동"),("G38","3-8 대칭이동")]
for k,v in _S:
    builder.SECTIONS[k]=(v, v[4:]); builder.SECTIONS[k+"C"]=(v[:3]+" 스스로 확인하기", v[4:])
builder.SECTIONS["GMIX"]=("스스로 마무리하기(대단원)", "대단원 종합평가")
OUT = '/tmp/claude-0/-home-user-claude-test/b3c9c0b1-2d20-5f6f-a984-cabdebc0e83c/scratchpad/'
SRC_ID = builder.SRC_ID; ZIP_SHA = builder.ZIP_SHA; PDF_SHA = builder.PDF_SHA
