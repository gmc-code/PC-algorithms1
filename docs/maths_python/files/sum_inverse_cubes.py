"""calculate sum of sum_inverse_cubes
10 1.197532; 100 1.202007; 1000 1.202056; 1000 1.202056; 10000 1.202057; 
"""

def sum_inverse_cubes(n):
    sum = 0
    for num in range(1, n  + 1):
        sum += 1/num**3
    return sum


for x in [10, 100, 1000, 1000, 10000]:
    print(x, f'{sum_inverse_cubes(x):6f}', end="; ")

    
    