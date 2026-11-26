"""One Word for the Boss — make.fun entry.

Writes the winning word to /output/entry.txt.
Pure standard library, no network, no secrets.
"""

import os

WORD = "Delegator"


def _check(word):
    """Enforce the gate before writing: 1-30 chars, exactly one word."""
    if not 1 <= len(word) <= 30:
        raise ValueError("word must be 1-30 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not word.strip():
        raise ValueError("entry must not be only white space")


def main():
    _check(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    with open(path, encoding="utf-8") as f:
        _check(f.read())


if __name__ == "__main__":
    main()
