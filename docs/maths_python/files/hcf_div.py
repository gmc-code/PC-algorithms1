def hcf_div(a, b):
    while b != 0:
        t = b
        b = a - (a // b) * b
        a = t
    return a


a = 48
b = 18
print(a, b, hcf_div(a, b))
# 48 18 6
