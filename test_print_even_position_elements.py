import pytest

def test_print_even_position_elements():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_output = [1, 3, 5, 7, 9]
    assert EvenPositionElements.print_even_position_elements(arr) == expected_output

def test_print_even_position_elements_with_single_element():
    arr = [1]
    expected_output = [1]
    assert EvenPositionElements.print_even_position_elements(arr) == expected_output

def test_print_even_position_elements_with_all_even_numbers():
    arr = [2, 4, 6, 8, 10]
    expected_output = [2, 6, 10]
    assert EvenPositionElements.print_even_position_elements(arr) == expected_output

def test_print_even_position_elements_with_all_odd_numbers():
    arr = [1, 3, 5, 7, 9]
    expected_output = [1, 5, 9]
    assert EvenPositionElements.print_even_position_elements(arr) == expected_output

def test_print_even_position_elements_with_negative_numbers():
    arr = [-1, -2, -3, -4, -5, -6]
    expected_output = [-1, -3, -5]
    assert EvenPositionElements.print_even_position_elements(arr) == expected_output

def test_print_even_position_elements_with_large_numbers():
    arr = [8675, 5189, 4963, 9465, 1485, 9737]
    expected_output = [8675, 4963, 1485]
    assert EvenPositionElements.print_even_position_elements(arr) == expected_output

def test_print_even_position_elements_with_large_array():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    expected_output = [1, 3, 5, 7, 9, 11]
    assert EvenPositionElements.print_even_position_elements(arr) == expected_output
