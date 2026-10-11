"""Build the study mind maps: keystage2_mindmap.html, keystage3_mindmap.html (IMC) and
imso_mindmap.html (IMSO).

Usage:  python tools/build.py
Inputs: the problems files (via categorize.load / categorize_imso.load), leaves_*.py, template.html
Also rewrites keystage{2,3}_categories.txt and imso_categories.txt.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import categorize  # noqa: E402
import categorize_imso  # noqa: E402
import leaves_imso  # noqa: E402
import leaves_ks2  # noqa: E402
import leaves_ks3  # noqa: E402

IMC_HOME = dict(home="ximc.html", home_label="Ôn luyện IMC")
PAGES = {
    "ks2": dict(src=categorize, stage="ks2", leaves=leaves_ks2, out="keystage2_mindmap.html",
                title="Bản đồ ôn IMC KS2", h1="Bản đồ ôn IMC Key Stage 2", root="IMC KS2",
                ls_key="imc-ks2-map", doc="ks2map", **IMC_HOME),
    "ks3": dict(src=categorize, stage="ks3", leaves=leaves_ks3, out="keystage3_mindmap.html",
                title="Bản đồ ôn IMC KS3", h1="Bản đồ ôn IMC Key Stage 3", root="IMC KS3",
                ls_key="imc-ks3-map", doc="ks3map", **IMC_HOME),
    "imso": dict(src=categorize_imso, stage="imso", leaves=leaves_imso, out="imso_mindmap.html",
                 title="Bản đồ ôn IMSO", h1="Bản đồ ôn IMSO Toán", root="IMSO",
                 ls_key="imso-map", doc="imsomap", home="imso.html", home_label="Ôn luyện IMSO"),
}

HEAD = ('<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>*,*::before,*::after{box-sizing:border-box}html{padding-top:env(safe-area-inset-top,0px);'
        'padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style>\n'
        '</head>\n<body>\n')


def build(name):
    cfg = PAGES[name]
    src, lv = cfg["src"], cfg["leaves"]
    probs, assign, tax = src.load(cfg["stage"])
    by_sub = {}
    for p in probs:
        by_sub.setdefault(assign[p["id"]], []).append(p["id"])

    problems = []
    groups = []
    for g in tax["groups"]:
        subs = []
        for s in (k for k in tax["subs"] if k.startswith(f"{g}.")):
            leaves = []
            for j, (title, sign, key, ex) in enumerate(lv.L.get(s, [])):
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

    data = dict(groups=groups, kinds=src.KINDS,
                probs={p["id"]: dict(t=p["text"], k=p["kind"], kn=p["kind_name"], y=p["year"], p=p["page"],
                                     f=p["file"], fl=p["file_label"], a=p["answer"], al=p["answer_label"])
                       for p in probs})
    years = sorted({p["year"] for p in probs})
    lower = getattr(src, "LOWER_KIND_NAMES", True)  # "345 cá nhân" but "485 Short Answer"
    counts = " · ".join(f"{sum(p['kind'] == k for p in probs)} {n.lower() if lower else n}" for k, n in src.KINDS
                        if any(p["kind"] == k for p in probs))
    sub = f"{len(probs)} bài ({counts}) · {years[0]}–{years[-1]}"

    html = (HERE / "template.html").read_text(encoding="utf-8")
    for k, v in {"__TITLE__": cfg["title"], "__H1__": cfg["h1"], "__SUB__": sub, "__ROOT__": cfg["root"],
                 "__KEY__": cfg["ls_key"], "__DOC__": cfg["doc"], "__HOME__": cfg["home"],
                 "__HOME_LABEL__": cfg["home_label"]}.items():
        html = html.replace(k, v)
    html = html.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    left = re.findall(r"__[A-Z_]+__", html.split("const DATA")[0])
    if left:
        raise SystemExit(f"unfilled placeholders: {left}")
    # The template is body content (the claude.ai artifact viewer adds its own skeleton);
    # a standalone page needs the document head, or browsers guess the wrong charset.
    out = categorize.ROOT / cfg["out"]
    out.write_text(HEAD + html + "\n</body>\n</html>\n", encoding="utf-8")
    n_leaves = sum(len(s["leaves"]) for g in groups for s in g["subs"])
    print(f"{out.name}: {len(probs)} problems, {n_leaves} leaves")


if __name__ == "__main__":
    for name, cfg in PAGES.items():
        cfg["src"].write_categories(cfg["stage"])
        build(name)
