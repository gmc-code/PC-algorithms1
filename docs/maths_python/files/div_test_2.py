import random


def is_div_by_2(num):
    endings = ["0", "2", "4", "6", "8"]
    last_digit = str(num)[-1]
    if last_digit in endings:
        return True
    else:
        return False

for _ in range(10):
    num = random.randint(10, 300)
    print(num, is_div_by_2(num))
