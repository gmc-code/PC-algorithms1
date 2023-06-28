=======================
Flow charts
=======================

Adding fractions
---------------------

| The flow chart shows the main steps involved in adding 2 fractions.

.. image:: files/flow_chart_add_fractions.png
    :width: 200
    :align: center

|   
| The code below carries out these steps for adding two fractions:

1. The `add_fractions` function takes two fractions as input, represented as tuples of the form `(numerator, denominator)`.
2. The function unpacks the fractions to extract the numerators and denominators.
3. The function finds the lowest common denominator (LCD) of the two fractions by calculating the least common multiple (LCM) of the denominators.
4. The function converts each fraction to an equivalent fraction with the LCD as the denominator by multiplying the numerator and denominator by the same factor.
5. The function adds the numerators of the two fractions to calculate the numerator of the sum.
6. The function simplifies the resulting fraction if possible by dividing both the numerator and denominator by their greatest common divisor (GCD).
7. If the resulting fraction is an improper fraction (i.e. if the numerator is greater than the denominator), the function converts it to a mixed number by calculating the whole number and remainder.
8. The function returns the sum of the fractions, either as a proper fraction or as a mixed number.


.. literalinclude:: files/add_fractions.py
    :linenos:

| The output is: 1/2 + 2/3 = 1 1/6

----

Adding fractions using fractions module
-------------------------------------------

| The fractions module can be used to create fraction objects which allow easy addition.
| Improper fractions results then have to be simplified.

.. literalinclude:: files/add_fractions_using_fractions.py
    :linenos:

