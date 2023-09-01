# def f(x):
#     return x**3 - 6.5*x**2 + 10*x - 1.5

# x_values = [1, 2, 3, 4]
# y_values = [f(x) for x in x_values]
# # [3.0, 0.5, -3.0, -1.5]
# print(y_values)

def hcf_div(a, b):
    while b != 0:
        t = b
        print(a==t, b==t)
        b = a - (a // b) * b
        a = t
        print(a==t, b==t)
    return a


a = 48
b = 18
print(a, b, hcf_div(a, b))
# 48 18 6
