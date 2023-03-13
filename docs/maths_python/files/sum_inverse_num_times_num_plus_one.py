"""calculate sum of inverse products
"""


def inverse_product_sum(n):
    sum = 1
    for num in range(1, n  + 1):
        sum += 1/(num * (num+1))
    return sum


for x in range(1, 10):
    print(x, f'{inverse_product_sum(x):6f}', end="; ")