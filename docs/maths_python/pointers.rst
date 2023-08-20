=======================
Pointers
=======================

| VC2M10A06: level 10: Implement algorithms that use data structures using pseudocode or a general purpose programming language

* Using pointers in algorithms

----

Pointers
----------------

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

| In the example provided, the function is called with the word `"racecar"` as an argument and its result is printed. Since `"racecar"` is a palindrome, the function returns `True`.

| The `is_palindrome` function takes a string as input and returns a boolean value indicating whether the string is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

| The function uses two pointers, `left` and `right`, to traverse the string from both ends. 
| The first pointer, `left`, starts at the beginning of the string, while the second pointer, `right`, starts at the end of the string. 
| The function then enters a loop that continues until the two pointers meet.

| Inside the loop, the function checks if the characters at the current pointers are equal. 
| If they are not equal, the function returns `False` because the string is not a palindrome. 
| If they are equal, it moves both pointers towards each other and checks again.
| If all characters are checked and no unequal pair is found, the function returns `True` because the string is a palindrome.


----

Two pointers: sum in list
-----------------------------

| The code below checks if 2 numbers in the list add to a given sum.

.. literalinclude:: files/pair_sum_in_list.py
    :linenos:

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

----

Two pointers: Length of longest substring
-------------------------------------------

| The code below returns the length of the longest string within the string.

.. literalinclude:: files/longest_substring.py
    :linenos:

| The `length_of_longest_substring` function takes a string `s` as input and returns the length of the longest substring without repeating characters.

| The function uses two pointers, `left` and `right`, to keep track of the current substring. 
| It also initializes a set `chars` to keep track of the characters in the current substring and a variable `max_len` to keep track of the maximum length found so far.

| The function then enters a loop that continues until the right pointer reaches the end of the string. 
| Inside the loop, the function checks if the character at the right pointer is not in the set `chars`. 
| If it is not, it adds the character to the set, increments the right pointer, and updates `max_len` with the maximum value between its current value and the length of the current substring.
| If the character at the right pointer is already in the set `chars`, it means that there is a repeating character in the current substring. 
| In this case, the function removes the character at the left pointer from the set and increments the left pointer to move to the next character.

| If all characters are checked and no longer substring is found, the function returns `max_len`.

| In this example, the function is called with the string `"a-bc-d-e"` as an argument and its result is assigned to the variable `result`. The function returns `4` because `"a-bc-d-e"` is the longest substring without repeating characters. The result is then printed.

----

| The code below modifies the code above to return the length of the longest string within the string as well as the substring.

.. literalinclude:: files/longest_substring_v2.py
    :linenos:

----

Two pointers: longest mountain
-------------------------------------------

| The code below returns the length of the longest mountain and its length from a list of numbers.

.. literalinclude:: files/longest_mountain.py
    :linenos:

| The `longest_mountain` function takes in a list of numbers `A` as an input and returns the length and the longest ascending-descending sequence (mountain) in the given list.

| The function starts by initializing the variables `mountain_length`, `base`, and `longest_seq` to 0, 0, and an empty list, respectively. 
| The variable `mountain_length` will keep track of the length of the longest mountain found so far, while `longest_seq` will keep track of the longest mountain sequence itself.

| The function then enters a while loop that continues until the variable `base` is less than the length of the input list `A`. 
| Inside the loop, the variable `end` is set to the value of `base`. 
| The function then checks if `end + 1` is less than the length of `A` and if the value at index `end` in list `A` is less than the value at index `end + 1`. 
| If this condition is true, it means that we have found an ascending sequence. 
| The function then enters another while loop that continues until `end + 1` is less than the length of `A` and the value at index `end` in list `A` is less than the value at index `end + 1`. 
| Inside this loop, we increment the value of `end` by 1 to move forward in the ascending sequence.

| After exiting this inner while loop, we check if `end + 1` is less than the length of `A` and if the value at index `end` in list `A` is greater than the value at index `end + 1`. 
| If this condition is true, it means that we have found a descending sequence after an ascending sequence, which forms a mountain. 
| The function then enters another while loop that continues until `end + 1` is less than the length of `A` and the value at index `end` in list `A` is greater than the value at index `end + 1`. 
| Inside this loop, we increment the value of `end` by 1 to move forward in the descending sequence.

| After exiting this inner while loop, we check if the current mountain length (`end - base + 1`) is greater than our current maximum mountain length (`mountain_length`). 
| If it is, we update our maximum mountain length to be equal to our current mountain length (`mountain_length = end - base + 1`) and update our longest mountain sequence (`longest_seq = A[base:end+1]`) to be equal to our current mountain sequence.

| Finally, we update our base index to be equal to either our current end index or our current base index plus one (`base = max(end, base + 1)`), whichever is greater. 
| This ensures that we move forward in our input list and do not get stuck in an infinite loop.
| After exiting the outer while loop, we return our maximum mountain length and longest mountain sequence as a tuple.

| In the example code, the function is called with an input list `[2, 1, 4, 7, 3, 2, 5]`. 
| The function returns `(5, [1, 4, 7, 3, 2])`, which means that the longest mountain sequence in the input list is `[1, 4, 7, 3, 2]`, with a length of 5.
