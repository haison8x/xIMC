"""Classify every extracted ICO problem into the combinatorics groups / sub-groups below.

Reads   data/ico_problems.txt (from extract_ico.py)
Writes  data/ico_categories.txt

Problem ids:  2021-R1-5 = ICO 2021, round 1, problem 5; 2021-R2-3 = round 2, problem 3.
              2025-J-5 / 2025-I-5 = round 1 sheet of the Junior / Intermediate level (no answers yet).
The classification is the hand-made table CODES below: one sub-group code per problem, listed per
year and paper in problem order. The taxonomy is kept small on purpose (few problems so far).
"""
import re

from paths import DATA, ROOT

ICO = ROOT / "papers" / "ico"
HEADER_RE = re.compile(r"=== Year (\d+) \| Paper (\w+) \| Problem (\d+) \| Page (\d+) \| Ref (\d+) ===\n"
                       r"(.*?)(?=\n=== Year|\Z)", re.S)

# Rounds shown as filter chips in the mind map: (code, name). Papers J and I are round-1 sheets.
KINDS = [("R1", "Vòng 1"), ("R2", "Vòng 2")]
LOWER_KIND_NAMES = False
KIND_OF = {"R1": "R1", "R2": "R2", "J": "R1", "I": "R1"}
LEVEL = {"J": "Junior", "I": "Intermediate"}

TAX = dict(
    groups={
        1: "COUNTING",
        2: "GRAPHS",
        3: "GAMES & PROCESSES",
        4: "EXTREMAL PRINCIPLES & INVARIANTS",
        5: "TABLES, COLOURINGS & GEOMETRY",
    },
    subs={
        "1.1": "Addition / multiplication rules, cases & probability",
        "1.2": "Bijections, double counting & recursion",
        "2.1": "Friendships, degrees & tournaments",
        "2.2": "Paths, trees & grid graphs",
        "3.1": "Games & winning strategies",
        "3.2": "Repeated operations & algorithms",
        "4.1": "Bound, then build an example",
        "4.2": "Invariants, monovariants & parity",
        "4.3": "Pigeonhole principle",
        "5.1": "Tables & colourings",
        "5.2": "Tilings & dissections",
        "5.3": "Combinatorial geometry",
    },
)

CODES = {
    2020: dict(R1="2.2 1.2 4.2 2.1 1.2 1.1 1.2 5.1 5.2 5.3 4.2 4.1 2.2 1.2 2.2", R2="2.1 1.1 5.3 4.3 4.1 4.2 3.2"),
    2021: dict(R1="5.3 4.1 1.1 5.2 1.1 5.1 4.1 4.1 1.1 5.1 1.1 4.1 4.3 1.2 4.1", R2="1.2 4.1 3.2 4.1 4.3 5.3 3.2"),
    2024: dict(R1="3.1 5.3 1.2 3.1 5.1 1.1 4.2 4.2 3.2 1.1 1.1 4.1 2.2 2.2 2.2", R2="4.1 4.1 1.2 2.1 4.1 4.1 5.3"),
    2025: dict(J="1.2 1.2 2.1 4.1 1.1 1.1 4.1 4.2 5.2 1.1 3.1 1.1 4.1 2.2 4.2", I="1.2 4.1 4.2 2.2 1.1 3.1 2.1 4.1 1.2 4.2 1.2 1.2 1.1 5.2 5.2", R2="4.1 5.2 4.1 4.1 5.3 3.1 1.1"),
}


def paper_file(year, paper):
    """The PDF of a paper, relative to the repo root."""
    level = {"J": "_junior", "I": "_intermediate"}.get(paper, "")
    if year == 2025 and paper == "R2":
        level = "_advanced"
    return f"papers/ico/ICO{year}{level}.pdf"


