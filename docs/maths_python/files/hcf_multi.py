import math


def hcf_gcd(*args):
    """Find the highest common factor (HCF) or greatest common divisor (GCD) of any number of numbers using math.gcd.

    Args:
        *args: Any number of integer arguments.

    Returns:
        int: The HCF or GCD of the given numbers.

    Raises:
        TypeError: If any of the arguments are not integers.
    """
    # Try to find the hcf using math.gcd
    try:
        result = args[0]
        for num in args[1:]:
            result = math.gcd(result, num)
        return result
    # Handle the TypeError if it occurs
    except TypeError:
        print("All arguments must be positive integers")
        return 0


def main():
    # Prompt the user to enter any number of positive integers separated by commas; 168, 180, 192
    nums = input("Enter the positive integers: ")

    # Check if the user enters any numbers at all
    if nums == "":
        print("Please enter at least one positive integers")
    else:
        # Try to convert the input to a list of integers
        try:
            nums = [int(num) for num in nums.split(",")]
            
            # Check if any of the numbers are negative
            if any(num < 0 for num in nums):
                print("The HCF is only defined for positive integers")
            else:
                # Call the hcf_gcd function and print the result
                print(f'The HCF of {", ".join(str(num) for num in nums)} is {hcf_gcd(*nums)}.')
                # The HCF of 168, 180, 192 is 12.
        # Handle the ValueError if it occurs
        except ValueError:
            print("Please enter only positive integers")

if __name__ == "__main__":
    main()



