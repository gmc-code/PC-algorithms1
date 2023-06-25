def f(x):
    return x**3 - 6.5*x**2 + 10*x - 1.5

def bisection(f, a, b, max_diff):
    if f(a) * f(b) > 0:
        return "Invalid interval"
    i = 0
    mid = (a + b) / 2
    while abs(f(mid)) > max_diff:
        mid = (a + b) / 2
        print(f'Iteration {i:2d}: a={a:.10f}, b={b:.10f}, mid={mid:.10f}, y={f(mid):.10f}')
        if f(mid) == 0:
            return mid
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
        i += 1
    return mid

bisec_value = bisection(f,1,3,0.0001) 

print(bisec_value)
# 2.12353515625