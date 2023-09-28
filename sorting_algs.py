def merge_sort(unsorted_array: list[int]) -> list[int]:
    length = len(unsorted_array)
    if length == 1:
        return unsorted_array
    sorted_array: list[int] = []
    first_half = merge_sort(unsorted_array[:int(length / 2)])
    second_half = merge_sort(unsorted_array[int(length / 2):])
    index_one, index_two = 0, 0
    while index_one != len(first_half) or index_two != len(second_half):
        if index_one == len(first_half) and index_two != len(second_half):
            sorted_array = sorted_array + second_half[index_two:]
            break
        elif index_one != len(first_half) and index_two == len(second_half):
            sorted_array = sorted_array + first_half[index_one:]
            break
        if first_half[index_one] > second_half[index_two]:
            sorted_array.append(second_half[index_two])
            index_two = index_two + 1
        else:
            sorted_array.append(first_half[index_one])
            index_one = index_one + 1
    return sorted_array

def quick_sort(unsorted_array: list[int]):
    length = len(unsorted_array)
    if len(unsorted_array) == 1:
        return unsorted_array
    # if unsorted_array[0] <= unsorted_array[int(length / 2)] <= unsorted_array[length - 1]:
    #     pivot = unsorted_array[int(length / 2)]
    # elif unsorted_array[0] >= unsorted_array[int(length / 2)] >= unsorted_array[length - 1]:
    #     temp = unsorted_array[0]
    #     unsorted_array[0] = unsorted_array[length - 1]
    #     unsorted_array[length - 1] = temp
    #     pivot = unsorted_array[int(length / 2)]
    # elif unsorted_array[int(length / 2)] <= unsorted_array[length - 1] <= unsorted_array[0]:
    pivot = int(length / 2)
    item_from_left = pivot
    item_from_right = pivot
    left_index = -2
    right_index = -1
    while left_index < right_index:
        for i in range(length):
            if i == int(length / 2):
                continue
            if unsorted_array[i] > pivot:
                left_index, item_from_left = i, unsorted_array[i]
                break
        for i in range(length):
            if i == int(length / 2):
                continue
            if unsorted_array[i] < pivot:
                right_index, item_from_right = i, unsorted_array[i]
                break
        if left_index < right_index:
            temp = unsorted_array[right_index]
            unsorted_array[right_index] = unsorted_array[left_index]
            unsorted_array[left_index] = temp

    # This means each side is smaller/larger than the pivot
    unsorted_array = quick_sort(unsorted_array[: int(length / 2)]) + \
                     quick_sort(unsorted_array[int(length / 2) + 1:])

array = [2, 3, 1, 5, 6, 7, 2, 3]
print(merge_sort(array))
