import math # import the math module

def pythagorean_triples(num):
    # create an empty list to store the triples
    triples = []
    # initialize c and m variables
    c, m = 0, 2
    # initialize a flag variable
    done = False
    # loop until c exceeds the given limit or done is True
    while m <= math.sqrt(num):
        # loop over n from 1 to m-1
        for n in range(1, m):
            # check if m and n are coprime and have different parity i.e not both odd by checking remainders form div by 2
            if math.gcd(m, n) == 1 and m % 2 != n % 2:
                # calculate a using Euclid's formula
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                # if c exceeds the limit, set done to True and break the inner loop
                if c < num:
                # append the triple to the list after checking the limit
                    triples.append([a, b, c])
                    # triples.append(sorted([a, b, c]))
                    print([n,m],[a, b, c])
        # increment m by 1
        m += 1
        # print([n,m],end=" ")
    # return the list of triples
    return triples

# print the result for num = 100
pt = pythagorean_triples(100)
pt = sorted(pt, key=lambda x: x[2])
print(pt)

#Output:
# [[3, 4, 5], [5, 12, 13], [15, 8, 17], [7, 24, 25], [21, 20, 29], [35, 12, 37], [9, 40, 41], [45, 28, 53], 
# [11, 60, 61], [33, 56, 65], [63, 16, 65], [55, 48, 73], [13, 84, 85], [77, 36, 85], [39, 80, 89], [65, 72, 97]]
