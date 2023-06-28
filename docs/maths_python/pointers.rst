=======================
Pointers
=======================

| Pointers are objects that store a memory address, which can be that of another value located in computer memory.
| Using pointers significantly improves performance for repetitive operations, like traversing iterable data structures.
| For example, the two pointers technique is a technique that involves using two pointers that traverse through an array or a list from different starting points or directions. 
| The pointers move based on certain rules and constraints, and the algorithm stops once both pointers meet a certain condition.


----

Two pointers: palindrome checker
---------------------------------

| The code below checks if words are palindromes, that is, words that are spelled the same when reversed.


.. literalinclude:: files/palindrome_checker.py
    :linenos:


| The `is_palindrome` function takes a string as input and returns a boolean value indicating whether the string is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

| The function uses two pointers, `left` and `right`, to traverse the string from both ends. 
| The first pointer, `left`, starts at the beginning of the string, while the second pointer, `right`, starts at the end of the string. 
| The function then enters a loop that continues until the two pointers meet.

| Inside the loop, the function checks if the characters at the current pointers are equal. 
| If they are not equal, the function returns `False` because the string is not a palindrome. 
| If they are equal, it moves both pointers towards each other and checks again.
| If all characters are checked and no unequal pair is found, the function returns `True` because the string is a palindrome.

| In the example provided, the function is called with the word `"racecar"` as an argument and its result is printed. Since `"racecar"` is a palindrome, the function returns `True`.

----

Two pointers: sum in list
-----------------------------

| The `isPairSum` function takes a sorted list of integers `A`, the length of the list `N`, and an integer `X` as input. 
| It returns a tuple containing a boolean value and two integers from the list if there exists a pair of elements `(A[i], A[j])` such that their sum is equal to `X`. 
| If no such pair exists, it returns `False`.

| The function uses two pointers, `i` and `j`, to traverse the list from both ends. 
| The first pointer, `i`, starts at the beginning of the list, while the second pointer, `j`, starts at the end of the list. 
| The function then enters a loop that continues until the two pointers meet.

| Inside the loop, the function checks if the sum of the elements at the current pointers is equal to `X`. 
| If it is, the function returns `True` and the values of the two elements. 
| If the sum is less than `X`, it moves the first pointer towards higher values by incrementing it. 
| If the sum is greater than `X`, it moves the second pointer towards lower values by decrementing it.
| If no pair is found by the time the loop exits, the function returns `False`.

| In the main code, an example list is created and sorted. The value to search for and the size of the array are also defined. The function is then called with these values as arguments and its result is printed.

.. literalinclude:: files/two_pointers.py
    :linenos:

