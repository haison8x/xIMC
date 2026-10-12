"""Classify every extracted IMAS problem into 8 groups / 33 sub-groups: Middle and Upper Primary
use the IMC Key Stage 2 sub-groups, Junior uses the Key Stage 3 ones (see categorize.py).

Reads   data/imas_{middle,upper,junior}_problems.txt (from extract_imas.py)
Writes  data/imas_{middle,upper,junior}_categories.txt

Problem ids:  2023-R1-5 = school year 2023-2024, round 1, problem 5.
The classification is the hand-made table CODES below: one sub-group code per problem,
listed per division, year and round in problem order.
"""
import re

import categorize
from paths import DATA, IMAS_PAPERS as IMAS, ROOT

HEADER_RE = re.compile(r"=== Year (\d+) \| Round (\d) \| Problem (\d+) \| Page (\d+) ===\n(.*?)(?=\n=== Year|\Z)", re.S)

# Paper types shown as filter chips in the mind map: (code, name), the first is the default.
KINDS = [("R1", "Vòng 1"), ("R2", "Vòng 2")]
# division -> (paper folder, IMC taxonomy, English name)
DIVISIONS = {
    "middle": ("middle_primary", "ks2", "Middle Primary"),
    "upper": ("upper_primary", "ks2", "Upper Primary"),
    "junior": ("junior", "ks3", "Junior"),
}

CODES = {
    "middle": {
        2012: dict(R1="8.1 3.5 2.4 3.1 5.4 5.4 6.5 3.1 5.2 3.5 5.4 1.1 8.1 8.1 2.2 4.2 3.1 5.4 7.1 3.2 5.4 5.4 2.4 2.2 3.5",
                   R2="1.1 3.1 6.1 5.4 5.4 3.2 4.3 2.4 5.1 3.5 8.1 8.2 4.1 6.1 6.4"),
        2013: dict(R1="6.3 4.2 4.2 3.2 6.3 4.2 7.1 8.1 3.1 3.5 3.2 3.5 8.1 6.4 3.5 3.5 3.2 8.1 2.2 6.4 1.1 5.3 3.5 6.3 5.5",
                   R2="7.1 3.1 2.4 6.4 1.2 5.4 8.2 8.2 7.4 6.1 2.2 7.1 7.4 7.3 2.1"),
        2014: dict(R1="3.1 2.4 5.2 8.1 5.4 8.1 7.4 5.4 3.5 3.1 3.2 4.2 6.1 4.2 5.5 3.5 3.5 8.1 8.2 5.4 8.1 5.1 7.4 1.1 6.1",
                   R2="3.1 3.1 3.4 6.1 6.5 3.2 3.2 3.1 4.2 6.3 3.5 6.1 5.4 1.1 7.4"),
        2015: dict(R1="3.1 5.2 3.2 2.3 3.5 6.3 1.2 5.4 8.1 8.1 5.4 5.1 3.5 3.5 3.2 3.2 7.3 3.5 3.1 1.1 2.3 7.4 7.1 3.5 7.4",
                   R2="2.1 6.1 8.1 6.1 3.5 2.1 6.1 5.1 5.1 5.5 1.1 4.3 7.4 7.3 2.3"),
        2016: dict(R1="3.1 5.5 6.3 7.3 3.2 4.2 8.1 3.5 6.2 7.1 3.1 3.5 3.5 7.3 5.5 3.5 4.1 6.3 7.4 6.4 8.1 3.2 3.5 7.1 6.2",
                   R2="1.2 6.1 8.2 3.5 5.1 5.4 3.5 6.1 8.3 3.4 2.4 7.3 6.2 7.3 7.4"),
        2017: dict(R1="3.1 2.2 5.1 6.1 6.5 5.4 6.1 3.5 8.1 6.1 3.5 8.3 3.1 3.4 6.1 5.1 1.1 6.4 8.1 6.5 5.4 3.2 1.1 3.5 7.4",
                   R2="8.1 3.5 2.2 6.4 4.1 6.1 8.1 3.4 6.5 5.4 3.5 2.4 6.3 5.4 7.4"),
        2018: dict(R1="3.1 3.5 8.1 5.4 6.3 5.5 6.2 6.3 6.4 6.4 3.1 3.4 5.5 6.2 4.2 3.5 4.2 5.4 4.2 6.4 5.5 6.1 5.4 7.4 7.4",
                   R2="3.1 6.3 7.3 2.1 4.2 5.4 3.2 5.1 6.1 4.1 6.4 5.1 5.5 6.4 8.2"),
        2019: dict(R1="3.1 3.5 5.1 5.4 2.2 6.2 3.2 8.1 8.2 8.1 1.1 5.4 6.2 1.1 7.3 6.3 8.1 3.5 5.4 6.4 6.1 6.1 3.5 6.3 6.1",
                   R2="6.1 3.4 2.2 3.5 5.4 8.1 8.1 1.2 3.4 5.4 2.3 5.4 5.5 7.4 8.1"),
        2020: dict(R1="2.4 2.1 3.1 1.1 4.2 6.3 3.5 5.1 5.4 1.1 5.4 4.3 5.4 4.2 4.2 8.1 5.5 2.2 7.4 5.1 8.3 6.1 3.5 5.4 6.1",
                   R2="3.1 5.4 8.1 5.4 2.3 1.1 7.4 7.4 5.3 5.4 8.3 6.4 7.3 7.4 6.4"),
        2021: dict(R1="5.5 7.1 3.5 3.1 1.4 3.1 3.5 1.4 7.4 6.4 7.3 5.4 8.1 3.5 5.1 3.2 8.1 6.3 7.1 6.3 4.1 2.3 7.3 3.5 2.2",
                   R2="7.3 3.2 7.4 8.2 5.5 4.1 4.1 2.3 2.2 7.4 5.1 6.4 6.3 8.2 7.3"),
        2022: dict(R1="7.1 3.5 2.3 6.1 6.3 3.5 6.1 5.2 3.3 1.1 7.3 5.1 3.2 6.4 1.1 3.4 5.4 2.3 3.5 5.5 5.5 6.3 8.1 2.1 7.4",
                   R2="5.5 5.1 1.4 6.2 6.4 2.4 3.5 3.2 5.4 2.2 6.1 6.4 7.4 6.1 6.3"),
        2023: dict(R1="8.1 4.2 5.4 4.3 7.1 8.1 5.4 3.2 3.1 7.4 7.1 3.3 1.1 1.2 3.2 8.2 3.1 5.2 1.1 3.2 7.1 5.3 6.3 6.4 1.2",
                   R2="8.1 6.1 3.5 3.3 4.1 5.1 5.5 5.4 7.4 6.2 8.2 7.4 6.3 5.2 7.4"),
        2024: dict(R1="3.5 7.1 3.5 8.1 8.1 5.4 1.3 5.5 3.2 3.5 6.2 5.4 4.2 7.3 3.1 7.3 5.2 3.3 5.1 2.3 2.2 6.3 1.3 6.4 6.1",
                   R2="4.3 7.4 5.4 1.1 1.1 3.5 1.1 7.3 6.4 8.3 5.2 1.1 7.4 7.4 7.3"),
        2025: dict(R1="7.1 6.4 3.3 6.2 5.1 3.3 7.1 3.2 3.5 1.1 4.1 7.1 8.2 7.4 1.1 5.1 3.4 3.2 6.2 3.5 5.1 6.2 2.3 6.3 8.3",
                   R2="3.5 4.1 6.5 5.5 7.1 8.1 8.2 2.1 5.2 7.4 5.2 5.1 5.4 7.4 6.2"),
    },
    "upper": {
        2011: dict(R1="3.1 4.2 5.1 5.1 3.5 8.1 3.2 5.1 8.1 6.1 8.1 3.5 5.5 4.3 5.4 7.1 4.2 7.4 1.2 5.5 7.3 7.3 6.1 8.2 6.5",
                   R2="5.4 3.3 6.5 4.2 2.2 3.2 2.4 7.4 1.3 3.3 5.5 3.5 6.4 2.1 7.4"),
        2012: dict(R1="3.1 5.4 3.2 5.4 8.1 5.2 4.2 8.1 5.4 3.2 5.2 3.2 8.2 7.4 3.5 8.2 3.5 1.3 7.4 7.4 5.5 6.4 2.2 3.1 3.1",
                   R2="3.2 1.2 3.5 1.1 5.5 5.1 4.1 7.4 6.5 5.4 5.1 8.3 6.4 1.4 6.4"),
        2013: dict(R1="3.1 3.2 4.3 1.1 8.1 5.1 5.4 3.2 3.2 3.3 5.1 2.1 5.3 7.4 3.2 3.5 3.1 1.2 7.4 3.2 7.4 6.5 8.3 2.3 5.5",
                   R2="3.1 1.2 1.4 5.1 1.4 3.5 5.3 7.4 7.4 5.3 7.1 1.4 2.4 5.3 6.4"),
        2014: dict(R1="3.1 1.2 3.1 3.2 3.5 3.5 1.1 7.1 4.3 3.4 7.4 3.5 5.4 4.3 5.5 6.1 5.1 5.4 6.3 5.3 8.2 4.2 1.2 5.4 6.1",
                   R2="3.1 3.4 8.1 1.4 5.5 3.3 3.2 5.1 6.1 6.4 1.1 5.1 1.2 1.2 7.4"),
        2015: dict(R1="2.1 1.1 3.2 3.3 5.1 3.5 6.3 3.5 8.2 5.5 1.2 3.5 3.2 5.5 1.3 3.4 5.4 4.1 6.1 7.4 3.5 2.1 5.4 6.3 6.1",
                   R2="3.1 3.2 5.1 5.1 3.5 3.2 4.2 3.5 2.3 6.2 6.3 6.1 6.4 1.4 7.4"),
        2016: dict(R1="3.1 3.2 5.4 3.2 5.4 3.4 1.3 8.1 6.1 3.2 3.4 3.5 8.1 3.3 1.1 1.3 4.2 3.4 6.3 5.3 6.1 7.3 5.3 1.1 1.1",
                   R2="3.1 6.1 1.2 3.5 5.1 1.1 5.2 8.3 7.3 3.5 5.5 6.4 6.4 7.4 6.4"),
        2017: dict(R1="3.1 1.1 8.1 3.2 3.4 6.2 8.1 3.2 5.4 5.4 7.4 4.1 5.4 1.3 2.2 4.2 3.4 3.5 6.4 5.5 7.4 5.5 2.1 6.4 7.4",
                   R2="8.1 3.4 5.3 5.1 3.5 7.4 5.1 7.4 6.3 5.4 5.1 4.3 6.2 7.4 7.4"),
        2018: dict(R1="1.3 3.5 3.4 3.2 3.2 4.2 3.2 3.2 5.1 5.4 1.1 3.4 5.5 5.3 6.2 3.3 1.1 5.3 1.3 6.3 8.2 6.1 8.1 5.4 7.4",
                   R2="1.2 3.4 5.3 5.5 2.1 6.1 4.3 1.2 6.1 5.5 5.2 6.4 6.1 5.1 7.4"),
        2019: dict(R1="3.1 3.2 3.2 3.2 3.2 3.4 3.2 5.5 1.2 1.1 1.1 6.3 3.5 5.1 5.1 3.5 7.3 6.4 5.3 5.5 1.1 1.3 8.2 7.4 3.1",
                   R2="4.2 3.4 1.1 5.2 3.5 5.4 6.1 3.2 5.5 5.3 6.1 5.4 1.2 1.1 7.4"),
        2020: dict(R1="3.2 3.2 5.5 1.2 4.3 5.4 3.4 5.4 1.1 3.2 3.2 7.4 4.3 5.4 6.1 3.2 3.5 6.5 1.3 5.5 6.4 5.4 1.1 6.1 7.4",
                   R2="3.1 5.4 1.1 1.3 5.4 4.3 1.1 8.3 5.2 6.3 7.3 5.1 8.1 1.1 6.4"),
        2021: dict(R1="3.1 1.4 3.5 1.2 8.1 7.1 7.4 6.1 1.1 5.1 6.3 1.3 5.1 7.4 6.1 8.1 3.4 3.4 5.5 5.1 3.5 6.3 5.2 6.4 1.1",
                   R2="3.1 5.1 8.2 6.2 7.4 3.5 4.3 2.3 5.3 3.2 6.4 7.4 6.1 8.2 5.2"),
        2022: dict(R1="5.4 1.2 5.2 3.2 4.3 5.3 6.2 5.2 8.1 1.1 7.4 3.3 7.1 5.3 1.1 5.5 1.2 7.3 8.3 7.2 3.3 2.4 6.3 7.3 1.2",
                   R2="1.1 8.1 4.3 6.1 1.2 1.3 3.5 3.5 6.3 5.5 6.4 7.4 6.4 6.1 5.1"),
        2023: dict(R1="1.2 1.1 1.1 4.3 5.2 3.4 7.1 5.5 1.2 5.1 7.4 5.4 1.2 3.1 1.3 2.1 5.4 3.2 5.1 3.2 6.4 6.4 3.5 6.1 6.1",
                   R2="1.3 2.1 3.2 3.5 8.2 1.2 1.1 5.2 2.1 6.1 5.5 5.1 6.1 7.4 7.4"),
        2024: dict(R1="7.1 1.3 3.3 3.2 5.5 5.4 3.3 4.3 7.1 3.5 7.3 2.4 3.1 5.1 7.1 1.3 1.3 1.2 1.2 5.1 4.2 8.3 3.4 6.1 6.4",
                   R2="4.2 5.1 3.5 5.4 6.1 3.2 5.1 2.4 3.2 5.4 1.1 6.1 6.2 1.1 6.4"),
        2025: dict(R1="3.2 5.5 6.5 6.1 4.2 7.3 3.3 7.4 2.1 1.3 3.3 5.3 4.3 1.1 6.1 1.3 3.5 8.2 7.1 1.1 6.2 8.3 5.1 7.4 6.2",
                   R2="5.5 2.4 5.3 3.5 3.4 1.1 7.3 3.5 7.4 5.2 4.3 1.3 6.1 5.2 6.4"),
    },
    "junior": {
        2011: dict(R1="3.5 3.5 3.5 5.5 4.3 5.5 8.1 5.2 4.1 5.2 4.1 5.5 5.1 4.3 5.5 4.4 5.4 5.2 5.2 8.1 5.4 5.4 6.1 8.2 6.5",
                   R2="2.1 6.5 3.1 5.4 4.4 4.3 1.1 7.4 5.3 2.1 5.1 3.3 6.3 5.4 7.3"),
        2012: dict(R1="3.5 5.2 5.2 5.1 5.4 5.5 4.3 7.3 4.4 8.1 6.3 4.4 4.1 5.5 7.3 1.1 1.1 6.2 5.4 7.3 7.3 3.2 3.1 5.2 7.3",
                   R2="4.1 3.5 1.4 5.4 3.1 5.2 5.1 3.5 5.1 1.1 6.5 6.1 1.2 3.3 6.3"),
        2013: dict(R1="3.5 3.5 1.1 5.1 3.5 4.1 5.4 3.5 5.2 4.1 3.5 5.2 1.4 5.2 1.4 4.3 5.3 6.2 4.3 1.1 5.2 8.1 7.3 3.1 1.2",
                   R2="2.1 3.5 6.3 6.5 3.3 5.1 8.1 1.4 5.4 1.3 5.4 3.5 1.2 5.6 1.1"),
        2014: dict(R1="3.5 3.5 4.4 4.4 1.1 6.4 4.3 5.5 3.1 3.5 1.2 5.4 5.1 5.4 1.4 5.3 1.4 3.1 5.4 3.4 5.2 1.1 4.1 1.2 1.4",
                   R2="3.5 5.1 1.3 5.1 8.2 3.3 6.1 5.3 8.1 1.3 5.2 1.3 1.4 5.6 7.3"),
        2015: dict(R1="3.5 4.3 5.2 4.1 5.4 4.4 7.3 5.1 4.4 5.2 6.1 5.2 3.1 5.3 7.3 5.5 1.1 5.5 6.1 1.2 5.1 3.1 3.1 1.3 7.3",
                   R2="4.4 1.2 3.5 5.1 6.3 6.1 5.1 3.1 5.4 6.1 3.3 5.4 1.4 7.3 5.6"),
        2016: dict(R1="3.5 4.2 1.1 5.1 3.5 4.3 6.2 4.4 5.2 1.2 4.4 4.2 3.1 4.4 5.2 6.3 3.3 5.4 1.2 7.3 1.1 1.3 5.2 3.1 3.2",
                   R2="1.2 5.2 4.4 3.5 1.4 7.4 5.4 5.4 6.3 1.1 3.1 5.1 6.2 5.6 1.4"),
        2017: dict(R1="3.5 1.3 4.1 4.1 5.2 1.2 2.1 3.5 5.2 1.3 5.1 6.1 3.5 4.1 4.3 4.4 6.2 3.1 5.4 3.1 1.4 3.4 5.4 6.3 7.3",
                   R2="3.5 5.2 1.4 3.2 1.3 6.3 2.1 7.3 6.2 1.3 5.2 7.3 7.3 1.1 5.6"),
        2018: dict(R1="3.5 5.2 3.5 1.1 3.1 3.5 6.1 5.5 1.3 1.1 1.4 5.1 6.3 5.3 4.1 3.2 7.3 5.4 8.1 6.1 1.2 5.2 3.1 1.2 7.3",
                   R2="1.1 3.2 5.4 2.1 5.1 6.3 3.3 5.4 1.4 3.1 7.4 5.4 3.5 5.6 7.3"),
        2019: dict(R1="3.5 5.2 6.3 5.2 1.2 4.4 4.4 3.4 3.5 5.2 3.3 5.1 7.4 1.1 1.1 3.1 5.4 3.5 5.4 7.3 5.2 1.2 6.1 3.1 7.3",
                   R2="1.1 5.4 3.1 6.3 1.3 1.2 7.3 6.1 3.3 6.1 5.2 5.6 7.3 1.1 5.6"),
        2020: dict(R1="3.1 5.4 1.1 5.1 6.1 5.2 3.5 3.4 5.4 4.4 4.1 5.5 6.5 4.4 1.1 8.1 3.5 1.4 5.2 2.1 1.2 5.2 1.2 7.3 2.2",
                   R2="3.5 3.5 5.4 1.4 3.3 3.4 3.4 3.1 1.4 7.4 5.1 1.3 1.4 5.6 1.2"),
        2021: dict(R1="4.4 3.2 6.3 4.2 5.4 1.1 7.3 5.2 7.3 5.1 1.1 4.3 1.3 3.5 2.1 3.1 4.4 4.4 6.3 6.1 3.2 6.1 8.1 5.2 6.1",
                   R2="3.1 5.4 7.3 7.3 6.3 3.5 4.1 3.5 1.1 5.3 5.4 6.3 6.2 7.3 3.1"),
        2022: dict(R1="6.3 4.4 4.2 3.2 1.2 3.5 3.1 5.4 6.3 5.2 7.3 6.1 2.1 7.1 5.3 3.5 6.4 3.2 1.1 5.2 3.5 5.3 1.4 7.3 7.3",
                   R2="1.2 3.1 4.4 5.3 4.1 3.3 5.5 7.3 7.3 1.3 6.4 2.1 5.2 6.1 7.3"),
        2023: dict(R1="3.2 4.2 7.3 4.3 1.4 3.5 5.3 7.4 4.4 7.3 7.3 1.4 5.2 1.4 5.4 3.2 3.2 5.4 6.1 5.3 6.4 5.4 2.1 7.3 6.1",
                   R2="4.4 1.4 1.4 4.1 5.1 1.3 5.2 5.3 7.3 6.2 1.3 7.3 6.4 6.3 5.6"),
        2024: dict(R1="4.4 5.2 1.3 5.2 1.1 7.3 6.1 5.1 7.3 7.3 6.1 5.3 5.3 1.4 5.4 6.4 4.2 1.4 7.4 4.2 6.4 5.1 1.1 5.3 7.3",
                   R2="3.4 4.3 1.3 5.2 5.1 2.1 2.1 7.3 5.2 6.4 6.3 7.3 1.4 2.2 5.6"),
        2025: dict(R1="4.3 4.3 5.1 7.3 5.2 1.1 5.1 1.3 5.4 7.3 5.2 3.2 1.1 3.5 6.4 1.4 7.3 1.2 1.3 6.3 6.2 1.4 5.2 6.2 6.2",
                   R2="1.4 5.3 8.1 6.4 4.4 1.1 5.3 1.4 5.3 5.4 1.4 8.1 6.2 5.6 6.1"),
    },
}


