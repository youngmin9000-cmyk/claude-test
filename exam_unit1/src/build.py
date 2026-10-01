import re
import subprocess
import sys
import os
import importlib

from h import ITEMS, verify

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..')
TMP = os.path.join(HERE, 'tex')
os.makedirs(TMP, exist_ok=True)

CIRC = ['①', '②', '③', '④', '⑤']

PREAMBLE = r"""
\documentclass[10.5pt,a4paper]{article}
\usepackage{kotex}
\setmainfont{NanumMyeongjo}[BoldFont=NanumMyeongjoBold]
\setmainhangulfont{NanumMyeongjo}[BoldFont=NanumMyeongjoBold]
\setsansfont{NanumGothic}[BoldFont=NanumGothicBold]
\setsanshangulfont{NanumGothic}[BoldFont=NanumGothicBold]
\usepackage{amsmath,amssymb}
\usepackage[%GEOM%]{geometry}
\usepackage{multicol,tabularx,array,enumitem,xcolor,tikz,fancyhdr,lastpage,longtable,booktabs,colortbl}
\usepackage[most]{tcolorbox}
\usetikzlibrary{calc,angles,quotes}
\setlength{\columnseprule}{0.4pt}
\setlength{\columnsep}{9mm}
\setlength{\parindent}{0pt}
\linespread{1.32}
\newcommand{\rA}{\mathrm{A}}\newcommand{\rB}{\mathrm{B}}\newcommand{\rC}{\mathrm{C}}
\newcommand{\rD}{\mathrm{D}}\newcommand{\rE}{\mathrm{E}}\newcommand{\rF}{\mathrm{F}}
\newcommand{\rG}{\mathrm{G}}\newcommand{\rM}{\mathrm{M}}\newcommand{\rO}{\mathrm{O}}
\newcommand{\rP}{\mathrm{P}}\newcommand{\rQ}{\mathrm{Q}}\newcommand{\rH}{\mathrm{H}}
\newcommand{\seg}[1]{\overline{\mathrm{#1}}}
\newcommand{\boxsub}[1]{\par\smallskip\begin{tcolorbox}[colback=white,colframe=black,boxrule=0.5pt,arc=0pt,
  left=3mm,right=2mm,top=1mm,bottom=1mm]{\centering\small\sffamily〈 보 기 〉\par}\smallskip #1\end{tcolorbox}}
\definecolor{acc}{RGB}{30,60,110}
\definecolor{soft}{RGB}{235,240,248}
"""


def plain_len(s):
    t = re.sub(r'\\dfrac\{([^{}]*)\}\{([^{}]*)\}', r'\1/\2', s)
    t = re.sub(r'\\[a-zA-Z]+', '', t)
    t = re.sub(r'[{}$^_ ]', '', t)
    return len(t)


def choices_tex(ch, ccols=None):
    n = max(plain_len(c) + (3 if '\\dfrac' in c else 0) + 3 * sum(c.count(z) for z in '<>=') for c in ch)
    if ccols is None:
        ccols = 5 if n <= 6 else (3 if n <= 16 else 1)
    cells = [f"{CIRC[i]}\\ \\mbox{{{c}}}" for i, c in enumerate(ch)]
    if ccols == 5:
        return r"\par\medskip\begin{tabularx}{\linewidth}{@{}*{5}{X}@{}}" + " & ".join(cells) + r"\end{tabularx}"
    if ccols == 3:
        return (r"\par\medskip\begin{tabularx}{\linewidth}{@{}XXX@{}}" + " & ".join(cells[:3]) + r"\\[3pt]"
                + " & ".join(cells[3:]) + r" & \end{tabularx}")
    if ccols == 2:
        return (r"\par\medskip\begin{tabularx}{\linewidth}{@{}XX@{}}" + " & ".join(cells[:2]) + r"\\[3pt]"
                + " & ".join(cells[2:4]) + r"\\[3pt]" + cells[4] + r" & \end{tabularx}")
    return r"\par\medskip" + r"\par\smallskip ".join(cells)


