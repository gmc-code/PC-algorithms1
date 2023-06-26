"""return text quotient and remainder from dividing dividend by divisor
    eg. 7/3 = 2 remainder 1.
    dividend is 7; divisor is 3; quotient is 2; remainder is 1
"""

def quotient_and_remainder(dividend, divisor):
    quotient = 0
    remainder = dividend
    while remainder >= divisor:
        remainder -= divisor
        quotient +=1
    return f'{dividend}/{divisor} = {quotient} R{remainder}'

print(quotient_and_remainder(7, 3))

