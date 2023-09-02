import math


def frequency(lst):
    """Return a dictionary with the frequency of each factor in lst.

    Args:
        lst (list): A list of integers.

    Returns:
        dict: A dictionary with factors as keys and frequencies as values.
    """
    # Create an empty dictionary to store the frequency
    freq = {}
    # Loop through the list
    for x in lst:
        # If x is already in the dictionary, increment its value by 1
        if x in freq:
            freq[x] += 1
        # Otherwise, set its value to 1
        else:
            freq[x] = 1
    # Return the dictionary
    return freq


def union_of_highest_powers(nums):
    """Return a list with the union of all factors with highest power.

    Args:
        nums (list): A list of positive integers.

    Returns:
        list: A list of integers with factors raised to their highest power.

    Raises:
        ValueError: If any element in nums is not positive.
    """
    # Create an empty list to store the result
    result = []
    # If there are no numbers or only one number, return 1
    if len(nums) == 0 or len(nums) == 1:
        return [1]
    # Create an empty dictionary to store the frequency of each factor in all numbers
    freq2 = {}
    # Loop through each number in nums
    for num in nums:
        # Find the prime factors of num using a get_prime_factors algorithm
        prime_factors = get_prime_factors(num)
        # Find the frequency of each factor in num using the frequency function
        freq1 = frequency(prime_factors)
        # Loop through each factor in freq1
        for x in freq1:
            # If x is also in freq2, compare their values (the powers)
            if x in freq2:
                # If freq1[x] is greater than freq2[x], update freq2[x] to freq1[x]
                if freq1[x] > freq2[x]:
                    freq2[x] = freq1[x]
            # Otherwise, add x and freq1[x] to freq2
            else:
                freq2[x] = freq1[x]
    # Loop through each factor in freq2
    for y in freq2:
        # Append y raised to freq2[y] to the result list
        result.append(y ** freq2[y])
    # Return the result list
    return result


def product(lst):
    """Return the product of all elements in lst.

    Args:
        lst (list): A list of numbers.

    Returns:
        number: The product of all elements in lst.
    """
    # Initialize the product to 1
    p = 1
    # Loop through the list and multiply each element with the product
    for x in lst:
        p *= x
    # Return the product
    return p


def get_prime_factors(num):
    """Return a list with the prime factors of num.

    Args:
        num (int): A positive integer.

    Returns:
        list: A list of integers with prime factors of num.

    Raises:
        ValueError: If num is not positive.
    """
    if num <= 0:
        raise ValueError("num must be positive")

    max_possible = int(math.sqrt(num)) + 1
    prime_factors = list()
    while num % 2 == 0:
        prime_factors.append(2)
        num = num // 2
    for factor in range(3, max_possible, 2):
        while num % factor == 0:
            prime_factors.append(factor)
            num = num // factor
    if num > 2:
        prime_factors.append(num)
    return prime_factors


# Define a main function to run the script
def main():
    """Prompt the user to enter a list of integers and display their LCM."""
    # Prompt the user to enter a list of integers and convert them to lists
    nums = input("Enter the numbers separated by commas: ")
    nums = [int(num) for num in nums.split(",")]
    # Find the union of all the factors with highest power using the union_of_highest_powers function
    all_factors = union_of_highest_powers(nums)
    # Find the LCM by multiplying all the factors using the product function
    lcm = product(all_factors)
    # Display the LCM
    print(f"LCM({nums}) is {lcm}; the product of {all_factors}.")


# Check if the script is run directly and call the main function
if __name__ == "__main__":
    main()


'''
Enter the numbers separated by commas: 12,15,16
LCM([12, 15, 16]) is 240; the product of [16, 3, 5].
'''