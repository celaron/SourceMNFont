import os
from urllib.request import urlopen

for path in ["charsets", "decomp", "downloads"]:
    os.makedirs(path, exist_ok=True)

# jf7000 charset

with urlopen(
    "https://raw.githubusercontent.com/NightFurySL2001/CJK-character-count/refs/heads/master/cjk-tables/jf7000-core-han.txt"
) as response:
    with open("charsets/jf7000.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(response.read().decode("utf-8").splitlines()[8:]))

# Decomposition data

with urlopen(
    "https://raw.githubusercontent.com/ButTaiwan/hanseeker/main/source/data_nosupp.txt"
) as response:
    with open("decomp/decomp.txt", "w", encoding="utf-8") as f:
        f.write(response.read().decode("utf-8"))
with urlopen(
    "https://raw.githubusercontent.com/ButTaiwan/hanseeker/main/source/data_vt.txt"
) as response:
    with open("decomp/variants.txt", "w", encoding="utf-8") as f:
        f.write(response.read().decode("utf-8"))

# Chiron HK

with urlopen(
    "https://raw.githubusercontent.com/chiron-fonts/chiron-hei-hk/source/source/regular/common/cmap"
) as response:
    # with open("Chiron/cmap", "w") as f:
    with open("downloads/chiron-cmap", "w") as f:
        f.write(response.read().decode("utf-8"))
for wght in [0, 1000]:
    with urlopen(
        f"https://raw.githubusercontent.com/chiron-fonts/chiron-hei-hk/source/source/regular/vf/masters/padding0_weight{wght}/cidfont.ps"
    ) as response:
        # with open(f"Chiron/wght{wght}.ps", "wb") as f:
        with open(f"downloads/chiron-wght{wght}.ps", "wb") as f:
            f.write(response.read())

# Source Han Sans

with urlopen(
    f"https://raw.githubusercontent.com/adobe-fonts/source-han-sans/master/UniSourceHanSansKR-UTF32-H"
) as response:
    # with open("SourceK/cmap", "w") as f:
    with open("downloads/source-cmap", "w") as f:
        f.write(response.read().decode("utf-8"))
for name, wght in zip(["ExtraLight", "Heavy"], [0, 1000]):
    with urlopen(
        f"https://raw.githubusercontent.com/adobe-fonts/source-han-sans/master/Masters/{name}/OTC/VF/cidfont.VF.K.unhinted"
    ) as response:
        # with open(f"SourceK/wght{wght}.ps", "wb") as f:
        with open(f"downloads/source-wght{wght}.ps", "wb") as f:
            f.write(response.read())

# SHS UFO Edits

with urlopen(
    "https://codeload.github.com/CoolMarvel43/SHS-UFO-Edits/zip/refs/heads/main"
) as response:
    # with open("AllTrad/main.zip", "wb") as f:
    with open("downloads/alltrad.zip", "wb") as f:
        f.write(response.read())

# ChiuKong

with urlopen(
    "https://raw.githubusercontent.com/ChiuMing-Neko/ChiuKongGothic/fontview/data/ivs.txt"
) as response:
    # with open("ChiuKong/ivs.txt", "w") as f:
    with open("downloads/chiukong-ivs.txt", "w") as f:
        f.write(response.read().decode("utf-8"))
with urlopen(
    "https://raw.githubusercontent.com/ChiuMing-Neko/ChiuKongGothic/main/Other/final_m_map.txt"
) as response:
    # with open("ChiuKong/cmap_m.txt", "w") as f:
    with open("downloads/chiukong-cmap.txt", "w") as f:
        f.write(response.read().decode("utf-8"))

for name, wght in zip(["EL", "H"], [0, 1000]):
    with urlopen(
        f"https://raw.githubusercontent.com/ChiuMing-Neko/ChiuKongGothic/main/Other/new_glyphs_raw/CKFontVF.{name}.out"
    ) as response:
        # with open(f"ChiuKong/wght{wght}.ps", "wb") as f:
        with open(f"downloads/chiukong-wght{wght}.ps", "wb") as f:
            f.write(response.read())
