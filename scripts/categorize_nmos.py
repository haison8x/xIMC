"""Classify every NMOS (National Mathematical Olympiad of Singapore) problem into the groups /
sub-groups below.

Reads   data/nmos_problems.txt (typed by hand from the papers; there is no extract script)
Writes  data/nmos_categories.txt

Problem ids:  2019-P-3 = NMOS 2019 Preliminary Round, problem 3; 2019-S-3 = Special Round, problem 3.
              Since 2024 there is a single paper, stored as paper P.
The classification is the hand-made table CODES below: one sub-group code per problem, listed per
year and paper in problem order. The taxonomy is kept small on purpose, so that every sub-group
collects at least 20 problems.
"""
import re
from urllib.parse import quote

from paths import DATA, ROOT

NMOS = "papers/nmos"
HEADER_RE = re.compile(r"=== Year (\d+) \| Paper (\w) \| Problem (\d+) \| Page (\d+) ===\n(.*?)(?=\n=== Year|\Z)",
                       re.S)

# Rounds shown as filter chips in the mind map: (code, name).
KINDS = [("P", "Vòng sơ khảo"), ("S", "Vòng đặc biệt")]
LOWER_KIND_NAMES = False

TAX = dict(
    groups={
        1: "NUMBER THEORY & DIGITS",
        2: "CALCULATION & SEQUENCES",
        3: "WORD PROBLEMS",
        4: "GEOMETRY",
        5: "COMBINATORICS & LOGIC",
    },
    subs={
        "1.1": "Divisibility, remainders, last digits & cycles",
        "1.2": "Factors, primes, HCF / LCM & integer equations",
        "1.3": "Digits, number structure & cryptarithms",
        "2.1": "Clever calculation, series & number patterns",
        "2.2": "Defined operations, algebraic expressions & estimation",
        "3.1": "Ratios, percentages & fractions of quantities",
        "3.2": "Sum-difference, averages, ages, assumption & money",
        "3.3": "Motion, clocks & work rates",
        "4.1": "Areas & area ratios",
        "4.2": "Angles, lengths, circles & solids",
        "5.1": "Counting",
        "5.2": "Inclusion-exclusion, pigeonhole & extremes",
        "5.3": "Logic, puzzles & games",
    },
)

CODES = {
    2011: dict(P="3.2 3.1 4.1 2.1 1.1 3.1 4.1 3.2 5.3 3.2 3.1 3.1 3.2 1.1 5.1 3.3 4.1 5.3 3.1 3.1 4.1 5.1 5.3 4.1 1.3 5.3 3.2 3.3 4.1 4.1"),
    2012: dict(P="3.2 3.1 4.1 2.1 4.2 3.1 2.1 3.1 3.3 2.2 4.1 3.1 1.2 4.2 3.3 4.1 3.1 5.3 4.1 1.1 4.1 5.3 5.2 3.2 5.3 5.1 3.2 5.3 4.2 5.3"),
    2013: dict(P="4.1 1.2 3.1 3.1 2.2 5.3 3.2 3.1 2.2 3.3 4.1 3.1 3.2 4.2 3.3 4.2 3.2 3.2 4.2 1.1 3.1 1.1 4.2 3.1 1.2 4.1 3.3 1.2 5.3 3.3",
               S="3.1 4.1 4.2 2.2 3.1 1.3 5.2 3.3 3.3 5.1 5.3 1.2 1.3 4.2 1.1 3.3 4.1 1.2 5.2 1.3"),
    2014: dict(P="2.2 4.1 4.2 4.1 2.1 3.3 3.2 3.1 3.3 2.1 3.1 4.2 2.1 3.1 3.3 5.3 4.2 3.1 3.2 4.2 3.3 1.2 4.1 3.3 1.3 4.1 1.2 5.3 4.2 5.3",
               S="3.1 2.1 4.1 1.3 3.3 4.1 3.1 5.2 4.2 3.3 5.1 1.2 5.1 2.1 4.1 2.2 4.2 2.1 2.1 5.3"),
    2015: dict(P="2.1 3.2 3.2 4.1 3.2 3.1 4.2 4.2 3.3 4.1 3.1 3.1 4.1 3.1 3.3 3.1 2.1 3.3 1.3 3.1 2.1 1.1 5.1 3.3 1.1 4.1 3.2 1.2 3.3 5.3",
               S="3.1 4.1 3.3 1.1 1.1 4.1 3.3 5.1 3.3 2.1 2.2 5.3 1.3 4.1 1.2 1.2 5.2 1.3 4.1 5.3"),
    2016: dict(P="2.1 3.2 3.2 4.1 1.2 3.1 4.2 3.1 3.2 4.1 3.1 5.3 3.1 5.3 3.2 4.2 3.1 3.2 4.2 3.3 3.3 4.1 5.2 1.3 4.1 3.1 4.1 1.3 4.1 3.2",
               S="3.1 4.1 3.2 2.2 5.2 4.1 3.3 3.1 3.1 3.3 1.2 3.3 3.3 5.3 4.2 5.1 1.2 2.1 4.2 1.3"),
    2017: dict(P="2.1 3.1 4.1 1.1 1.2 1.1 2.1 4.2 3.1 5.2 3.3 4.2 3.2 4.2 3.3 5.1 5.1 4.1 3.1 1.3 3.1 4.2 4.1 4.1 2.2 5.1 4.1 1.2 3.3 5.1",
               S="3.1 4.1 5.1 4.2 3.1 1.1 3.3 3.3 4.1 1.3 3.3 4.2 3.2 3.3 4.1 2.1 2.2 1.1 5.3 5.3"),
    2018: dict(P="2.1 4.2 1.2 3.2 3.1 3.2 3.3 5.2 4.2 3.3 3.2 4.2 4.2 4.1 3.2 5.1 3.3 1.2 4.2 5.2 4.1 3.3 4.1 5.1 1.3 4.1 3.2 1.2 1.2 5.3",
               S="4.1 3.2 1.1 4.1 1.1 2.2 5.2 3.2 4.1 4.2 4.1 3.2 1.2 1.1 3.3 5.2 3.3 2.2 4.2 4.2"),
    2019: dict(P="2.1 5.1 3.1 4.1 3.2 5.3 4.1 3.3 2.1 3.2 3.2 1.2 4.2 3.3 3.2 2.1 2.2 4.2 4.1 4.2 3.1 1.2 4.2 3.3 1.2 5.1 4.1 2.1 5.3 5.2",
               S="2.1 1.1 4.1 3.1 3.3 2.2 4.2 3.3 1.2 5.2 4.1 1.1 5.1 5.1 1.3 4.1 2.1 2.1 4.1 2.2"),
    2021: dict(P="2.1 4.2 3.1 4.1 1.3 4.2 3.1 5.1 3.3 1.3 4.2 1.3 3.3 3.3 1.2 3.2 3.3 1.3 5.1 5.1 1.3 3.1 2.1 4.2 1.1 4.1 5.2 4.1 1.1 5.1"),
    2022: dict(P="2.1 3.2 4.1 3.2 4.2 3.1 1.1 4.2 4.1 1.1 1.3 5.1 4.1 4.1 1.2 4.1 2.1 3.3 1.3 5.3 4.2 3.1 2.2 3.1 5.1 3.3 2.2 5.3 5.1 5.2",
               S="2.1 1.2 3.2 4.1 1.1 1.2 5.1 2.2 3.2 5.1 3.3 2.2 5.2 1.3 2.1 3.3 4.1 5.3 5.2 4.1"),
    2023: dict(P="2.1 3.1 3.1 3.2 4.1 3.2 3.2 5.2 3.1 4.1 4.1 3.1 4.1 5.1 3.3 3.1 1.1 3.3 5.1 5.3 1.2 3.1 5.3 4.1 1.3 5.3 1.2 5.3 1.2 1.3",
               S="3.2 1.1 3.1 5.2 1.2 4.1 3.3 5.1 3.1 4.2 2.1 5.1 3.3 1.3 2.1 4.1 1.2 4.1 5.3 2.1"),
    2024: dict(P="2.1 5.1 3.2 1.2 3.3 1.3 3.1 4.1 3.3 3.2 3.1 1.3 4.1 3.3 4.2 1.2 4.1 3.3 1.1 5.2 4.2 2.1 4.2 1.1 3.1 3.1 3.2 4.1 5.2 3.1 1.2 1.2 3.2 2.1 5.2"),
    2025: dict(P="2.1 5.3 3.1 3.3 2.2 3.1 5.3 3.1 4.1 5.2 3.1 3.1 4.1 1.2 3.2 1.2 3.1 4.2 3.3 5.3 1.2 4.2 3.1 3.1 3.1 4.2 1.2 1.2 5.2 5.2 4.2 2.1 5.1 2.1 5.3"),
}


