def test_compute_running_total():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_output = [1, 3, 6, 10, 15, 21, 28, 36, 45]
    assert compute_running_total(arr) == expected_output

def test_compute_running_total_with_single_element():
    arr = [1]
    expected_output = [1]
    assert compute_running_total(arr) == expected_output

def test_compute_running_total_with_empty_array():
    arr = []
    expected_output = []
    assert compute_running_total(arr) == expected_output

def test_compute_running_total_with_all_zeros():
    arr = [0, 0, 0, 0, 0]
    expected_output = [0, 0, 0, 0, 0]
    assert compute_running_total(arr) == expected_output

def test_compute_running_total_with_negative_numbers():
    arr = [-1, 2, -3, 4, -5]
    expected_output = [-1, 1, -2, 2, -3]
    assert compute_running_total(arr) == expected_output

def test_compute_running_total_with_large_numbers():
    arr = [1000000, 2000000, 3000000]
    expected_output = [1000000, 3000000, 6000000]
    assert compute_running_total(arr) == expected_output

def test_compute_running_total_with_repeated_numbers():
    arr = [2, 2, 2, 2, 2]
    expected_output = [2, 4, 6, 8, 10]
    assert compute_running_total(arr) == expected_output
