=======================
Prime factors
=======================

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

| The following code checks all the numbers form 2 to 100 for prime factors and list those with atleast 3 prime factors (which can include the same prime factor more than once).

.. literalinclude:: files/prime_factor_list.py
    :linenos:

| Sample output is:

.. parsed-literal::

    8 [2, 2, 2]
    12 [2, 2, 3]
    16 [2, 2, 2, 2]
    18 [2, 3, 3]
    20 [2, 2, 5]
    24 [2, 2, 2, 3]
    27 [3, 3, 3]
    28 [2, 2, 7]
    30 [2, 3, 5]
    32 [2, 2, 2, 2, 2]
    36 [2, 2, 3, 3]
    40 [2, 2, 2, 5]
    42 [2, 3, 7]
    44 [2, 2, 11]
    45 [3, 3, 5]
    48 [2, 2, 2, 2, 3]
    50 [2, 5, 5]
    52 [2, 2, 13]
    54 [2, 3, 3, 3]
    56 [2, 2, 2, 7]
    60 [2, 2, 3, 5]
    63 [3, 3, 7]
    64 [2, 2, 2, 2, 2, 2]
    66 [2, 3, 11]
    68 [2, 2, 17]
    70 [2, 5, 7]
    72 [2, 2, 2, 3, 3]
    75 [3, 5, 5]
    76 [2, 2, 19]
    78 [2, 3, 13]
    80 [2, 2, 2, 2, 5]
    81 [3, 3, 3, 3]
    84 [2, 2, 3, 7]
    88 [2, 2, 2, 11]
    90 [2, 3, 3, 5]
    92 [2, 2, 23]
    96 [2, 2, 2, 2, 2, 3]
    98 [2, 7, 7]
    99 [3, 3, 11]
    100 [2, 2, 5, 5]