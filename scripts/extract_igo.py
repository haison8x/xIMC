"""Extract the problems of every IGO booklet into one text file.

Input:  papers/igo/IGO{year}.pdf: "Problems and Solutions" booklets, three levels of 5 problems.
Output: data/igo_problems.txt

Each problem is written as:
    === Year 2021 | Level I | Problem 3 | Page 17 | Solution 22 ===
    <problem text>
Level E/I/A = Elementary/Intermediate/Advanced. Page = PDF page of the statement in the problems
section, Solution = PDF page where its solution starts (solutions restate the problem).

Requires: pip install pymupdf
"""
import re

import pymupdf

import extract_imso as imso  # sequence splitting
from paths import DATA, ROOT

IGO = ROOT / "papers" / "igo"
LEVELS = {"Elementary": "E", "Intermediate": "I", "Advanced": "A"}
WANT = 5

LEVEL_RE = re.compile(r"\b(Elementary|Intermediate|Advanced)\s*(?:Level|\))")
PROBLEMS_RE = re.compile(r"^Problems\b(?!\s+and)")       # "Problems" / "Problems of 4th IGO 2017 (Elementary)"
SOLUTIONS_RE = re.compile(r"^Solutions\b")
# "Problem 3." (2018, 2020-), "3." (2017), "3)" (2019)
MARK_RE = re.compile(r"^(?:Problem\s+)?(\()?(\d{1,2})\s*([.．)])(?!\d)\s*(.*)$")
JUNK_RE = re.compile(r"^Proposed by|^\(?\s*→\s*p\.\s*\d+\s*\)?$|^\d+$|^(Elementary|Intermediate|Advanced) Level$"
                     r"|^[-−–\s]{8,}$")


def years():
    return sorted(int(p.stem[3:]) for p in IGO.glob("IGO*.pdf") if p.stem[3:].isdigit())


def source_pdf(year):
    return IGO / f"IGO{year}.pdf"


def page_texts(pdf):
    with pymupdf.open(pdf) as doc:
        return [page.get_text() for page in doc]


def norm(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def blocks(texts):
    """Problems sections as (level, [(line, page)]): from a "Problems" heading to the next
    "Problems" / "Solutions" heading. A page that lists several such headings is a table of
    contents and is skipped."""
    out, level, cur = [], None, None
    for page_no, text in enumerate(texts, 1):
        text = re.sub(r"(Elementary|Intermediate|Advanced)\s*\n\s*Level", r"\1 Level", text)  # "Intermediate\nLevel"
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        if sum(bool(PROBLEMS_RE.match(ln)) for ln in lines) > 1:
            continue
        for ln in lines:
            m = LEVEL_RE.search(ln)
            if m:
                level = LEVELS[m[1]]
            if PROBLEMS_RE.match(ln):
                cur = (level, [])
                out.append(cur)
            elif SOLUTIONS_RE.match(ln):
                cur = None
            elif cur is not None:
                cur[1].append((ln, page_no))
    return out


def is_junk(ln):
    """Running heads, page numbers, "Proposed by", "(→ p.5)" pointers and figure labels."""
    if MARK_RE.match(ln):
        return False
    return bool(JUNK_RE.search(ln)) or (len(ln) <= 3 and not re.search(r"[a-z]{2}", ln))


def clean(parts):
    text = " ".join(" ".join(parts).replace("\uffff", "").split())
    text = re.sub(r"(\w)- (?=[a-z])", r"\1", text)  # "bi- sector" broken at a line end
    return re.sub(r" (?=[.,;:?!)])", "", text)  # "segment XY ." before a period


def extract(year):
    pdf = source_pdf(year)
    texts = page_texts(pdf)
    found = {}
    sections = blocks(texts)
    problem_pages = {p for _, lines in sections for _, p in lines}
    for level, lines in sections:
        if level is None or level in found:
            continue
        lines = [(ln, p) for ln, p in lines if not is_junk(ln)]
        seqs = imso.split_sequences(lines, WANT, MARK_RE)
        exact = [s for s in seqs if len(s) == WANT]
        if exact:
            found[level] = sorted((n, clean(parts), page) for n, parts, page in exact[-1])
    problems = []
    for level in "EIA":
        if level not in found:
            raise SystemExit(f"IGO{year}: no {WANT} problems found for level {level}")
        for n, text, page in found[level]:
            key = norm(text)[:40]
            # Solutions restate the problem; skip the problems pages (2017 repeats a problem in two levels).
            sol = next((p for p in range(page + 1, len(texts) + 1)
                        if p not in problem_pages and key in norm(texts[p - 1])), None)
            if sol is None:
                raise SystemExit(f"IGO{year} {level}{n}: solution page not found")
            problems.append((level, n, page, sol, text))
    return pdf, problems


def main():
    out = DATA / "igo_problems.txt"
    total = 0
    with out.open("w", encoding="utf-8") as fh:
        for year in years():
            pdf, problems = extract(year)
            print(f"{pdf.relative_to(ROOT).as_posix()}: {len(problems)} problems")
            for level, n, page, sol, text in problems:
                fh.write(f"=== Year {year} | Level {level} | Problem {n} | Page {page} | Solution {sol} ===\n{text}\n\n")
            total += len(problems)
    print(f"-> {out.name}: {total} problems")


if __name__ == "__main__":
    main()
