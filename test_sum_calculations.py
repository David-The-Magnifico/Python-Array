def test_sum_calculations():
    numbers = [1, 2, 3, 4, 5]
    assert sum_with_for_loop(numbers) == 15
    assert sum_with_while_loop(numbers) == 15
    assert sum_with_do_while_loop(numbers) == 15

    empty_array = []
    assert sum_with_for_loop(empty_array) == 0
    assert sum_with_while_loop(empty_array) == 0
    assert sum_with_do_while_loop(empty_array) == 0

    single_number_array = [10]
    assert sum_with_for_loop(single_number_array) == 10
    assert sum_with_while_loop(single_number_array) == 10
    assert sum_with_do_while_loop(single_number_array) == 10

    negative_numbers = [-1, -2, -3, -4, -5]
    assert sum_with_for_loop(negative_numbers) == -15
    assert sum_with_while_loop(negative_numbers) == -15
    assert sum_with_do_while_loop(negative_numbers) == -15

    large_numbers = [1000, 2000, 3000, 4000, 5000]
    assert sum_with_for_loop(large_numbers) == 15000
    assert sum_with_while_loop(large_numbers) == 15000
    assert sum_with_do_while_loop(large_numbers) == 15000

    mixed_numbers = [-1, 2, -3, 4, -5, 6]
    assert sum_with_for_loop(mixed_numbers) == 3
    assert sum_with_while_loop(mixed_numbers) == 3
    assert sum_with_do_while_loop(mixed_numbers) == 3
