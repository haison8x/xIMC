"""Extract the problems of every IMAS paper PDF into one text file per division.

Input:  papers/imas/{middle_primary,upper_primary,junior}/{YYYY-YYYY}_round{1,2}.pdf
Output: data/imas_{middle,upper,junior}_problems.txt

Each problem is written as:
    === Year 2023 | Round 1 | Problem 5 | Page 3 ===
    <problem text>

Year is the first year of the school year (2023-2024 -> 2023). Round 1 has 25 problems
(20 multiple choice, 5 with answers 000-999), round 2 has 15 (5 multiple choice, 8 short
answer, 2 with full solutions).

Requires: pip install pymupdf
"""
import re
import sys

import extract_imc as imc  # line cleaning
import extract_imso as imso  # sequence splitting
from paths import DATA, IMAS_PAPERS as IMAS

DIVISIONS = {"middle": "middle_primary", "upper": "upper_primary", "junior": "junior"}
FILE_RE = re.compile(r"^(\d{4})-\d{4}_round([12])$")
EXPECTED = {1: 25, 2: 15}
# Page codes printed in the footer: "UP 2", "MP 3", "JP 4", "J 5".
PAGE_CODE_RE = re.compile(r"^(MP|UP|JP|JR|J)\s*\d+$")
# Section headings and cover-page lines that would otherwise end up in the problem before them.
JUNK_RE = re.compile(r"^Questions?\s+\d+\s*(-|to|and|~)|^\(?Detailed solutions|ROUND PAPER|"
                     r"^International Mathematics Assessments|^Time allowed|^[─—-]{5,}|\d+ marks each\s*$", re.I)
# Problem markers as in IMSO, but a decimal like "6.25" in a table is not problem 6.
MARK_RE = re.compile(r"^(\()?(\d{1,2})\s*([.．)])(?!\d)\s*(.*)$")
# Round 1 instructions are numbered "1. Do not open the booklet ..." like the problems.
INSTRUCTION_RE = re.compile(imso.INSTRUCTION_RE.pattern + r"|Do not open|told to do so", re.I)


def papers(folder):
    """Yield (year, round, pdf) for every paper of a division, sorted."""
    found = []
    for pdf in (IMAS / folder).glob("*.pdf"):
        m = FILE_RE.match(pdf.stem)
        if m:
            found.append((int(m[1]), int(m[2]), pdf))
    yield from sorted(found)


def tidy(text):
    """Full-width brackets of the choices "（A）" -> "(A)"; drop the "ANSWER" box label of
    round 2 and the answer sheet after it."""
    text = re.split(r"\s*\bANSWER\b", text)[0]
    return re.sub(r"\s+", " ", text.replace("（", "(").replace("）", ")")).strip()


def extract(pdf, want):
    lines = [(ln, page) for ln, page in imc.page_lines(pdf)
             if not PAGE_CODE_RE.match(ln) and not JUNK_RE.search(ln)]
    sequences = imso.split_sequences(lines, want, MARK_RE)
    if not sequences:
        return []
    exact = [s for s in sequences if len(s) == want]
    if exact:
        # The numbered instructions ("1. Do not open ...", "1. Use only pencils.") also run on
        # into the real problems and reach the full count; the paper itself starts last.
        seq = exact[-1]
    else:
        real = [s for s in sequences if not INSTRUCTION_RE.search(" ".join(s[0][1])[:200])]
        seq = max(real or sequences, key=lambda s: sum(len(" ".join(parts)) for _, parts, _ in s))
    return sorted((n, tidy(imc.clean_text(parts)), page) for n, parts, page in seq)


def main():
    bad = 0
    for name, folder in DIVISIONS.items():
        out = DATA / f"imas_{name}_problems.txt"
        total = 0
        with out.open("w", encoding="utf-8") as fh:
            for year, rnd, pdf in papers(folder):
                want = EXPECTED[rnd]
                problems = extract(pdf, want)
                if len(problems) != want:
                    bad += 1
                    print(f"  WARNING: {folder}/{pdf.name} has {len(problems)} problems, expected {want}",
                          file=sys.stderr)
                for n, text, page in problems:
                    fh.write(f"=== Year {year} | Round {rnd} | Problem {n} | Page {page} ===\n{text}\n\n")
                total += len(problems)
        print(f"-> {out.name}: {total} problems")
    if bad:
        raise SystemExit(f"{bad} papers with the wrong number of problems")


if __name__ == "__main__":
    main()