def q_tex(it, sub_no=None):
    label = f"{it['no']}." if sub_no is None else f"서답형 {sub_no}."
    s = (r"\begin{minipage}{\linewidth}" + r"{\bfseries\sffamily " + label + r"}\ " + it['q']
         + f" \\hfill{{\\small [{it['pts']}점]}}")
    if it.get('fig'):
        s += r"\par\smallskip\begin{center}" + it['fig'] + r"\end{center}"
    if it['choices']:
        s += choices_tex(it['choices'], it.get('ccols'))
    s += r"\end{minipage}"
    space = '3.6cm' if it['choices'] else '6.2cm'
    if it.get('fig') and it['choices']:
        space = '2.6cm'
    return s + f"\\par\\vspace{{{space}}}\n"


def header(exam, kind):
    title = "1단원 실전 예상시험" if exam <= 5 else "시험 직전 최종 점검"
    sub = "정규 실전" if exam <= 5 else ("전체 범위 최종 점검" if exam == 6 else "시험 직전 마지막 실전")
    return (r"""
\begin{tcolorbox}[enhanced,colback=white,colframe=black,boxrule=1pt,arc=0pt,left=3mm,right=3mm,top=2mm,bottom=2mm]
{\small\sffamily 서울공업고등학교 내신 대비 \hfill 공통수학2 \quad Ⅰ. 도형의 방정식}\par\vspace{1mm}
\begin{center}{\LARGE\bfseries\sffamily %s \ 제 %d 회}\\[1mm]{\small\sffamily (%s)}\end{center}
\vspace{-1mm}
{\small 객관식 16문항(1$\sim$8번 각 4점, 9$\sim$16번 각 5점) \ $\cdot$ \ 서답형 4문항(각 7점) \ $\cdot$ \ 총 100점 \ $\cdot$ \ 50분}
\par\vspace{1.5mm}
\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash}p{12mm}|X|>{\centering\arraybackslash}p{12mm}|X|>{\centering\arraybackslash}p{12mm}|X|}
\hline 학년 & & 반 / 번호 & & 이름 & \\ \hline
\end{tabularx}
\end{tcolorbox}
\vspace{2mm}
""" % (title, exam, sub))


def exam_doc(exams, fname, doc_title):
    body = []
    for e in exams:
        items = ITEMS[e]
        body.append(r"\setcounter{page}{1}" if False else "")
        body.append(header(e, 'stu'))
        body.append(r"\begin{multicols}{2}")
        for it in items[:16]:
            body.append(q_tex(it))
        body.append(r"\columnbreak" if False else "")
        body.append(r"\end{multicols}")
        body.append(r"\clearpage")
        body.append(r"{\large\bfseries\sffamily 서답형}\ {\small (풀이 과정과 답을 모두 쓰시오. 각 7점)}\par\medskip\hrule\medskip")
        body.append(r"\begin{multicols}{2}")
        for i, it in enumerate(items[16:], 1):
            body.append(q_tex(it, i))
        body.append(r"\end{multicols}")
        body.append(r"\vfill\begin{center}{\small\sffamily --- 제 %d 회 끝 ---}\end{center}\clearpage" % e)
    foot = (r"\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}"
            r"\fancyfoot[C]{\small\sffamily %s \quad -- \thepage\ --}" % doc_title)
    write_and_compile(fname, PREAMBLE.replace('%GEOM%', 'top=14mm,bottom=18mm,left=14mm,right=14mm')
                      + r"\begin{document}" + foot + "\n".join(body) + r"\end{document}")


