"""calculate sum of inverse products
1 1.500000; 2 1.666667; 3 1.750000; 4 1.800000; 5 1.833333; 6 1.857143; 7 1.875000; 8 1.888889; 9 1.900000; 
"""


def inverse_product_sum(n):
    sum = 1
    for num in range(1, n  + 1):
        sum += 1/(num * (num+1))
    return sum


for x in range(1, 10):
    print(x, f'{inverse_product_sum(x):6f}', end="; ")
