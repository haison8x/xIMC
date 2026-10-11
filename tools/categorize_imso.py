"""Classify every extracted IMSO mathematics problem into the 8 groups / 33 sub-groups used
for IMC Key Stage 2 (see categorize.py).

Reads   imso_problems.txt (from extract-imso-problems.py)
Writes  imso_categories.txt

Problem ids:  2013-S5 (Short Answer), 2013-E5 (Essay), 2013-X5 (Exploration),
              2008-Q5 (Short Answer, Taiwan first round; 2005/2008/2009 are Taiwan papers)
The classification is the hand-made table CODES below: one sub-group code per problem,
listed per year and paper in problem order.
"""
import re
from pathlib import Path

import categorize

ROOT = categorize.ROOT
IMSO = ROOT / "IMSO"
HEADER_RE = re.compile(r"=== Year (\d+) \| Paper (\w) \| Problem (\d+) \| Page (\d+) ===\n(.*?)(?=\n=== Year|\Z)", re.S)

# Paper types shown as filter chips in the mind map: (code, name), the first is the default.
KINDS = [("S", "Short Answer"), ("E", "Essay"), ("X", "Exploration"), ("Q", "Taiwan vòng 1")]
LOWER_KIND_NAMES = False
PAPER = {"S": "ShortAnswer", "Q": "ShortAnswer", "E": "Essay", "X": "Exploration"}
TAIWAN_YEARS = {2005, 2008, 2009}

CODES = {
    2005: dict(
        S="3.2 7.4 1.3 5.5 5.1 1.1 6.3 2.1 3.2 8.1 1.4 3.4 5.3 3.3 5.2 5.2 2.3 5.1 5.5 7.3",
        E="6.3 3.5 6.2 6.1 1.1 6.2 6.5 7.2 5.3 5.1",
        X="8.3 6.1 7.3 8.2 7.4"),
    2006: dict(
        S="1.3 3.5 8.1 5.1 8.1 6.1 6.2 4.2 3.4 8.3 6.3 5.5 5.4 6.4 5.2 7.3 5.5 7.4 2.2 1.1 5.5 5.3 2.2 6.1 2.2",
        E="2.1 3.3 5.4 3.2 3.2 4.1 3.3 5.2 6.1 7.3 4.1 5.1 6.3",
        X="8.3 8.3 8.3 6.3 7.4 6.3"),
    2007: dict(
        S="3.2 3.5 5.3 3.1 2.4 2.4 3.5 5.5 1.2 5.3 8.3 5.3 6.4 7.4 5.2 3.4 3.5 5.2 3.1 6.3 8.1 6.2 2.3 5.1 8.1",
        E="3.5 3.1 5.1 3.2 3.4 5.1 3.5 5.3 3.5 5.2 3.4 5.3 4.2",
        X="8.3 6.4 5.5 6.4 6.4 5.2"),
    2008: dict(
        Q="3.5 5.1 5.3 3.5 3.2 2.2 4.2 4.1 7.1 7.4 1.2 5.3",
        S="5.4 4.3 2.1 4.1 4.1 3.2 1.3 3.5 2.3 3.5 1.1 4.3 6.2 1.1 5.3 5.2 7.4 5.2 5.5 5.1",
        E="1.4 3.2 4.3 5.2 6.5 2.1 6.4 5.1 5.1 5.2",
        X="6.4 6.3 6.1 7.4 8.1"),
    2009: dict(
        Q="1.1 7.4 5.5 3.5 6.1 2.2 4.3 1.4 6.3 5.4 7.1 5.2",
        S="2.2 3.5 3.5 2.1 4.2 4.3 3.5 1.1 2.2 3.5 5.4 8.1 5.5 2.4 5.5 7.3 6.3 4.3 7.4 6.3",
        E="4.2 1.1 5.2 5.4 7.1 7.1 2.1 2.1 5.3 5.3",
        X="7.1 3.3 6.4 7.3 6.3"),
    2010: dict(
        S="5.1 5.1 5.3 1.4 8.3 5.3 6.4 5.5 4.2 5.2 3.4 3.3 3.1 1.1 2.2 7.4 7.3 5.3 2.3 6.2 1.2 5.3 5.5 1.2 1.2",
        E="5.1 1.1 5.1 7.1 5.2 5.1 4.1 5.3 3.2 5.5 3.5 3.5 2.2",
        X="5.5 7.1 5.5 6.4 2.2 7.4"),
    2011: dict(
        S="1.2 3.4 5.3 3.2 1.4 6.3 1.2 3.1 1.1 4.3 5.2 2.1 3.2 3.4 5.4 6.4 5.3 6.1 5.4 5.3 5.5 1.1 6.1 6.1 3.2",
        E="4.2 8.1 7.1 7.4 1.1 1.1 7.4 3.5 4.3 1.1 7.4 5.1 5.3",
        X="7.3 7.3 6.5 6.4 7.4 7.3"),
    2012: dict(
        S="3.3 1.3 3.5 5.2 5.3 6.1 1.1 1.1 6.1 6.1 8.1 2.1 1.2 5.2 5.1 3.4 3.1 6.5 1.1 3.5 5.1 8.3 1.4 5.4 2.1",
        E="3.2 2.1 3.4 8.1 3.5 4.1 7.1 5.2 2.2 5.2 5.1 5.1 7.3",
        X="7.4 1.1 6.3 7.4 2.4 7.3"),
    2013: dict(
        S="5.4 3.1 3.4 6.5 3.1 2.1 5.3 1.1 7.1 5.2 5.1 5.1 4.2 3.3 7.4 7.4 3.2 7.3 5.2 2.1 5.5 5.4 3.5 4.3 7.2",
        E="3.5 5.1 2.2 7.3 5.1 5.2 1.1 1.1 6.2 6.2 7.4 6.5 5.2",
        X="5.5 7.4 7.1 2.2 7.3 7.3"),
    2014: dict(
        S="3.1 3.2 5.1 3.3 3.5 5.4 2.4 6.2 5.1 3.5 2.2 5.2 7.4 3.2 5.1 3.5 1.2 1.1 1.1 7.4 4.3 6.4 2.4 5.2 5.2",
        E="3.2 3.5 5.2 3.5 5.1 1.1 5.1 2.4 5.2 2.1 5.4 6.5 5.4",
        X="7.4 1.4 6.4 1.3 7.3 6.4"),
    2015: dict(
        S="1.4 1.3 3.1 5.2 3.2 6.1 7.3 1.3 6.1 2.3 2.2 7.3 5.5 1.3 4.1 6.2 5.2 5.1 5.1 7.1 5.4 3.4 7.4 3.2 7.4",
        X="7.3 6.4 1.2 6.4 7.3 6.4"),
    2016: dict(
        S="4.3 3.5 5.4 5.5 3.5 3.2 3.2 3.3 4.2 5.1 1.2 7.3 8.1 3.5 5.1 5.2 3.1 5.4 1.2 8.1 4.3 6.3 2.4 5.1 1.1",
        E="7.3 1.2 2.2 5.4 1.1 5.2 1.2 5.2 6.2 6.4 8.3 2.1 6.1",
        X="6.4 2.2 7.4 5.4 7.4 6.4"),
    2017: dict(
        S="1.2 5.3 8.1 3.1 6.2 3.5 2.2 6.3 3.3 2.4 6.1 3.2 5.3 2.1 2.4 4.1 5.1 5.2 1.4 8.2 5.3 7.4 5.3 7.4 6.4",
        E="8.1 2.1 1.1 8.1 5.1 3.3 5.1 2.3 6.4 5.2 5.1 6.3 7.4",
        X="5.5 7.3 7.4 7.4 6.3 7.4"),
    2018: dict(
        S="4.3 5.1 8.2 5.1 2.3 5.4 4.3 7.4 1.1 6.2 5.4 1.1 8.2 1.1 2.2 5.2 7.3 6.3 7.3 7.3 7.3 2.2 1.1 6.4 6.4",
        E="5.1 6.3 1.2 7.3 2.1 5.1 1.2 6.4 2.2 6.4 2.1 6.2 6.4",
        X="2.2 5.5 6.5 7.4 8.2 7.4"),
    2019: dict(
        S="5.4 3.3 7.1 1.3 5.4 5.4 4.1 8.1 2.2 2.2 5.3 6.4 5.1 3.5 6.1 1.1 2.2 7.4 7.4 2.2 5.2 3.4 2.1 7.1 6.2",
        E="5.2 2.1 3.5 5.5 8.3 7.3 1.4 5.1 5.4 2.4 6.5 6.4 7.2",
        X="1.1 6.4 7.4 6.1 6.4 5.5"),
    2020: dict(
        S="2.1 5.2 1.1 7.3 3.2 3.1 7.4 6.3 6.2 1.2 5.4 5.2 5.5 6.1 7.4 1.2 2.3 7.4 5.1 6.1 7.1 7.4 2.1 5.1 5.3",
        E="6.1 7.3 7.1 3.5 4.3 6.3 5.1 6.5 1.2 5.4 6.5 7.4 5.1",
        X="6.4 5.4 7.4 6.5 7.2 1.2"),
    2021: dict(
        S="6.5 5.4 5.5 4.1 4.1 5.1 6.3 1.2 5.1 7.4 5.3 3.5 6.1 5.2 6.4 7.2 3.2 1.1 6.4 6.1 2.1 2.1 5.2 5.3 6.1",
        E="7.4 7.4 5.2 2.2 1.2 7.4 6.1 4.2 2.1 7.2 3.1 5.2 7.1",
        X="7.4 6.1 6.3 3.4 7.4 7.4"),
    2022: dict(
        S="3.5 3.5 8.1 8.3 5.3 1.3 3.5 2.4 5.2 3.5 1.1 5.4 2.3 7.4 2.4 6.1 5.1 1.2 2.2 5.1 6.1 2.3 5.2 3.1 1.2",
        E="3.3 2.3 1.1 6.1 5.1 3.5 8.2 7.4 5.2 6.1 6.4 1.2 5.1",
        X="7.3 5.4 7.4 7.4 8.1 6.1"),
    2023: dict(
        S="5.5 3.4 3.4 2.1 3.2 3.2 5.3 3.5 8.3 6.5 8.2 7.4 8.1 2.1 5.2 6.2 4.2 3.2 5.2 7.4 6.4 4.3 5.1 2.1 7.1",
        E="3.1 1.4 2.3 7.3 5.3 2.1 1.3 5.1 6.4 5.2 7.4 6.1 6.4",
        X="7.4 7.3 7.4 6.1 7.3 5.4"),
    2025: dict(
        S="8.2 1.1 5.4 1.1 7.4 7.4 5.2 3.2 5.1 1.2 2.3 1.1 5.2 2.1 7.3 6.2 5.1 1.1 7.3 1.4 2.1 5.1 6.4 2.2 6.2",
        E="1.4 6.2 5.4 1.1 5.1 4.2 2.1 5.4 7.4 6.4 2.1 6.5 1.4",
        X="5.4 6.4 6.4 6.3 7.1 7.3"),
}