def sol_tex(it, e):
    s = it['sol']
    if it['choices']:
        ans = CIRC[it['ans'] - 1]
    else:
        ans = it['ans']
    label = f"{it['no']}번" if it['no'] <= 16 else f"서답형 {it['no'] - 16} ({it['no']}번)"
    steps = "".join(r"\item " + st + "\n" for st in s['steps'])
    return (r"""
\begin{tcolorbox}[enhanced,breakable,colback=white,colframe=acc,boxrule=0.6pt,arc=1mm,left=3mm,right=3mm,top=1.5mm,bottom=1.5mm,
title={\sffamily\bfseries 제%d회 \ %s \hfill {\normalfont\small %s \ | \ 난이도 %s}},colbacktitle=acc,coltitle=white]
{\sffamily\bfseries [정답]} \ %s\par\smallskip
{\sffamily\bfseries\color{acc}[핵심 개념]} \ %s\par\smallskip
{\sffamily\bfseries\color{acc}[왜 이렇게 푸는가]} \ %s\par\smallskip
{\sffamily\bfseries\color{acc}[단계별 풀이 · 계산 과정]}
\begin{enumerate}[label=\textsf{\arabic*단계},leftmargin=13mm,itemsep=2pt,topsep=2pt]
%s\end{enumerate}
{\sffamily\bfseries\color{red!60!black}[주의할 점 · 자주 하는 실수]} \ %s\par\smallskip
{\sffamily\bfseries [최종 답]} \ %s
\end{tcolorbox}
""" % (e, label, it['typ'], it['diff'], ans if it['choices'] else it['ans'], s['concept'], s['why'], steps,
       s['caution'], s['final']))


def answer_table(e):
    items = ITEMS[e]
    row1 = " & ".join(str(i) for i in range(1, 17))
    row2 = " & ".join(CIRC[it['ans'] - 1] for it in items[:16])
    t = (r"\begin{center}\small\begin{tabular}{|c|" + "c|" * 16 + r"}\hline 번호 & " + row1 + r"\\\hline 정답 & " + row2
         + r"\\\hline\end{tabular}\end{center}")
    t += r"\begin{center}\small\begin{tabularx}{\linewidth}{|c|X|}\hline"
    for i, it in enumerate(items[16:], 1):
        t += f"서답형 {i} & {it['ans']}" + r"\\\hline"
    t += r"\end{tabularx}\end{center}"
    return t


def solution_doc(fname):
    body = [r"""
\begin{center}{\LARGE\bfseries\sffamily 서울공고 공통수학2 \ Ⅰ. 도형의 방정식}\\[2mm]
{\Large\sffamily 실전 예상시험 1$\sim$5회 $\cdot$ 최종 점검 6$\sim$7회}\\[2mm]
{\Large\bfseries\sffamily 정답 및 상세 해설}\end{center}
\vspace{4mm}
\begin{tcolorbox}[colback=soft,colframe=acc,boxrule=0.5pt,arc=1mm]
\textbf{해설 읽는 법} \ 각 문항은 \textsf{[정답] → [핵심 개념] → [왜 이렇게 푸는가] → [단계별 풀이·계산 과정] → [주의할 점] → [최종 답]} 순서로 되어 있습니다.
먼저 스스로 풀어 본 뒤, 막힌 단계부터 읽어 보세요. 모든 풀이는 교과서 1단원에서 배운 공식과 방법만 사용합니다.
\end{tcolorbox}
\vspace{3mm}
{\large\bfseries\sffamily 빠른 정답표}
"""]
    for e in sorted(ITEMS):
        body.append(r"\par\medskip{\bfseries\sffamily 제 %d 회}" % e + answer_table(e))
    body.append(r"\clearpage")
    for e in sorted(ITEMS):
        body.append(r"\section*{\sffamily 제 %d 회 \ %s}" % (e, "실전 예상시험" if e <= 5 else "시험 직전 최종 점검"))
        for it in ITEMS[e]:
            body.append(sol_tex(it, e))
        body.append(r"\clearpage")
    foot = (r"\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}"
            r"\fancyfoot[C]{\small\sffamily 정답 및 상세 해설 \quad -- \thepage\ --}")
    write_and_compile(fname, PREAMBLE.replace('%GEOM%', 'top=15mm,bottom=18mm,left=18mm,right=18mm')
                      + r"\begin{document}" + foot + "\n".join(body) + r"\end{document}")


