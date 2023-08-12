"""calculate sum of inverse factorials
0 1.000000; 1 2.000000; 2 2.500000; 3 2.666667; 4 2.708333; 5 2.716667; 6 2.718056; 7 2.718254; 8 2.718279; 9 2.718282; 
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


for x in range(0, 10):
    print(x, f'{inverse_factorial_sum(x):7f}', end="; ")

