"""calculate sum of inverse factorials
"""

def factorial(n):
    product = 1
    for num in range(1, n  + 1):
        product = product*num
    return product


def inverse_factorial_sum(n):
    sum = 1
    for num in range(1, n  + 1):
        sum += 1/factorial(num)
    return sum


for x in range(50, 52):
    print(x, f'{inverse_factorial_sum(x):7f}', end="; ")