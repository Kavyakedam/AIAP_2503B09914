"""
sum_even_odd.py

Provides a small utility to compute the sum of even numbers and the sum of odd numbers
from a list (or any iterable) of numeric-like values.

Function:
- sum_even_and_odd(numbers) -> (sum_even, sum_odd)

Example usage:
    python sum_even_odd.py

The script will also print a demonstration when run directly.
"""
from typing import Iterable, Tuple


def sum_even_and_odd(numbers: Iterable) -> Tuple[int, int]:
    """Calculate sums of even and odd integers from `numbers`.

    - Non-integer values are ignored (e.g., strings that can't convert to int).
    - Values that can be converted to int will be converted (e.g., 3.0 -> 3).

    Returns:
        (sum_even, sum_odd)
    """
    sum_even = 0
    sum_odd = 0

    for value in numbers:
        try:
            n = int(value)
        except (ValueError, TypeError):
            # ignore values that are not numeric-like
            continue

        if n % 2 == 0:
            sum_even += n
        else:
            sum_odd += n

    return sum_even, sum_odd


if __name__ == "__main__":
    # Example list and demonstration output
    example = [1, 2, 3, 4, 5, 6, "7", 8.0, "x", None]
    even_sum, odd_sum = sum_even_and_odd(example)
    print(f"Example list: {example}")
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")
