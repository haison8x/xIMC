"""Classify every APMOPS (SMOPS) problem into the IMC Key Stage 2 groups and sub-groups (see
categorize.py), with the thin sub-groups merged into a neighbour (MERGE).

Reads   data/apmops_problems.txt
Writes  data/apmops_categories.txt

data/apmops_problems.txt has no extractor: the Round 1 papers of 2001-2025 are scans without a
text layer, so every paper was transcribed by hand from the page images (figures are described in
[brackets]). 2011 problem 1 was voided on the paper and is left out.

Problem ids:  2010-R1-5 = 2010, round 1, problem 5. Round 2 exists for 2012, 2014, 2015 and 2018.
The classification is the hand-made table CODES below: one KS2 sub-group code per problem,
listed per year and round in problem order.
"""
import copy
import re

import categorize
from paths import DATA, ROOT

APMOPS = ROOT / "papers" / "apmops"  # MTC-{year}-{SMOPS|APMOPS}-Rd-{1,2}-{Paper,Answers}.pdf
HEADER_RE = re.compile(r"=== Year (\d+) \| Paper R(\d) \| Problem (\d+) \| Page (\d+) ===\n(.*?)(?=\n=== Year|\Z)", re.S)

# Paper types shown as filter chips in the mind map: (code, name), the first is the default.
KINDS = [("R1", "Vòng 1"), ("R2", "Vòng 2")]

# KS2 sub-groups with fewer than 10 APMOPS problems -> the sub-group they are merged into,
# and the new English names of the sub-groups that absorb them.
MERGE = {"2.3": "2.1", "2.4": "2.1", "3.4": "3.5", "6.5": "6.1", "7.2": "7.1"}
MERGED_NAMES = {
    "2.1": "Digit relations, digit sums over a range & largest/smallest numbers",
    "3.5": "Equations, averages, money, age & quantity word problems",
    "6.1": "Arrangements, selections, tournaments & handshakes",
    "7.1": "Logic deduction, truth-tellers/liars & games",
}

