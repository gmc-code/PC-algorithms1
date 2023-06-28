def hcf_mod(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


a = 48   #1071
b = 18   #462
print(a, b, hcf_mod(a, b))
# 48 18 6
