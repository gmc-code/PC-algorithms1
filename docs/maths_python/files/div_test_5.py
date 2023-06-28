import random


def is_div_by_5(num):
    endings = ["0", "5"]
    last_digit = str(num)[-1]
    if last_digit in endings:
        return True
    else:
        return False


for _ in range(10):
    num = random.randint(10, 300)
    print(num, num/5, is_div_by_5(num))
