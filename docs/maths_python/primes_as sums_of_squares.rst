==============================
Primes as sums of squares
==============================

| VCMNA221: level 6: Design algorithms involving branching and iteration to solve specific classes of mathematical problems

* implementing algorithms such as the Euclidean division algorithm

----

Primes 1 mod 4
---------------------

| If a prime number is divided by 4 and its remainder is 1, then it can be written as the sum of 2 squares.

| Steps:

* Define the upper limit of the prime numbers to check
* Generate the primes using the sieve_of_eratosthenes function
* Iterate over the primes and check if they are 1 mod 4 (have a remainder of 1 when divided by 4) 
* Find the sum of squares for each prime:
* Print the list of primes with the sums of squares.

.. literalinclude:: files/prime_sum_two_squares.py
    :linenos:

| Sample output is:

.. parsed-literal::

    5 = 1^2 + 2^2 = 1 + 4
    13 = 2^2 + 3^2 = 4 + 9
    17 = 1^2 + 4^2 = 1 + 16
    29 = 2^2 + 5^2 = 4 + 25
    37 = 1^2 + 6^2 = 1 + 36
    41 = 4^2 + 5^2 = 16 + 25
    53 = 2^2 + 7^2 = 4 + 49
    61 = 5^2 + 6^2 = 25 + 36
    73 = 3^2 + 8^2 = 9 + 64
    89 = 5^2 + 8^2 = 25 + 64
    97 = 4^2 + 9^2 = 16 + 81
