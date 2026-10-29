"""Build the study mind maps: mindmaps/keystage2.html, mindmaps/keystage3.html (IMC),
mindmaps/imso.html (IMSO), mindmaps/imas_{middle,upper,junior}.html (IMAS), mindmaps/igo.html (IGO),
mindmaps/ico.html (ICO) and mindmaps/rmo.html (RMO).

Usage:  python scripts/build_mindmaps.py
Inputs: the problems files (via the load() of categorize, categorize_imso, categorize_imas, categorize_igo,
        categorize_ico, categorize_rmo),
        leaves_*.py, mindmap_template.html
Also rewrites data/keystage{2,3}_categories.txt, data/imso_categories.txt,
data/imas_{middle,upper,junior}_categories.txt, data/igo_categories.txt, data/ico_categories.txt and
data/rmo_categories.txt.
"""
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import categorize  # noqa: E402
import categorize_ico  # noqa: E402
import categorize_igo  # noqa: E402
import categorize_imas  # noqa: E402
import categorize_imso  # noqa: E402
import categorize_rmo  # noqa: E402
import leaves_ico  # noqa: E402
import leaves_igo  # noqa: E402
import leaves_imas_junior  # noqa: E402
import leaves_imas_middle  # noqa: E402
import leaves_imas_upper  # noqa: E402
import leaves_imso  # noqa: E402
import leaves_ks2  # noqa: E402
import leaves_ks3  # noqa: E402
import leaves_rmo  # noqa: E402
from paths import MINDMAPS, ROOT  # noqa: E402

IMC_HOME = dict(home="ximc.html", home_label="Ôn luyện IMC")
IMAS_HOME = dict(src=categorize_imas, home="imas.html", home_label="Ôn luyện IMAS")
PAGES = {
    "ks2": dict(src=categorize, stage="ks2", leaves=leaves_ks2, out="keystage2.html",
                title="Bản đồ ôn IMC KS2", h1="Bản đồ ôn IMC Key Stage 2", root="IMC KS2",
                ls_key="imc-ks2-map", doc="ks2map", **IMC_HOME),
    "ks3": dict(src=categorize, stage="ks3", leaves=leaves_ks3, out="keystage3.html",
                title="Bản đồ ôn IMC KS3", h1="Bản đồ ôn IMC Key Stage 3", root="IMC KS3",
                ls_key="imc-ks3-map", doc="ks3map", **IMC_HOME),
    "imso": dict(src=categorize_imso, stage="imso", leaves=leaves_imso, out="imso.html",
                 title="Bản đồ ôn IMSO", h1="Bản đồ ôn IMSO Toán", root="IMSO",
                 ls_key="imso-map", doc="imsomap", home="imso.html", home_label="Ôn luyện IMSO"),
    "imas_middle": dict(stage="middle", leaves=leaves_imas_middle, out="imas_middle.html",
                        title="Bản đồ ôn IMAS Middle Primary", h1="Bản đồ ôn IMAS Middle Primary",
                        root="IMAS MP", ls_key="imas-mp-map", doc="imasmpmap", **IMAS_HOME),
    "imas_upper": dict(stage="upper", leaves=leaves_imas_upper, out="imas_upper.html",
                       title="Bản đồ ôn IMAS Upper Primary", h1="Bản đồ ôn IMAS Upper Primary",
                       root="IMAS UP", ls_key="imas-up-map", doc="imasupmap", **IMAS_HOME),
    "imas_junior": dict(stage="junior", leaves=leaves_imas_junior, out="imas_junior.html",
                        title="Bản đồ ôn IMAS Junior", h1="Bản đồ ôn IMAS Junior",
                        root="IMAS Junior", ls_key="imas-jr-map", doc="imasjrmap", **IMAS_HOME),
    "igo": dict(src=categorize_igo, stage="igo", leaves=leaves_igo, out="igo.html",
                title="Bản đồ ôn IGO", h1="Bản đồ ôn Olympic Hình học Iran", root="IGO",
                ls_key="igo-map", doc="igomap", home="igo.html", home_label="Ôn luyện IGO"),
    "ico": dict(src=categorize_ico, stage="ico", leaves=leaves_ico, out="ico.html",
                title="Bản đồ ôn ICO", h1="Bản đồ ôn Olympic Tổ hợp Iran", root="ICO",
                ls_key="ico-map", doc="icomap", home="ico.html", home_label="Ôn luyện ICO"),
    "rmo": dict(src=categorize_rmo, stage="rmo", leaves=leaves_rmo, out="rmo.html",
                title="Bản đồ ôn RMO", h1="Bản đồ ôn Raffles Mathematical Olympiad", root="RMO",
                ls_key="rmo-map", doc="rmomap", home="rmo.html", home_label="Ôn luyện RMO"),
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

    # Paths are relative to the repo root; the page lives in mindmaps/, so link from there.
    rel = lambda path: path and Path(os.path.relpath(ROOT / path, MINDMAPS)).as_posix()
    data = dict(groups=groups, kinds=src.KINDS,
                probs={p["id"]: dict(t=p["text"], k=p["kind"], kn=p["kind_name"], y=p["year"], p=p["page"],
                                     f=rel(p["file"]), fl=p["file_label"], a=rel(p["answer"]),
                                     al=p["answer_label"])
                       for p in probs})
    years = sorted({p["year"] for p in probs})
    lower = getattr(src, "LOWER_KIND_NAMES", True)  # "345 cá nhân" but "485 Short Answer"
    counts = " · ".join(f"{sum(p['kind'] == k for p in probs)} {n.lower() if lower else n}" for k, n in src.KINDS
                        if any(p["kind"] == k for p in probs))
    sub = f"{len(probs)} bài ({counts}) · {years[0]}–{years[-1]}"

    html = (HERE / "mindmap_template.html").read_text(encoding="utf-8")
    for k, v in {"__TITLE__": cfg["title"], "__H1__": cfg["h1"], "__SUB__": sub, "__ROOT__": cfg["root"],
                 "__KEY__": cfg["ls_key"], "__DOC__": cfg["doc"], "__HOME__": rel(cfg["home"]),
                 "__HOME_LABEL__": cfg["home_label"], "__NGROUPS__": str(len(tax["groups"])),
                 "__NSUBS__": str(len(tax["subs"]))}.items():
        html = html.replace(k, v)
    html = html.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    left = re.findall(r"__[A-Z_]+__", html.split("const DATA")[0])
    if left:
        raise SystemExit(f"unfilled placeholders: {left}")
    # The template is body content (the claude.ai artifact viewer adds its own skeleton);
    # a standalone page needs the document head, or browsers guess the wrong charset.
    out = MINDMAPS / cfg["out"]
    out.write_text(HEAD + html + "\n</body>\n</html>\n", encoding="utf-8")
    n_leaves = sum(len(s["leaves"]) for g in groups for s in g["subs"])
    print(f"{out.name}: {len(probs)} problems, {n_leaves} leaves")


if __name__ == "__main__":
    for name, cfg in PAGES.items():
        cfg["src"].write_categories(cfg["stage"])
        build(name)
