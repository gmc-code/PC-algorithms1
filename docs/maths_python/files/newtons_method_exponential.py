"""newton's method: exponential
"""
# import the math module to use the exponential function
import math

def newton(f, df, x0, max_iter, tol):
    i = 0
    while i < max_iter:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) <= tol:
            return x1
        x0 = x1
        i += 1
    return x1

f = lambda x: math.exp(x) - 3
df = lambda x: math.exp(x)


result = newton(f, df, 1, 100, 1e-6)
print(result)
# 1.0986122886681096

