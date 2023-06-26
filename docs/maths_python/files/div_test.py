"""general divisor test by adding """

def is_div_by_divisor(num,divisor):
    total = 0
    while total < num:
        total = total + divisor
    if total == num:
        return True
    else:
        return False


num = int(input("Type the number to test: "))
divisor = int(input("Type the number you want to see if it is divisible by: "))
print(num, "can be divided by", divisor, is_div_by_divisor(num,divisor))