def school_year(year):
    """2023 -> '2023-2024' (file names) and '2023–24' (labels)."""
    return f"{year}-{year + 1}", f"{year}–{str(year + 1)[2:]}"


def paper_file(stage, year, rnd):
    return (IMAS / DIVISIONS[stage][0] / f"{school_year(year)[0]}_round{rnd}.pdf").relative_to(ROOT).as_posix()


def answer_file(year, rnd):
    """The answer key of a round, one table for all three divisions."""
    path = IMAS / "answers" / f"{school_year(year)[0]}_round{rnd}.pdf"
    return path.relative_to(ROOT).as_posix() if path.exists() else ""


def load(stage):
    """Return (problems in file order, {id: sub-group code}, taxonomy) in the shape of
    categorize.load."""
    tax = categorize.STAGES[DIVISIONS[stage][1]]
    probs = []
    for m in HEADER_RE.finditer((DATA / f"imas_{stage}_problems.txt").read_text(encoding="utf-8")):
        year, rnd, n, page = int(m[1]), int(m[2]), int(m[3]), int(m[4])
        label = school_year(year)[1]
        probs.append(dict(id=f"{year}-R{rnd}-{n}", year=year, label=f"R{rnd}-{n}", page=page, kind=f"R{rnd}",
                          text=" ".join(m[5].split()), kind_name=f"Vòng {rnd}",
                          file=paper_file(stage, year, rnd), file_label=f"Đề vòng {rnd} {label}",
                          answer=answer_file(year, rnd), answer_label=f"Đáp án vòng {rnd} {label}"))
    assign = {}
    for year, rounds in CODES[stage].items():
        for kind, codes in rounds.items():
            ids = [p["id"] for p in probs if p["year"] == year and p["kind"] == kind]
            codes = codes.split()
            if len(codes) != len(ids):
                raise SystemExit(f"imas {stage} {year} {kind}: {len(codes)} codes for {len(ids)} problems")
            for pid, c in zip(ids, codes):
                if c not in tax["subs"]:
                    raise SystemExit(f"imas {stage} {pid}: unknown sub-group {c}")
                assign[pid] = c
    missing = [p["id"] for p in probs if p["id"] not in assign]
    if missing:
        raise SystemExit(f"imas {stage}: unclassified problems {missing[:10]}")
    return probs, assign, tax


