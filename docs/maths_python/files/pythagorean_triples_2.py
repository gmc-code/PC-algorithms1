import math # import the math module

def pythagorean_triples(num):
    # create a list comprehension to generate the triples
    triples = [[int(a), int(b), int(c)] for m in range(2, math.ceil(math.sqrt(num))) 
               for n in range(1, m) 
               if math.gcd(m, n) == 1 and m % 2 != n % 2 
               and (c := math.pow(m, 2) + math.pow(n, 2)) < num 
               and (a := math.pow(m, 2) - math.pow(n, 2)) > 0 
               and (b := 2 * m * n) > 0]
    # return the sorted list of triples
    return sorted(triples, key=lambda x: x[2])

# print the result for num = 100
print(pythagorean_triples(100))


#Output:
# [[3, 4, 5], [5, 12, 13], [15, 8, 17], [7, 24, 25], [21, 20, 29], [35, 12, 37], [9, 40, 41], [45, 28, 53], 
# [11, 60, 61], [33, 56, 65], [63, 16, 65], [55, 48, 73], [13, 84, 85], [77, 36, 85], [39, 80, 89], [65, 72, 97]]

