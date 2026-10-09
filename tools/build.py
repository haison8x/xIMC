"""Build the two study mind maps (keystage2_mindmap.html, keystage3_mindmap.html).

Usage:  python tools/build.py
Inputs: the problems files (via categorize.load), leaves_ks{2,3}.py, template.html
Also rewrites keystage{2,3}_categories.txt.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import categorize  # noqa: E402
import leaves_ks2  # noqa: E402
import leaves_ks3  # noqa: E402

PAGES = {
    "ks2": dict(leaves=leaves_ks2, title="Bản đồ ôn IMC KS2", h1="Bản đồ ôn IMC Key Stage 2",
                root="IMC KS2", ls_key="imc-ks2-map", doc="ks2map"),
    "ks3": dict(leaves=leaves_ks3, title="Bản đồ ôn IMC KS3", h1="Bản đồ ôn IMC Key Stage 3",
                root="IMC KS3", ls_key="imc-ks3-map", doc="ks3map"),
}


def build(stage):
    cfg = PAGES[stage]
    lv = cfg["leaves"]
    probs, assign, tax = categorize.load(stage)
    by_sub = {}
    for p in probs:
        by_sub.setdefault(assign[p["id"]], []).append(p["id"])

    problems = []
    groups = []
    for g in tax["groups"]:
        subs = []
        for s in (k for k in tax["subs"] if k.startswith(f"{g}.")):
            leaves = []
            for j, (title, sign, key, ex) in enumerate(lv.L[s]):
                for e in ex:
                    if e not in assign:
                        problems.append(f"{s}: example {e} does not exist")
                    elif assign[e] != s:
                        problems.append(f"{s}: example {e} is classified as {assign[e]}")
                leaves.append(dict(id=f"{s}-{chr(97 + j)}", t=title, sign=sign, key=key, ex=ex))
            subs.append(dict(id=s, vn=lv.SUB_VN[s], leaves=leaves, probs=by_sub.get(s, [])))
        groups.append(dict(id=g, vn=lv.GROUP_VN[g][0], count=sum(len(x["probs"]) for x in subs), subs=subs))
    if problems:
        raise SystemExit("\n".join(problems))

    data = dict(groups=groups,
                probs={p["id"]: dict(t=p["text"], k=p["kind"], y=p["year"], p=p["page"]) for p in probs})
    n_t = sum(p["kind"] == "T" for p in probs)
    years = sorted({p["year"] for p in probs})
    sub = f"{len(probs)} bài ({len(probs) - n_t} cá nhân · {n_t} đồng đội) · {years[0]}–{years[-1]}"

    html = (HERE / "template.html").read_text(encoding="utf-8")
    for k, v in {"__TITLE__": cfg["title"], "__H1__": cfg["h1"], "__SUB__": sub, "__ROOT__": cfg["root"],
                 "__KEY__": cfg["ls_key"], "__DOC__": cfg["doc"], "__PDFDIR__": categorize.DIRS[stage]}.items():
        html = html.replace(k, v)
    html = html.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    left = re.findall(r"__[A-Z]+__", html.split("const DATA")[0])
    if left:
        raise SystemExit(f"unfilled placeholders: {left}")
    # The template is body content (the claude.ai artifact viewer adds its own skeleton);
    # a standalone page needs the document head, or browsers guess the wrong charset.
    html = ('<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<style>*,*::before,*::after{box-sizing:border-box}html{padding-top:env(safe-area-inset-top,0px);'
            'padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style>\n'
            '</head>\n<body>\n' + html + '\n</body>\n</html>\n')
    out = categorize.ROOT / f"{categorize.DIRS[stage]}_mindmap.html"
    out.write_text(html, encoding="utf-8")
    n_leaves = sum(len(s["leaves"]) for g in groups for s in g["subs"])
    print(f"{out.name}: {len(probs)} problems ({n_t} team), {n_leaves} leaves")


if __name__ == "__main__":
    for s in PAGES:
        categorize.write_categories(s)
        build(s)
