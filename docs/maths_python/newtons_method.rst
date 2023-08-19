=======================
Newton's method
=======================


| Newton's method is an iterative method for finding the roots of a real-valued function. 
| It starts with an initial guess for the root (x0) and iteratively refines this guess using the formula to calculate a new x value closer to the root: x1 = x0 - f(x0) / f'(x0), until a desired level of accuracy is achieved. 

.. image:: images/newtons_quadratic.png
    :width: 600
    :align: center

| 
| Pseudocode:

| **define** newton(f(x), f'(x), x0, max_iter, tol)
|     i ← 0
|     **while** i < max_iter
|         x1 ← x0 - f(x0) / f'(x0)
|         **if** abs(x1 - x0) <= tol **then**
|             **return** x1
|         x0 ← x1
|         i ← i + 1
|     **return** x1

| This pseudocode defines a function newton that takes five arguments: f(x), f'(x), x0, max_iter, and tol. 
| The function initializes a loop counter i to 0 and enters a while loop that iterates max_iter times. 
| The maximum number of iterations allowed is specified by the max_iter parameter.
| In each iteration, the code calculates a new value for x1 using the formula x1 = x0 - f(x0) / f'(x0). 
| It then checks if the absolute difference between x1 and x0 is less than tol. 
| If it is, the function returns x1. 
| Otherwise, the value of x0 is updated to be equal to x1 and the loop counter i is incremented by 1. 
| After the loop has completed, the function returns the final value of x1.

| Python implementation:

.. code-block:: python

    def newton(f, df, x0, max_iter, tol):
        i = 0
        while i < max_iter:
            x1 = x0 - f(x0) / df(x0)
            if abs(x1 - x0) <= tol:
                return x1
            x0 = x1
            i += 1
        return x1


----

Usage Example - cubic
-------------------------

.. image:: images/newtons_cubic.png
    :width: 600
    :align: center
    
| 
| 

.. literalinclude:: files/newtons_method_cubic.py
    :linenos:


| 
| This is an example of how you can use the newton's method 
| to find the root of the function y = x\ :sup:`3` - 2.


| The f function calculates the value of x\ :sup:`3` - 2 for a given value of x.
| The df function calculates the derivative of f, which is 3x\ :sup:`2`. 
| The code then calls the newton function with f set to the f lambda function, df set to the df lambda function, x0 set to an initial guess of 1.5, max_iter set to 100, and tolerance, tol, set to 1e-6. 

| The output value of 1.2599210498953948 is an approximate root of the function y = x\ :sup:`3` - 2 found using Newton's method with an initial guess of 1.5, a maximum of 100 iterations, and a tolerance of 1e-6.



Usage Example - exponential
-----------------------------

.. image:: images/newtons_exponential.png
    :width: 600
    :align: center
    
| 
| 

.. literalinclude:: files/newtons_method_exponential.py
    :linenos:




