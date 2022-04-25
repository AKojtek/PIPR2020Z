from zadanie1 import find_largest_subarray
import pytest

def test_find_largest_subarray():
    array = [4, -10, 3, 29, -3, 12, -5, 4]
    assert find_largest_subarray(array) == 41


def test_find_largest_subarray_empty():
    array = []
    with pytest.raises(ValueError):
        find_largest_subarray(array)


def test_find_largest_subarray_negative():
    array = [-3, -5, -7, -1, -8, -12]
    assert find_largest_subarray(array) == -1


def test_find_largest_subarray_strings():
    array = [-3, 1, 5, "Wrong", "Type", "of", "Data"]
    with pytest.raises(ValueError):
        find_largest_subarray(array)
