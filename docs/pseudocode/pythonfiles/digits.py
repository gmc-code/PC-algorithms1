import random

n = int(input("Enter a number between 1 and 10: "))
n = n * 3
n = n + 18
n = n * 3
n = str(n)
mixed_digits_list = random.sample(n, len(n) - 1)
digit_str = "".join(mixed_digits_list)
print(digit_str)