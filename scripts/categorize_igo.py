"""Classify every extracted IGO problem into the geometry groups / sub-groups below.

Reads   data/igo_problems.txt (from extract_igo.py)
Writes  data/igo_categories.txt

Problem ids:  2021-I3 = IGO 2021, Intermediate level, problem 3 (E = Elementary, A = Advanced).
The classification is the hand-made table CODES below: one sub-group code per problem, listed per
year and level in problem order.
"""
import re

import extract_igo
from paths import DATA, ROOT

HEADER_RE = re.compile(r"=== Year (\d+) \| Level (\w) \| Problem (\d+) \| Page (\d+) \| Solution (\d+) ===\n"
                       r"(.*?)(?=\n=== Year|\Z)", re.S)

# Levels shown as filter chips in the mind map: (code, name).
KINDS = [("E", "Elementary"), ("I", "Intermediate"), ("A", "Advanced")]
LOWER_KIND_NAMES = False

TAX = dict(
    groups={
        1: "ANGLES & TRIANGLES",
        2: "LENGTHS, RATIOS & AREAS",
        3: "CIRCLES",
        4: "TRIANGLE CENTRES",
        5: "TRANSFORMATIONS",
        6: "COMBINATORIAL GEOMETRY",
        7: "EXTREMAL PROBLEMS, LOCI & SOLIDS",
    },
    subs={
        "1.1": "Angle chasing, isosceles & equilateral triangles",
        "1.2": "Congruent triangles & auxiliary constructions",
        "1.3": "Polygons, regular polygons & angle sums",
        "2.1": "Lengths & Pythagoras",
        "2.2": "Similar triangles, parallels & ratios",
        "2.3": "Areas & area ratios",
        "2.4": "Collinearity & concurrency (Menelaus, Ceva)",
        "3.1": "Cyclic quadrilaterals & concyclic points",
        "3.2": "Tangents & tangent circles",
        "3.3": "Power of a point & radical axes",
        "3.4": "Incircles & excircles",
        "4.1": "Orthocentre, centroid, circumcentre & Euler line",
        "4.2": "Incentre & arc midpoints",
        "5.1": "Reflections, rotations & translations",
        "5.2": "Homothety & spiral similarity",
        "5.3": "Inversion & projective methods",
        "6.1": "Dissections, tilings, folding & colouring",
        "6.2": "Points & lines in general position, convex polygons",
        "7.1": "Geometric inequalities & extremal values",
        "7.2": "Loci, fixed points & fixed lines",
        "7.3": "Constructions & solid geometry",
    },
)

CODES = {
    2017: dict(E="2.3 1.1 1.3 6.2 7.1", I="2.1 3.1 6.2 7.1 2.2", A="3.4 7.1 5.2 3.2 7.3"),
    2018: dict(E="6.1 2.3 2.1 7.1 6.2", I="2.1 1.1 3.1 7.3 2.2", A="3.1 4.1 6.2 5.3 3.3"),
    2019: dict(E="5.1 2.2 6.2 1.2 6.2", I="3.1 1.3 2.4 4.1 7.1", A="3.1 6.2 3.3 5.3 5.3"),
    2020: dict(E="6.1 1.2 7.1 7.2 6.2", I="1.1 1.2 3.3 3.3 7.3", A="1.1 4.2 7.1 3.2 5.2"),
    2021: dict(E="6.1 2.3 3.2 1.2 1.3", I="4.1 7.1 5.2 4.2 7.2", A="3.1 3.3 5.3 6.2 4.1"),
    2022: dict(E="1.3 5.1 1.1 7.1 5.1", I="1.2 3.1 3.1 6.1 5.2", A="3.2 3.2 5.3 3.4 5.3"),
    2023: dict(E="1.2 1.2 6.1 7.1 6.2", I="1.3 5.1 3.2 3.3 6.2", A="3.3 2.3 7.1 5.3 5.3"),
    2024: dict(E="6.1 2.2 7.1 6.2 3.1", I="1.1 2.2 3.2 6.1 5.2", A="5.1 3.1 3.4 3.3 7.2"),
    2025: dict(E="1.3 1.1 6.1 7.1 1.2", I="2.2 1.2 5.1 7.1 7.2", A="3.2 3.3 5.3 5.3 5.3"),
}


def norm(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def load(stage="igo"):
    """Return (problems in file order, {id: sub-group code}, taxonomy) in the shape of
    categorize.load."""
    probs = []
    for m in HEADER_RE.finditer((DATA / "igo_problems.txt").read_text(encoding="utf-8")):
        year, level, n, page, sol = int(m[1]), m[2], int(m[3]), int(m[4]), int(m[5])
        pdf = extract_igo.source_pdf(year).relative_to(ROOT).as_posix()
        probs.append(dict(id=f"{year}-{level}{n}", year=year, label=f"{level}{n}", page=page, kind=level,
                          text=" ".join(m[6].split()), kind_name=dict(KINDS)[level],
                          file=pdf, file_label=f"Sách IGO {year}", answer=f"{pdf}#page={sol}",
                          answer_label=f"Lời giải, trang {sol}"))
    assign = {}
    for year, levels in CODES.items():
        for level, codes in levels.items():
            ids = [p["id"] for p in probs if p["year"] == year and p["kind"] == level]
            codes = codes.split()
            if len(codes) != len(ids):
                raise SystemExit(f"igo {year} {level}: {len(codes)} codes for {len(ids)} problems")
            for pid, c in zip(ids, codes):
                if c not in TAX["subs"]:
                    raise SystemExit(f"igo {pid}: unknown sub-group {c}")
                assign[pid] = c
    missing = [p["id"] for p in probs if p["id"] not in assign]
    if missing:
        raise SystemExit(f"igo: unclassified problems {missing[:10]}")
    return probs, assign, TAX


def same_problems(probs):
    """{id: id of the same problem set at another level of that year}."""
    first, same = {}, {}
    for p in probs:
        key = (p["year"], norm(p["text"]))
        if key in first:
            same[p["id"]] = first[key]
            same[first[key]] = p["id"]
        else:
            first[key] = p["id"]
    return same


def write_categories(stage="igo"):
    probs, assign, tax = load(stage)
    same = same_problems(probs)
    by = {}
    for p in probs:
        by.setdefault(assign[p["id"]], []).append(p)
    years = sorted({p["year"] for p in probs})
    per_kind = ", ".join(f"{sum(p['kind'] == k for p in probs)} {n}" for k, n in KINDS)
    L = ["IRANIAN GEOMETRY OLYMPIAD - PROBLEM CATEGORISATION", "=" * 60,
         f"Total problems: {len(probs)} ({per_kind}), {years[0]}-{years[-1]}.",
         "IDs: Year-Level+Problem. E = Elementary, I = Intermediate, A = Advanced.",
         "A problem set at two levels is listed at both (marked = other id).",
         "", "SUMMARY", "-" * 60]
    count = lambda prefix: sum(len(v) for k, v in by.items() if k.startswith(prefix))
    for g, name in tax["groups"].items():
        L.append(f"{g}. {name}  [{count(f'{g}.')} problems]")
        for k, sub in tax["subs"].items():
            if k.startswith(f"{g}."):
                L.append(f"     {k}  {sub}  ({count(k)})")
    L += ["", "NOTE: Each problem is placed in ONE best-fit sub-group (main idea of the official solution).",
          "Formulas and figures were partly lost in PDF text extraction; check the booklet when unclear.", "",
          "DETAILS", "=" * 60]
    for g, name in tax["groups"].items():
        L.append(f"\n##### {g}. {name}  [{count(f'{g}.')}] #####")
        for k, sub in tax["subs"].items():
            if not k.startswith(f"{g}."):
                continue
            L.append(f"\n--- {k} {sub} ({len(by.get(k, []))}) ---")
            for p in by.get(k, []):
                t = p["text"][:110] + ("..." if len(p["text"]) > 110 else "")
                mark = f" (= {same[p['id']]})" if p["id"] in same else ""
                L.append(f"  {p['id'] + mark:<17} {t}")
    out = DATA / "igo_categories.txt"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out.name}: {len(probs)} problems")


if __name__ == "__main__":
    write_categories()
