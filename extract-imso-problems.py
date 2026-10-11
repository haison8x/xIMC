"""Extract the mathematics problems of every IMSO paper PDF into one text file.

Input  (next to this script): IMSO/{ShortAnswer,Essay,Exploration}/IMSO_{year}_{Paper}[_Taiwan[-RoundN]].pdf
Output (next to this script): imso_problems.txt

Each problem is written as:
    === Year 2013 | Paper S | Problem 5 | Page 3 ===
    <problem text>

Paper codes: S = Short Answer, E = Essay, X = Exploration, Q = Short Answer of the Taiwan
first round (2008, 2009). 2005/2008/2009 are Taiwan selection papers; the second round is
stored under the normal codes.

Requires: pip install pymupdf
"""
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
IMSO = ROOT / "IMSO"

# Reuse the line cleaning / problem splitting of the IMC extractor.
_spec = importlib.util.spec_from_file_location("imc_extract", ROOT / "extract-imc-problems.py")
imc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(imc)

FILE_RE = re.compile(r"IMSO_(\d{4})_(ShortAnswer|Essay|Exploration)(?:_Taiwan(?:-Round(\d))?)?\.pdf$")
PAPER_CODE = {"ShortAnswer": "S", "Essay": "E", "Exploration": "X"}
# Expected number of problems per paper, to flag extraction problems.
EXPECTED = {"S": 25, "E": 13, "X": 6, "Q": 12}
EXPECTED_TAIWAN = {"S": 20, "E": 10, "X": 5, "Q": 12}


def papers():
    """Yield (year, code, taiwan, pdf) for every paper, sorted by year then paper."""
    found = []
    for pdf in IMSO.glob("*/*.pdf"):
        m = FILE_RE.search(pdf.name)
        if not m or pdf.parent.name == "Answers":
            continue
        year, paper, rnd = int(m[1]), m[2], m[3]
        code = "Q" if rnd == "1" else PAPER_CODE[paper]
        found.append((year, "QSEX".index(code), code, "_Taiwan" in pdf.name, pdf))
    for year, _, code, taiwan, pdf in sorted(found):
        yield year, code, taiwan, pdf


# IMSO papers number problems as "1.", "1)" or "(1)", the number often alone on its line.
MARK_RE = re.compile(r"^(\()?(\d{1,2})\s*([.．)])\s*(.*)$")
INSTRUCTION_RE = re.compile(r"Write (down )?your|answer sheet|minutes|index number|Participant ID|"
                            r"Do not turn|Instructions", re.I)


def split_sequences(lines, want):
    """Every "1" marker opens a candidate sequence, and every candidate parses the rest of
    the paper on its own: it accepts markers of the same style as its "1" ("1." / "1)" /
    "(1)") whose number is new and at most 3 past its highest (the layout sometimes prints
    problem 18 after 21); any other line is text of its current problem. So a list
    "(1) ... (6)" inside problem 20 stays part of problem 20 in the real sequence.
    Returns sequences of [number, text-lines, start-page]."""
    open_seqs = []  # [style, seen, problems]
    for ln, page in lines:
        m = MARK_RE.match(ln)
        mark = (bool(m[1]), m[3].replace("．", "."), int(m[2])) if m else None
        if mark and mark[2] == 1:
            open_seqs.append([mark[:2], set(), []])
        for style, seen, problems in open_seqs:
            if (mark and mark[:2] == style and mark[2] not in seen
                    and 1 <= mark[2] <= min(max(seen, default=0) + 3, want)):
                problems.append([mark[2], [m[4]], page])
                seen.add(mark[2])
            elif problems:
                problems[-1][1].append(ln)
    return [p for _, _, p in open_seqs if p]


def extract(pdf, want):
    """[(number, text, page)] for one paper. Instruction bullets and answer-sheet pages also
    form numbered sequences, so take the one with the expected number of problems (the
    longest text wins a tie), else the one with the most text."""
    sequences = split_sequences(imc.page_lines(pdf), want)
    # Drop the candidate that starts at the instruction bullets.
    sequences = [s for s in sequences if not INSTRUCTION_RE.search(" ".join(s[0][1])[:200])]
    if not sequences:
        return []
    size = lambda s: sum(len(" ".join(parts)) for _, parts, _ in s)
    exact = [s for s in sequences if len(s) == want]
    seq = max(exact or sequences, key=size)
    return sorted((n, imc.clean_text(parts), page) for n, parts, page in seq)


def main():
    out = ROOT / "imso_problems.txt"
    total = 0
    with out.open("w", encoding="utf-8") as fh:
        for year, code, taiwan, pdf in papers():
            want = (EXPECTED_TAIWAN if taiwan else EXPECTED)[code]
            problems = extract(pdf, want)
            flag = "" if len(problems) == want else f"   <-- expected {want}"
            print(f"{pdf.parent.name}/{pdf.name}: {len(problems)} problems{flag}")
            if flag:
                print(f"  WARNING: {pdf.name} has {len(problems)} problems, expected {want}", file=sys.stderr)
            for n, text, page in problems:
                fh.write(f"=== Year {year} | Paper {code} | Problem {n} | Page {page} ===\n{text}\n\n")
            total += len(problems)
    print(f"-> {out.name}: {total} problems")


if __name__ == "__main__":
    main()
