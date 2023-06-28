def hcf_sub(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


a = 48
b = 18
hcf = hcf_sub(a, b)

print(a, b, hcf)
# 48 18 6
