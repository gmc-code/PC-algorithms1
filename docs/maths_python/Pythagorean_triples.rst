=======================
Pythagorean triples
=======================

| VC2M9SP03: level 9: design, test and refine algorithms involving a sequence of steps and decisions based on geometric constructions and theorems; discuss and evaluate refinements

* creating an algorithm using pseudocode or flow charts to apply the triangle inequality, or an algorithm to generate Pythagorean triples

------------------------------------------------
Pythagorean triples up to a given integer
------------------------------------------------

| See: https://en.wikipedia.org/wiki/Pythagorean_triple
| Euclid's formula for Pythagorean triples is a way to generate sets of three positive integers that satisfy the equation :math:`a^2 + b^2 = c^2`, where a, b and c are the sides of a right-angled triangle. The formula states that if you choose any two positive integers m and n, where m > n, then the following equations will give you a Pythagorean triple:
| :math:`a = 2mn`
| :math:`b = m^2 - n^2`
| :math:`c = m^2 + n^2`

| For example, if you choose m = 3 and n = 2, then you get:
| :math:`a = 2 \times 3 \times 2 = 12`
| :math:`b = 3^2 - 2^2 = 9 - 4 = 5`
| :math:`c = 3^2 + 2^2 = 9 + 4 = 13`


.. literalinclude:: files/pythagorean_triples.py
    :linenos:

| Sample output giving lists of Pythagorean triples for numbers up to 100.
| [[3, 4, 5], [5, 12, 13], [15, 8, 17], [7, 24, 25], [21, 20, 29], [35, 12, 37], [9, 40, 41], [45, 28, 53], 
| [11, 60, 61], [33, 56, 65], [63, 16, 65], [55, 48, 73], [13, 84, 85], [77, 36, 85], [39, 80, 89], [65, 72, 97]]


| A second verion is below that uses list comprehension with conditionals:
| The `:=` operator is called the walrus operator or the assignment expression. It allows you to assign a value to a variable and use it in the same expression.
| In `and (c := math.pow(m, 2) + math.pow(n, 2)) < num `, 
| the value of `math.pow(m, 2) + math.pow(n, 2)` 
| is assigned to the variable c and then compared with num. This way, you don't have to calculate c twice or use a separate line to assign it. 
| The walrus operator was introduced in Python 3.8 and can be used in list comprehensions, lambda functions, if statements and other places where you want to avoid repeating calculations or code.

.. literalinclude:: files/pythagorean_triples_2.py
    :linenos:


