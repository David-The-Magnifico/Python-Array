import pytest

# Function to check if an element is present in a list
def contains_element(lst, element):
    return element in lst

# Pytest test method
def test_contains_element():
    # Test case 1: Element present in the list
    list1 = [1, 2, 3, 4, 5]
    element1 = 3
    assert contains_element(list1, element1) == True

    # Test case 2: Element not present in the list
    list2 = [10, 20, 30, 40, 50]
    element2 = 15
    assert contains_element(list2, element2) == False

    # Test case 3: Empty list
    list3 = []
    element3 = 5
    assert contains_element(list3, element3) == False

    # Test case 4: Element present in a list of negative integers
    list4 = [-1, -2, -3, -4, -5]
    element4 = -3
    assert contains_element(list4, element4) == True

    # Test case 5: Element present in a list of identical integers
    list5 = [1, 1, 1, 1, 1]
    element5 = 1
    assert contains_element(list5, element5) == True

    # Test case 6: Element not present in a list with a single element
    list6 = [10]
    element6 = 5
    assert contains_element(list6, element6) == False