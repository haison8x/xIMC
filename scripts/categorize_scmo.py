"""Classify every SCMO (Spring Cup Mathematical Olympiad) problem into the groups / sub-groups below.
There are two mind maps with their own taxonomy: primary (P1-P6 and the 2023 Round 2 finals) and
secondary (S1, Secondary Junior, Secondary Advanced).

Reads   data/scmo_{primary,secondary}_problems.txt (typed by hand from the papers; there is no extract script)
Writes  data/scmo_{primary,secondary}_categories.txt

Problem ids:  2023-P4-5 = SCMO 2023 Primary 4, problem 5; 2023-UP-3 = 2023 Round 2 Upper Primary, problem 3;
              2026-SJ-1 = 2026 Secondary Junior, problem 1 (SA = Secondary Advanced).
Papers live in papers/scmo/SCMO-{year}-{Level}-Rd-{round}-{Paper|Answers}.pdf; "Page" in the problems file is
the page of the problem in the Paper file, "Ref" the page of its answer in the Answers file (0 = no Answers file).
The classification is the hand-made table CODES below: one sub-group code per problem, listed per
year and paper in problem order. The taxonomies are kept small on purpose, so that every sub-group
collects enough problems.
"""
import re
from urllib.parse import quote

from paths import DATA, ROOT

SCMO = "papers/scmo"
HEADER_RE = re.compile(r"=== Year (\d+) \| Paper (\w+) \| Round (\d) \| Problem (\d+) \| Page (\d+) \| Ref (\d+) ===\n"
                       r"(.*?)(?=\n=== Year|\Z)", re.S)

# Paper code in the problems file -> level in the PDF file name.
LEVEL = dict(LP="LowerPrimary", MP="MiddlePrimary", UP="UpperPrimary", SJ="SecJunior", SA="SecAdvanced")

# Papers shown as filter chips in each mind map: (code, name).
KINDS = {
    "primary": [("P1", "P1"), ("P1P2", "P1 & P2"), ("P2", "P2"), ("P2P3", "P2 & P3"), ("P3", "P3"), ("P4", "P4"),
                ("P4P5", "P4 & P5"), ("P5", "P5"), ("P6", "P6"), ("LP", "Vòng 2 Lower"), ("MP", "Vòng 2 Middle"),
                ("UP", "Vòng 2 Upper")],
    "secondary": [("S1", "Secondary 1"), ("SJ", "Secondary Junior"), ("SA", "Secondary Advanced")],
}
LOWER_KIND_NAMES = False

# Answers files that are only a list of final answers (all others have worked solutions).
ANSWER_LISTS = {(2016, "P3"), (2019, "P3"), (2020, "P3"), (2021, "P3"), (2023, "LP"), (2023, "MP"), (2023, "UP"),
                (2025, "P2P3")}
ANSWER_NOTE = {(2025, "P2P3"): " (viết tay trên đề)", (2025, "P4P5"): " (tiếng Trung)"}

TAX = {
    "primary": dict(
        groups={
            1: "CALCULATION & NUMBERS",
            2: "PATTERNS & UNKNOWNS",
            3: "WORD PROBLEMS",
            4: "GEOMETRY & SPATIAL",
            5: "COUNTING & LOGIC",
        },
        subs={
            "1.1": "Clever calculation, order of operations, signs & brackets, fraction sums",
            "1.2": "Divisibility, primes, factors & remainders",
            "1.3": "Digits, cryptarithms & palindromes",
            "2.1": "Sequences, figure patterns & periodicity",
            "2.2": "Shape equations, defined operations & working backwards",
            "3.1": "Sum-difference, transfers, ages, assumption, surplus-shortage",
            "3.2": "Ratio, fractions, percentages, averages, work & mixtures",
            "3.3": "Speed: meeting, chasing, trains & boats",
            "3.4": "Time, calendar, intervals, positions & measurement",
            "4.1": "Perimeter",
            "4.2": "Area",
            "4.3": "Counting figures & angles",
            "4.4": "Cubes, nets, folding, tiling & matchsticks",
            "5.1": "Counting methods & pigeonhole",
            "5.2": "Logical reasoning: truth-tellers, rankings, balances",
            "5.3": "Grid puzzles, number placement, games & optimisation",
        },
    ),
    "secondary": dict(
        groups={
            1: "ALGEBRA",
            2: "NUMBER THEORY",
            3: "GEOMETRY",
            4: "COMBINATORICS",
        },
        subs={
            "1.1": "Powers, surds, fractions & absolute values",
            "1.2": "Equations, systems, Vieta & functions",
            "1.3": "Extremes & inequalities: squares, absolute values, AM-GM",
            "2.1": "Primes, factorisation & integer equations",
            "2.2": "Divisibility, remainders, digits & integer parts",
            "3.1": "Angles",
            "3.2": "Lengths, areas & similar triangles",
            "4.1": "Counting, logic & extremal problems",
        },
    ),
}

