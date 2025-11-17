from typing import Iterable, Union

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


if __name__ == "__main__":
    # simple manual demo
    demo = [1, 2, 3.0]
    print(f"sum_of_squares({demo}) -> {sum_of_squares(demo)}")
