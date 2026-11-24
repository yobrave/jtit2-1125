"""jtit2-1125: weirdest job title; gate 60 chars."""

import json
import os
import pathlib
import sys

PLATE = 60


def punch_badge():
    lobby = pathlib.Path(__file__).resolve().parent
    card = (lobby / "entry.txt").read_text(encoding="utf-8")
    return lobby, [t for t in (line.strip() for line in card.splitlines()) if t]


def stamp(line):
    if not line:
        sys.exit("badge error: blank card")
    if len(line) > PLATE:
        sys.exit("badge error: %d chars wider than plate %d" % (len(line), PLATE))
    return line


def mount(lobby, line):
    wall = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or lobby)
    wall.mkdir(parents=True, exist_ok=True)
    plate = wall / "entry.txt"
    plate.write_text(line + "\n", encoding="utf-8", newline="\n")
    return plate


lobby, cards = punch_badge()
line = stamp(cards[0] if cards else "")
plate = mount(lobby, line)
print(json.dumps({"plate": plate.as_posix(), "chars": len(line), "oversize": len(line) > PLATE, "title": "job", "stamped": True}))