CODES = {
    "primary": {
        2016: dict(P3="1.1 3.2 3.1 4.3 3.1 1.3 3.4 4.4 1.1 5.3 3.1"),
        2019: dict(P3="3.4 4.3 1.2 1.3 3.3 4.1 2.2 5.3 5.2 5.3 5.3"),
        2020: dict(P3="1.1 4.3 1.3 5.3 4.2 2.2 1.3 3.1 5.1 5.2 5.3",
                   P4="1.1 5.1 4.3 2.1 3.1 4.1 1.3 4.2 5.3 5.3 4.4"),
        2021: dict(P3="1.1 5.1 4.3 2.2 2.1 5.3 4.4 1.3 4.4 5.3 5.2"),
        2023: dict(P1P2="2.2 4.3 2.1 2.1 1.3 5.2 1.1 2.1 3.4 4.4 3.4 4.4 2.1 5.2 3.1 3.1 5.3 4.4 5.3",
                   P3="3.1 3.4 3.4 3.4 3.4 3.1 5.3 4.3 5.1 3.1 4.1 1.3 5.3 5.3 5.3 4.1 2.2 5.2 5.3",
                   P4="1.1 3.1 3.2 3.2 4.2 5.2 4.2 2.2 2.1 4.1 1.2 4.2 5.1 3.3 1.3 4.1 5.1 3.1 5.2",
                   P5="1.1 2.1 1.3 4.4 4.2 3.2 4.3 4.3 3.2 3.2 3.3 1.2 1.3 1.2 5.1 4.2 3.3 1.3 1.2",
                   P6="2.2 1.2 3.2 4.2 5.1 3.2 4.2 2.1 1.2 1.1 1.2 5.1 5.3 5.1 3.3 4.2 3.3 1.3 4.4",
                   LP="2.2 5.3 1.1 5.3 5.2 1.3 5.2 5.3 4.4 4.4 3.4 5.3",
                   MP="1.1 4.3 3.4 4.1 3.1 1.3 5.2 5.3 5.1 3.1 5.3",
                   UP="1.1 4.2 3.2 4.4 1.3 3.2 1.2 5.2 5.3 3.3 5.1 4.2 2.1"),
        2024: dict(P2P3="1.1 2.2 4.3 3.1 2.1 4.1 4.4 1.1 3.1 1.3 5.1 1.3 3.1 3.4 5.2 4.2 1.3 2.2 5.3",
                   P4P5="1.1 3.2 1.2 4.2 3.1 3.2 3.3 3.3 3.1 4.3 2.1 5.1 3.2 4.2 1.3 4.2 5.1 3.2 4.2",
                   P6="4.4 3.3 3.2 4.2 1.2 3.2 4.2 1.1 1.3 4.2 3.3 1.2 1.1 5.1 1.2 5.1 1.3 1.2 2.1"),
        2025: dict(P2P3="1.1 2.2 4.3 3.1 5.2 3.2 4.1 1.3 2.1 3.1 3.4 1.3 4.1 3.1 2.1 3.1 5.3 5.2 1.3",
                   P4P5="1.1 3.4 4.1 4.3 2.1 1.3 4.2 5.2 3.1 5.3 5.1"),
        2026: dict(P1="2.2 2.1 1.3 4.4 5.1 4.3 3.4 5.3 3.1 2.1 5.2",
                   P2="2.2 1.2 5.1 2.1 4.3 3.1 1.1 2.1 2.1 3.1 4.1 5.3 5.1",
                   P3="1.1 1.1 3.1 5.1 3.4 3.1 4.3 4.1 1.3 3.2 5.2 4.1 5.1 4.4 3.1 5.3 5.2 1.3 2.1",
                   P4="1.1 3.1 3.1 3.3 4.1 4.3 3.2 3.1 5.1 4.2 3.4 3.2 1.2 4.2 5.1 1.3 2.1 5.2 5.3",
                   P5="1.1 4.3 5.2 4.3 3.2 3.3 1.2 4.2 4.2 5.3 3.3 2.1 1.2 1.3 1.2 3.2 5.2 5.1 4.2",
                   P6="1.1 4.3 3.4 1.3 3.3 4.3 1.3 4.2 1.1 5.3 3.2 4.2 3.3 1.2 4.4 1.2 5.1 4.2 5.1"),
    },
    "secondary": {
        2022: dict(SJ="1.1 1.2 3.1 1.2 3.1 1.2 1.3 2.1 4.1 2.1 4.1 1.3 4.1",
                   SA="1.1 1.3 1.2 1.1 2.1 3.2 1.2 1.2 3.1 1.3 4.1 3.2 3.2"),
        2023: dict(S1="1.1 2.2 3.1 2.2 1.1 1.2 3.2 1.1 1.3 1.2 4.1 1.1 1.2 1.2 2.1 3.2 2.1"),
        2025: dict(SJ="1.1 1.2 1.3 3.1 2.2 1.3 1.3 3.2 3.1 2.2 4.1 2.2 4.1"),
        2026: dict(SJ="1.1 3.1 1.1 3.2 1.1 2.2 2.1 3.2 1.3 3.2 2.1 1.2 4.1 1.3 4.1",
                   SA="1.2 1.3 1.1 3.2 2.2 1.2 1.1 3.2 4.1 3.2 4.1 2.1 2.1"),
    },
}


