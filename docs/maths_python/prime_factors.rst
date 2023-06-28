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

----

Prime factor lists to 100
---------------------------

.. literalinclude:: files/prime_factor_list.py
    :linenos:
