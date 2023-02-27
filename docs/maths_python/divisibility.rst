=======================
Divisibility
=======================

* testing a number for divisibility

----------------------------------
Prime number divisibility tests
----------------------------------


Divibility by 2
-------------------

| A number is divisible by 2 if the last digit is 0, 2, 4, 6 or 8.
| For example: 234 is divisible by 2, because the last digit is 4.
| The code below checks if the last digit to see if it is divisible by 2.
| To get the last digit, the number is converted to a string, **str(num)**, then string indexing, **str(num)[-1]**, gets the last character.

.. code-block:: python

    import random


    def div_by_2(num):
        endings = ["0", "2", "4", "6", "8"]
        last_digit = str(num)[-1]
        if last_digit in endings:
            return True
        else:
            return False


    num = random.randint(10, 300)
    print(num, div_by_2(num))


----

Divibility by 3
-------------------

| A number is divisible by 3 if the sum of the digits in the number is divisible by 3.
| For example: 162 is divisible by 3 since the sum of the digits is 9 (1 + 6 + 2 = 9) and 9 is divisible 
by 3.
| The code below sums the digits of the number via **sum_digits**, and repeats summing the digits via **repeated_sum_digits** until there is just one digit, then, in **div_by_3**, checks if that sum is 3, 6, or 9.

.. code-block:: python

    import random


    def div_by_3(num):
        sum_of_digits = repeated_sum_digits(num)
        if sum_of_digits in [3, 6, 9]:
            return True
        else:
            return False


    def sum_digits(num):
        sum = 0
        for digit in str(num):
            sum += int(digit)
        return sum


    def repeated_sum_digits(num):
        sum_of_digits = sum_digits(num)
        while sum_of_digits > 10:
            sum_of_digits = sum_digits(sum_of_digits)
        return sum_of_digits


    num = random.randint(12, 300)
    print(num, div_by_3(num))

----

Divibility by 5
-------------------

| A number is divisible by 5 if the last digit is either 0 or 5.
| For example: 125 and 120 are both divisible by 5 since their last digits are 5 and 0.
| The code below checks if the last digit is a 5 or 0.
| To get the last digit, the number is converted to a string, **str(num)**, then string indexing, **str(num)[-1]**, gets the last character.

.. code-block:: python

    import random


    def div_by_5(num):
        endings = ["0", "5"]
        last_digit = str(num)[-1]
        if last_digit in endings:
            return True
        else:
            return False


    num = random.randint(10, 300)
    print(num, div_by_5(num))


----

Divisibility by 7
------------------

| The process for divisibility by 7 requires a few steps. Follow the steps below to test divisibility by 7, and then work through the example provided.
| 1.	Write down all the digits in the number except the last digit.
| 2.	Take the last digit of the number you're testing and double it. 
| 3.	Subtract this number from the rest of the digits in the original number that you wrote down. 
| 4.	If this new number is either 0 or a number that's divisible by 7, then the original number is also divisible by 7. 
| 5.	If you can't tell yet if the new number is divisible by 7, go back to the first step with this new (smaller) number and repeat. 

.. code-block:: python

    import random


    def div_by_7(num):
        diff = repeated_diff_from_dbl_last(num)
        if diff in [0, 7, -7]:
            return True
        else:
            return False


    def diff_from_dbl_last(num):
        last = int(str(num)[-1])
        all_but_last = int(str(num)[:-1])
        return all_but_last - 2 * last


    def repeated_diff_from_dbl_last(num):
        diff = diff_from_dbl_last(num)
        while diff > 10:
            diff = diff_from_dbl_last(diff)
        return diff


    num = random.randint(12, 300)
    print(num, div_by_7(num))

