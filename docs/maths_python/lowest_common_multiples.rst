=======================
Lowest common multiple
=======================

| VC2M5N10: level 6:  Follow a mathematical algorithm involving branching and repetition (iteration); create and use algorithms involving a sequence of steps and decisions and digital tools to experiment with factors, multiples and divisibility; identify, interpret and describe emerging patterns

* identifying lowest common multiples and highest common factors of pairs or triples of natural numbers; for example, the lowest common multiple of {6, 9} is 18, and the highest common factor is 3, and the lowest common multiple of {3, 4, 5} is 60 and the highest common factor is 1

----

LCM
------------------------------------------------

| LCM of two or more numbers is the smallest positive integer that is divisible by each of the numbers. 
| For example, the LCM of 4 and 6 is 12, because 12 is the smallest positive integer that is divisible by both 4 and 6.

----

LCM psudocode
------------------------------------------------

| The Pseudocode to find LCM of two numbers has the steps to find the lowest common multiple of two numbers:

| **begin**
|   // Declare variables for the two numbers and the LCM
|   **number** num1, num2, lcm
|   
|   // Prompt the user to enter the two numbers
|   **ouput** "Enter the first number: "
|   **input** num1
|   **ouput** "Enter the second number: "
|   **input** num2
|   
|   // Find the prime factors of each number
|   **list** factors1 = prime_factors(num1)
|   **list** factors2 = prime_factors(num2)
|   
|   // Find the union of all the prime factors with highest power
|   **list** all_factors = union(factors1, factors2)
|   
|   // Multiply all the prime factors
|   lcm = product(all_factors)
|   
|   // Display the LCM
|   **ouput** "The LCM of " + num1 + " and " + num2 + " is " + lcm
| **end**


.. literalinclude:: files/lcm_using_primes.py
    :linenos:

----

LCM of triples
---------------------------------------------------

| The highest common factors of triples of natural numbers can be found by finding the HCF of two numbers first, then finding the HCF of the result and a third number.
| e.g. w(168, 180, 192) is 12.

.. literalinclude:: files/hcf_sub_multi.py
    :linenos:

----

LCM using gcd 
-------------

| The Python math.gcd() function is a built-in function that returns the greatest common divisor (GCD) of two or more integers. 
| The GCD of two or more numbers is the largest positive integer that divides each of the numbers without leaving a remainder.
| 