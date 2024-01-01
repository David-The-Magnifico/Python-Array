def test_list_concatenation():
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    expected_concatenated_list = ["a", "b", "c", 1, 2, 3]
    assert concatenate_lists(list1, list2) == expected_concatenated_list

    empty_list = []
    assert concatenate_lists(empty_list, list2) == list2
    assert concatenate_lists(list1, empty_list) == list1

    single_item_list = ["single"]
    single_item_list2 = ["item"]
    assert concatenate_lists(single_item_list, single_item_list2) == ["single", "item"]
