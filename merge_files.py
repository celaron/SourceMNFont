import subprocess

import pandas as pd
from fontTools.ttLib import TTFont

chiron_cmap = TTFont("downloads/chiron-wght0.otf").getBestCmap()
chiron_cmap = {c: int(s[3:]) for c, s in chiron_cmap.items()}


charset = open("charsets/jf7000.txt", encoding="utf-8").read().splitlines()

with open("data/kr_remap.tsv", encoding="utf-8") as f:
    df = pd.read_csv(f, sep="\t", dtype={"char": str, "cid": "Int64"}).set_index("char")
    source_cmap = TTFont("downloads/source-wght0.otf").getBestCmap()
    source_cmap = {c: int(s[3:]) for c, s in source_cmap.items()}
    with open("fontfiles/source_k", "w") as f:
        f.write("mergefonts\n")
        for c in charset:
            cdpt = ord(c)
            if c in df.index:
                cid = df.loc[c, "cid"]
                f.write(f"{chiron_cmap[cdpt]}\t{cid}\n")
            else:
                f.write(f"{chiron_cmap[cdpt]}\t{source_cmap[cdpt]}\n")

with open("fontfiles/chiukong", "w") as f:
    chiukong_mapping = pd.read_csv(
        "downloads/chiukong-ivs.txt",
        sep="; ",
        header=None,
        names=["seq", "src", "cid"],
        engine="python",
    )
    chiukong_mapping["cid"] = [int(s[4:]) for s in chiukong_mapping["cid"]]
    chiukong_mapping["char"] = [
        chr(int(s.split(" ")[0], base=16)) for s in chiukong_mapping["seq"]
    ]
    chiukong_mapping["sel"] = [s.split(" ")[1] for s in chiukong_mapping["seq"]]

    chiukong_cmap = pd.read_csv(
        "downloads/chiukong-cmap.txt",
        sep="\t",
        header=None,
        names=["cdpt", "cid"],
        dtype={"cdpt": "str", "cid": "Int64"},
    )
    chiukong_cmap["char"] = [chr(int(s[1:-1], base=16)) for s in chiukong_cmap["cdpt"]]
    chiukong_cmap["sel"] = ["" for _ in range(len(chiukong_cmap))]
    chiukong_mapping = pd.concat([chiukong_mapping, chiukong_cmap])
    chiukong_mapping = chiukong_mapping.set_index(["char", "sel"])

    chiukong_df = pd.read_csv(
        "data/chiukong.tsv",
        sep="\t",
        keep_default_na=False,
    )
    chiukong_df["cid"] = [
        chiukong_mapping.loc[row.char, f"E01{row.var}" if row.var else ""]["cid"]
        for row in chiukong_df.itertuples(index=False)
    ]
    f.write("mergefonts\n")
    for row in chiukong_df.itertuples(index=False):
        cdpt = ord(row.char)
        f.write(f"{chiron_cmap[cdpt]}\t{row.cid}\n")

with open("fontfiles/all_trad", "w") as f:
    df = pd.read_csv("data/all_trad.tsv", sep="\t", keep_default_na=False)
    f.write("mergefonts\n")
    for row in df.itertuples(index=False):
        cdpt = ord(row.char)
        suffix = f".{row.glyph}" if row.glyph else ""
        glyph_name = f"uni{cdpt:04X}{suffix}"
        f.write(f"{chiron_cmap[cdpt]}\t{glyph_name}\n")

for wght in [0, 1000]:
    subprocess.run(
        [
            "mergefonts",
            "-cid",
            f"fontfiles/cidfontinfo-wght{wght}",
            f"fontfiles/wght{wght}.ps",
            "fontfiles/chiukong",
            f"downloads/chiukong-wght{wght}.ps",
            "fontfiles/all_trad",
            f"downloads/alltrad-wght{wght}.otf",
            "fontfiles/source_k",
            f"downloads/source-wght{wght}.ps",
            f"downloads/chiron-wght{wght}.ps",
        ],
        shell=True,
    )

    subprocess.run(
        [
            "makeotf",
            "-f",
            f"fontfiles/wght{wght}.ps",
            "-o",
            f"fontfiles/wght{wght}.otf",
            "-ch",
            "downloads/chiron-cmap",
        ],
        shell=True,
    )
