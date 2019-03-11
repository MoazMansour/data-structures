"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    pivot = len(array)-1
    i = 0
    while i < pivot:
        if array[i] > array[pivot]:
            change = array[i]
            array[i] = array[pivot-1]
            array[pivot-1] = array[pivot]
            array[pivot] = change
            pivot = pivot - 1
            i = 0
        else:
            i += 1
    left_array = array[:pivot]
    right_array = array[pivot:]
    if (len(left_array) > 1):
        left_array = quicksort(left_array)
    if (len(right_array) > 1):
        right_array = quicksort(right_array)
    array = left_array + array[pivot:pivot] + right_array
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
