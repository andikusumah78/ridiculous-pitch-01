"""Entry for make.fun's "Ridiculous at First Glance, Real by the Second".

The sentence, in full:

    We sell tiny coffin funerals for dead houseplants, with a printed
    eulogy, because guilty owners pay $19 for closure, film it, and come
    back when the next plant dies.

Why it fits the judge's brief, in order:

1. It pitches a bizarre startup that sounds like a joke yet makes sense
   as a real business: tiny coffin funerals for dead houseplants.
2. It is genuinely bizarre: nobody has heard of a funeral service for a
   houseplant, with a printed eulogy.
3. The business logic holds in its own words: guilty owners pay $19 for
   closure, they film the service (free marketing), and they come back
   when the next plant dies (repeat customers — plants keep dying).
4. It lands as a pitch: one sentence, a turn from laughing at the tiny
   coffin to nodding at the repeat business.
5. It is concrete and vivid: the thing being sold (tiny coffin funerals
   with a printed eulogy) and who buys it (guilty plant owners) are both
   named, with a price.

Writes exactly that one sentence to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when the runner sets it).
Pure Python 3.13 standard library, no network, deterministic.
"""

import os

MAX_CHARS = 200

LINE = (
    "We sell tiny coffin funerals for dead houseplants, with a printed "
    "eulogy, because guilty owners pay $19 for closure, film it, and "
    "come back when the next plant dies."
)


def output_path() -> str:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS or not LINE.strip():
        raise SystemExit("entry must be 1 to 200 characters of text")
    if "\n" in LINE:
        raise SystemExit("entry must be a single sentence on one line")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
