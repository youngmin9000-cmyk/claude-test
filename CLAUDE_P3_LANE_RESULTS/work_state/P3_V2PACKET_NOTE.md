# P3 V2-packet source note (text-only; overrides page-image instructions in other notes)
Source text = existing Python preprocessing packets (_FULL_AUDIT_REPREPROCESS_V2, pdf_text extraction), already saved locally:
  /tmp/claude-0/w/P3/src/<QID>/v2_body.txt   (problem book; blocks "=== p<start>-<end> cand_no=<n> ===" — page markers are the packet's
                                              candidate pages; when a block spans many pages, estimate the page from position / running heads)
  /tmp/claude-0/w/P3/src/<QID>/v2_answer.txt (정답과 풀이/해설 book, same format) — may be absent (then answer is inside v2_body).
There are NO page images and you must NOT re-OCR or re-parse any PDF, and NEVER touch Google Drive.
Glyph map (pdf_text of Korean math books; verify by context): `Û`=², `Ü`=³, `Ý`=⁴, `Þ`=⁵, `ß`=⁶ (after a base: xÛ` = x^2); `'3`/`'¶17` = √3/√17;
`"Ã1-xÛ`` = √(1-x²); `;2!;` `;2#;` `;[!;` etc. = fractions (;a b; numerator/denominator glyph-coded — decode from context/solution);
`´` or `_` = ×; `É`=≤, `¾`=≥, `+` between expr and 0 in "x+0" condition = ≠; `aø`=vector a, `AB³`=vector AB; `Á` subscript 1, `ª` subscript 2;
풍산자 style: `rt3`=√3, `pai`=π, `^(..^)`=parentheses/brackets, `^^2`=², `a / b`=fraction. EBS: stacked fractions appear as "num\nden" lines.
Figures/graphs are NOT visible: if the answer needs figure data not recoverable from text (statement + book solution) → HOLD (HOLD_VISUAL).
If the statement is too garbled to reconstruct with certainty → HOLD_SOURCE. Otherwise solve independently (sympy for computation), compare to book key.
Official exam reprints (problem carries a tag like "20XX학년도 대수능 / 6월·9월 모의평가 / 학력평가 / 교육청", incl. 수능완성/수능특강 "필수 유형"/"대표 기출"
items with such tags, 자이스토리 [YYYY 학력평가 N번] tags) → NOT rows; list them in your reply.
printed_no: EBS items → the ID "21054-0123" style; EBS 예제 → "<chapter no> 예제 N"; other books → as printed with section label to make it unique
(e.g. "Ⅰ-01 개념 3", "유형07 12", "0082"). Every printed_no must be unique within your output.
Fields/verdict rules: /tmp/claude-0/w/AGENT_TASK.md and /tmp/claude-0/w/P3/P3_TEXT_TASK.md (key, sol_page = answer-book page marker, n running index).
Reply only with: count, verdict counts, non-PASS list (printed_no@page: reason), skipped official list.
