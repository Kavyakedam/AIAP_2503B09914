import pytest

from task4 import sum_of_squares


def test_sum_of_squares_ints():
    assert sum_of_squares([1, 2, 3]) == 1 + 4 + 9


def test_sum_of_squares_floats():
    assert sum_of_squares([1.5, 2.0]) == pytest.approx(1.5 * 1.5 + 4.0)


def test_sum_of_squares_empty():
    assert sum_of_squares([]) == 0


def test_sum_of_squares_type_error():
    with pytest.raises(TypeError):
        sum_of_squares([1, 'a', 3])
