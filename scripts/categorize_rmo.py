"""Classify every RMO (Raffles Mathematical Olympiad, RIPMWC before 2024) Round 1 problem into the
groups / sub-groups below.

Reads   data/rmo_problems.txt (typed by hand from the scanned papers; there is no extract script)
Writes  data/rmo_categories.txt

Problem ids:  2024-5 = RMO 2024, Round 1, problem 5.
The classification is the hand-made table CODES below: one sub-group code per problem, listed per
year in problem order. The taxonomy is kept small on purpose, so that every sub-group collects at
least 15 problems.
"""
import re

from paths import DATA, RMO_PAPERS, ROOT

HEADER_RE = re.compile(r"=== Year (\d+) \| Paper (\w+) \| Problem (\d+) \| Page (\d+) ===\n(.*?)(?=\n=== Year|\Z)",
                       re.S)

# Paper types shown as filter chips in the mind map: (code, name). Only Round 1 papers are public.
KINDS = [("R1", "Vòng 1")]
LOWER_KIND_NAMES = False

TAX = dict(
    groups={
        1: "NUMBER THEORY",
        2: "CLEVER CALCULATION",
        3: "DIGITS & PATTERNS",
        4: "WORD PROBLEMS",
        5: "GEOMETRY",
        6: "COMBINATORICS & LOGIC",
    },
    subs={
        "1.1": "Divisibility, remainders, last digits & cycles",
        "1.2": "Divisors, primes, HCF / LCM & integer equations",
        "2.1": "Sums of sequences: telescoping & geometric",
        "2.2": "Substitution, grouping & common factors",
        "3.1": "Digits: digit sums, digit counts & number structure",
        "3.2": "Number arrays, sequences & repeated processes",
        "4.1": "Ratios, percentages, mixtures & equations",
        "4.2": "Motion, clocks & work rates",
        "5.1": "Areas & area ratios of polygons",
        "5.2": "Circles, arcs & shaded regions",
        "5.3": "Angles, lengths & solids",
        "6.1": "Counting arrangements & selections",
        "6.2": "Counting figures, paths & recursion",
        "6.3": "Logic, pigeonhole, games & extremal problems",
    },
)

CODES = {
    2008: "6.3 2.2 1.1 3.1 3.2 1.1 6.1 5.2 4.1 6.2 6.3 1.1 1.2 4.2 6.2 4.2 5.1 4.1 1.2 4.2",
    2009: "5.3 4.1 6.2 2.2 6.3 4.1 5.2 6.1 6.3 3.2 2.2 4.2 2.1 5.1 4.2 1.1 5.3 6.2 6.2 3.1",
    2010: "6.3 4.2 1.2 3.1 2.1 5.2 3.1 1.2 1.1 5.3 2.2 3.1 6.2 5.1 6.1 6.1 4.2 1.2 5.3 4.2",
    2011: "1.2 6.3 4.1 2.2 2.2 5.3 1.2 6.2 3.1 5.2 6.2 3.2 5.1 1.1 2.1 5.1 1.2 3.2 3.1 4.2",
    2012: "3.1 2.2 4.1 5.2 1.2 4.2 2.1 3.2 4.2 6.1 5.3 2.2 1.1 5.1 6.1 2.1 4.2 5.1 4.1 6.3",
    2013: "3.1 2.2 1.2 1.1 2.2 4.1 6.2 6.3 5.1 6.3 3.2 6.1 6.2 4.2 2.2 2.1 1.1 5.3 4.1 1.1",
    2014: "5.1 5.2 4.2 1.2 2.2 6.1 1.1 4.2 1.1 1.2 5.3 5.2 2.2 2.1 1.1 6.3 6.1 3.1 1.2 1.2",
    2015: "2.2 2.1 1.2 2.2 5.2 6.3 1.2 3.1 4.2 3.2 6.2 5.1 1.1 6.1 4.2 2.1 5.3 6.1 3.2 6.3",
    2016: "2.2 6.1 5.3 1.2 3.2 4.1 1.1 5.1 5.3 5.3 5.2 5.3 1.1 3.2 1.1 6.1 4.2 6.1 5.1 6.3",
    2017: "2.1 5.3 2.2 3.2 6.1 4.2 6.3 5.2 2.1 1.1 6.1 5.2 3.1 5.1 3.2 1.2 1.1 6.3 1.2 4.1",
    2018: "3.2 5.2 2.2 2.2 6.3 6.2 3.2 4.2 3.2 4.2 6.1 1.1 1.1 5.1 1.1 5.1 1.1 2.2 6.1 1.2",
    2019: "2.2 6.1 4.1 2.2 2.2 1.2 5.1 5.2 4.2 6.2 3.1 2.2 6.1 5.3 3.2 4.2 5.1 3.1 3.2 2.1",
    2021: "3.1 3.2 1.2 5.1 5.2 4.2 4.1 4.1 6.1 6.3 2.1 1.1 5.3 3.1 5.1 1.1 1.1 6.1 5.3 1.2",
    2022: "2.1 1.1 1.1 2.1 2.1 5.2 2.1 2.2 4.1 4.2 4.2 1.1 6.1 6.1 4.1 5.1 2.1 5.3 1.2 6.1",
    2023: "2.1 3.1 2.2 1.1 2.2 4.1 4.1 5.2 1.2 1.2 4.2 4.1 6.3 5.3 5.1 6.1 6.1 5.1 3.2 3.1",
    2024: "1.1 5.1 4.2 6.2 1.2 1.2 2.1 6.3 5.3 2.1 5.3 1.2 6.2 4.1 6.3 4.1 4.1 3.1 5.3 3.2",
    2025: "2.1 6.3 6.3 1.2 1.2 2.1 5.1 5.3 5.2 4.1 2.2 1.1 6.1 2.2 3.1 1.2 4.2 4.2 6.3 6.3",
}


