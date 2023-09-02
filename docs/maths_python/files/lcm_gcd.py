# Import the math module to use the gcd function
import math

# Define a function to find the lcm of two numbers
def lcm(a, b):
    # Use the formula lcm = (a * b) // gcd(a, b)
    return (a * b) // math.gcd(a, b)

# Prompt the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the lcm function and print the result
print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))


a = 48
b = 18
# Display the LCM
print(f'LCM({a}, {b}) is {lcm(a , b)}.')

