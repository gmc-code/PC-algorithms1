def hcf_sub(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


a = 168
b = 180
c = 192

print(f'HCF({a}, {b}, {c}) is {hcf_sub(hcf_sub(a, b), c)}.')
# HCF(168, 180, 192) is 12.

