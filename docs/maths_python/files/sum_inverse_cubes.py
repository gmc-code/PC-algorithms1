"""calculate sum of squares
2 5; 3 14; 4 30; 5 55; 6 91; 7 140; 8 204; 9 285; 10 385;
"""

def sum_inverse_cubes(n):
    sum = 0
    for num in range(1, n  + 1):
        sum += 1/num**3
    return sum


for x in [10, 100, 1000, 1000, 10000]:
    print(x, f'{sum_inverse_cubes(x):6f}', end="; ")

    
    