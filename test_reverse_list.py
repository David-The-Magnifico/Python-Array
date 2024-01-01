import pytest

def reverse_list(lst):
    return list(reversed(lst))

def test_reverse_list():
    list1 = [1, 2, 3, 4, 5]
    assert reverse_list(list1) == [5, 4, 3, 2, 1]

    list2 = [10, 20, 30, 40, 50]
    assert reverse_list(list2) == [50, 40, 30, 20, 10]

    list3 = [5, 4, 3, 2, 1]
    assert reverse_list(list3) == [1, 2, 3, 4, 5]

    list4 = [-1, -2, -3, -4, -5]
    assert reverse_list(list4) == [-5, -4, -3, -2, -1]

    list5 = [1, 1, 1, 1, 1]
    assert reverse_list(list5) == [1, 1, 1, 1, 1]

    list6 = [1]
    assert reverse_list(list6) == [1]

    list7 = [-10, 20, -30, 40, -50]
    assert reverse_list(list7) == [-50, 40, -30, 20, -10]
