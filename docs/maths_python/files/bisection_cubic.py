def f(x):
    return x**3 - 6.5*x**2 + 10*x - 1.5

def bisection(f, a, b, max_iter):
    if f(a) * f(b) > 0:
        return "Invalid interval"
    i = 0
    while i < max_iter:
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
        i += 1
    return mid

bisec_value = bisection(f,1,3,10) 

print(bisec_value)
# 2.123046875