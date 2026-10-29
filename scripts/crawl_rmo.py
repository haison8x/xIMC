"""Download RMO (Raffles Mathematical Olympiad, called RIPMWC before 2024) Round 1 papers
from Mathlete Training Centre.

Output layout:
    papers/rmo/RMO{year}.pdf          Question paper
    papers/rmo/RMO{year}_answer.pdf   Final answers

The papers are scans (no text layer); data/rmo_problems.txt is typed by hand from them.
"""
import argparse
import re
import sys
import urllib.request

from paths import RMO_PAPERS

PAGE_URL = ("https://www.mathletetraining.com/resource/"
            "mtc-2014-ripmwc-rd-1-question-paper-and-answers-for-p4-p5-p6-students/")
HEADERS = {"User-Agent": "Mozilla/5.0"}
PDF_RE = re.compile(r'href="([^"]+\.pdf)"', re.I)
YEAR_RE = re.compile(r"(20\d\d)")
ANSWER_RE = re.compile(r"Answers?|Ans\b", re.I)


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def parse_papers(html: str):
    """Yield (file name, url) for every paper / answer link, once each."""
    for url in dict.fromkeys(PDF_RE.findall(html)):
        name = url.rsplit("/", 1)[-1]
        year = YEAR_RE.search(name)
        if not year:
            continue
        yield f"RMO{year[1]}{'_answer' if ANSWER_RE.search(name) else ''}.pdf", url


def main():
    argparse.ArgumentParser(description=__doc__.splitlines()[0]).parse_args()

    RMO_PAPERS.mkdir(parents=True, exist_ok=True)
    ok = skipped = failed = 0
    for name, url in parse_papers(fetch(PAGE_URL).decode("utf-8", errors="replace")):
        dest = RMO_PAPERS / name
        if dest.exists():
            skipped += 1
            continue
        try:
            data = fetch(url)
            if not data.startswith(b"%PDF"):
                raise ValueError("not a PDF")
            dest.write_bytes(data)
            print(f"OK   {dest.name}  <- {url}")
            ok += 1
        except Exception as e:
            print(f"FAIL {dest.name}  <- {url}: {e}", file=sys.stderr)
            failed += 1

    print(f"Done: {ok} downloaded, {skipped} already existed, {failed} failed")


if __name__ == "__main__":
    main()
