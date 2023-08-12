def pythagorean_triples(num):
    # create an empty list to store the triples
    triples = []
    # initialize c and m variables
    c, m = 0, 2
    # loop until c exceeds the given limit
    while c < num:
        # loop over n from 1 to m-1
        for n in range(1, m):
            # calculate a using Euclid's formula
            a = m * m - n * n
            # calculate b using Euclid's formula
            b = 2 * m * n
            # calculate c using Euclid's formula
            c = m * m + n * n
            # if c exceeds the limit, break the inner loop
            if c > num:
                break
            # append the triple to the list
            triples.append([a, b, c])
        # increment m by 1
        m = m + 1
    # return the list of triples
    return triples

# print the result for num = 50
print(pythagorean_triples(50))

#Output:
[[3, 4, 5], [8, 6, 10], [5, 12, 13], [15, 8, 17], [12, 16, 20], [7, 24, 25], [24, 10, 26], [21, 20, 29], [16, 30, 34], [9, 40, 41], [35, 12, 37], [32, 24, 40], [27, 36, 45]]
