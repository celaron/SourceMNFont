import fontTools.misc.filesystem as fs
import ufoLib2
from afdko.makeotf import main as makeotf
from ufo2ft import compileOTF

for font_name in ["chiron", "source"]:
    makeotf(
        [
            "-f",
            f"downloads/{font_name}-EL.ps",
            "-ch",
            f"downloads/{font_name}-cmap",
            "-o",
            f"downloads/{font_name}.otf",
        ]
    )

all_trad = fs.zipfs.ZipFS("downloads/alltrad.zip")
for wght in [0, 1000]:
    name, short_name = {
        0: ("ExtraLight", "EL"),
        1000: ("Heavy", "H"),
    }[wght]
    ufo = ufoLib2.Font.open(
        all_trad.opendir(
            f"SHS-UFO-Edits-main/Sources/All-Traditional/Sans/WIPSHDC-All-Traditional-Sans-{name}.ufo"
        )
    )
    otf = compileOTF(ufo)
    otf.save(f"downloads/alltrad-{short_name}.otf")
