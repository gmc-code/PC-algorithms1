# Import the math module to use the gcd function
import math

# Define a function to find the lcm of any number of numbers
def lcm(*args):
    # Use the formula lcm(a, b, c) = lcm(lcm(a, b), c)
    result = args[0]
    for num in args[1:]:
        result = (result * num) // math.gcd(result, num)
    return result

# Prompt the user to enter any number of numbers separated by commas
nums = input("Enter the numbers separated by spaces: ")
nums = [int(num) for num in nums.split(",")]

# Display the LCM
print(f'The LCM of {", ".join(str(num) for num in nums)} is {lcm(*nums)}.')

'''Enter the numbers separated by spaces: 12 15 16
The LCM of 12, 15, 16 is 240.'''

