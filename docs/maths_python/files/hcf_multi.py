import math

# Define a function to find the hcf of any number of numbers using math.gcd
def hcf_gcd(*args):
    # Use the formula hcf(a, b, c) = hcf(hcf(a, b), c)
    result = args[0]
    for num in args[1:]:
        result = math.gcd(result, num)
    return result

# Prompt the user to enter any number of numbers separated by commas; 168, 180, 192
nums = input("Enter the numbers: ")
nums = [int(num) for num in nums.split(",")]

# Call the hcf_gcd function and print the result
print(f'The HCF of {", ".join(str(num) for num in nums)} is {hcf_gcd(*nums)}.')
# The HCF of 168, 180, 192 is 12.


