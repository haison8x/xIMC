"""Classify every SASMO (Singapore and Asian Schools Math Olympiad) problem into the groups /
sub-groups below.

Reads   data/sasmo_problems.txt (typed by hand from the papers; there is no extract script)
Writes  data/sasmo_categories.txt

Problem ids:  2019-G3-5 = SASMO 2019 Grade 3, problem 5; 2024-G1-5 = SASMO 2024 Grade 1, problem 5;
              2013-PR-5 = problem 5 of the 2013 "Math Olympiad Challenges" practice set.
The papers are kept as they were copied into papers/sasmo/: the 2013-2020 Grade 3 papers are one
combined book, so every problem links to its page there ("Page" = first page of the problem,
"Ref" = page of its worked solution or answer, 0 when there is none).
The classification is the hand-made table CODES below: one sub-group code per problem, listed per
year and paper in problem order. The taxonomy is kept small on purpose, so that every sub-group
collects at least 14 problems.
"""
import re
from urllib.parse import quote

from paths import DATA, ROOT

SASMO = "papers/sasmo"
BOOK = "SASMO P3 (Grade 3) 2013-2020 Past Papers.pdf"
HEADER_RE = re.compile(r"=== Year (\d+) \| Paper (\w+) \| Problem (\d+) \| Page (\d+) \| Ref (\d+) ===\n"
                       r"(.*?)(?=\n=== Year|\Z)", re.S)

# Papers shown as filter chips in the mind map: (code, name).
KINDS = [("G3", "Grade 3"), ("G2", "Grade 2"), ("G1", "Grade 1"), ("PR", "Luyện tập 2013")]
LOWER_KIND_NAMES = False

TAX = dict(
    groups={
        1: "NUMBERS & DIGITS",
        2: "PATTERNS",
        3: "WORD PROBLEMS",
        4: "GEOMETRY & SPATIAL",
        5: "COUNTING & LOGIC",
    },
    subs={
        "1.1": "Mental calculation, place value & number sentences",
        "1.2": "Divisibility, multiples & factors",
        "1.3": "Digits, mystery numbers & cryptarithms",
        "2.1": "Number sequences & growing patterns",
        "2.2": "Mystery operators, numbers in figures & picture grids",
        "3.1": "Sum-difference, transfers, ages, assumption & picture graphs",
        "3.2": "Time, calendar, measurement & gaps",
        "3.3": "Unknown quantities: pictures for numbers, balances & working backwards",
        "4.1": "Perimeter & area",
        "4.2": "Counting shapes, cubes & objects in a figure",
        "4.3": "Spatial & visual puzzles: mirror, views, nets, folding",
        "5.1": "Counting choices & numbers",
        "5.2": "Logic, number placement, pigeonhole & extremes",
    },
)

CODES = {
    2013: dict(PR="1.1 1.1 1.2 1.2 5.2 5.2 5.1 1.3 3.2 3.2 3.2 3.1 2.1 5.2 2.1 3.2 3.2 5.2 2.1 4.1 4.1 4.1 1.3 4.1 4.1 "
                  "3.1 3.1 4.1 3.1 3.1 3.1 2.1 3.1 3.3 3.1 5.2 1.1 1.1 2.2 3.1 5.2 4.2 2.1 3.1 5.1"),
    2014: dict(G3="3.1 1.2 1.1 1.1 4.1 2.1 3.2 3.1 5.1 2.1 1.2 5.2 3.1 1.2 5.2 1.3 4.2 3.1 1.3 5.2"),
    2015: dict(G3="2.1 1.1 2.2 4.1 1.1 1.1 5.1 4.2 1.2 4.1 5.2 1.2 1.2 3.2 4.1 5.2 1.3 3.1 3.1 4.1"),
    2016: dict(G3="1.1 3.2 3.2 3.2 4.1 3.2 3.1 2.1 4.2 4.3 1.2 1.2 3.2 5.2 4.3 3.2 1.1 5.2 3.1 3.1 5.2 4.1 1.2 1.3 1.3"),
    2017: dict(G3="1.1 1.1 3.2 2.1 5.2 4.3 1.1 3.3 3.3 5.1 4.3 4.1 4.2 1.2 2.2 3.3 4.2 3.1 5.2 3.1 2.2 1.3 3.1 1.3 5.2"),
    2018: dict(G3="4.2 3.2 3.1 5.2 3.2 2.1 5.1 5.1 4.3 4.3 3.2 4.2 4.1 2.2 3.1 1.1 4.2 3.1 1.2 3.3 2.2 5.2 3.3 1.3 5.2"),
    2019: dict(G3="1.1 2.2 5.2 4.3 5.2 5.1 4.3 1.2 3.3 3.2 2.2 4.1 3.2 1.2 3.3 4.2 2.2 3.1 3.1 1.1 1.3 3.1 1.3 2.2 1.3"),
    2020: dict(G3="1.1 1.1 2.2 3.2 1.2 4.2 3.2 2.1 1.2 1.3 5.2 3.1 3.3 3.2 4.3 1.1 4.1 4.2 3.1 3.3 4.1 3.3 5.1 5.2 1.3"),
    2024: dict(G1="1.1 1.1 1.2 1.1 3.2 4.2 4.3 4.2 2.1 4.2 4.3 4.2 5.2 5.2 4.3 2.2 3.1 3.2 3.3 1.3 1.3 2.2 5.1 3.1 5.1",
               G2="3.2 4.2 1.2 4.3 2.1 1.2 4.2 4.3 4.2 5.2 1.1 5.2 3.1 3.2 4.3 3.1 3.3 1.3 1.3 1.3 5.1 3.1 3.1 5.1 1.3",
               G3="1.1 4.2 2.1 4.2 1.2 3.1 3.1 4.1 3.1 5.1 1.2 5.2 2.2 4.3 5.2 1.3 3.3 3.1 4.2 4.1 1.3 5.1 5.1 1.3 2.2"),
}


