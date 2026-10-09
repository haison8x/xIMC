"""Extract the problems of every IMC past paper PDF into one text file per keystage.

Input  (next to this script): keystage2/{year}.pdf, keystage3/{year}.pdf
Output (next to this script): keystage2_problems.txt, keystage3_problems.txt

Each problem is written as:
    === Year 2012 | Problem 3 ===        (Section A / B problems: "Problem B2")
    <problem text>

Requires: pip install pymupdf
"""
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

import pymupdf

ROOT = Path(__file__).parent
KEYSTAGES = ["keystage2", "keystage3"]

PROBLEM_RE = re.compile(r"^\s*(?:Q\s*)?(\d{1,2})\s*[.．]\s*(.*)$")
ANSWER_LINE_RE = re.compile(r"^\s*Answers?\s*[:：]?\s*_{3,}.*$|^\s*_{5,}\s*$", re.I)
SECTION_RE = re.compile(r"^\s*Section\s+([A-Z]|I{1,3})\b", re.I)
PAGE_NO_RE = re.compile(r"^\s*(Page\s*)?\d+\s*(/|of)?\s*\d*\s*$", re.I)


def is_garbage(line: str) -> bool:
    """Garbled CJK / symbol-font header lines that carry no ASCII text."""
    if re.search(r"[A-Za-z0-9]", line):
        return False
    return any(ord(c) >= 0x600 and unicodedata.category(c)[0] in "LM" for c in line)


def page_lines(pdf: Path):
    """Return the cleaned lines of the whole PDF, repeated headers removed."""
    pages = []
    with pymupdf.open(pdf) as doc:
        for page in doc:
            pages.append([ln.rstrip() for ln in page.get_text().splitlines()])
    repeated = Counter(
        ln.strip() for lines in pages for ln in set(lines) if len(ln.strip()) > 12
    )
    min_pages = max(3, len(pages) // 2 + 1)
    lines = []
    for page in pages:
        for ln in page:
            s = ln.strip()
            if not s or is_garbage(s) or repeated[s] >= min_pages:
                continue
            if ANSWER_LINE_RE.match(s) or PAGE_NO_RE.match(s):
                continue
            lines.append(s)
    return lines


def parse_problems(lines):
    """Walk the lines; a line "N." starts a problem only when N is the next
    expected number. Returns a list of sequences (A, B, ...), each a list of
    [number, text-lines]."""
    sequences, current, expected = [], None, 1
    for ln in lines:
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
                current.append([n, [m.group(2)], False])
                expected += 1
                continue
        if current and not current[-1][2]:
            current[-1][1].append(ln)
    return sequences


def clean_text(parts):
    text = " ".join(parts)
    text = text.replace(" ", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_pdf(pdf: Path):
    """Return [(label, text)] for one PDF."""
    sequences = parse_problems(page_lines(pdf))
    sequences = [s for s in sequences if s]
    out = []
    for idx, seq in enumerate(sequences):
        prefix = "" if len(sequences) == 1 else chr(ord("A") + idx)
        for n, parts, _ in seq:
            out.append((f"{prefix}{n}", clean_text(parts)))
    return out


def main():
    for ks in KEYSTAGES:
        pdfs = sorted((ROOT / ks).glob("*.pdf"), key=lambda p: p.stem)
        pdfs = [p for p in pdfs if p.stem.isdigit()]
        out_path = ROOT / f"{ks}_problems.txt"
        total = 0
        with out_path.open("w", encoding="utf-8") as fh:
            for pdf in pdfs:
                problems = extract_pdf(pdf)
                print(f"{ks}/{pdf.name}: {len(problems)} problems")
                if not problems:
                    print(f"  WARNING: nothing extracted from {pdf}", file=sys.stderr)
                for label, text in problems:
                    fh.write(f"=== Year {pdf.stem} | Problem {label} ===\n{text}\n\n")
                total += len(problems)
        print(f"-> {out_path.name}: {total} problems\n")


if __name__ == "__main__":
    main()
