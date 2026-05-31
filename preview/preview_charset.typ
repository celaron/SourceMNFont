#set text(font: "Source MN", size: 11pt)
#set par(leading: 1em)

#let show_char(char) = {
  box()[
    #grid(
      columns: 1,
      align: center,
      inset: 0.5em,
      text(size: 3em, char),
      text(font: "DejaVu Sans Mono", upper(str(
        char.to-unicode(),
        base: 16,
      ))),
    )
  ]
}

#{
  let charset = read("../charsets/jf7000.txt").split("\r\n")
  grid(
    align: center + horizon,
    columns: 10 * (1fr,),
    rows: 100% / 10,
    ..charset.map(show_char)
  )
}
