=======================
Divisibility
=======================

| VCMNA282: Use algorithms and related testing procedures to identify and correct errors

* Testing a number for divisibility

----------------------------------
Prime number divisibility tests
----------------------------------


Divibility by 2
-------------------

| A number is divisible by 2 if the last digit is 0, 2, 4, 6 or 8.
| For example: 234 is divisible by 2, because the last digit is 4.
| The code below checks if the last digit to see if it is divisible by 2.
| To get the last digit, the number is converted to a string, **str(num)**, then string indexing, **str(num)[-1]**, gets the last character.

.. literalinclude:: files/div_test_2.py
    :linenos:


| Pseudocode:

| **function** is_div_by_2(num)
|     endings ← ["0", "2", "4", "6", "8"]
|     last_digit ← str(num)[-1]
|     **if** last_digit in endings **then**
|         **return** **true**
|     **else**
|         **return** **false**
|     **endif**
| **endfunction**
| 
| num ← random integer from 10 to 300
| **print** num, is_div_by_2(num)


----

Divibility by 3
-------------------

| A number is divisible by 3 if the sum of the digits in the number is divisible by 3.
| For example: 162 is divisible by 3 since the sum of the digits is 9 (1 + 6 + 2 = 9) and 9 is divisible by 3.
| The code below sums the digits of the number via **sum_digits**, and repeats summing the digits via **repeated_sum_digits** until there is just one digit, then, **is_div_by_3** checks if that sum is 3, 6, or 9.


.. literalinclude:: files/div_test_3.py
    :linenos:

----

Divibility by 5
-------------------

| A number is divisible by 5 if the last digit is either 0 or 5.
| For example: 125 and 120 are both divisible by 5 since their last digits are 5 and 0.
| The code below checks if the last digit is a 5 or 0.
| To get the last digit, the number is converted to a string, **str(num)**, then string indexing, **str(num)[-1]**, gets the last character.

.. literalinclude:: files/div_test_5.py
    :linenos:

----

Divisibility by 7
------------------

| The process for divisibility by 7 requires a few steps. Follow the steps below to test divisibility by 7, and then work through the example provided.
| 1.	Write down all the digits in the number except the last digit.
| 2.	Take the last digit of the number you're testing and double it. 
| 3.	Subtract this number from the rest of the digits in the original number that you wrote down. 
| 4.	If this new number is either 0 or a number that's divisible by 7, then the original number is also divisible by 7. 
| 5.	If you can't tell yet if the new number is divisible by 7, go back to the first step with this new (smaller) number and repeat. 

.. literalinclude:: files/div_test_7.py
    :linenos:

----

------------------------------------
Other divisibility tests
------------------------------------

Divibility by 6
-------------------

| A number is divisible by 2 and by 3.

.. literalinclude:: files/div_test_6.py
    :linenos:

----

Divibility by 4
-------------------

| A number is divisible by 4 if the last 2 digits are divisible by 4.
| The code below checks if the last digit to see if it is divisible by 2, then divides it by 2 and checks again for divisibility by 2.
| To get the last 2 digits, the number is converted to a string, **str(num)**, then string indexing, **str(num)[-2:]**, gets the last 2 characters.

.. literalinclude:: files/div_test_4.py
    :linenos:

| Pseudocode:

| **function** is_div_by_2(num)
|     endings ← ["0", "2", "4", "6", "8"]
|     last_digit ← str(num)[-1]
|     **if** last_digit in endings **then**
|         **return** **true**
|     **else**
|         **return** **false**
|     **endif**
| **endfunction**
|  
| **function** is_divisible_by_4(num)
|    last_two_digits ← int(str(num)[-2:])
|    **if** is_div_by_2(last_two_digits) **then**
|        half_last_two_digits ← int(last_two_digits / 2)
|        **if** is_div_by_2(half_last_two_digits) then
|            **return** **true**
|        **else**
|            **return** **false**
|        **endif**
|    **else**
|        **return** **false**
|     **endif**
| **endfunction**
| 
| num ← random integer from 10 to 300
| **print** num, is_divisible_by_4(num)

----

General Divisibility by repeated addition
--------------------------------------------

| A general divisibility test can be done by counting up in steps equal to the divisor until the number to test is reached.

.. literalinclude:: files/div_test.py
    :linenos: 

----

Division by repeated subtraction
--------------------------------------------
  
| The code below returns the quotient and remainder from dividing a dividend by a divisor
| eg. 7/3 = 2 remainder 1.
| dividend is 7; divisor is 3; quotient is 2; remainder is 1

.. literalinclude:: files/division_by_subtraction.py
    :linenos: 


