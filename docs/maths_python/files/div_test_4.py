import random


def is_div_by_2(num):
    endings = ["0", "2", "4", "6", "8"]
    last_digit = str(num)[-1]
    if last_digit in endings:
        return True
    else:
        return False


def is_divisible_by_4(num):
    last_two_digits = int(str(num)[-2:])
    if is_div_by_2(last_two_digits):
        half_last_two_digits = int(last_two_digits / 2)
        if is_div_by_2(half_last_two_digits):
            return True
        else:
            return False
    else:
        return False


# Test the function
for _ in range(10):
    num = random.randrange(10, 300, 2)
    print(num, is_divisible_by_4(num))
