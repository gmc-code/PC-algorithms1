"""bisection
"""

from math import sin

f = lambda x: sin(x)

def bisection(f, a, b, max_iter):
    if f(a) * f(b) > 0:
        #need one pos and one neg
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

bisec_value = bisection(f,2,4,5) 

print(bisec_value)
# 3.1875

