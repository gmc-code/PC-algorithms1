
def is_multiple_or_factor(a, b):
    """Check if a is a multiple or a factor of b.

    Parameters:
    a (int): The first number
    b (int): The second number

    Returns:
    str: A string indicating the relationship between a and b
    """
    # Check for 0 values of a or b
    if a == 0 or b == 0:
        return "Do not use 0 for a or b"    
    if b % a == 0:
        # a is a factor of b
        return f'{a} is a factor of {b}'
    elif a % b == 0:
        # a is a multiple of b
        return f'{a} is a multiple of {b}'
    # Otherwise, return "neither", since neither condition is met
    else:
        return f'{a} is neither factor nor multiple of {b}'

# Test the function with some examples
a, b = 6, 18
print(is_multiple_or_factor(a, b)) # 6 is a factor of 18
a, b = 20, 4
print(is_multiple_or_factor(a, b))  # 20 is a multiple of 4
a, b = 9, 2
print(is_multiple_or_factor(a, b))  # 9 is neither factor nor multiple of 2
a, b = 2, 0
print(is_multiple_or_factor(a, b))  # Do not use 0 for a or b


