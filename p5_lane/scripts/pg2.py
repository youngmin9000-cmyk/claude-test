import sys, pymupdf as fitz
src,a,b,out=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
dpi=int(sys.argv[5]) if len(sys.argv)>5 else 110
d=fitz.open(src); r=d[0].rect; pg=list(range(a,b+1))
o=fitz.open(); P=o.new_page(width=r.width*len(pg),height=r.height)
for k,i in enumerate(pg): P.show_pdf_page(fitz.Rect(k*r.width,0,(k+1)*r.width,r.height),d,i)
P.get_pixmap(dpi=dpi).save(out)
