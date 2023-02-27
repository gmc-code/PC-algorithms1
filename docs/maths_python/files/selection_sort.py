import random


def selectionSort(array):
    size = len(array)
    # last index in array is size -1 
    # range goes up to size - 2; the second last index
    for ind in range(size - 1):
        min_index = ind
        # j from next index after ind, up to last element
        # range goes up to size - 1 which is last element
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the minimum right side element with ind if here is a lower number to right
        if min_index != ind:
            (array[ind], array[min_index]) = (array[min_index], array[ind])
    return array


num_list = list(range(0, 100))
arr = random.sample(num_list, 5)
print(f"Unsorted array: {arr}")
sorted_arr = selectionSort(arr)
print(f"Sorted array:   {sorted_arr}")
