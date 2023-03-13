"""calculate square root approximately
"""


def square_root(n, approx):
    diff = 0.0001
    sum = 1
    while approx**2 > (n + diff) or approx**2 < (n - diff):
        approx = 0.5 * (approx + n/approx)
    return approx


for x in range(1, 10):
    print(x, f'{square_root(x, 2):6f}', end="; ")