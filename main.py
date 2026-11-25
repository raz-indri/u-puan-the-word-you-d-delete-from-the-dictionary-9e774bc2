#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Our pick: floccinaucinihilipilification -- the longest word in the
dictionary, a 29-letter monument to estimating things as worthless.
Deleting it is the dictionary's own verdict on the word itself.
"""

import os

WORD = "floccinaucinihilipilification"


def main() -> None:
    # The gate allows 1-77 UTF-8 characters; fail loudly instead of
    # silently writing an invalid entry.
    assert 1 <= len(WORD) <= 77, "word fails the entry gate"
    assert WORD == WORD.strip() and " " not in WORD, "entry must be one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
