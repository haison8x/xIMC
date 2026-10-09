"""Download IMC (Chiuchang) past papers and sort them by keystage.

Output layout (next to this script):
    keystage2/{year}.pdf
    keystage3/{year}.pdf

Per year and keystage three files are saved:
    {year}.pdf          Individual paper
    {year}_team.pdf     Team paper
    {year}_answer.pdf   Answers / solutions
"""
import argparse
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urljoin

PAGE_URL = "https://chiuchang.org/imc/en/%e6%ad%b7%e5%b1%86%e8%a9%a6%e9%a1%8c/"
HEADERS = {"User-Agent": "Mozilla/5.0"}
OUT_DIR = Path(__file__).parent

# One regex walks the page in order: <h2> year, <h3> keystage, <a> paper link.
TOKEN_RE = re.compile(
    r"<h2[^>]*>(?P<h2>.*?)</h2>"
    r"|<h3[^>]*>(?P<h3>.*?)</h3>"
    r'|<a\s[^>]*href="(?P<href>[^"]+\.pdf)"[^>]*>\s*(?P<label>Individual|Team|Answers?)',
    re.S | re.I,
)
TAG_RE = re.compile(r"<[^>]+>")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def keystage_of(heading: str):
    """IWYMIC = Keystage 3, EMIC (and its yearly variants) = Keystage 2."""
    if re.search(r"keystage\s*3|IWYMIC", heading, re.I):
        return "keystage3"
    if re.search(r"keystage\s*2|EMIC", heading, re.I):
        return "keystage2"
    return None


def parse_papers(html: str):
    """Yield (year, keystage, kind, url) for every paper link."""
    year = keystage = None
    for m in TOKEN_RE.finditer(html):
        if m.group("h2") is not None:
            found = re.search(r"\d{4}", TAG_RE.sub("", m.group("h2")))
            year, keystage = (found.group() if found else None), None
        elif m.group("h3") is not None:
            keystage = keystage_of(TAG_RE.sub("", m.group("h3")))
        elif year and keystage:
            kind = m.group("label").lower().rstrip("s")  # individual / team / answer
            yield year, keystage, kind, urljoin(PAGE_URL, m.group("href"))


def main():
    argparse.ArgumentParser(description=__doc__.splitlines()[0]).parse_args()

    html = fetch(PAGE_URL).decode("utf-8", errors="replace")
    wanted = {
        "individual": "{year}.pdf",
        "team": "{year}_team.pdf",
        "answer": "{year}_answer.pdf",
    }

    ok = skipped = failed = 0
    for year, keystage, kind, url in parse_papers(html):
        if kind not in wanted:
            continue
        dest = OUT_DIR / keystage / wanted[kind].format(year=year)
        if dest.exists():
            skipped += 1
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            dest.write_bytes(fetch(url))
            print(f"OK   {keystage}/{dest.name}  <- {url}")
            ok += 1
        except Exception as e:
            print(f"FAIL {keystage}/{dest.name}  <- {url}: {e}", file=sys.stderr)
            failed += 1

    print(f"Done: {ok} downloaded, {skipped} already existed, {failed} failed")


if __name__ == "__main__":
    main()
