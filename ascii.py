#!/usr/bin/env python

names = {
    0: ("NUL", "null"),
    1: ("SOH", "start of heading"),
    2: ("STX", "start of text"),
    3: ("ETX", "end of text"),
    4: ("EOT", "end of transmission"),
    5: ("ENQ", "enquiry"),
    6: ("ACK", "acknowledge"),
    7: ("BEL", "bell"),
    8: ("BS", "backspace"),
    9: ("TAB", "horizontal tab"),
    10: ("LF", "line feed"),
    11: ("VT", "vertical tab"),
    12: ("FF", "form feed"),
    13: ("CR", "carriage return"),
    14: ("SO", "shift out"),
    15: ("SI", "shift in"),
    16: ("DLE", "data link escape"),
    17: ("DC1", "device control 1"),
    18: ("DC2", "device control 2"),
    19: ("DC3", "device control 3"),
    20: ("DC4", "device control 4"),
    21: ("NAK", "negative acknowledge"),
    22: ("SYN", "synchronous idle"),
    23: ("ETB", "end of transmission block"),
    24: ("CAN", "cancel"),
    25: ("EM", "end of medium"),
    26: ("SUB", "substitute"),
    27: ("ESC", "escape"),
    28: ("FS", "file separator"),
    29: ("GS", "group separator"),
    30: ("RS", "record separator"),
    31: ("US", "unit separator"),
    31: ("SP", "space"),
    127: ("DEL", "delete"),
}

print(
    """<!doctype HTML>
<html>
<head>
  <title>ASCII Table</title>
  <style type="text/css">
:root { --double: 3px double black; }
body { font-family: monospace; }
table { border-collapse: collapse; }
table :is(th, td) {
  border: 1px solid grey;
}
table :is(th, td):nth-child(3n) {
  border-right: var(--double);
}
table :is(thead, tbody) {
  border: var(--double);
}
th { font-size: 80%; }
td { padding: 0.2em 1ch; }
td[^class] { width: 5ch; text-align: right; }
td.named { color: orange; width: 6ch; }
td.lit { color: blue; }
  </style>
</head>
<body>
<table>
  <thead><tr>"""
)
print("    <th>Dec</th><th>Hex</th><th></th>\n" * 4, end="")
print(
    """</tr></thead>
  <tbody>"""
)
for r in range(0, 32):
    print("    <tr>")
    for c in range(0, 4):
        v = c * 32 + r
        if v in names:
            cls = "named"
            s = names[v][0]
            tip = f' title="{names[v][1]}"'
        else:
            cls = "lit"
            s = str(bytes([v]), encoding="utf-8")
            tip = ""
            assert s.isprintable()
        print(f"      <td>{v}</td><td>0x{v:0>2x}</td>", end="")
        print(f'<td class="{cls}"{tip}>{s}</td>')

    print("    </tr>")

print(
    """  </tbody>
</table>
</body>
</html>"""
)
