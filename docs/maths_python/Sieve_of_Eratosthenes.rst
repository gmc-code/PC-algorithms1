=======================
Sieve of Eratosthenes
=======================

| VCMNA221: level 6: Design algorithms involving branching and iteration to solve specific classes of mathematical problems

* implementing algorithms such as the Euclidean division algorithm

----

| This Python code snippet uses iteration to implement the Sieve of Eratosthenes algorithm to find all prime numbers below 100.

.. image:: images/Sieve_of_Eratosthenes.png
    :width: 600
    :align: center

----

Sieve_v1: Primes below 100
------------------------------

| This code creates a list of boolean values representing the numbers from 0 to n (in this case, n is 100). 
| It then iterates over the list, starting from the first prime number p (2), and marks all multiples of p as not prime. 
| This process is repeated for all numbers until p squared is greater than n. 
| Finally, the code iterates over the list of boolean values and appends the index of each True value to a list of prime numbers. 
| The resulting list of prime numbers is then printed.

.. literalinclude:: files/Sieve_of_Eratosthenes.py

| The output is: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

----

Sieve_v2: Primes below 100
------------------------------

| This can be improved such that p is incremented until the next lowest prime is found. 
| In this version of the code, after marking all multiples of p as not prime, we enter a while loop that increments p until a True value is found. 
| This ensures that we only consider prime numbers as potential values for p.

.. literalinclude:: files/Sieve_of_Eratosthenes2.py
    :linenos:

| The output is: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
