import os
import zipfile

from afdko.makeotf import main as makeotf

for font_name in ["chiron", "source"]:
    makeotf(
        [
            "-f",
            f"downloads/{font_name}-EL.ps",
            "-ch",
            f"downloads/{font_name}-cmap",
            "-o",
            f"downloads/{font_name}.otf",
            "-nS",
        ]
    )

with zipfile.ZipFile("downloads/alltrad.zip", "r") as all_trad:
    prefix = "SHS-UFO-Edits-main/Sources/All-Traditional/Sans/"
    for file in all_trad.namelist():
        if file.startswith(prefix):
            path = f"downloads/alltrad/{file.removeprefix(prefix)}"
            if path.endswith("/"):
                os.makedirs(path, exist_ok=True)
            else:
                with open(path, "wb") as f:
                    f.write(all_trad.read(file))


for name, short_name in zip(["ExtraLight", "Heavy"], ["EL", "H"]):
    makeotf(
        [
            "-f",
            f"downloads/alltrad/WIPSHDC-All-Traditional-Sans-{name}.ufo",
            "-o",
            f"downloads/alltrad-{short_name}.otf",
            "-nS",
        ]
    )
