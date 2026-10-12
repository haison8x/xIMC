"""Download IMAS (Chiuchang) past papers and sort them by division.

Output layout:
    papers/imas/middle_primary/{year}_round{1,2}.pdf   Problems
    papers/imas/upper_primary/{year}_round{1,2}.pdf
    papers/imas/junior/{year}_round{1,2}.pdf
    papers/imas/answers/{year}_round{1,2}.pdf          Solution keys (all divisions)

{year} is the school year, e.g. 2025-2026.
"""
import argparse
import re
import sys
import urllib.request

from paths import IMAS_PAPERS

PAGE_URLS = [
    "https://chiuchang.org/imas/problems/imas-2025-2026/",
    "https://chiuchang.org/imas/imas-2024-2025/",
    "https://chiuchang.org/imas/imas-2023-2024-2/",
    "https://chiuchang.org/imas/imas-2022-2023/",
    "https://chiuchang.org/imas/imas-2021-2022-4/",
    "https://chiuchang.org/imas/problems/imas-2020-2021/",
    "https://chiuchang.org/imas/problems/imas-2019-2020/",
    "https://chiuchang.org/imas/problems/imas-2018-2017/",
    "https://chiuchang.org/imas/problems/2017-2/",
    "https://chiuchang.org/imas/problems/2016-2/",
    "https://chiuchang.org/imas/problems/2015-2/",
    "https://chiuchang.org/imas/problems/2014-2/",
    "https://chiuchang.org/imas/problems/2013-2/",
    "https://chiuchang.org/imas/problems/2012-2/",
    "https://chiuchang.org/imas/problems/2011-2/",
]
HEADERS = {"User-Agent": "Mozilla/5.0"}

# One regex walks the page in order: <h2> year, division name, <h3> round, <a> link.
TOKEN_RE = re.compile(
    r"<h2[^>]*>(?P<h2>.*?)</h2>"
    r"|(?P<division>Middle Primary|Upper Primary|Junior) Division"
    r"|<h3[^>]*>(?P<h3>.*?)</h3>"
    r'|<a\s[^>]*href="(?P<href>[^"]+)"[^>]*>(?P<label>.*?)</a>',
    re.S | re.I,
)
TAG_RE = re.compile(r"<[^>]+>")
DRIVE_ID_RE = re.compile(r"drive\.google\.com/(?:file/d/|open\?id=|uc\?.*?id=)([\w-]+)")


def fetch(url: str):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.geturl(), resp.read()


def text(html: str) -> str:
    return TAG_RE.sub("", html).replace("&nbsp;", " ").strip()


def round_of(label: str):
    if re.search(r"first", label, re.I):
        return "round1"
    if re.search(r"second", label, re.I):
        return "round2"
    return None


def parse_papers(html: str):
    """Yield (year, folder, round, url) for every paper link."""
    for paper in dict.fromkeys(_paper_links(html)):  # solution keys repeat per division
        yield paper


def _paper_links(html: str):
    start = html.find("entry-content")
    html = html[start:html.find("</article", start)]
    year = division = rnd = None
    for m in TOKEN_RE.finditer(html):
        if m.group("h2") is not None:
            found = re.search(r"\d{4}-\d{4}", text(m.group("h2")))
            year = found.group() if found else None
        elif m.group("division"):
            division = m.group("division").lower().replace(" ", "_")
        elif m.group("h3") is not None:
            heading = text(m.group("h3"))
            # "Solution Keys" heading: the links below are labelled by round.
            rnd = round_of(heading)
        elif year:
            label = text(m.group("label"))
            if re.match(r"problems", label, re.I) and division and rnd:
                yield year, division, rnd, m.group("href")
            elif re.match(r"solution", label, re.I) and rnd:
                yield year, "answers", rnd, m.group("href")
            elif round_of(label) and rnd is None:
                yield year, "answers", round_of(label), m.group("href")


def download_pdf(url: str) -> bytes:
    """Follow chiuchang.org.tw redirects and turn Drive viewer links into downloads."""
    final_url, data = fetch(url)
    if data.startswith(b"%PDF"):
        return data
    found = DRIVE_ID_RE.search(final_url) or DRIVE_ID_RE.search(url)
    if not found:
        raise ValueError(f"not a PDF and not a Drive link: {final_url}")
    drive_id = found.group(1)
    _, data = fetch(
        f"https://drive.usercontent.google.com/download?id={drive_id}&export=download&confirm=t"
    )
    if not data.startswith(b"%PDF"):
        raise ValueError(f"Drive file {drive_id} is not a PDF")
    return data


def main():
    argparse.ArgumentParser(description=__doc__.splitlines()[0]).parse_args()

    ok = skipped = failed = 0
    for page in PAGE_URLS:
        _, html = fetch(page)
        for year, folder, rnd, url in parse_papers(html.decode("utf-8", errors="replace")):
            dest = IMAS_PAPERS / folder / f"{year}_{rnd}.pdf"
            if dest.exists():
                skipped += 1
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            try:
                dest.write_bytes(download_pdf(url))
                print(f"OK   {folder}/{dest.name}  <- {url}")
                ok += 1
            except Exception as e:
                print(f"FAIL {folder}/{dest.name}  <- {url}: {e}", file=sys.stderr)
                failed += 1

    print(f"Done: {ok} downloaded, {skipped} already existed, {failed} failed")


if __name__ == "__main__":
    main()
