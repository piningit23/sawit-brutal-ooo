#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes one brutally honest but still polite out-of-office auto-reply
to /output/entry.txt (1-200 characters, UTF-8, single sentence).

make.fun competition: u-po-pu-the-painfully-honest-out-of-office-63e7ca0b
"""

import os

TEXT = (
    "I'm away and honestly relieved; your email will be read in the order "
    "it least ruins my holiday, so thank you for writing as if a rested "
    "human will eventually care."
)


def main() -> None:
    # One sentence: admits the sender is relieved to be away (the private
    # truth) while thanking the reader and promising the email will be read
    # (the polite part a manager would let stand).
    assert 1 <= len(TEXT) <= 200, f"entry is {len(TEXT)} chars, must be 1-200"
    assert TEXT.strip(), "entry must not be whitespace only"
    assert TEXT.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
