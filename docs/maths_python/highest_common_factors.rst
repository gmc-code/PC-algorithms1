=======================
Highest common factors
=======================

| VC2M5N10: level 6:  Follow a mathematical algorithm involving branching and repetition (iteration); create and use algorithms involving a sequence of steps and decisions and digital tools to experiment with factors, multiples and divisibility; identify, interpret and describe emerging patterns

* identifying lowest common multiples and highest common factors of pairs or triples of natural numbers; for example, the lowest common multiple of {6, 9} is 18, and the highest common factor is 3, and the lowest common multiple of {3, 4, 5} is 60 and the highest common factor is 1

----

Euclidean algorithm for HCF
------------------------------

See: https://en.wikipedia.org/wiki/Euclidean_algorithm 

| The **highest common factor**, HCF, is known as the greatest common divisor, gcd.
| The Euclidean algorithm is based on the principle that the **highest common factor** of two numbers does not change if the larger number is replaced by its difference with the smaller number. 
| For example, 6 is the HCF of 48 and 18 (as 48 = 8 x 6 and 18 = 3 x 6), and the same number 6 is also the HCF of 18 and 30 (obtained by 48 - 18; taking 3 sixes from 8 sixes leaves 5 sixes). 
| Since this replacement reduces the larger of the two numbers, repeating this process gives successively smaller pairs of numbers until the two numbers become equal. 
| 48 and 18 becomes 30 and 18 which becomes 18 and 12 which becomes 12 and 6 which becomes 6 and 6.
| When that occurs, they are the HCF of the original two numbers. 

----


HCF pseudocode
------------------------------------------------

| The pseudocode to find HCF of two numbers by repeated subtraction is below.


| **function** hcf_sub(a, b)
|     // Repeat until the two numbers are equal
|     **while** a is not equal to b
|         // If a is larger than b, subtract b from a
|         **if** a is greater than b
|             a ← a minus b
|         // Otherwise, subtract a from b
|         **else**
|             b ← b minus a
|     // Return either a or b as the HCF
|     **return** a


----

HCF by repeated subtraction
------------------------------------------------

.. literalinclude:: files/hcf_sub.py
    :linenos:

----

HCF by repeatedly getting remainders from division
---------------------------------------------------

| Instead of repeated subtractions, a division can be used to get the remainder that would occur if all the possible subtractions of that number were to be done at once.
| Starting with 48 and 18, instead of subtracting 18 from 48, subtract the largest multiple of 18 that is less than 48. 
| 48 - (48//18)*18 = 12
| 48 - 2*18 = 12. 
| Note that 48//18 gives 2, the largest multiple of 18 that is less than 48. 
| **//** is floor division, rounding down to an integer.

| The code below runs the while loop until **b** equals 0.
| **b** is stored in **t** so b can be calculated, then **a** is set to **t**.
| An example of **b = a - (a // b) * b** 
| is **b = 48 - (48//18)*18**, 
| which is b = 48 - 36 = 12.

.. literalinclude:: files/hcf_div.py
    :linenos:

| The line, **b = a - (a // b) * b**, can be replaced by **b = a % b**, which finds the remainder from division.
| Instead of: 48 - (48//18)*18 = 12
| use: 48 % 18 = 12

.. literalinclude:: files/hcf_mod.py
    :linenos:

----

HCF of triples and more
---------------------------------------------------

| The highest common factors of triples or more natural numbers can be found by finding the HCF of two numbers first, then finding the HCF of the result and a third number and so on for all numbers being tested.
| e.g. HCF(168, 180, 192) is 12.

----

HCF of triples and more by repeated subtraction
---------------------------------------------------

| The code below uses repeated subtraction with multiple numbers to find their HCF.

.. literalinclude:: files/hcf_sub_multi.py
    :linenos:

----

HCF of triples and more by math.gcd
---------------------------------------------------

| The code below uses the python math.gcd function for multiple numbers to find their HCF.
| The code uses error chekcing as well.

.. literalinclude:: files/hcf_multi.py
    :linenos:

