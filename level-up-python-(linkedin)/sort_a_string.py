import re


def sort_string(s: str) -> str:
    """Sort words case-insensitively while preserving their original casing.

    Example: "PYTHON excited" -> "excited PYTHON"
    """
    words = s.split()
    return " ".join(sorted(words, key=str.casefold))


def sort_string_natural(s: str) -> str:
    """Sort words naturally (case-insensitive) so numbers are ordered by value.

    Example: "a2 a10 a1 a11" -> "a1 a2 a10 a11"
    """

    def natural_key(token: str):
        parts = re.findall(r"\d+|\D+", token)
        return [int(p) if p.isdigit() else p.casefold() for p in parts]

    words = s.split()
    return " ".join(sorted(words, key=natural_key))


if __name__ == "__main__":
    # Case-insensitive sort (preserve original casing)
    print(sort_string("hello world"))  # hello world
    print(sort_string("PYTHON excited"))  # excited PYTHON
    print(sort_string("science DATA"))  # DATA science

    # Natural sort (numbers in words sorted by numeric value)
    print(sort_string_natural("a2 a10 a1 a11"))  # a1 a2 a10 a11
