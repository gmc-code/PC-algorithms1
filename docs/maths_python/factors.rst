=======================
Prime factors
=======================

| VCMNA221: level 6: Design algorithms involving branching and iteration to solve specific classes of mathematical problems

* implementing algorithms such as the Euclidean division algorithm

----

Prime factor list
---------------------

| The modulus operator can be used to test for a remainder when division is carried out.
| Steps:

    * Check if 2 goes into the number, num, with no remainder.
    * While 2 goes into the number exactly, add 2 to the list of prime factors and divide the number by 2.
    * For every odd number from 3 up to the square root of the number, check if the odd number goes in exactly.
    * While the factor goes in exactly, add it to the prime factors list and divide the number, num, by the factor.
    * Return the list of prime factors.

.. literalinclude:: files/prime_factors.py
    :linenos:

| Sample output is:

.. parsed-literal::

    97 [97]
    235 [5, 47]
    96 [2, 2, 2, 2, 2, 3]       
    256 [2, 2, 2, 2, 2, 2, 2, 2]
    210 [2, 3, 5, 7]
    247 [13, 19]
    78 [2, 3, 13]
    194 [2, 97]
    34 [2, 17]
    47 [47]

----

Prime factor lists
------------------------------

| The following code checks all the numbers from 2 to 100 for prime factors and lists those with atleast 3 different prime factors.
| A crictical line of code is: ``if len(set(fact)) > 2:`` which converts the list of prime factors to a set, which can only include one copy of each prime factor. 

.. literalinclude:: files/prime_factor_sets.py
    :linenos:

| Sample output is:

.. parsed-literal::

    30 [2, 3, 5]
    42 [2, 3, 7]   
    60 [2, 2, 3, 5]
    66 [2, 3, 11]  
    70 [2, 5, 7]   
    78 [2, 3, 13]  
    84 [2, 2, 3, 7]
    90 [2, 3, 3, 5]

    