def paper_file(year, paper):
    """The PDF holding a paper, relative to the repo root and URL-encoded (the file names have
    spaces and brackets)."""
    name = f"SASMO {year} Grade {paper[1]}.pdf" if year == 2024 else BOOK
    assert (ROOT / SASMO / name).exists(), name
    return quote(f"{SASMO}/{name}")


def label(year, paper):
    """Paper name for the UI, e.g. 'Đề SASMO 2019 Grade 3'."""
    if paper == "PR":
        return "Sách luyện tập SASMO 2013"
    return f"Đề SASMO {year} {dict(KINDS)[paper]}"


def load(stage="sasmo"):
    """Return (problems in file order, {id: sub-group code}, taxonomy) in the shape of
    categorize.load."""
    probs = []
    for m in HEADER_RE.finditer((DATA / "sasmo_problems.txt").read_text(encoding="utf-8")):
        year, paper, n, page, ref = int(m[1]), m[2], int(m[3]), int(m[4]), int(m[5])
        pdf = paper_file(year, paper)
        if ref == 0:
            answer, answer_label = "", ""
        else:
            answer = f"{pdf}#page={ref}"
            answer_label = f"{'Đáp án' if year == 2024 else 'Lời giải'}, trang {ref}"
        probs.append(dict(id=f"{year}-{paper}-{n}", year=year, label=f"{paper}-{n}", page=page, kind=paper,
                          text=" ".join(m[6].split()), kind_name=dict(KINDS)[paper],
                          file=pdf, file_label=label(year, paper), answer=answer, answer_label=answer_label))
    assign = {}
    for year, papers in CODES.items():
        for paper, codes in papers.items():
            ids = [p["id"] for p in probs if p["id"].startswith(f"{year}-{paper}-")]
            codes = codes.split()
            if len(codes) != len(ids):
                raise SystemExit(f"sasmo {year} {paper}: {len(codes)} codes for {len(ids)} problems")
            for pid, c in zip(ids, codes):
                if c not in TAX["subs"]:
                    raise SystemExit(f"sasmo {pid}: unknown sub-group {c}")
                assign[pid] = c
    missing = [p["id"] for p in probs if p["id"] not in assign]
    if missing:
        raise SystemExit(f"sasmo: unclassified problems {missing[:10]}")
    return probs, assign, TAX


def write_categories(stage="sasmo"):
    probs, assign, tax = load(stage)
    by = {}
    for p in probs:
        by.setdefault(assign[p["id"]], []).append(p)
    years = sorted({p["year"] for p in probs})
    per_kind = ", ".join(f"{sum(p['kind'] == k for p in probs)} {n}" for k, n in KINDS)
    L = ["SINGAPORE AND ASIAN SCHOOLS MATH OLYMPIAD (SASMO) - PROBLEM CATEGORISATION", "=" * 60,
         f"Total problems: {len(probs)} ({per_kind}), {years[0]}-{years[-1]}.",
         "Grade 3 papers 2014-2020 and 2024; Grade 1 and Grade 2 papers 2024; 2013 is a practice set",
         "(\"Math Olympiad Challenges\", Middle Primary 3 and 4), not a contest paper.",
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
                L.append(f"  {p['id']:<11} {t}")
    out = DATA / "sasmo_categories.txt"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out.name}: {len(probs)} problems")


if __name__ == "__main__":
    write_categories()
