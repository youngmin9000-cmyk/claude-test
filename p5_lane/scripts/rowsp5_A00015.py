import json
from cfgp5 import *
D = "서술형"
E = json.load(open(OUT + "p5l/A00015/ex.json")); import re as _re
ST = {int(k): (v[0], _re.sub(r"[\x00-\x08\x0b-\x1f\uf000-\uf8ff]", "∥", v[1])) for k, v in E['stmt'].items()}; SO = {int(k): v for k, v in E['sol'].items()}
def tax(n):
    if n <= 4: return ("기본 도형","평행선과 각","중1","GEO.BASIC.ANGLES_PARALLEL")
    if n <= 9: return ("평면도형","다각형의 내각과 외각","중1","GEO.POLYGON.ANGLE_SUM")
    if n <= 12: return ("삼각형의 성질","이등변삼각형","중2","GEO.TRIANGLE.ISOSCELES_PROOF")
    if n <= 17: return ("사각형의 성질","평행사변형과 여러 가지 사각형","중2","GEO.QUAD.PARALLELOGRAM_PROOF")
    if n == 18: return ("피타고라스 정리","피타고라스 정리의 증명","중2","GEO.PYTHAGORAS.PROOF")
    if n <= 22: return ("원의 성질","현과 접선의 성질","중3","GEO.CIRCLE.CHORD_TANGENT_PROOF")
    if n <= 25: return ("삼각형의 성질","외심·내심·무게중심","중2","GEO.TRIANGLE.CENTERS_PROOF")
    if n <= 29: return ("원의 성질","원주각의 성질","중3","GEO.CIRCLE.INSCRIBED_ANGLE_PROOF")
    if n == 30: return ("도형의 닮음","각의 이등분선의 성질","중2","GEO.SIMILAR.ANGLE_BISECTOR_RATIO")
    return ("원의 성질(심화)","원과 비례(방멱)","중3 심화","GEO.CIRCLE.POWER_OF_POINT_PROOF")
KEY = {n: f"증명 — 원문 풀이 PDF p{SO[n]}" for n in ST}
KEY[1] = "공리 수용(증명 불요) — 원문 풀이 PDF p51"
setup("A00015", "1LOy1ecbxRJgNuXtaIEPszkg6DMJ8YKd_", "전자책_맑은개념수학시리즈2024_중학도형_0413_@Logic_Files.pdf", "p5l/A00015/src.pdf", "일격필살팀(맑은개념수학)", "2024", "중학도형 증명 워크북 예제", "중1~중3", "중학 수학(도형)", CURR="2015 개정",
      KEY=KEY, KEYPAGE="각 예제 직후 풀이 쪽(PDF p51~91)", KEYSRC="",
      VIS="전자책 PDF(텍스트층 있음, 97쪽) 텍스트 추출; 도형 그림은 증명 보조", TEXT="PREVIEW_ONLY 캐시 → 원본 텍스트층 전체 추출")
builder.SOL_PAGE.update({k:0 for k in range(1,2000)})
for n in sorted(ST):
    pg, txt = ST[n]
    mid, small, grade, tid = tax(n)
    nsub = max(1, sum(txt.count(c) for c in "①②③④⑤⑥"))
    kw = dict(atype="증명", fig="도형")
    if n == 1:
        kw.update(review="REVIEW-비문항(공리 수용 진술)", ready="REVIEW", status="문항 아님(공리 수용) — 색인용 보존", trust="중간")
    diff = "하" if n <= 9 else ("중하" if n <= 25 else "중")
    R(n, pg, "도형", mid, small, tid, txt[:90].replace("  ", " "), "증명;"+small, diff, D, KEY[n], f"맑은개념 중학도형 예제{n}",
      f"표준 정리 증명 — 원문 풀이 PDF p{SO[n]} 대조(논리 전개 확인)", label=f"예제{n}", nsub=nsub, c=("보통" if n > 25 else "낮음"), **kw)
    r = ROWS[-1]; r.update({"출처대분류": "시판 개념서(전자책) 증명 예제", "학교명": "", "주관기관": "일격필살팀(오르비)", "학교/시험명": f"맑은개념수학 중학도형 예제{n}",
        "학년": grade, "원본페이지": f"PDF p{pg}", "문항이미지/좌표": f"PDF p{pg} 예제{n}"})
print(len(ROWS)); build("A00015", ROWS, 22)
