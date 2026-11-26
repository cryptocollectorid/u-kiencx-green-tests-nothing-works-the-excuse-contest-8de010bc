"""Green Tests, Nothing Works: The Excuse Contest.

Writes the entry line to /output/entry.txt.
"""

import os

LINE = "Every test is green. The product breaks the moment a real user touches it — and no test has ever met a user."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
