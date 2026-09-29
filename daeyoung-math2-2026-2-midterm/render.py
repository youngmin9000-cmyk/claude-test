"""HTML 보고서를 A4 PDF로 변환한다. 사용: python3 render.py"""
import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
FOOT = ('<div style="width:100%;text-align:center;font-family:NanumGothic;font-size:7.5pt;color:#5d6673">'
        '{label} · <span class="pageNumber"></span> / <span class="totalPages"></span></div>')

JOBS = [
    ("teacher.html", "대영고1_공통수학2_2학기중간_강사용_최종사후분석.pdf",
     "대영고 1학년 공통수학2 2학기 중간고사 최종 사후분석"),
    ("parent.html", "대영고1_공통수학2_2학기중간_학생학부모용_분석.pdf", None),
]

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    page = browser.new_page()
    for src, out, label in JOBS:
        page.goto((HERE / src).as_uri())
        page.wait_for_load_state("networkidle")
        opts = dict(path=str(HERE / out), format="A4", print_background=True, prefer_css_page_size=True)
        if label:
            opts.update(display_header_footer=True, header_template="<div></div>",
                        footer_template=FOOT.format(label=label))
        page.pdf(**opts)
        print("wrote", out)
    browser.close()