def load(stage="ico"):
    """Return (problems in file order, {id: sub-group code}, taxonomy) in the shape of
    categorize.load."""
    probs = []
    for m in HEADER_RE.finditer((DATA / "ico_problems.txt").read_text(encoding="utf-8")):
        year, paper, n, page, ref = int(m[1]), m[2], int(m[3]), int(m[4]), int(m[5])
        pdf = paper_file(year, paper)
        if ref == 0:
            answer, answer_label = "", ""
        elif paper == "R2":
            answer, answer_label = f"{pdf}#page={ref}", f"Lời giải, trang {ref}"
        else:
            answer, answer_label = f"{pdf}#page={ref}", f"Đáp số, trang {ref}"
        level = LEVEL.get(paper) or ("Advanced" if year == 2025 else "")
        kind = KIND_OF[paper]
        probs.append(dict(id=f"{year}-{paper}-{n}", year=year, label=f"{paper}-{n}", page=page, kind=kind,
                          text=" ".join(m[6].split()), kind_name=dict(KINDS)[kind] + (f" · {level}" if level else ""),
                          file=pdf, file_label=f"Đề ICO {year} {level}" if level else f"Sách ICO {year}",
                          answer=answer, answer_label=answer_label))
    assign = {}
    for year, papers in CODES.items():
        for paper, codes in papers.items():
            ids = [p["id"] for p in probs if p["id"].startswith(f"{year}-{paper}-")]
            codes = codes.split()
            if len(codes) != len(ids):
                raise SystemExit(f"ico {year} {paper}: {len(codes)} codes for {len(ids)} problems")
            for pid, c in zip(ids, codes):
                if c not in TAX["subs"]:
                    raise SystemExit(f"ico {pid}: unknown sub-group {c}")
                assign[pid] = c
    missing = [p["id"] for p in probs if p["id"] not in assign]
    if missing:
        raise SystemExit(f"ico: unclassified problems {missing[:10]}")
    return probs, assign, TAX


def write_categories(stage="ico"):
    probs, assign, tax = load(stage)
    by = {}
    for p in probs:
        by.setdefault(assign[p["id"]], []).append(p)
    years = sorted({p["year"] for p in probs})
    per_kind = ", ".join(f"{sum(p['kind'] == k for p in probs)} {n}" for k, n in KINDS)
    L = ["IRANIAN COMBINATORICS OLYMPIAD - PROBLEM CATEGORISATION", "=" * 60,
         f"Total problems: {len(probs)} ({per_kind}), {', '.join(map(str, years))}.",
         "IDs: Year-Paper-Problem. R1 / R2 = round 1 / round 2; J / I = round-1 sheet of the Junior /",
         "Intermediate level (2025, no answers yet). 2025 R2 is the Advanced & Free level sheet.",
         "", "SUMMARY", "-" * 60]
    count = lambda prefix: sum(len(v) for k, v in by.items() if k.startswith(prefix))
    for g, name in tax["groups"].items():
        L.append(f"{g}. {name}  [{count(f'{g}.')} problems]")
        for k, sub in tax["subs"].items():
            if k.startswith(f"{g}."):
                L.append(f"     {k}  {sub}  ({count(k)})")
    L += ["", "NOTE: Each problem is placed in ONE best-fit sub-group (main idea of the official solution,",
          "or of the statement when there is no solution yet). Figures were lost in PDF text extraction;",
          "check the PDF when the text is unclear.", "", "DETAILS", "=" * 60]
    for g, name in tax["groups"].items():
        L.append(f"\n##### {g}. {name}  [{count(f'{g}.')}] #####")
        for k, sub in tax["subs"].items():
            if not k.startswith(f"{g}."):
                continue
            L.append(f"\n--- {k} {sub} ({len(by.get(k, []))}) ---")
            for p in by.get(k, []):
                t = p["text"][:110] + ("..." if len(p["text"]) > 110 else "")
                L.append(f"  {p['id']:<11} {t}")
    out = DATA / "ico_categories.txt"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out.name}: {len(probs)} problems")


if __name__ == "__main__":
    write_categories()
