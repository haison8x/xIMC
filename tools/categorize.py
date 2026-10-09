"""Classify every extracted IMC problem (Individual + Team) into 8 groups / 33 sub-groups.

Reads   keystage{2,3}_problems.txt and keystage{2,3}_team_problems.txt (from extract-imc-problems.py)
Writes  keystage{2,3}_categories.txt

Problem ids:  Individual  2015-3 (KS2) / 2015-A3 (KS3)      Team  2015-T3
The classification itself is the hand-made table in STAGES below: one sub-group code per
problem, listed per year in the same order as the problems file.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADER_RE = re.compile(r"=== Year (\d+) \| Problem (\w+)(?: \| Page (\d+))? ===\n(.*?)(?=\n=== Year|\Z)", re.S)

STAGES = {
    "ks2": dict(
        groups={
            1: "NUMBER THEORY",
            2: "DIGITS & NUMBER PUZZLES",
            3: "ARITHMETIC, RATIO & ALGEBRAIC WORD PROBLEMS",
            4: "MOTION, RATE & TIME",
            5: "GEOMETRY",
            6: "COMBINATORICS & COUNTING",
            7: "LOGIC, GAMES & OPTIMIZATION",
            8: "SEQUENCES, PATTERNS & PROCESSES",
        },
        subs={
            "1.1": "Divisibility, remainders & congruences",
            "1.2": "Primes, factors & number of divisors",
            "1.3": "GCD / LCM, cycles & inclusion-exclusion on multiples",
            "1.4": "Perfect squares, cubes & powers",
            "2.1": "Two/three-digit numbers with digit relations (reversal, digit sum)",
            "2.2": "Cryptarithms & digit-placement equations",
            "2.3": "Counting / summing digits over a range",
            "2.4": "Building largest/smallest numbers from digit constraints",
            "3.1": "Clever computation (telescoping, alternating sums, operations)",
            "3.2": "Ratios, fractions & proportions",
            "3.3": "Percentages",
            "3.4": "Averages / means",
            "3.5": "Equations, money, age & quantity word problems",
            "4.1": "Meeting, chasing & relative motion (straight line)",
            "4.2": "Circular tracks, clocks & periodic motion",
            "4.3": "Rates, work, current & multi-stage journeys",
            "5.1": "Area & area ratios of polygons",
            "5.2": "Angles, triangles & regular polygons",
            "5.3": "Circles, arcs & shaded regions",
            "5.4": "Rectangles, squares, perimeter & dissections",
            "5.5": "3D solids, cubes, nets & surfaces",
            "6.1": "Arrangements, selections & distributions",
            "6.2": "Counting numbers with digit/property constraints",
            "6.3": "Counting rectangles/squares in grids & figures",
            "6.4": "Paths, tilings, colourings, recursion & partitions",
            "6.5": "Handshakes, tournaments & friendship graphs",
            "7.1": "Logic deduction & truth-tellers/liars",
            "7.2": "Turn-taking games & removal processes",
            "7.3": "Number-placement puzzles (magic sums, diagram fills)",
            "7.4": "Extremal / pigeonhole / minimum-moves optimisation",
            "8.1": "Regular sequences, indexing & cyclic position",
            "8.2": "Recursive sequences & repeated operations",
            "8.3": "Growing geometric patterns, spirals & grid patterns",
        },
        # One sub-group code per problem, in file order (Individual paper).
        individual={
            2003: "3.5 3.3 4.1 3.2 4.3 2.1 5.1 2.1 3.1 5.1 3.3 3.2 1.1 1.1 2.4",
            2004: "3.4 3.1 1.1 1.1 7.4 7.4 7.2 3.2 3.3 6.2 4.2 3.1 7.1 5.2 5.2",
            2005: "8.1 1.4 3.2 2.2 3.5 1.3 1.3 4.2 4.3 2.3 4.1 3.5 8.3 3.2 7.3",
            2006: "3.5 5.4 3.4 8.1 3.4 6.2 4.1 5.1 5.2 6.1 3.5 1.3 7.1 8.3 5.3",
            2007: "2.2 5.1 5.5 2.1 1.1 5.3 4.2 3.1 3.2 1.4 4.1 7.4 5.1 1.2 5.1",
            2008: "6.4 3.5 3.3 4.1 6.1 6.4 1.2 6.2 5.1 2.2 5.3 6.5 2.2 8.3 6.2",
            2009: "1.1 1.2 1.2 5.4 8.2 1.2 5.3 2.1 1.4 4.1 5.5 5.3 6.4 1.1 6.4",
            2010: "1.3 2.3 2.2 3.5 5.2 4.3 5.2 1.1 6.1 5.1 5.5 8.1 7.3 3.5 2.4",
            2011: "3.1 3.2 3.1 4.2 7.2 6.1 1.3 5.1 6.3 1.1 5.2 2.1 5.2 8.3 8.3",
            2012: "6.1 8.1 2.1 5.3 5.1 6.5 5.4 7.4 7.4 3.5 3.3 7.4 1.1 5.1 3.5",
            2013: "8.1 6.1 1.3 5.1 6.3 1.4 2.3 1.4 6.2 5.2 5.1 1.1 1.4 6.3 8.1",
            2014: "1.4 3.2 3.5 3.2 6.1 1.2 3.5 5.4 6.5 3.5 5.4 3.1 5.1 4.3 6.4",
            2015: "1.2 6.1 5.4 3.5 4.3 2.2 5.4 3.4 5.5 2.1 1.2 1.1 5.1 6.4 6.1",
            2016: "7.4 4.1 5.3 1.1 3.5 4.3 3.5 7.4 1.3 5.1 2.4 2.1 6.2 1.1 6.1",
            2017: "3.2 1.3 5.1 3.5 5.2 1.3 5.1 8.2 6.2 6.1 6.3 2.3 6.4 5.1 6.3",
            2018: "3.2 3.5 7.3 2.2 5.2 2.2 2.2 2.4 5.2 1.2 6.4 6.3 5.1 7.4 6.3",
            2019: "5.1 5.3 8.1 3.3 3.4 5.1 3.2 7.4 1.2 5.1 5.2 6.1 2.3 6.4 2.2",
            2021: "7.4 6.4 1.1 3.2 4.1 4.1 3.5 5.1 7.3 1.4 6.3 6.1 5.2 5.2 6.2",
            2022: "5.1 3.5 3.4 5.4 3.5 6.4 3.4 7.3 5.1 3.1 7.4 2.2 5.2 1.2 6.4",
            2023: "5.3 3.5 1.2 6.2 4.1 2.2 7.4 4.2 5.3 7.4 1.1 8.2 5.1 7.4 5.5",
            2024: "3.2 1.2 3.5 1.1 3.1 7.3 2.2 2.2 5.1 5.1 6.1 5.3 6.5 8.1 6.4",
            2025: "5.1 3.5 7.2 5.2 3.4 1.2 2.3 5.1 3.4 2.2 5.2 6.1 6.4 6.2 1.2",
            2026: "4.1 7.1 3.1 6.5 5.3 7.4 6.3 5.1 8.2 6.4 8.3 1.1 2.2 1.2 6.1",
        },
        # Team paper.
        team={
            2003: "5.1 3.5 5.1 1.1 3.3 5.5 1.1 5.3 6.1 6.2",
            2004: "2.1 5.5 1.3 1.2 3.1 6.1 3.1 2.2 7.3 7.3",
            2005: "5.1 5.1 6.4 2.3 7.3 7.4 7.3 7.1 2.2 7.4",
            2006: "6.1 2.4 2.1 5.1 3.4 5.5 5.5 1.1 6.1 6.4",
            2007: "4.3 2.3 5.1 2.1 1.2 1.2 3.5 1.2 1.3 1.2",
            2008: "2.1 5.2 4.1 3.1 7.3 6.1 7.4 7.4 7.3 7.4",
            2009: "8.1 5.5 1.3 6.4 4.3 8.3 5.1 5.3 6.4 7.3",
            2010: "8.3 7.4 5.4 3.5 3.5 2.4 7.3 7.4 7.3 6.4",
            2011: "7.3 8.2 5.2 4.3 6.4 6.2 7.3 2.2 7.1 1.2",
            2012: "7.3 8.1 8.1 3.2 3.5 5.4 1.1 5.2 7.3 8.2",
            2013: "6.4 3.1 6.4 5.1 6.1 7.4 7.3 6.4 2.2 7.1",
            2014: "3.1 7.3 5.4 7.1 1.1 6.3 6.5 5.1 8.2 7.4",
            2015: "7.3 7.4 7.4 4.1 5.3 7.1 6.1 5.2 2.4 6.2",
            2016: "7.3 6.4 7.3 5.1 1.2 3.5 6.2 6.4 7.3 5.2",
            2017: "5.4 2.2 1.1 1.4 7.4 7.3 5.1 7.3 8.2 2.1",
            2018: "7.1 5.4 1.2 5.4 8.3 1.1 5.4 4.1 7.3 1.3",
            2019: "3.5 5.1 7.4 1.4 6.1 7.1 7.3 5.4 6.3 8.2",
            2021: "6.4 7.4 1.2 3.4 5.2 5.5 3.2 6.2 7.3 4.1",
            2022: "8.2 7.3 8.3 2.4 6.2 3.4 6.5 5.4 7.4 6.1",
            2023: "6.3 3.5 4.1 6.4 1.1 1.4 5.5 5.2 8.3 6.3",
            2024: "3.3 2.3 4.2 5.1 8.1 5.2 5.4 7.4 7.2 7.4",
            2025: "1.4 7.4 1.2 6.4 5.1 7.2 1.2 7.4 6.1 6.3",
            2026: "5.3 1.2 8.2 6.1 5.1 3.5 7.3 5.2 4.3 6.4",
        },
    ),
    "ks3": dict(
        groups={
            1: "NUMBER THEORY",
            2: "DIGITS & NUMBER PUZZLES",
            3: "ALGEBRA",
            4: "ARITHMETIC & WORD PROBLEMS (ratio, average, rate)",
            5: "GEOMETRY",
            6: "COMBINATORICS & PROBABILITY",
            7: "LOGIC, GAMES & OPTIMIZATION",
            8: "SEQUENCES, PATTERNS & PROCESSES",
        },
        subs={
            "1.1": "Divisibility, remainders, factorials & trailing zeros",
            "1.2": "Primes, factors & number of divisors",
            "1.3": "Perfect squares, powers & special forms",
            "1.4": "Integer solutions, Diophantine equations & GCD/LCM",
            "2.1": "Digit relations & cryptarithms",
            "2.2": "Counting / summing digits",
            "3.1": "Systems & symmetric expressions in real numbers",
            "3.2": "Inequalities & extreme values (min/max)",
            "3.3": "Polynomials & quadratic roots (Vieta)",
            "3.4": "Floor / fractional part & functional equations",
            "3.5": "Computation & evaluation (telescoping, large expressions)",
            "4.1": "Ratio, percent & fractions",
            "4.2": "Averages / means",
            "4.3": "Motion, clocks & rates",
            "4.4": "Quantity & equation word problems",
            "5.1": "Area & area ratios",
            "5.2": "Angle chasing & triangles",
            "5.3": "Circles, tangency, arcs & cyclic figures",
            "5.4": "Lengths, squares/rectangles/polygons & Pythagoras",
            "5.5": "3D solids & folding",
            "5.6": "Geometric proofs & advanced configurations",
            "6.1": "Arrangements & selections",
            "6.2": "Counting numbers / strings with constraints",
            "6.3": "Grid paths, tilings, colourings & figure counting",
            "6.4": "Probability",
            "6.5": "Graphs, tournaments & networks",
            "7.1": "Logic & knowledge puzzles",
            "7.2": "Games & winning strategies",
            "7.3": "Extremal, construction, invariants & algorithms",
            "7.4": "Number-placement puzzles",
            "8.1": "Sequences, indexing & ordered lists",
            "8.2": "Recursive sequences & iterated processes",
            "8.3": "Growing patterns on grids",
        },
        # One sub-group code per problem, in file order (Individual paper).
        individual={
            1999: "1.1 5.2 2.2 5.4 3.5 6.2 5.3 1.4 2.1 5.1 6.3 4.4 6.5 5.4 2.1",
            2000: "1.1 3.5 1.1 8.1 1.3 1.2 5.2 2.1 5.4 4.4 5.4 8.1 5.6 7.3 2.1",
            2001: "1.4 5.4 5.1 1.1 4.3 5.3 1.4 3.1 3.5 1.1 3.2 3.3 5.6",
            2002: "4.1 3.1 7.3 3.3 7.3 5.1 1.1 8.2 5.2 3.1 5.2 5.2 2.1 3.1 5.6",
            2004: "5.3 3.1 5.1 6.1 1.4 6.3 7.4 7.3 7.3 7.1 3.4 3.2 6.2 5.4 5.6",
            2005: "2.1 5.4 3.1 1.1 1.3 5.3 3.3 3.1 5.3 3.5 2.1 5.1 3.1 5.1 8.2",
            2006: "4.4 5.3 5.2 1.4 5.1 3.1 4.3 5.1 3.1 8.2 5.5 3.2 7.3 5.3 7.3",
            2007: "4.2 7.3 5.1 4.4 1.3 5.5 1.1 5.4 5.4 2.1 3.4 2.2 7.3 6.5 1.2",
            2008: "6.3 1.1 3.1 3.2 6.2 8.2 1.3 5.1 3.2 5.4 1.2 5.3 3.4 5.4 1.3",
            2009: "3.1 8.2 4.4 5.2 7.3 3.5 5.6 4.2 1.4 2.1 6.1 4.4 6.5 5.2 1.1",
            2010: "3.1 4.4 1.4 5.4 1.2 3.3 5.3 1.2 7.3 5.2 4.4 7.1 5.3 1.4 8.2",
            2011: "1.4 7.1 1.3 5.1 1.2 7.1 5.3 1.1 5.4 6.2 7.3 3.2 5.6 3.3 7.3",
            2012: "1.1 5.3 2.1 5.1 6.3 1.2 6.2 5.3 6.2 6.1 5.3 6.1 3.5 3.2 5.2",
            2013: "2.1 5.1 6.1 1.4 5.3 1.3 5.4 6.1 1.4 5.3 2.1 6.3 3.5 5.4 7.3",
            2014: "2.1 3.5 5.2 3.2 5.4 1.1 3.1 5.1 6.1 1.4 2.2 5.3 7.3 5.4 8.2",
            2015: "7.4 2.1 7.3 6.3 4.3 1.4 5.3 2.1 6.3 1.2 5.1 7.3 1.3 6.4 5.1",
            2016: "4.4 1.4 5.3 1.4 5.1 2.2 4.4 5.4 5.4 4.2 6.4 5.4 3.1 5.3 1.1",
            2017: "4.1 4.2 5.4 3.2 3.2 5.3 3.2 5.1 3.2 5.2 3.1 1.4 1.3 5.2 3.3",
            2018: "6.5 1.4 6.4 1.3 5.3 1.1 3.3 5.2 6.1 5.3 3.1 3.1 3.3 6.3 5.2",
            2019: "2.2 1.2 6.4 8.3 6.2 5.1 1.4 1.4 6.3 3.4 5.4 8.1 8.1 1.4 5.4",
            2021: "6.3 7.3 3.3 7.3 5.4 3.1 5.1 1.2 5.2 1.1 6.5 3.1 5.4 1.4 1.1",
            2022: "3.3 1.2 3.2 5.3 1.4 2.2 3.3 6.1 5.4 8.2 6.2 5.2 7.2 5.4 2.1",
            2023: "3.2 5.3 5.1 1.3 1.4 3.1 8.1 5.1 7.3 7.3 7.3 6.3 3.4 6.3 5.6",
            2024: "1.1 3.1 1.3 5.2 3.3 5.1 2.1 6.1 7.3 3.4 7.3 7.3 7.3 5.4 7.2",
            2025: "1.4 5.2 1.4 5.3 1.1 5.4 7.2 1.4 1.1 7.3 1.1 3.2 3.5 5.3 6.4",
            2026: "5.1 6.1 3.3 3.1 1.4 5.2 2.1 6.1 2.1 3.2 6.1 5.1 6.3 7.3 5.6",
        },
        # Team paper.
        team={
            1999: "1.2 8.2 1.4 6.3 7.4",
            2000: "5.6 7.4 1.4 7.1 1.4 5.5",
            2001: "7.4 7.3 6.3 6.3 2.1 5.4 2.1 6.3",
            2002: "3.1 3.4 6.3 1.4 1.4 5.6 5.6 7.3",
            2004: "5.4 6.3 7.4 1.1 7.3 6.5 6.3 6.3",
            2005: "1.4 7.3 8.1 5.6 6.3 7.2 7.3 1.2 6.3 1.4",
            2006: "5.3 5.2 6.3 7.4 2.1 7.2 1.1 3.4 5.4 1.3",
            2007: "7.4 7.3 7.4 1.1 1.4 6.5 7.3 5.6 7.3 6.3",
            2008: "1.4 7.3 7.3 7.3 7.3 5.2 5.3 6.2 7.3 1.3",
            2009: "8.2 1.2 7.4 6.5 7.3 3.2 7.3 5.4 6.5 1.4",
            2010: "3.1 5.6 1.4 6.3 3.2 7.3 5.2 1.4 7.4 6.3",
            2011: "3.1 7.3 7.4 6.3 5.4 3.3 8.2 5.2 7.3 7.1",
            2012: "7.3 4.2 7.4 6.2 2.1 1.2 6.3 7.3 6.3 2.1",
            2013: "7.4 5.4 6.4 5.2 8.2 6.5 5.1 7.2 7.3 6.3",
            2014: "3.5 1.2 1.4 6.3 1.4 1.2 6.2 5.3 5.2 7.3",
            2015: "7.4 1.3 5.4 6.1 7.3 1.4 7.4 5.1 1.3 5.2",
            2016: "7.4 2.1 1.4 5.3 7.3 6.1 3.1 7.3 6.3 1.2",
            2017: "5.5 7.3 5.3 1.4 3.3 5.6 1.1 3.2 6.3 6.3",
            2018: "1.2 1.4 5.1 1.3 3.2 7.3 1.2 5.1 6.3 6.2",
            2019: "1.2 7.3 5.4 1.1 6.1 5.4 7.3 6.1 6.3 2.2",
            2021: "7.4 3.1 5.2 1.3 3.5 6.5 5.1 5.3 1.2 6.2",
            2022: "1.1 3.4 7.3 5.3 3.1 6.1 5.1 5.3 1.4 8.1",
            2023: "3.3 5.6 5.2 7.3 5.4 1.3 1.3 7.3 6.2 7.4",
            2024: "1.4 3.3 2.2 5.6 5.4 1.3 5.2 6.3 8.2 7.2",
            2025: "1.4 3.3 1.3 3.4 5.1 1.1 7.3 6.5 5.3 6.2",
            2026: "6.1 1.3 5.2 3.1 7.3 3.2 5.3 6.2 7.3 5.6",
        },
    ),
}
DIRS = {"ks2": "keystage2", "ks3": "keystage3"}


def read_problems(path, kind):
    """[(id, year, label, page, text)] in file order."""
    out = []
    for m in HEADER_RE.finditer(path.read_text(encoding="utf-8")):
        year, label, page = int(m[1]), m[2], int(m[3] or 1)
        pid = f"{year}-T{label}" if kind == "T" else f"{year}-{label}"
        out.append(dict(id=pid, year=year, label=label, page=page, kind=kind, text=" ".join(m[4].split())))
    return out


def load(stage):
    """Return (problems in file order, {id: sub-group code}, stage table)."""
    cfg, d = STAGES[stage], DIRS[stage]
    probs = read_problems(ROOT / f"{d}_problems.txt", "I") + read_problems(ROOT / f"{d}_team_problems.txt", "T")
    assign = {}
    for kind, table in (("I", cfg["individual"]), ("T", cfg["team"])):
        for year, codes in table.items():
            ids = [p["id"] for p in probs if p["kind"] == kind and p["year"] == year]
            codes = codes.split()
            if len(codes) != len(ids):
                raise SystemExit(f"{stage} {kind} {year}: {len(codes)} codes for {len(ids)} problems")
            for pid, code in zip(ids, codes):
                if code not in cfg["subs"]:
                    raise SystemExit(f"{stage} {pid}: unknown sub-group {code}")
                assign[pid] = code
    missing = [p["id"] for p in probs if p["id"] not in assign]
    if missing:
        raise SystemExit(f"{stage}: unclassified problems {missing[:10]}")
    return probs, assign, cfg


def write_categories(stage):
    probs, assign, cfg = load(stage)
    d = DIRS[stage]
    by = {}
    for p in probs:
        by.setdefault(assign[p["id"]], []).append(p)
    n_i = sum(p["kind"] == "I" for p in probs)
    years = sorted({p["year"] for p in probs})
    L = [f"{'KEY STAGE 2' if stage == 'ks2' else 'KEY STAGE 3'} - PROBLEM CATEGORISATION", "=" * 60,
         f"Total problems: {len(probs)} ({n_i} individual + {len(probs) - n_i} team), {years[0]}-{years[-1]}. "
         f"8 primary groups, {len(cfg['subs'])} sub-groups.",
         "IDs: Year-Problem; team problems are marked T (e.g. 2015-T3).", "", "SUMMARY", "-" * 60]
    def count(prefix):
        ps = [p for k, v in by.items() if k.startswith(prefix) for p in v]
        return len(ps), sum(p["kind"] == "T" for p in ps)
    for g, name in cfg["groups"].items():
        n, t = count(f"{g}.")
        L.append(f"{g}. {name}  [{n} problems, {t} team]")
        for k, sub in cfg["subs"].items():
            if k.startswith(f"{g}."):
                n, t = count(k)
                L.append(f"     {k}  {sub}  ({n}, team {t})")
    L += ["", "NOTE: Each problem is placed in ONE best-fit sub-group (primary technique). Formulas and figures",
          "were partly lost in PDF text extraction; check the original PDF when the text is unclear.", "",
          "DETAILS", "=" * 60]
    for g, name in cfg["groups"].items():
        L.append(f"\n##### {g}. {name}  [{count(f'{g}.')[0]}] #####")
        for k, sub in cfg["subs"].items():
            if not k.startswith(f"{g}."):
                continue
            L.append(f"\n--- {k} {sub} ({len(by.get(k, []))}) ---")
            for p in by.get(k, []):
                t = p["text"][:110] + ("..." if len(p["text"]) > 110 else "")
                L.append(f"  {p['id']:<9} {t}")
    out = ROOT / f"{d}_categories.txt"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out.name}: {len(probs)} problems")


if __name__ == "__main__":
    for s in STAGES:
        write_categories(s)
