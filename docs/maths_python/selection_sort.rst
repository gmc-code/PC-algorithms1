=======================
Selection sort
=======================

| The selection sort algorithm sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning. 

Selection sort algorithm
------------------------------

| The algorithm maintains two subarrays in a given array. 

1. The subarray which is already sorted. 
2. Remaining subarray which is unsorted. 

| In every iteration of selection sort, the minimum element from the unsorted subarray is picked and moved to the sorted subarray. 
| See: https://www.geeksforgeeks.org/python-program-for-selection-sort/

| Main Steps:

1. Check all items in the list for the smallest in the list.
2. Put it into the first position
3. Check all remaining items in the list the for the next smallest in the list
4. Put it into the next position
5. Repeat steps 3 and 4 until all items are sorted

----

| Python implementation:

.. literalinclude:: files/selection_sort.py
    :linenos:


| ``def selection_sort(numbers):`` defines a function named `selection_sort` that takes a single argument `numbers`, which is the list of integers to be sorted.
| ``for i in range(len(numbers)):`` starts a `for` loop that iterates over the indices of the `numbers` list. The variable `i` represents the index of the first element in the unsorted part of the list.
| ``min_index = i`` initializes a variable named `min_index` to store the index of the minimum element in the unsorted part of the list. The variable is initially set to `i`, which is the index of the first element in the unsorted part.
| ``for j in range(i+1, len(numbers)):`` starts another `for` loop that iterates over the indices of the unsorted part of the list, starting from `i+1`. The variable `j` represents the index of each element in the unsorted part.
| ``if numbers[j] < numbers[min_index]:`` checks if the element at index `j` is less than the element at index `min_index`. If it is, then this element is the new minimum element in the unsorted part of the list.
| ``min_index = j`` updates the value of `min_index` to `j`, which is the index of the new minimum element in the unsorted part of the list.
| ``numbers[i], numbers[min_index] = numbers[min_index], numbers[i]`` swaps the first element in the unsorted part of the list (i.e. the element at index `i`) with the minimum element in the unsorted part (i.e. the element at index `min_index`). This moves the minimum element to its correct position in the sorted part of the list.
| ``return numbers`` returns the sorted list of integers.
| ``numbers = [29, 10, 14, 37, 13, 25, 1, 67, 18, 9]`` creates a list named `numbers` containing 10 integers.
| ``sorted_numbers = selection_sort(numbers)`` calls the `selection_sort` function with `numbers` as an argument and assigns the result to a variable named `sorted_numbers`. The result is a sorted version of the input list.
| ``print(sorted_numbers)``prints the sorted list to the console.

----

Example
-------------

| The list `[29, 10, 14, 37, 13, 25, 1, 67, 18, 9]`
| is sorted to give  `[1, 9, 10, 13, 14, 18, 25, 29, 37, 67]`

----

Usage: find the median
------------------------

| The sorted list can then be used to find the median.
| In this example, the `find_median` function is called with a sorted list of 10 integers as input. Since 10 is an even number, the function calculates the median as the average of the two middle elements, which are 14 and 18. The average of these two numbers is 16, so the function returns 16 as the median.

.. literalinclude:: files/median_in_list.py
    :linenos:

| Here is a summary of how the Python code calculates the median of a sorted list of integers:

1. The `find_median` function takes a sorted list of integers as input.
2. The function calculates the length of the list and assigns it to a variable `n`.
3. The function checks if `n` is even by calculating the remainder when `n` is divided by 2 using the modulo operator (`%`). If `n` is even, the remainder will be 0.
4. If `n` is even, the function calculates the median as the average of the two middle elements in the sorted list. The two middle elements are at indices `n//2` and `n//2 - 1`, where `//` is the integer division operator. The function calculates the average of these two elements and assigns it to a variable named `median`.
5. If `n` is odd, the function calculates the median as the middle element in the sorted list, which is at index `n//2`. The function assigns this value to the `median` variable.
6. The function returns the value of the `median` variable as the result.

----

Selection sort of a dictionary
---------------------------------

| A dictionary can also be sorted by converting it to a list of tuples then converting the sorted list of tuples back to a dictionary.
| Main steps:

1. The input dictionary is first converted into a list of tuples using the `items()` method, where each tuple contains a key-value pair from the dictionary.
2. The selection sort algorithm is then applied to this list of tuples. The algorithm works by iterating over the list and finding the minimum value in the unsorted portion of the list. This is done by comparing the second element of each tuple (i.e., the value in the key-value pair) using the condition `if numbers[j][1] < numbers[min_index][1]:`.
3. Once the minimum value is found, it is swapped with the first element in the unsorted portion of the list using the line `numbers[i], numbers[min_index] = numbers[min_index], numbers[i]`.
4. This process is repeated until the entire list is sorted in ascending order by value.
5. Finally, the sorted list of tuples is converted back into a dictionary using the `dict()` constructor and returned as the output.


| Python implementation:

.. literalinclude:: files/selection_sort_dictionary.py
    :linenos:

----

Example: Life expectancy by state
------------------------------------

The life expectancy from birth for each state is given below as a dictionary.

life_expectancy = {
    'Victoria': 81.8,
    'Australian Capital Territory': 82.7,
    'Western Australia': 80.9,
    'New South Wales': 80.7,
    'South Australia': 80.4,
    'Queensland': 80.3,
    'Tasmania': 79.5,
    'Northern Territory': 76.3
}

Sorting this in ascending order by life expectancy gives this result: 

{
    "Northern Territory": 76.3,
    "Tasmania": 79.5,
    "Queensland": 80.3,
    "South Australia": 80.4,
    "New South Wales": 80.7,
    "Western Australia": 80.9,
    "Victoria": 81.8,
    "Australian Capital Territory": 82.7,
}