def paper_file(year, code):
    """The question paper of (year, paper code), relative to the repo root."""
    folder = IMSO / PAPER[code]
    if year not in TAIWAN_YEARS:
        name = f"IMSO_{year}_{PAPER[code]}.pdf"
    elif year == 2005:
        name = f"IMSO_{year}_{PAPER[code]}_Taiwan.pdf"
    else:
        name = f"IMSO_{year}_{PAPER[code]}_Taiwan-Round{1 if code == 'Q' else 2}.pdf"
    return (folder / name).relative_to(ROOT).as_posix()


def answer_file(year, code):
    """Per-paper Taiwan solutions if there are any, else the year's answer key, else ''."""
    paper = Path(paper_file(year, code)).stem
    for cand in (IMSO / "Answers" / f"{paper}_Solutions.pdf", IMSO / "Answers" / f"IMSO_{year}_Answers.pdf"):
        if cand.exists():
            return cand.relative_to(ROOT).as_posix()
    return ""


def label(year, code):
    """Paper name for the UI, e.g. 'Essay', 'Short Answer · Taiwan R1'."""
    if code == "Q":
        return "Short Answer · Taiwan R1"
    name = dict(KINDS)[code]
    return f"{name} · Taiwan R2" if year in (2008, 2009) else f"{name} · Taiwan" if year == 2005 else name


