import random

def random_walk(n):
    """Return coordinates after 'n' block random walk."""
    x, y = 0, 0
    for _ in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

number_of_walks = 1000

for walkn in range(30):
    less_than_4 = 0
    for _ in range(number_of_walks):
        walk = random_walk(walkn)
        if abs(walk[0]) + abs(walk[1]) <= 4:
            less_than_4 += 1
    print(walkn, 100 * less_than_4 / number_of_walks)
