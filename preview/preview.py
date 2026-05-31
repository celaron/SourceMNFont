from itertools import batched
from textwrap import dedent

from decomp import lookup_chars

components = "眔糸丸艹𡈼厶小縣㡀爪朁八亠𠆢金宀食延"
completed = "母巳亡直爲為辛𤰇具羽弱旡率𦐇曼尔者韋舛夅象差免鬼善曾平半㒸酋开俞並虛兌龹兼文青牙欠冫攸非丰几儿㕣幾羊灰丩身耳𫡑勺卜才冉匕杀卑化叟益兹󰑴艮幺袁睘告周厭广於匸吳強老天丂䧹釆臥卧处查丑勻𦣞𧘇⺜垂畢那刃華辰畏臽耒幸󰓡囱囪禿术朮彔𠂢󰒠凡巩瓦負色亏彖冊夐敻彐蚩戎奐鹿卂永勇祭䍃將尃七入夕舛"
charset = open("charsets/jf7000.txt", encoding="utf-8").read().splitlines()

with open("preview/preview.typ", "w", encoding="utf-8") as f:
    f.write('#set text(font: "Source MN")\n\n')
    f.write(dedent("""\
        #let preview(char) = {
            box(align(center)[
                #text(size: 2em, char)\\
                #text(font: "DejaVu Sans Mono", upper(str(char.to-unicode(), base: 16)))
            ])
            h(1em)
        }\n\n"""))

    all_chars = sorted(
        [(comp, lookup_chars(comp, charset)) for comp in components],
        key=lambda x: len(x[1]),
    )

    for comp, chars in all_chars:
        for c in chars:
            f.write(f'#preview("{c}")\n')
        f.write("\n#v(1em)\n\n")

    f.write("#pagebreak()\n")
    f.write("= Completed\n")
    all_chars = sorted(
        [(comp, lookup_chars(comp, charset)) for comp in completed],
        key=lambda x: len(x[1]),
    )
    for comp, chars in all_chars:
        for c in chars:
            f.write(f'#preview("{c}")\n')
        f.write("\n#v(1em)\n\n")
