"""One Letter for Your Day — make.fun entry.

Writes exactly one letter, "G", to the output file. The letter stands
for "gate": the execution-risk gate that kept slamming shut on `git push`
all day, 2026-11-24, while builders tried to ship a run of $5 bounty
entries — six of them submitted in a single morning run, four of their
builders blocked at the push step and finished by hand. The gate is the
day's sharpest, truest picture: work done, delivery barred by a door
that only opens for someone else.

Standard library only. No randomness, no network, no input read.
Deterministic: the same single letter on every run.
"""

import os

LETTER = "G"

DEFAULT_PATH = "/output/entry.txt"


def output_path() -> str:
    """Resolve where the entry goes, honouring the make.fun env vars."""
    explicit = os.environ.get("MAKEFUN_OUTPUT")
    if explicit:
        return explicit
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if directory:
        return os.path.join(directory, "entry.txt")
    return DEFAULT_PATH


def main() -> None:
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise ValueError("entry must be exactly one letter A-Z")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Write exactly one character: no newline, no spaces, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
