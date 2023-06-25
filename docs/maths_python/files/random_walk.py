import random

def random_walk_1d(start=3):
    x = start
    x_positions = [x]
    while x > 0 and x < 10:
        step = random.randint(0,1)
        if step:
            x += 1
        else:
            x -= 1
        x_positions.append(x)
    return x_positions

number_of_walks = 1000

for start_pos in range(1,10):
    safe_count = 0
    for _ in range(number_of_walks):
        walk_x_positions = random_walk_1d(start_pos)
        if walk_x_positions[-1] == 0:
            safe_count += 1
    print(start_pos,100 * safe_count / number_of_walks)
