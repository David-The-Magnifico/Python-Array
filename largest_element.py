from array import array

def find_largest_element(arr):
    arr.sort()
    return arr[-1]

arr = array('i', [3, 5, 1, 9, 7, 2, 8, 4, 6])
print(find_largest_element(arr))
