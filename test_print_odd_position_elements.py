import pytest
from odd_position_elements import print_odd_position_elements

def test_print_odd_position_elements():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_output = [2, 4, 6, 8]
    assert print_odd_position_elements(arr) == expected_output

def test_print_odd_position_elements_with_single_element():
    arr = [1]
    expected_output = []
    assert print_odd_position_elements(arr) == expected_output

def test_print_odd_position_elements_with_all_even_numbers():
    arr = [2, 4, 6, 8, 10]
    expected_output = [4, 8]
    assert print_odd_position_elements(arr) == expected_output

def test_print_odd_position_elements_with_all_odd_numbers():
    arr = [1, 3, 5, 7, 9]
    expected_output = [3, 7]
    assert print_odd_position_elements(arr) == expected_output

def test_print_odd_position_elements_with_negative_numbers():
    arr = [-1, -2, -3, -4, -5, -6]
    expected_output = [-2, -4, -6]
    assert print_odd_position_elements(arr) == expected_output

def test_print_odd_position_elements_with_double_digits_numbers():
    arr = [51, 22, 73, 84, 95, 56]
    expected_output = [22, 84, 56]
    assert print_odd_position_elements(arr) == expected_output