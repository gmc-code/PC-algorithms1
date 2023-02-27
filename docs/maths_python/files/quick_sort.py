import random


# This function is same in both iterative and recursive
def partition(arr, low, high):
    # elements less than the pivot will go to the left of `pivot_index`
    # elements more than the pivot will go to the right of `pivot_index`
    # equal elements can go either way
    pivot_index = low
    # Pick the rightmost element as a pivot from the list
    pivot = arr[high]
    # each time we find an element less  than or equal to the pivot,
    # `pivot_index` is incremented, and that element would be placed
    # before the pivot.
    for i in range(low, high):
        if arr[i] <= pivot:
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
            # swap i, pivot_index
            pivot_index += 1
    # swap `pivot_index` with pivot at high
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    # return index of the pivot element
    return pivot_index


# Function to do Quick sort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index
def iterativeQuicksort(arr):
    # Create an auxiliary stack
    size = len(arr)
    stack = [0] * (size)
    # get the low and high index of arr
    low = 0
    high = size - 1
    # push initial values of low and high to stack
    stack[0] = low
    stack[1] = high
    top = 1
    #
    print("*", stack, low, high)
    # Keep popping from stack while is not empty
    while top >= 0:
        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, low, high)
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high
        print(stack, arr)


num_list = list(range(0, 100))
arr = random.sample(num_list, 5)
print(f"Unsorted array: {arr}")
n = len(arr)
iterativeQuicksort(arr)
print(f"Sorted array:   {arr}")