def load(stage="imso"):
    """Return (problems in file order, {id: sub-group code}, taxonomy) in the shape of
    categorize.load, using the Key Stage 2 groups and sub-groups."""
    tax = categorize.STAGES["ks2"]
    probs = []
    for m in HEADER_RE.finditer((ROOT / "imso_problems.txt").read_text(encoding="utf-8")):
        year, code, n, page = int(m[1]), m[2], int(m[3]), int(m[4])
        name = label(year, code)
        probs.append(dict(id=f"{year}-{code}{n}", year=year, label=f"{code}{n}", page=page, kind=code,
                          text=" ".join(m[5].split()), kind_name=name,
                          file=paper_file(year, code), file_label=f"Đề {name} {year}",
                          answer=answer_file(year, code), answer_label=f"Đáp án {year}"))
    assign = {}
    for year, papers in CODES.items():
        for code, codes in papers.items():
            ids = [p["id"] for p in probs if p["year"] == year and p["kind"] == code]
            codes = codes.split()
            if len(codes) != len(ids):
                raise SystemExit(f"imso {year} {code}: {len(codes)} codes for {len(ids)} problems")
            for pid, c in zip(ids, codes):
                if c not in tax["subs"]:
                    raise SystemExit(f"imso {pid}: unknown sub-group {c}")
                assign[pid] = c
    missing = [p["id"] for p in probs if p["id"] not in assign]
    if missing:
        raise SystemExit(f"imso: unclassified problems {missing[:10]}")
    return probs, assign, tax


def write_categories(stage="imso"):
    probs, assign, tax = load(stage)
    by = {}
    for p in probs:
        by.setdefault(assign[p["id"]], []).append(p)
    years = sorted({p["year"] for p in probs})
    per_kind = ", ".join(f"{sum(p['kind'] == k for p in probs)} {n}" for k, n in KINDS)
    L = ["IMSO (MATHEMATICS) - PROBLEM CATEGORISATION", "=" * 60,
         f"Total problems: {len(probs)} ({per_kind}), {years[0]}-{years[-1]}.",
         "Groups and sub-groups are the same as IMC Key Stage 2.",
         "IDs: Year-Paper+Problem. S = Short Answer, E = Essay, X = Exploration, Q = Taiwan round 1.",
         "2005, 2008 and 2009 are Taiwan selection papers.", "", "SUMMARY", "-" * 60]
    count = lambda prefix: sum(len(v) for k, v in by.items() if k.startswith(prefix))
    for g, name in tax["groups"].items():
        L.append(f"{g}. {name}  [{count(f'{g}.')} problems]")
        for k, sub in tax["subs"].items():
            if k.startswith(f"{g}."):
                L.append(f"     {k}  {sub}  ({count(k)})")
    L += ["", "NOTE: Each problem is placed in ONE best-fit sub-group (primary technique). Formulas and figures",
          "were partly lost in PDF text extraction; check the original PDF when the text is unclear.", "",
          "DETAILS", "=" * 60]
    for g, name in tax["groups"].items():
        L.append(f"\n##### {g}. {name}  [{count(f'{g}.')}] #####")
        for k, sub in tax["subs"].items():
            if not k.startswith(f"{g}."):
                continue
            L.append(f"\n--- {k} {sub} ({len(by.get(k, []))}) ---")
            for p in by.get(k, []):
                t = p["text"][:110] + ("..." if len(p["text"]) > 110 else "")
                L.append(f"  {p['id']:<9} {t}")
    out = ROOT / "imso_categories.txt"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out.name}: {len(probs)} problems")


if __name__ == "__main__":
    write_categories()
