=======================
Pythagorean triples
=======================

| VC2M9SP03: level 9: design, test and refine algorithms involving a sequence of steps and decisions based on geometric constructions and theorems; discuss and evaluate refinements

* creating an algorithm using pseudocode or flow charts to apply the triangle inequality, or an algorithm to generate Pythagorean triples

------------------------------------------------
Pythagorean triples up to a given integer
------------------------------------------------

| Euclid's formula for Pythagorean triples is a way to generate sets of three positive integers that satisfy the equation :math:`a^2 + b^2 = c^2`, where a, b and c are the sides of a right-angled triangle. The formula states that if you choose any two positive integers m and n, where m > n, then the following equations will give you a Pythagorean triple:
| :math: `a = 2mn`
| :math: `b = m^2 - n^2`
| :math: `c = m^2 + n^2`

| For example, if you choose m = 3 and n = 2, then you get:
| :math: `a = 2 \times 3 \times 2 = 12`
| :math: `b = 3^2 - 2^2 = 9 - 4 = 5`
| :math: `c = 3^2 + 2^2 = 9 + 4 = 13`


.. literalinclude:: files/pythagorean_triples.py
    :linenos:

| Sample output giving lists of Pythagorean triples for numbers up to 50.
| [[3, 4, 5], [8, 6, 10], [5, 12, 13], [15, 8, 17], [12, 16, 20], [7, 24, 25], [24, 10, 26], [21, 20, 29], [16, 30, 34], [9, 40, 41], [35, 12, 37], [32, 24, 40], [27, 36, 45]]

