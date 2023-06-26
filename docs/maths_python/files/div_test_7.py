# The process for divisibility by 7 requires a few steps. Follow the steps below to test divisibility by 7, and then work through the example provided.
# 1.	Write down all the digits in the number except the last digit.
# 2.	Take the last digit of the number you're testing and double it. 
# 3.	Subtract this number from the rest of the digits in the original number that you wrote down. 
# 4.	If this new number is either 0 or a number that's divisible by 7, then the original number is also divisible by 7. 
# 5.	If you can't tell yet if the new number is divisible by 7, go back to the first step with this new (smaller) number and repeat. 

import random


def is_div_by_7(num):
    diff = repeated_diff_from_dbl_last(num)
    if diff in [0, 7, -7]:
        return True
    else:
        return False


def diff_from_dbl_last(num):
    last = int(str(num)[-1])
    all_but_last = int(str(num)[:-1])
    return all_but_last - 2 * last


def repeated_diff_from_dbl_last(num):
    diff = diff_from_dbl_last(num)
    while diff > 10:
        diff = diff_from_dbl_last(diff)
    return diff


num = random.randint(12, 300)
print(num, is_div_by_7(num))
