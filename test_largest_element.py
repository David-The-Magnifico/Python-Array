import pytest

def test_find_largest_element():
    assert find_largest_element([3, 5, 1, 9, 7, 2, 8, 4, 6]) == 9
    assert find_largest_element([10, 20, 30, 40, 50]) == 50
    assert find_largest_element([5, 4, 3, 2, 1]) == 5
    assert find_largest_element([-1, -2, -3, -4, -5]) == -1
    assert find_largest_element([1, 1, 1, 1, 1]) == 1
    assert find_largest_element([1]) == 1
    assert find_largest_element([100, 200, 50, 75, 300]) == 300

def find_largest_element(arr):
    if not arr:
        return None
    arr.sort()
    return arr[-1]