CODES = {
    2001: dict(R1="3.1 3.1 8.1 8.1 1.3 5.2 5.1 6.3 4.2 5.4 1.1 3.5 3.3 4.3 8.3 5.5 6.4 5.4 5.3 5.1 5.4 8.1 7.4 3.5 7.1 3.2 4.3 3.2 2.1 6.4"),
    2002: dict(R1="8.1 8.1 8.1 3.1 3.4 5.1 5.1 5.1 5.3 5.2 2.2 3.4 3.3 3.2 4.1 8.3 5.1 5.4 5.4 8.3 1.1 2.3 8.2 3.2 3.5 3.5 6.4 6.1 3.5 6.5"),
    2003: dict(R1="7.4 8.1 5.4 7.4 3.1 8.1 5.1 7.1 1.1 1.1 8.2 6.1 7.4 5.2 5.1 3.5 5.1 1.1 3.5 5.5 4.3 3.1 3.2 3.3 5.3 6.4 3.1 8.3 7.1 7.3"),
    2004: dict(R1="3.5 1.3 5.1 3.3 1.2 7.4 3.1 3.3 7.1 8.1 8.1 8.1 1.1 8.3 6.3 2.2 3.1 5.1 4.2 5.1 8.1 5.4 7.1 4.3 4.3 4.3 3.4 5.3 2.2 3.5"),
    2005: dict(R1="8.3 5.1 3.2 5.4 7.4 3.1 3.2 3.5 6.1 4.2 5.4 7.1 5.3 3.1 3.2 1.1 6.2 1.2 3.1 4.1 3.5 7.4 4.1 5.1 4.1 5.1 7.4 3.2 1.3 8.3"),
    2006: dict(R1="5.3 5.4 5.3 3.5 6.5 8.1 7.1 4.3 5.4 7.4 5.2 5.3 4.3 5.2 1.4 6.3 3.1 5.1 7.1 5.4 3.1 5.3 4.3 7.4 5.1 3.1 1.1 6.4 4.1 2.1"),
    2007: dict(R1="3.1 5.3 5.1 5.5 8.1 5.1 8.2 7.4 5.3 3.3 1.1 5.5 5.3 4.3 3.1 4.2 4.2 5.1 7.1 5.4 6.1 4.3 7.1 7.4 5.3 7.1 3.1 5.3 7.4 8.2"),
    2008: dict(R1="3.1 5.2 3.1 5.4 7.3 3.1 5.3 7.3 5.2 2.3 5.3 5.3 5.1 7.4 1.1 4.3 5.5 5.1 5.1 7.4 7.1 1.1 5.2 7.2 7.1 1.1 3.2 6.1 4.3 5.2"),
    2009: dict(R1="1.2 3.1 8.1 7.4 5.1 3.3 8.3 3.1 5.1 7.1 5.3 4.1 1.4 5.5 1.4 5.3 5.2 3.2 6.1 7.4 7.4 4.3 8.3 1.4 3.5 6.3 5.1 3.1 3.5 4.1"),
    2010: dict(R1="3.1 3.1 1.1 6.1 7.1 7.4 3.1 5.3 1.3 5.1 3.3 5.2 5.1 8.1 4.3 1.3 6.1 5.2 5.1 8.2 5.3 8.1 3.1 1.2 5.3 1.2 5.2 1.4 6.3 7.4"),
    # problem 1 was voided: the codes start at problem 2
    2011: dict(R1="3.1 7.4 5.2 1.2 5.2 3.2 5.3 4.1 8.1 5.3 3.4 7.4 2.3 5.1 6.1 3.5 5.2 5.1 5.1 5.3 1.3 2.1 5.1 1.2 5.3 6.2 2.3 7.1 5.2"),
    2012: dict(R1="3.1 5.1 1.1 5.3 1.2 5.3 1.1 7.1 3.4 5.1 5.3 8.3 3.1 4.1 3.1 1.4 3.2 3.5 6.4 5.2 5.1 4.3 6.1 4.2 8.1 3.1 5.4 4.3 5.2 2.1",
               R2="7.4 4.3 5.1 1.1 1.2 5.2"),
    2013: dict(R1="3.1 2.3 5.3 7.4 3.1 5.5 3.4 5.5 1.2 5.4 1.1 6.4 5.1 3.1 5.2 6.1 7.3 3.5 5.3 6.5 5.1 7.4 4.3 6.3 4.1 1.2 7.4 5.2 1.3 6.1"),
    2014: dict(R1="5.2 3.2 2.4 4.2 1.4 5.3 6.1 1.1 4.3 5.4 3.1 7.1 6.1 1.1 3.1 5.4 7.4 2.2 5.3 8.3 6.1 8.1 3.3 1.1 6.2 5.2 1.1 5.1 6.2 4.1",
               R2="3.5 6.3 5.1 6.4 1.1 4.2"),
    2015: dict(R1="4.2 5.5 3.1 3.5 3.2 8.1 2.2 5.5 5.1 3.5 5.5 1.1 7.4 7.4 5.2 5.3 6.3 3.5 5.2 5.1 6.5 4.3 1.1 7.4 7.4 4.1 3.2 6.1 6.2 5.2",
               R2="1.1 7.3 4.1 5.1 5.3 6.4"),
    2016: dict(R1="3.1 5.1 1.3 3.1 5.1 5.2 8.3 5.5 5.1 4.1 5.5 1.3 6.3 3.1 1.2 1.1 5.1 3.2 6.2 5.2 7.1 1.2 7.4 2.4 5.3 6.1 7.3 3.5 1.1 6.3"),
    2017: dict(R1="3.1 3.1 3.3 1.2 8.2 3.4 1.1 2.1 1.2 8.2 1.1 8.1 7.4 5.3 6.1 5.5 6.1 7.4 5.1 7.4 2.2 4.2 3.2 4.1 3.2 5.1 7.3 5.2 7.4 8.1"),
    2018: dict(R1="3.1 4.2 1.4 5.3 2.1 2.4 8.1 3.5 5.2 5.5 5.1 8.1 1.3 2.1 1.3 3.1 5.1 7.4 6.3 5.2 6.2 6.4 6.2 1.1 3.1 1.2 4.1 5.1 3.1 6.1",
               R2="4.2 5.5 5.3 2.1 6.4 5.5 1.3 5.1 6.4 2.2 1.3 1.1 8.2 2.2"),
    2019: dict(R1="2.1 6.1 5.5 5.3 6.5 3.1 7.3 7.4 6.1 8.1 1.3 4.2 2.3 3.5 3.2 2.3 6.1 5.1 5.2 7.4 3.1 6.3 5.1 3.1 5.5 3.2 6.1 1.1 5.1 2.1 5.2"),
    2020: dict(R1="7.1 3.2 1.2 4.2 5.1 8.3 1.2 5.2 7.3 1.1 3.5 5.2 1.1 7.3 3.3 1.2 5.3 1.1 8.1 6.3 6.2 3.1 3.1 3.5 1.4 6.2 6.1 6.4 6.1 8.1"),
    2021: dict(R1="3.1 3.4 3.1 3.1 1.1 6.1 1.3 2.3 6.4 5.3 1.3 6.4 1.2 5.4 6.2 6.5 1.2 5.2 6.1 1.1 3.3 4.2 6.2 5.3 2.2 6.2 7.4 5.2 6.5 5.5"),
    2022: dict(R1="3.3 3.5 8.2 5.5 6.1 7.4 4.1 5.1 7.4 5.3 1.2 7.4 6.1 2.4 8.1"),
    2023: dict(R1="1.1 2.1 1.2 3.2 8.1 3.2 6.2 4.3 5.2 5.5 8.1 6.1 3.5 1.2 2.3 3.5 5.1 1.3 3.5 8.1 1.1 5.3 6.4 6.4 6.2 5.1 7.4 6.2 6.3 6.3"),
    2024: dict(R1="1.2 3.3 3.3 8.2 6.1 1.1 1.2 5.3 6.2 3.4 5.2 2.2 5.2 3.5 6.3 8.3 5.4 5.2 1.4 8.3 1.2 1.3 1.2 3.5 6.1 1.2 8.1 1.1 1.2 6.2"),
    2025: dict(R1="8.1 6.1 2.2 8.1 3.5 3.3 5.2 1.1 3.3 8.1 8.2 1.2 3.2 1.4 4.1 6.1 5.5 6.2 5.1 5.4 2.2 3.5 1.3 6.3 5.1 5.3 6.4 3.5 6.1 6.4"),
    2026: dict(R1="3.2 3.3 5.3 2.1 3.2 3.2 6.1 3.5 8.2 1.4 3.1 4.3 4.3 1.2 6.2 3.1 5.1 7.1 6.1 5.1 6.2 1.2 6.4 6.1 1.3 6.3 6.2 6.1 1.1 8.1"),
}


