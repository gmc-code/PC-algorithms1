def f(x):
    return x**3 - 6.5*x**2 + 10*x - 1.5

def bisection(f, a, b, max_iter, max_diff):
    if f(a) * f(b) > 0:
        return "Invalid interval"
    i = 0
    while i < max_iter:
        mid = (a + b) / 2
        print('Iteration {:2d}: a={:.10f}, b={:.10f}, mid={:.10f}, y={: .10f}'.format  (i, a, b, mid, f(mid)))
        if abs(f(mid)) <= max_diff:
            return mid
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
        i += 1
    return mid


bisec_value = bisection(f,1,3,100,0.0001) 

print(bisec_value)
# 2.12353515625