def paper_file(year, paper):
    """The question paper, relative to the repo root and URL-encoded (the file names have spaces)."""
    name = (f"NMOS {year} Special Round.pdf" if paper == "S" else
            f"NMOS {year}.pdf" if year >= 2024 else f"NMOS {year} Preliminary Round.pdf")
    assert (ROOT / NMOS / name).exists(), name
    return quote(f"{NMOS}/{name}")


def answer_file(year, paper):
    """The answer sheet of a paper (final answers only), relative to the repo root and URL-encoded."""
    return paper_file(year, paper).replace(".pdf", quote(" (ANS).pdf"))


def label(year, paper):
    """Paper name for the UI, e.g. 'NMOS 2019 Special Round'."""
    if paper == "S":
        return f"NMOS {year} Special Round"
    return f"NMOS {year}" if year >= 2024 else f"NMOS {year} Preliminary Round"


def load(stage="nmos"):
    """Return (problems in file order, {id: sub-group code}, taxonomy) in the shape of
    categorize.load."""
    probs = []
    for m in HEADER_RE.finditer((DATA / "nmos_problems.txt").read_text(encoding="utf-8")):
        year, paper, n, page = int(m[1]), m[2], int(m[3]), int(m[4])
        name = "Đề chung" if year >= 2024 else dict(KINDS)[paper]
        probs.append(dict(id=f"{year}-{paper}-{n}", year=year, label=f"{paper}-{n}", page=page, kind=paper,
                          text=" ".join(m[5].split()), kind_name=name,
                          file=paper_file(year, paper), file_label=f"Đề {label(year, paper)}",
                          answer=answer_file(year, paper), answer_label=f"Đáp án {year}"))
    assign = {}
    for year, papers in CODES.items():
        for paper, codes in papers.items():
            ids = [p["id"] for p in probs if p["id"].startswith(f"{year}-{paper}-")]
            codes = codes.split()
            if len(codes) != len(ids):
                raise SystemExit(f"nmos {year} {paper}: {len(codes)} codes for {len(ids)} problems")
            for pid, c in zip(ids, codes):
                if c not in TAX["subs"]:
                    raise SystemExit(f"nmos {pid}: unknown sub-group {c}")
                assign[pid] = c
    missing = [p["id"] for p in probs if p["id"] not in assign]
    if missing:
        raise SystemExit(f"nmos: unclassified problems {missing[:10]}")
    return probs, assign, TAX


def write_categories(stage="nmos"):
    probs, assign, tax = load(stage)
    by = {}
    for p in probs:
        by.setdefault(assign[p["id"]], []).append(p)
    years = sorted({p["year"] for p in probs})
    per_kind = ", ".join(f"{sum(p['kind'] == k for p in probs)} {n}" for k, n in KINDS)
    L = ["NATIONAL MATHEMATICAL OLYMPIAD OF SINGAPORE (NMOS) - PROBLEM CATEGORISATION", "=" * 60,
         f"Total problems: {len(probs)} ({per_kind}), {years[0]}-{years[-1]} (no papers for 2020).",
         "P = Preliminary Round (since 2024 the single paper), S = Special Round (2013-2019, 2022, 2023).",
         "IDs: Year-Paper-Problem. The text was typed by hand from the papers.",
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
                L.append(f"  {p['id']:<10} {t}")
    out = DATA / "nmos_categories.txt"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out.name}: {len(probs)} problems")


if __name__ == "__main__":
    write_categories()