def paper_file(year, paper, rnd, answers=False):
    """The PDF of a paper (or of its answers), relative to the repo root and URL-encoded."""
    name = f"SCMO-{year}-{LEVEL.get(paper, paper)}-Rd-{rnd}-{'Answers' if answers else 'Paper'}.pdf"
    assert (ROOT / SCMO / name).exists(), name
    return quote(f"{SCMO}/{name}")


def label(year, paper, rnd, kinds):
    """Paper name for the UI, e.g. 'Đề SCMO 2023 P4' or 'Đề SCMO 2023 vòng 2 Upper Primary'."""
    if rnd == 2:
        return f"Đề SCMO {year} vòng 2 {LEVEL[paper].replace('Primary', ' Primary')}"
    return f"Đề SCMO {year} {kinds[paper]}"


def load(stage):
    """Return (problems in file order, {id: sub-group code}, taxonomy) in the shape of
    categorize.load."""
    kinds = dict(KINDS[stage])
    probs = []
    for m in HEADER_RE.finditer((DATA / f"scmo_{stage}_problems.txt").read_text(encoding="utf-8")):
        year, paper, rnd, n, page, ref = int(m[1]), m[2], int(m[3]), int(m[4]), int(m[5]), int(m[6])
        if paper not in kinds:
            raise SystemExit(f"scmo {stage}: paper {paper} does not belong here")
        if ref == 0:
            answer, answer_label = "", ""
        else:
            answer = f"{paper_file(year, paper, rnd, answers=True)}#page={ref}"
            kind = "Đáp án" if (year, paper) in ANSWER_LISTS else "Lời giải"
            answer_label = f"{kind}{ANSWER_NOTE.get((year, paper), '')}, trang {ref}"
        probs.append(dict(id=f"{year}-{paper}-{n}", year=year, label=f"{paper}-{n}", page=page, kind=paper,
                          text=" ".join(m[7].split()), kind_name=kinds[paper],
                          file=paper_file(year, paper, rnd), file_label=label(year, paper, rnd, kinds),
                          answer=answer, answer_label=answer_label))
    tax = TAX[stage]
    assign = {}
    for year, papers in CODES[stage].items():
        for paper, codes in papers.items():
            ids = [p["id"] for p in probs if p["id"].startswith(f"{year}-{paper}-")]
            codes = codes.split()
            if len(codes) != len(ids):
                raise SystemExit(f"scmo {year} {paper}: {len(codes)} codes for {len(ids)} problems")
            for pid, c in zip(ids, codes):
                if c not in tax["subs"]:
                    raise SystemExit(f"scmo {pid}: unknown sub-group {c}")
                assign[pid] = c
    missing = [p["id"] for p in probs if p["id"] not in assign]
    if missing:
        raise SystemExit(f"scmo {stage}: unclassified problems {missing[:10]}")
    return probs, assign, tax


def write_categories(stage):
    probs, assign, tax = load(stage)
    by = {}
    for p in probs:
        by.setdefault(assign[p["id"]], []).append(p)
    years = sorted({p["year"] for p in probs})
    per_kind = ", ".join(f"{sum(p['kind'] == k for p in probs)} {n}" for k, n in KINDS[stage]
                         if any(p["kind"] == k for p in probs))
    L = [f"SPRING CUP MATHEMATICAL OLYMPIAD (SCMO) {stage.upper()} - PROBLEM CATEGORISATION", "=" * 60,
         f"Total problems: {len(probs)} ({per_kind}), {years[0]}-{years[-1]}.",
         "IDs: Year-Paper-Problem. The text was typed by hand from the papers."]
    if stage == "primary":
        L += ["2016-2021 are English translations of Round 1 papers; LP, MP, UP are the 2023 Round 2 (final)",
              "papers for Lower, Middle and Upper Primary."]
    else:
        L += ["SJ = Secondary Junior, SA = Secondary Advanced. The 2022 papers were sat on 28 January 2023."]
    L += ["", "SUMMARY", "-" * 60]
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
    out = DATA / f"scmo_{stage}_categories.txt"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out.name}: {len(probs)} problems")


if __name__ == "__main__":
    write_categories("primary")
    write_categories("secondary")
