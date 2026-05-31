import subprocess
import textwrap

from fontTools.designspaceLib import (
    AxisDescriptor,
    DesignSpaceDocument,
    InstanceDescriptor,
    SourceDescriptor,
)

CONFIG = {
    "postName": "SourceMN",
    "familyName": "Source MN",
    "version": "0.001",
    "masters": [
        {"styleName": "ExtraLight", "weight": 0, "shortName": "EL"},
        {"styleName": "Heavy", "weight": 1000, "shortName": "H"},
    ],
    "instances": [
        {"styleName": "ExtraLight", "weight": 0},
        {"styleName": "Light", "weight": 160},
        {"styleName": "Normal", "weight": 320},
        {"styleName": "Regular", "weight": 390},
        {"styleName": "Medium", "weight": 560},
        {"styleName": "Bold", "weight": 780},
        {"styleName": "Heavy", "weight": 1000},
    ],
}
DESIGNSPACE_PATH = "fontfiles/font.designspace"

mapping = {
    250: 0,
    300: 160,
    350: 320,
    400: 390,
    500: 560,
    700: 780,
    900: 1000,
}


def write_fontinfo():
    for master in CONFIG["masters"]:
        with open(f"fontfiles/cidfontinfo-{master['shortName']}", "w") as f:
            f.write(textwrap.dedent(f"""\
                FontName     ({CONFIG['postName']}-{master['styleName']})
                FullName     ({CONFIG['familyName']} {master['styleName']})
                FamilyName   ({CONFIG['familyName']})
                Weight       ({master['styleName']})
                version      (0.001)
                Registry     (Adobe)
                Ordering     (Identity)
                Supplement   0
                AdobeCopyright  (Copyright 2014-2026 Adobe (http://www.adobe.com/).)
            """))


def write_name_db():
    with open("fontfiles/FontMenuNameDB", "w") as f:
        for master in CONFIG["masters"]:
            f.write(textwrap.dedent(f"""\
                [{CONFIG['postName']}-{master['styleName']}]
                    f={CONFIG['familyName']}
                    s={master['styleName']}
            """))


def write_designspace():
    doc = DesignSpaceDocument()
    doc.addAxis(
        AxisDescriptor(
            default=250,
            minimum=250,
            maximum=900,
            name="weight",
            tag="wght",
            map=list(mapping.items()),
        )
    )
    for master in CONFIG["masters"]:
        doc.addSource(
            SourceDescriptor(
                path=f".temp/{master['shortName']}.otf",
                familyName=CONFIG["familyName"],
                location={"weight": master["weight"]},
                copyInfo=True if master["weight"] == 0 else False,
            )
        )
    for instance in CONFIG["instances"]:
        doc.addInstance(
            InstanceDescriptor(
                location={"weight": instance["weight"]},
                familyName=CONFIG["familyName"],
                styleName=instance["styleName"],
                postScriptFontName=f"{CONFIG['postName']}-{instance['styleName']}",
            )
        )
    doc.write(DESIGNSPACE_PATH)


def build_masters():
    for master in CONFIG["masters"]:
        short_name = master["shortName"]
        subprocess.run(
            [
                "mergefonts",
                "-cid",
                f"fontfiles/cidfontinfo-{short_name}",
                f"fontfiles/{short_name}.ps",
                ".temp/chiukong",
                f"downloads/chiukong-{short_name}.ps",
                ".temp/all_trad",
                f"downloads/alltrad-{short_name}.otf",
                ".temp/source_k",
                f"downloads/source-{short_name}.ps",
                f"downloads/chiron-{short_name}.ps",
            ],
            shell=True,
        )
        subprocess.run(
            [
                "makeotf",
                "-nshw",
                "-f",
                f"fontfiles/{short_name}.ps",
                "-o",
                f".temp/{short_name}.otf",
                "-mf",
                "fontfiles/FontMenuNameDB",
                "-ch",
                "downloads/chiron-cmap",
                "-ff",
                "fontfiles/features.fea",
                "-nS",
            ],
            shell=True,
        )


def build_vf():
    subprocess.run(
        [
            "buildcff2vf",
            "-d",
            DESIGNSPACE_PATH,
            "-o",
            "var_otf/vf.otf",
            "-c",
        ]
    )


write_fontinfo()
write_name_db()
write_designspace()
build_masters()
build_vf()
