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

.. code-block:: python

    import random
    import math


    def get_prime_factors(num):
        max_possible = int(math.sqrt(num)) + 1
        prime_factors = list()
        while num % 2 == 0:
            prime_factors.append(2)
            num = num // 2
        for factor in range(3, max_possible, 2):
            while num % factor == 0:
                prime_factors.append(factor)
                num = num // factor
        if num > 2:
            prime_factors.append(num)
        return prime_factors


    num = random.randint(12, 300)
    print(num, get_prime_factors(num))


----

Prime factor lists to 100
---------------------------

.. code-block:: python

    import random
    import math


    def get_prime_factors(num):
        max_possible = int(math.sqrt(num)) + 1
        prime_factors = list()
        while num % 2 == 0:
            prime_factors.append(2)
            num = num // 2
        for factor in range(3, max_possible, 2):
            while num % factor == 0:
                prime_factors.append(factor)
                num = num // factor
        if num > 2:
            prime_factors.append(num)
        return prime_factors


    for num in range(1, 101):
        fact  = get_prime_factors(num)
        print(num, fact)


