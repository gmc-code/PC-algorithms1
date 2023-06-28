import random


def is_div_by_2(num):
    endings = ["0", "2", "4", "6", "8"]
    last_digit = str(num)[-1]
    if last_digit in endings:
        return True
    else:
        return False


def is_divisible_by_8(num):
    last_three_digits = int(str(num)[-3:])
    if is_div_by_2(last_three_digits):
        half_last_three_digits = int(last_three_digits / 2)
        if is_div_by_2(half_last_three_digits):
            quarter_last_three_digits = int(half_last_three_digits / 2)
            if is_div_by_2(quarter_last_three_digits):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


for _ in range(10):
    num = random.randrange(10, 300, 2)
    print(num, num/8, is_divisible_by_8(num))

 