def teacher_doc(fname):
    rows = []
    for e in sorted(ITEMS):
        for it in ITEMS[e]:
            if it['choices']:
                ans = CIRC[it['ans'] - 1]
            else:
                ans = it['ans']
            no = str(it['no']) if it['no'] <= 16 else f"서{it['no'] - 16}"
            rows.append(f"{e} & {no} & {it['src']} & {it['typ']} & {it['mode']} & {it['diff']} & {ans}" + r"\\\hline")
        rows.append(r"\rowcolor{soft}\multicolumn{7}{|l|}{\small %s}\\\hline" % summary(e))
    tex = (PREAMBLE.replace('%GEOM%', 'landscape,top=12mm,bottom=14mm,left=12mm,right=12mm')
           + r"""\begin{document}\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\small\sffamily 교사용 문항 관리표 \quad -- \thepage\ --}
\begin{center}{\Large\bfseries\sffamily 교사용 문항 관리표 \ (서울공고 공통수학2 Ⅰ. 도형의 방정식, 1$\sim$7회)}\end{center}
{\small 원교과서 위치: 업로드 자료(미래엔 22개정 교과서 문제 모음) PDF 쪽수 \# 문항번호 [교과서 소단원·문항명]. \
변형방식: N = 숫자변형, M = 유형결합(1단원 내부 두 세부유형 결합). 난이도: 하 / 중 / 상(약간의 응용).}
\par\medskip
\small\renewcommand{\arraystretch}{1.25}
\begin{longtable}{|c|c|p{62mm}|p{88mm}|c|c|p{50mm}|}\hline
\rowcolor{soft}\textbf{회차} & \textbf{번호} & \textbf{원교과서 위치} & \textbf{원유형} & \textbf{N/M} & \textbf{난이도} & \textbf{정답}\\\hline\endhead
""" + "\n".join(rows) + r"\end{longtable}\end{document}")
    write_and_compile(fname, tex)


def summary(e):
    its = ITEMS[e]
    nN = sum(1 for i in its if i['mode'] == 'N')
    nM = sum(1 for i in its if i['mode'] == 'M')
    d = {k: sum(1 for i in its if i['diff'] == k) for k in ['하', '중', '상']}
    pos = [0] * 5
    for i in its[:16]:
        pos[i['ans'] - 1] += 1
    return (f"제{e}회 요약: N {nN}문항 / M {nM}문항 \\quad 난이도 하 {d['하']} · 중 {d['중']} · 상 {d['상']}"
            f" \\quad 객관식 정답 분포 " + " ".join(f"{CIRC[i]}{pos[i]}" for i in range(5)))


def write_and_compile(fname, tex):
    path = os.path.join(TMP, fname + '.tex')
    open(path, 'w').write(tex)
    for _ in range(2):
        p = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error', fname + '.tex'],
                           cwd=TMP, capture_output=True, text=True)
        if p.returncode != 0:
            print(p.stdout[-3000:])
            raise SystemExit(f"compile failed: {fname}")
    os.replace(os.path.join(TMP, fname + '.pdf'), os.path.join(OUT, fname + '.pdf'))
    print('built', fname)


if __name__ == '__main__':
    exams = [int(v) for v in sys.argv[1:]] or [1, 2, 3, 4, 5, 6, 7]
    for e in exams:
        importlib.import_module(f'e{e}')
    bad = []
    for e in exams:
        bad += verify(e)
    if bad:
        for b in bad:
            print('ERR', b)
        raise SystemExit(1)
    print('all verified:', exams)
    reg = [e for e in exams if e <= 5]
    fin = [e for e in exams if e >= 6]
    if reg:
        exam_doc(reg, '1_학생용_실전예상시험_1-5회', '서울공고 1단원 실전 예상시험')
    if fin:
        exam_doc(fin, '2_학생용_최종점검_6-7회', '서울공고 시험 직전 최종 점검')
    solution_doc('3_정답및상세해설_1-7회')
    teacher_doc('4_교사용_문항관리표')
