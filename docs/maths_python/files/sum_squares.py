"""calculate sum of squares
2 5; 3 14; 4 30; 5 55; 6 91; 7 140; 8 204; 9 285; 10 385;
"""

def sum_squares(n):
    sum = 0
    for num in range(1, n  + 1):
        sum += num**2
    return sum


for x in range(2, 11):
    print(x, sum_squares(x), end="; ")