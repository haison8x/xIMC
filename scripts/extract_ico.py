"""Extract the problems of every ICO paper into one text file.

Input:  papers/ico/ICO{year}.pdf (booklets: round 1 short answers + answer table, round 2 with solutions)
        papers/ico/ICO{year}_{level}.pdf (problem sheets without answers)
Output: data/ico_problems.txt

Each problem is written as:
    === Year 2021 | Paper R1 | Problem 5 | Page 10 | Ref 14 ===
    <problem text>
Paper: R1 / R2 = round 1 / round 2 of a booklet; J / I = round 1 sheet of the Junior / Intermediate
level. Page = PDF page of the statement; Ref = page of the answer table (round 1) or of the
solution (round 2), 0 if the paper has neither.

Requires: pip install pymupdf
"""
import re

import pymupdf

import extract_imso as imso  # sequence splitting
from paths import DATA, ROOT

ICO = ROOT / "papers" / "ico"

# How problems are numbered, as (open paren, number, separator, rest) for extract_imso.split_sequences.
# Only that style counts, so sub-questions "1." "2." inside a "Problem 1." are not taken as problems.
MARKS = {
    "problem": re.compile(r"^Problem\s+()(\d{1,2})(\.)\s*(.*)$"),        # "Problem 3." (2021, 2024)
    "paren": re.compile(r"^()(\d{1,2})(\))\s*(.*)$"),                       # "3)" (2020 round 1)
    "dash": re.compile(r"^()(\d{1,2})(-)\s+(.*)$"),                          # "3- Title." (2020 round 2)
    "dot": re.compile(r"^()(\d{1,2})(\.)(?!\d)\s*(.*)$"),                  # "3." (2025 sheets)
}

# file, year, paper code, numbering, first and last page of the statements, problems, answer-table
# page (None = solutions follow and are found by their restated problem; 0 = no answers)
PAPERS = [
    ("ICO2020.pdf", 2020, "R1", "paren", 6, 9, 15, 10),
    ("ICO2020.pdf", 2020, "R2", "dash", 14, 16, 7, None),
    ("ICO2021.pdf", 2021, "R1", "problem", 5, 9, 15, 11),
    ("ICO2021.pdf", 2021, "R2", "problem", 15, 17, 7, None),
    ("ICO2024.pdf", 2024, "R1", "problem", 5, 10, 15, 11),
    ("ICO2024.pdf", 2024, "R2", "problem", 15, 17, 7, None),
    ("ICO2025_junior.pdf", 2025, "J", "dot", 1, 5, 15, 0),
    ("ICO2025_intermediate.pdf", 2025, "I", "dot", 1, 5, 15, 0),
    ("ICO2025_advanced.pdf", 2025, "R2", "dot", 1, 2, 7, 0),
]
JUNK_RE = re.compile(r"^\d+$|^Problems$|^(First|Second) Round$|^(Short Answer|Main) Exam$|^Proposed by"
                     r"|^\(?\s*→\s*p\.\s*\d+\s*\)?$|^[-−–\s]{8,}$|^Short Answers:$"
                     r"|^Combinatorics Olympiad$|^(Junior|Intermediate|Advanced & Free) Levels?$|^October \d{4}$")
# A short title line ("Strawberry farm") opens a context shared by the problems that follow it.
TITLE_RE = re.compile(r"^[A-Z][A-Za-z’' ]{2,30}$")


def norm(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def clean(parts):
    text = " ".join(" ".join(parts).replace("￿", "").split())
    text = re.sub(r"(\w)- (?=[a-z])", r"\1", text)  # "ran- domly" broken at a line end
    return re.sub(r" (?=[.,;:?!)])", "", text)


def lines_of(texts, first, last):
    """(line, page) of the statement pages, junk removed. A title line starts a context that is
    moved from the end of the problem before it to the start of the next problem."""
    out = []
    for page in range(first, last + 1):
        for ln in texts[page - 1].splitlines():
            ln = ln.strip()
            if ln and not JUNK_RE.search(ln):
                out.append((ln, page))
    return out


def split(lines, want, mark):
    seqs = imso.split_sequences(lines, want, MARKS[mark])
    exact = [s for s in seqs if len(s) == want]
    if not exact:
        return None
    problems = sorted(exact[-1])
    # Move a trailing "Title" + context paragraph to the next problem: a short title line between
    # the end of a sentence and a new sentence (not a line broken mid-sentence like "Assign a").
    for k in range(len(problems) - 1):
        parts = problems[k][1]
        for j in range(1, len(parts) - 1):
            if (TITLE_RE.match(parts[j]) and parts[j - 1].rstrip().endswith((".", "?", "!", ":", ")"))
                    and parts[j + 1][:1].isupper()):
                problems[k + 1][1][:0] = parts[j:]
                del parts[j:]
                break
    return problems


def extract():
    out = []
    docs = {}
    for name, year, paper, mark, first, last, want, answers in PAPERS:
        if name not in docs:
            with pymupdf.open(ICO / name) as doc:
                docs[name] = [page.get_text() for page in doc]
        texts = docs[name]
        problems = split(lines_of(texts, first, last), want, mark)
        if problems is None:
            raise SystemExit(f"{name} {paper}: {want} problems not found on pages {first}-{last}")
        for n, parts, page in problems:
            text = clean(parts)
            if answers is None:
                # The restated problem may have its "Title." at the foot of the page before.
                keys = {norm(text)[:40], norm(re.sub(r"^[A-Z][\w ’']{2,30}\.\s*", "", text))[:40]}
                ref = next((p for p in range(last + 1, len(texts) + 1)
                            if any(k in norm(texts[p - 1]) for k in keys)), None)
                if ref is None:
                    raise SystemExit(f"{name} {paper}{n}: solution page not found")
            else:
                ref = answers
            out.append((name, year, paper, n, page, ref, text))
    return out


def main():
    problems = extract()
    path = DATA / "ico_problems.txt"
    with path.open("w", encoding="utf-8") as fh:
        for name, year, paper, n, page, ref, text in problems:
            fh.write(f"=== Year {year} | Paper {paper} | Problem {n} | Page {page} | Ref {ref} ===\n{text}\n\n")
    for name in dict.fromkeys(p[0] for p in problems):
        print(f"papers/ico/{name}: {sum(p[0] == name for p in problems)} problems")
    print(f"-> {path.name}: {len(problems)} problems")


if __name__ == "__main__":
    main()