def write_categories(stage):
    probs, assign, tax = load(stage)
    folder, ks, name = DIVISIONS[stage]
    by = {}
    for p in probs:
        by.setdefault(assign[p["id"]], []).append(p)
    years = sorted({p["year"] for p in probs})
    per_kind = ", ".join(f"{sum(p['kind'] == k for p in probs)} {n}" for k, n in KINDS)
    L = [f"IMAS {name.upper()} DIVISION - PROBLEM CATEGORISATION", "=" * 60,
         f"Total problems: {len(probs)} ({per_kind}), school years {years[0]}-{years[0] + 1} to {years[-1]}-{years[-1] + 1}.",
         f"Groups and sub-groups are the same as IMC Key Stage {ks[-1]}.",
         "IDs: Year-Round-Problem, Year = first year of the school year (2023-R1-5 = 2023-2024, round 1, problem 5).",
         "", "SUMMARY", "-" * 60]
    count = lambda prefix: sum(len(v) for k, v in by.items() if k.startswith(prefix))
    for g, gname in tax["groups"].items():
        L.append(f"{g}. {gname}  [{count(f'{g}.')} problems]")
        for k, sub in tax["subs"].items():
            if k.startswith(f"{g}."):
                L.append(f"     {k}  {sub}  ({count(k)})")
    L += ["", "NOTE: Each problem is placed in ONE best-fit sub-group (primary technique). Formulas and figures",
          "were partly lost in PDF text extraction; check the original PDF when the text is unclear.", "",
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
    out = DATA / f"imas_{stage}_categories.txt"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{out.name}: {len(probs)} problems")


if __name__ == "__main__":
    for stage in DIVISIONS:
        write_categories(stage)
