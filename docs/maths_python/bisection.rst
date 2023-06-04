=======================
Bisection
=======================

| Pseudocode for the bisection method is below.
| This code defines a function bisection that takes four arguments: f, a, b, and max_iter. 
| The function checks if the product of f(a) and f(b) is greater than 0 and returns "Invalid interval" if it is. 
| Otherwise, it enters a while loop that iterates max_iter times. 
| In each iteration, the code calculates the midpoint between a and b and checks if f(mid) is equal to 0. 
| If it is, the function returns mid. 
| If not, the code checks if the product of f(a) and f(mid) is less than 0. 
| If it is, the value of b is updated to be equal to mid. 
| Otherwise, the value of a is updated to be equal to mid. 
| The loop counter i is then incremented by 1. 
| After the loop has completed, the function returns the final value of mid.

| Pseudocode:

| **define** bisection (f(x), a, b, max)
|     **if** f(a) x f(b) > 0 **then**		
|         **return** "Invalid interval"
|     i ← 0 
|     **while** i < max
|         mid ← (a + b) ÷ 2 
|         **if** f(mid) = 0 **then** 
|             **return** mid 
|         **else if** f(a) x f(mid) < 0 **then** 
|             b ← mid 
|         **else**
|             a ← mid 
|         i ← i + 1 
|     **end while** 
|     **return** mid 


| Python implementation:

.. code-block:: python

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


----

Usage Example
----------------

| Here's an example of how you can use the bisection function to find the root of the sin(x) function in the interval [3, 5] with a maximum of 2 iterations.
| The output value is 3.5.

.. code-block:: python

    from math import sin

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

    bisec_value = bisection(sin,3,5,2) 

    print(bisec_value)
    # 3.5