def taxonomy():
    """The KS2 groups and sub-groups without the merged sub-groups."""
    tax = copy.deepcopy(categorize.STAGES["ks2"])
    for k in MERGE:
        del tax["subs"][k]
    tax["subs"].update(MERGED_NAMES)
    return tax


def pdf(year, rnd, part):
    """papers/apmops/... path of a question paper (part='Paper') or answer key (part='Answers')."""
    name = "APMOPS" if year == 2025 else "SMOPS"
    return (APMOPS / f"MTC-{year}-{name}-Rd-{rnd}-{part}.pdf").relative_to(ROOT).as_posix()


def load(stage="apmops"):
    """Return (problems in file order, {id: sub-group code}, taxonomy) in the shape of
    categorize.load."""
    tax = taxonomy()
    probs = []
    for m in HEADER_RE.finditer((DATA / "apmops_problems.txt").read_text(encoding="utf-8")):
        year, rnd, n, page = int(m[1]), int(m[2]), int(m[3]), int(m[4])
        probs.append(dict(id=f"{year}-R{rnd}-{n}", year=year, label=f"R{rnd}-{n}", page=page, kind=f"R{rnd}",
                          text=" ".join(m[5].split()), kind_name=f"Vòng {rnd}",
                          file=pdf(year, rnd, "Paper"), file_label=f"Đề vòng {rnd} {year}",
                          answer=pdf(year, rnd, "Answers"), answer_label=f"Đáp số vòng {rnd} {year}"))
    assign = {}
    for year, rounds in CODES.items():
        for kind, codes in rounds.items():
            ids = [p["id"] for p in probs if p["year"] == year and p["kind"] == kind]
            codes = codes.split()
            if len(codes) != len(ids):
                raise SystemExit(f"apmops {year} {kind}: {len(codes)} codes for {len(ids)} problems")
            for pid, c in zip(ids, codes):
                c = MERGE.get(c, c)
                if c not in tax["subs"]:
                    raise SystemExit(f"apmops {pid}: unknown sub-group {c}")
                assign[pid] = c
    missing = [p["id"] for p in probs if p["id"] not in assign]
    if missing:
        raise SystemExit(f"apmops: unclassified problems {missing[:10]}")
    return probs, assign, tax


def write_categories(stage="apmops"):
    probs, assign, tax = load(stage)
    by = {}
    for p in probs:
        by.setdefault(assign[p["id"]], []).append(p)
    years = sorted({p["year"] for p in probs})
    per_kind = ", ".join(f"{sum(p['kind'] == k for p in probs)} {n}" for k, n in KINDS)
    merged = ", ".join(f"{a} -> {b}" for a, b in MERGE.items())
    L = ["APMOPS / SMOPS - PROBLEM CATEGORISATION", "=" * 60,
         f"Total problems: {len(probs)} ({per_kind}), {years[0]}-{years[-1]}.",
         f"Groups and sub-groups are those of IMC Key Stage 2, with thin sub-groups merged ({merged}).",
         "IDs: Year-Round-Problem (2010-R1-5 = 2010, round 1, problem 5). Round 2: 2012, 2014, 2015, 2018.",
         "", "SUMMARY", "-" * 60]
    count = lambda prefix: sum(len(v) for k, v in by.items() if k.startswith(prefix))
    for g, gname in tax["groups"].items():
        L.append(f"{g}. {gname}  [{count(f'{g}.')} problems]")
        for k, sub in tax["subs"].items():
            if k.startswith(f"{g}."):
                L.append(f"     {k}  {sub}  ({count(k)})")
    L += ["", "NOTE: Each problem is placed in ONE best-fit sub-group (primary technique). The papers were",
          "transcribed from scans and figures are described in [brackets]; check the original PDF for figures.", "",
          "DETAILS", "=" * 60]
    for g, gname in tax["groups"].items():
        L.append(f"\n##### {g}. {gname}  [{count(f'{g}.')}] #####")
        for k, sub in tax["subs"].items():
            if not k.startswith(f"{g}."):
                continue
            L.append(f"\n--- {k} {sub} ({len(by.get(k, []))}) ---")
            for p in by.get(k, []):
                t = p["text"][:110] + ("..." if len(p["text"]) > 110 else "")
                L.append(f"  {p['id']:<11} {t}")
    out = DATA / "apmops_categories.txt"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out.name}: {len(probs)} problems")


if __name__ == "__main__":
    write_categories()
