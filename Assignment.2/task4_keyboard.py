from typing import Iterable, Union
import re
import sys

Number = Union[int, float]


def sum_of_squares(numbers: Iterable[Number]) -> Number:
    """Return the sum of squares of the given iterable of numbers.

    Args:
        numbers: An iterable of ints or floats.

    Returns:
        The sum of each value squared. Returns 0 for empty input.

    Raises:
        TypeError: If any element in `numbers` is not int/float.
    """
    total: Number = 0
    for i, x in enumerate(numbers):
        if not isinstance(x, (int, float)):
            raise TypeError(f"Element at index {i} is not a number: {x!r}")
        total += x * x
    return total


def parse_numbers(text: str) -> list[Number]:
    """Parse a string containing numbers separated by spaces or commas.

    Accepts ints and floats. Raises ValueError on invalid tokens.
    """
    tokens = re.split(r"[,\s]+", text.strip())
    nums: list[Number] = []
    for t in tokens:
        if not t:
            continue
        try:
            # try integer parse first, otherwise float
            if re.fullmatch(r"[+-]?\d+", t):
                val: Number = int(t)
            else:
                val = float(t)
        except ValueError:
            raise ValueError(f"Could not parse token {t!r} as a number")
        nums.append(val)
    return nums


if __name__ == "__main__":
    # If stdin is a pipe (not a TTY) read everything; otherwise prompt the user.
    prompt = "Enter numbers separated by space or comma: "
    if not sys.stdin.isatty():
        # piped input: read all lines and join
        line = sys.stdin.read()
    else:
        try:
            line = input(prompt)
        except EOFError:
            line = ""

    line = (line or "").strip()
    if not line:
        print("No numbers provided. sum -> 0")
        sys.exit(0)

    try:
        numbers = parse_numbers(line)
    except ValueError as exc:
        print(f"Error parsing numbers: {exc}")
        sys.exit(1)

    try:
        result = sum_of_squares(numbers)
    except TypeError as exc:
        print(f"Error computing sum of squares: {exc}")
        sys.exit(1)

    print(result)
