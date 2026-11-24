"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt (the grader's
output path) and prints it. The sentence is a single roast of
lawmakers who would regulate AI, crypto or the internet but cannot
convert a file to PDF.
"""

import os
import re
import sys

SENTENCE = (
    "They will happily write the rules for the entire internet, then "
    "email their staff a Word document asking, in all caps, "
    "HOW DO I MAKE THIS A PDF."
)


def check_gate(sentence):
    """Self-check the competition gate: 1-320 chars, one sentence."""
    if not sentence or sentence.isspace():
        return False, "empty entry"
    if len(sentence) > 320:
        return False, "over 320 characters"
    # Exactly one sentence: a single terminal stop, at the very end.
    if len(re.findall(r"[.!?]", sentence)) != 1 or not sentence.endswith("."):
        return False, "not a single sentence"
    return True, "ok"


def main():
    sentence = SENTENCE.strip()
    ok, reason = check_gate(sentence)
    if not ok:
        print(f"gate check failed: {reason}", file=sys.stderr)
        return 1
    print(sentence)
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(sentence)
    # Also keep a copy beside this program so the entry is visible in-repo.
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"),
              "w", encoding="utf-8") as f:
        f.write(sentence)
    return 0


if __name__ == "__main__":
    sys.exit(main())
