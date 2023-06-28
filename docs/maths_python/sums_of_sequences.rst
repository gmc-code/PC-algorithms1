=======================
Sums of sequences
=======================

| VCMNA254: Design and implement mathematical algorithms using a simple general purpose programming language

* finding the sum of a set of consecutive numbers using a loop structure

----

------------------------------
Sum of consecutive numbers
------------------------------

Listed numbers
-------------------

| The code below uses a for loop which iterates over the **nums** list.
| Each number, **num**, in the list, **nums**, is added to the **sum**.

.. literalinclude:: files/sum_consec_num1.py
    :linenos:

| Pseudocode:

| nums ← [1, 2, 3, 4, 5]
| sum ← 0
| **for** each num in nums
|     sum ← sum + num
| **print** sum

----

Range from 0
-----------------------------------

| The code below uses the range function to provide a list of integers from 0 to 5.

.. literalinclude:: files/sum_consec_num2.py
    :linenos:

| Pseudocode:

| nums ← list from 0 to 5
| **print** nums
| sum ← 0
| **for** each num in nums
|     sum ← sum + num
| **print** sum

----

Range: first and last
-----------------------------------

| The code below uses the range function to provide a list of integers from **start_num** to **end_num**.

.. literalinclude:: files/sum_consec_num3.py
    :linenos:

| Pseudocode:

| start_num ← 4
| end_num ← 12
| nums ← list of integers from start_num to end_num
| **print** nums
| sum ← 0
| **for** each num in nums
|     sum ← sum + num
| **print** sum

----

Range: step size
-----------------------------------

| The code below uses the range function to provide a list of integers from **start_num** to **end_num** in steps of **step_size**. 

.. literalinclude:: files/sum_consec_num4.py
    :linenos:

| Pseudocode:

| start_num ← 4
| end_num ← 12
| step_size ← 2
| nums ← list of integers from start_num to end_num in steps of step_size
| **print** nums
| sum ← 0
| **for** each num in nums
|     sum ← sum + num
| **print** sum

----

Arithmetic sequence formula 1
-----------------------------------

| One formula for the sum of a sequence of numbers with the same difference between them is:
| S = n/2[2a + (n-1)d]
| where
| S is the sum
| n is the number of numbers
| a is the start number
| d is the difference between numbers

.. literalinclude:: files/sum_consec_num5.py
    :linenos:

| Pseudocode:

| a ← 4
| n ← 5
| d ← 2
| sum ← (n/2) * (2*a + (n-1)*d)
| **print** sum


----

Arithmetic sequence formula 2
-----------------------------------

| Another formula for the sum of a sequence of numbers with the same difference between them is:
| S = n/2[a + l]
| where
| S is the sum
| n is the number of numbers
| a is the start number
| l is the last number

.. literalinclude:: files/sum_consec_num6.py
    :linenos:

| Pseudocode:

| a ← 4
| n ← 5
| l ← 12
| sum ← (n/2) * (a + l)
| **print** sum



