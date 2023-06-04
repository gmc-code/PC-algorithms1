"""newton's method
"""

def newton(f, df, x0, max_iter, tol):
    i = 0
    while i < max_iter:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
        i += 1
    return x1

f = lambda x: x**3 - 2
df = lambda x: 3 * x**2

result = newton(f, df, 1.5, 100, 1e-6)
print(result)

# 1.2599210498953948

