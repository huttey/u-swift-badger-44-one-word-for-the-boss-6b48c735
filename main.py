"""One Word for the Boss — make.fun entry.

Writes the winning word to /output/entry.txt.
Pure standard library, no network, no secrets.
"""

import os

# "Delegator": one-word boss label, specific not generic. The boss whose
# whole job is handing work down — every task, decision and meeting passed
# along until nothing is left but the passing along. It lands on its own:
# funny because it rings true, fresh (not "bossy" or "lazy"), and it
# travels — a delegator exists in every kitchen, warehouse and office.
WORD = "Delegator"


def _check(word):
    """Enforce the gate before writing: 1-30 chars, exactly one word.

    Each rule fails loudly with its own message so a bad word can never
    slip through silently: the gate refuses anything over 30 chars,
    anything with a space in it, or whitespace-only text.
    """
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not 1 <= len(word) <= 30:
        raise ValueError(f"word must be 1-30 characters, got {len(word)}")
    if word != word.strip():
        raise ValueError("entry must not start or end with white space")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must contain no white space at all")
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
        data = f.read()
    _check(data)
    if data != WORD:
        raise ValueError("written entry does not match the word exactly")


if __name__ == "__main__":
    main()
