=======================
Simple stats
=======================

| See: https://docs.python.org/3/library/statistics.html

----

Mean
---------------------------------

| The mean of a list can be found using the `sum` and `len` functions.
| The average is found by dividing the `sum` by `len` of the list.

.. code-block:: python

    mylist = [17, 13, 14, 16, 12, 12]
    mymean = sum(mylist)/len(mylist)
    print("Mean:", mymean)
    # 14.0

| Alternatively, the mean of a list can be found using `statistics.mean(list)`.

.. code-block:: python

    from statistics import mean

    mylist = [17, 13, 14, 16, 12, 12]
    mymean = mean(mylist)
    print("Mean usings statistics module:", mymean)
    # 14

| The mean above is 14.

----

Sort list
---------------------------------

| The list of numbers can be sorted in ascending order using `mylist.sort()`.
| This is useful for manually checking for the median and mode.

.. code-block:: python

    mylist = [17, 13, 14, 16, 12, 12]
    mylist.sort()
    print("Sorted list:", mylist)
    # [12, 12, 13, 14, 16, 17]

| The sorted list is: [12, 12, 13, 14, 16, 17]

----

Median
---------------------------------

| For the median, the middle value is returned if there is an odd number of numbers in the list.
| The average of the two middle values is returned if there is an even number of numbers in the list.

.. code-block:: python

    mylist = [17, 13, 14, 16, 12, 12]
    mylist.sort()
    n = len(mylist)
    if n % 2 == 0:
        # average of middle 2 for even number of numbers
        mymedian = (mylist[n//2 - 1] + mylist[n//2]) / 2
    else:
        # middle number of odd number of numbers
        mymedian = mylist[n//2]

    print("Median:", mymedian)
    # 13.5

| ``mylist.sort()`` sorts the list in ascending order.
| ``n = len(mylist)`` calculates the length of the list `mylist` using the `len` function and stores the result in a variable `n`.
| ``if n % 2 == 0:`` checks if `n` is even by calculating the remainder of `n` divided by `2` using the modulo operator `%`. If the remainder is `0`, this means that `n` is even.
| ``mymedian = (mylist[n//2 - 1] + mylist[n//2]) / 2`` calculate the median of the list `mylist` as the average of the two middle elements, if `n` is even. The two middle elements are accessed using indexing with the expression `n//2 - 1` and `n//2`. ``n//2`` performs integer division (also known as floor division). The result of the division is rounded down to the nearest integer. The average is calculated by adding these two elements and dividing by `2`. The result is stored in a variable `mymedian`.
| ``mymedian = mylist[n//2]`` calculate the median of the list `mylist` as the middle element if n is odd. The middle element is accessed using indexing with the expression `n//2`. The result is stored in a variable `mymedian`.
| It's important to note that this code assumes that the list `mylist` is already sorted in ascending order.

----

| Alternatively, the median of a list can be found using `statistics.median(list)`.

.. code-block:: python

    from statistics import median

    mylist = [17, 13, 14, 16, 12, 12]
    mymedian = median(mylist)
    print("Median usings statistics module:", mymedian)
    # 13.5

| The mean above is 13.5.

----

Mode
---------------------------------

| The mode can be found by first creating a dictionary that counts the number of occurances of each number.

.. code-block:: python

    mylist = [17, 13, 14, 16, 12, 12]

    # Count the occurrences of each number
    num_counts = {}
    for num in mylist:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    # Print the frequency of each number
    for num, cnt in num_counts.items():
        print(f"{num}: {cnt}")
    # Find the number with the highest count
    mode_count = max(num_counts.values())
    mode_num = [num for num, cnt in num_counts.items() if cnt == mode_count]
    print("Mode:", mode_num)
    # [12]

| Below is the output showing the frequencies of each number.

.. parsed-literal::

    Table of counts:
    12: 2
    13: 1
    14: 1
    16: 1
    17: 1

| Here's an explanation of how each line in the given Python code works:

| ``mylist = [17, 13, 14, 16, 12, 12]`` defines a list `mylist` with the given elements.
| ``num_counts = {}`` defines an empty dictionary `num_counts` that will be used to store the number of occurrences of each number in the list `mylist`.
| ``for num in mylist:`` starts a `for` loop that iterates over each element `num` in the list `mylist`.
| ``if num in num_counts:`` checks if `num` is already a key in the dictionary `num_counts`.
| ``num_counts[num] += 1`` increments the value associated with this key by `1` if `num` is already a key in the dictionary.
| ``num_counts[num] = 1`` adds a new key-value pair to the dictionary with key `num` and value `1` if `num` is not already a key in the dictionary.
| ``for num, cnt in num_counts.items():`` starts another `for` loop that iterates over each key-value pair `(num, cnt)` in the dictionary `num_counts`. The variable `num` takes on the value of each key and the variable `cnt` takes on the value of each value.
| ``print(f"{num}: {cnt}")`` prints the current key-value pair `(num, cnt)` to the console.
| ``mode_count = max(num_counts.values())`` uses the `max` function to find the maximum value in the dictionary `num_counts`. This maximum value is stored in a variable `mode_count`.
| ``mode_num = [num for num, cnt in num_counts.items() if cnt == mode_count]`` uses a list comprehension to create a list `mode_num` of all keys (i.e., numbers) in the dictionary that have a value equal to `mode_count`. In other words, this list contains all numbers that have the highest count.
| ``print("Mode:", mode_num)`` prints the list `mode_num` to the console. 

----

| Alternatively, the mode of a list can be found using `statistics.multimode(list)`.
| This returns a list of modes.
| A list is returned even if there is just a single mode.

.. code-block:: python

    from statistics import multimode

    mylist = [17, 13, 14, 16, 12, 12]
    mymode = multimode(mylist)
    print("Mode:", mymode)
    # [12]

----

Range
---------------------------------

| The range can be found using the max and min values.

.. code-block:: python

    mylist = [17, 13, 14, 16, 12, 12]
    myrange = max(mylist) - min(mylist)
    print(myrange)
    # 5
