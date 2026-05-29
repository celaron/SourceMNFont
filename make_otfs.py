from afdko.makeotf import main as makeotf
import zipfile

for font_name in ["chiron", "source"]:
    makeotf(
        [
            "-f",
            f"downloads/{font_name}-wght0.ps",
            "-ch",
            f"downloads/{font_name}-cmap",
            "-o",
            f"downloads/{font_name}-wght0.otf",
        ]
    )

with zipfile.ZipFile("downloads/alltrad.zip", "r") as all_trad:
    all_trad.extractall("downloads/alltrad")

for wght in [0, 1000]:
    name = "ExtraLight" if wght == 0 else "Heavy"
    makeotf(
        [
            "-f",
            f"downloads/alltrad/SHS-UFO-Edits-main/Sources/All-Traditional/Sans/WIPSHDC-All-Traditional-Sans-{name}.ufo",
            "-o",
            f"downloads/alltrad-wght{wght}.otf",
        ]
    )

# for font_name in ["Chiron", "SourceK"]:
#     for wght in [0]:
#         makeotf(
#             [
#                 "-f",
#                 f"{font_name}/wght{wght}.ps",
#                 "-ch",
#                 f"{font_name}/cmap",
#                 "-o",
#                 f"{font_name}/wght{wght}.otf",
#             ]
#         )

# with zipfile.ZipFile("AllTrad/main.zip", "r") as all_trad:
#     all_trad.extractall("AllTrad/main")

# for wght in [0, 1000]:
#     name = "ExtraLight" if wght == 0 else "Heavy"
#     makeotf(
#         [
#             "-f",
#             f"AllTrad/main/SHS-UFO-Edits-main/Sources/All-Traditional/Sans/WIPSHDC-All-Traditional-Sans-{name}.ufo",
#             "-o",
#             f"AllTrad/wght{wght}.otf",
#         ]
#     )