def paper_file(year):
    """The question paper of a year, relative to the repo root."""
    return (RMO_PAPERS / f"RMO{year}.pdf").relative_to(ROOT).as_posix()


def answer_file(year):
    """The final-answer sheet of a year, relative to the repo root, or '' if there is none."""
    pdf = RMO_PAPERS / f"RMO{year}_answer.pdf"
    return pdf.relative_to(ROOT).as_posix() if pdf.exists() else ""


def load(stage="rmo"):
    """Return (problems in file order, {id: sub-group code}, taxonomy) in the shape of
    categorize.load."""
    probs = []
    for m in HEADER_RE.finditer((DATA / "rmo_problems.txt").read_text(encoding="utf-8")):
        year, paper, n, page = int(m[1]), m[2], int(m[3]), int(m[4])
        probs.append(dict(id=f"{year}-{n}", year=year, label=f"{paper}-{n}", page=page, kind=paper,
                          text=" ".join(m[5].split()), kind_name=dict(KINDS)[paper],
                          file=paper_file(year), file_label=f"Đề RMO {year}",
                          answer=answer_file(year), answer_label=f"Đáp án {year}"))
    assign = {}
    for year, codes in CODES.items():
        ids = [p["id"] for p in probs if p["year"] == year]
        codes = codes.split()
        if len(codes) != len(ids):
            raise SystemExit(f"rmo {year}: {len(codes)} codes for {len(ids)} problems")
        for pid, c in zip(ids, codes):
            if c not in TAX["subs"]:
                raise SystemExit(f"rmo {pid}: unknown sub-group {c}")
            assign[pid] = c
    missing = [p["id"] for p in probs if p["id"] not in assign]
    if missing:
        raise SystemExit(f"rmo: unclassified problems {missing[:10]}")
    return probs, assign, TAX


def write_categories(stage="rmo"):
    probs, assign, tax = load(stage)
    by = {}
    for p in probs:
        by.setdefault(assign[p["id"]], []).append(p)
    years = sorted({p["year"] for p in probs})
    L = ["RAFFLES MATHEMATICAL OLYMPIAD (RMO) ROUND 1 - PROBLEM CATEGORISATION", "=" * 60,
         f"Total problems: {len(probs)}, {years[0]}-{years[-1]} (no paper for 2020).",
         "The contest was called RIPMWC (RI Primary Mathematics World Contest) before 2024.",
         "IDs: Year-Problem. The text was typed by hand from the scanned papers.",
         "", "SUMMARY", "-" * 60]
    count = lambda prefix: sum(len(v) for k, v in by.items() if k.startswith(prefix))
    for g, name in tax["groups"].items():
        L.append(f"{g}. {name}  [{count(f'{g}.')} problems]")
        for k, sub in tax["subs"].items():
            if k.startswith(f"{g}."):
                L.append(f"     {k}  {sub}  ({count(k)})")
    L += ["", "NOTE: Each problem is placed in ONE best-fit sub-group (main idea of the solution).",
          "Figures are described in [Figure: ...]; check the PDF when the text is unclear.", "",
          "DETAILS", "=" * 60]
    for g, name in tax["groups"].items():
        L.append(f"\n##### {g}. {name}  [{count(f'{g}.')}] #####")
        for k, sub in tax["subs"].items():
            if not k.startswith(f"{g}."):
                continue
            L.append(f"\n--- {k} {sub} ({len(by.get(k, []))}) ---")
            for p in by.get(k, []):
                t = p["text"][:110] + ("..." if len(p["text"]) > 110 else "")
                L.append(f"  {p['id']:<8} {t}")
    out = DATA / "rmo_categories.txt"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out.name}: {len(probs)} problems")


if __name__ == "__main__":
    write_categories()
