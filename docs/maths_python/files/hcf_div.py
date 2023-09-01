def hcf_div(a, b):
    while b != 0:
        t = b
        b = a - (a // b) * b
        a = t
    return a


a = 48
b = 18
print(f'HCF({a}, {b}) is {hcf_div(a, b)}.')
# HCF(48, 18) is 6.
