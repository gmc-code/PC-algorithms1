# see https://en.wikipedia.org/wiki/Euclidean_algorithm
# 
def hcf_div(a, b):
    while b != 0:
        t = b
        b = a - (a // b) * b
        a = t
    return a


a = 48   #1071
b = 18   #462
print(a, b, hcf_div(a, b))


def hcf_mod(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


a = 48   #1071
b = 18   #462
print(a, b, hcf_mod(a, b))


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
