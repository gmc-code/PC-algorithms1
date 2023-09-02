# Define a function to find the hcf of any number of numbers using subtraction
def hcf_sub_multi(*args):
    # Use the logic for subtraction a-b-c-... = ((a-b)-c)-...
    result = args[0]
    for num in args[1:]:
        while result != num:
            if result > num:
                result = result - num
            else:
                num = num - result
    return result

# Prompt the user to enter any number of numbers separated by commas; 168, 180, 192
nums = input("Enter the numbers: ")
nums = [int(num) for num in nums.split(",")]

# Call the hcf_sub function and print the result
print(f'The HCF of {", ".join(str(num) for num in nums)} is {hcf_sub_multi(*nums)}.')
# The HCF of 168, 180, 192 is 12.

