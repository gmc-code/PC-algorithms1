=======================
Simple stats
=======================

| See: https://docs.python.org/3/library/statistics.html

----

Mean
---------------------------------

| The mean of a list can be found using `statistics.mean(list)`.

.. code-block:: python

    from statistics import mean

    mylist = [17, 13, 14, 16, 12, 12]
    mymean = mean(mylist)
    print(mymean)

----

Sort list
---------------------------------

| The list of numbers can be sorted in ascending order using `mylist.sort()`.
| This is useful for manually checking for the median and mode.

.. code-block:: python

    mylist = [17, 13, 14, 16, 12, 12]
    mylist.sort()
    print(mylist)

----

Median
---------------------------------

| The mean of a list can be found using `statistics.median(list)`.
| The middle value is returned if there is an odd number of numbers in the list.
| The average of the two middle values is returned if there is an even number of numbers in the list.

.. code-block:: python

    from statistics import median

    mylist = [17, 13, 14, 16, 12, 12]
    mymedian = median(mylist)
    print(mymedian)

----

Mode
---------------------------------

| The mode of a list can be found using `statistics.multimode(list)`.
| This returns a list of modes.
| A list is returned even if there is just a single mode.

.. code-block:: python

    from statistics import multimode

    mylist = [17, 13, 14, 16, 12, 12]
    mymode = multimode(mylist)
    print(mymode)

----

Range
---------------------------------

| The range can be found using the max and min values.

.. code-block:: python

    mylist = [17, 13, 14, 16, 12, 12]
    myrange = max(mylist) - min(mylist)
    print(myrange)

