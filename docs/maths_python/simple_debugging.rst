=======================
Simple debugging
=======================

| Debugging Search and Sort Programs
| An error in code is called a bug. 
| Correcting the errors in code is called debugging.
| Debugging includes checking that the algorithm returns the correct output from a given input.
| To help find errors in the code, test smaller sections of the code by printing the result part way to see if, at that point, it is correct.

----

Checking that a list has been sorted in ascending order
--------------------------------------------------------

| The list, [12, 13, 14, 16, 12, 17], is not sorted in ascending order.
| The 12 at index 4 is out of order.
| The function below can be used to indicate that the list was not sorted correctly.

.. code-block:: python

    def check_sorted_list(sorted_list):
        is_list_sorted = True
        for i in range (len(sorted_list)-1):
            if sorted_list[i+1] < sorted_list[i]:
                is_list_sorted = False
        return is_list_sorted
        

    mylist = [12, 13, 14, 16, 12, 17]
    print(mylist, "sorted", check_sorted_list(mylist))
    # [12, 13, 14, 16, 12, 17] sorted False

