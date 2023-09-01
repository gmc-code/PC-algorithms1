def hcf_mod(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


a = 48   #1071
b = 18   #462

print(f'HCF({a}, {b}) is {hcf_mod(a, b)}.')
# HCF(48, 18) is 6.
