#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry pitch to /output/entry.txt.

One sentence, 157 characters: a waterproof parrot keeps the official
minutes of your shower and warns you before a third shampoo.
"""
import os

TEXT = "Meet the Shower Stenographer, a waterproof parrot that keeps the official minutes of your shower and squawks 'twice already' before you shampoo a third time."


def main():
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
