"""Extract the problems of every IMC past paper PDF into one text file per keystage.

Input:  papers/imc/keystage{2,3}/{year}.pdf and {year}_team.pdf
Output: data/keystage{2,3}_problems.txt       (Individual papers)
        data/keystage{2,3}_team_problems.txt  (Team papers)

Each problem is written as:
    === Year 2012 | Problem 3 | Page 1 ===   (Section A / B problems: "Problem B2";
                                              Page = PDF page where the problem starts)
    <problem text>

Requires: pip install pymupdf
"""
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

import pymupdf

from paths import DATA, IMC_PAPERS

KEYSTAGES = ["keystage2", "keystage3"]

PROBLEM_RE = re.compile(r"^\s*(?:[QT]\s*)?(\d{1,2})\s*[.．]\s*(.*)$")
ANSWER_LINE_RE = re.compile(r"^\s*Answers?\s*[:：]?\s*(_{3,}.*)?$|^\s*_{5,}\s*$", re.I)
SECTION_RE = re.compile(r"^\s*Section\s+([A-Z]|I{1,3})\b", re.I)
PAGE_NO_RE = re.compile(r"^\s*(Page\s*)?\d+\s*(/|of)?\s*\d*\s*$", re.I)


def is_garbage(line: str) -> bool:
    """Garbled CJK / symbol-font header lines that carry no ASCII text."""
    if re.search(r"[A-Za-z0-9]", line):
        return False
    return any(ord(c) >= 0x600 and unicodedata.category(c)[0] in "LM" for c in line)


def page_lines(pdf: Path):
    """Return (line, page_no) for the whole PDF, repeated headers removed."""
    pages = []
    with pymupdf.open(pdf) as doc:
        for page in doc:
            pages.append([ln.rstrip() for ln in page.get_text().splitlines()])
    repeated = Counter(
        ln.strip() for lines in pages for ln in set(lines) if len(ln.strip()) > 12
    )
    min_pages = max(3, len(pages) // 2 + 1)
    lines = []
    for page_no, page in enumerate(pages, 1):
        for ln in page:
            s = ln.strip()
            if not s or is_garbage(s) or repeated[s] >= min_pages:
                continue
            if ANSWER_LINE_RE.match(s) or PAGE_NO_RE.match(s):
                continue
            lines.append((s, page_no))
    return lines


def parse_problems(lines):
    """Walk the lines; a line "N." starts a problem only when N is the next
    expected number. Returns a list of sequences (A, B, ...), each a list of
    [number, text-lines, closed, start-page]."""
    sequences, current, expected = [], None, 1
    for ln, page_no in lines:
        if SECTION_RE.match(ln) and current:
            # Section heading closes the problem in progress, never its text.
            current[-1][2] = True
            continue
        m = PROBLEM_RE.match(ln)
        if m:
            n = int(m.group(1))
            if n == 1:
                # A real new sequence, or the first problem again after instruction
                # bullets like "1. For decimal ..." that came before it.
                if current is not None and len(current) < 8:
                    sequences.pop()
                current = []
                sequences.append(current)
                expected = 1
            if n == expected and current is not None:
                current.append([n, [m.group(2)], False, page_no])
                expected += 1
                continue
        if current and not current[-1][2]:
            current[-1][1].append(ln)
    return sequences


def clean_text(parts):
    text = " ".join(parts)
    text = text.replace(" ", " ")
    text = re.sub(r"\s+", " ", text).strip()
    # Everything after an "Answer:" blank is answer-sheet boilerplate / page header.
    text = re.split(r"\s*Answers?\s*[:：ǺĈ]", text, maxsplit=1)[0]
    return text.strip()


def extract_pdf(pdf: Path):
    """Return [(label, text, page)] for one PDF."""
    sequences = parse_problems(page_lines(pdf))
    sequences = [s for s in sequences if s]
    out = []
    for idx, seq in enumerate(sequences):
        prefix = "" if len(sequences) == 1 else chr(ord("A") + idx)
        for n, parts, _, page_no in seq:
            out.append((f"{prefix}{n}", clean_text(parts), page_no))
    return out


def write_problems(ks: str, suffix: str, out_name: str):
    """Extract all {year}{suffix}.pdf of a keystage into one text file."""
    pdfs = [
        p
        for p in (IMC_PAPERS / ks).glob(f"*{suffix}.pdf")
        if p.stem[: len(p.stem) - len(suffix)].isdigit()
    ]
    pdfs.sort(key=lambda p: p.stem)
    out_path = DATA / out_name
    total = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for pdf in pdfs:
            year = pdf.stem[: len(pdf.stem) - len(suffix)]
            problems = extract_pdf(pdf)
            print(f"{ks}/{pdf.name}: {len(problems)} problems")
            if not problems:
                print(f"  WARNING: nothing extracted from {pdf}", file=sys.stderr)
            for label, text, page_no in problems:
                fh.write(f"=== Year {year} | Problem {label} | Page {page_no} ===\n{text}\n\n")
            total += len(problems)
    print(f"-> {out_path.name}: {total} problems\n")


def main():
    for ks in KEYSTAGES:
        write_problems(ks, "", f"{ks}_problems.txt")
        write_problems(ks, "_team", f"{ks}_team_problems.txt")


if __name__ == "__main__":
    main()
