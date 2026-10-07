import sys, pymupdf as fitz
src,pg,x0,y0,x1,y1,out=sys.argv[1],int(sys.argv[2]),*map(float,sys.argv[3:7]),sys.argv[7]
d=fitz.open(src); r=d[pg].rect
cl=fitz.Rect(r.width*x0,r.height*y0,r.width*x1,r.height*y1)
d[pg].get_pixmap(dpi=int(sys.argv[8]) if len(sys.argv)>8 else 250,clip=cl).save(out)
