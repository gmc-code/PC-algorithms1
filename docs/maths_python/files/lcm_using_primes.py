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


def union_of_highest_powers(lst1, lst2):
    """Return a list with the union of factors with highest power from lst1 and lst2.

    Args:
        lst1 (list): A list of integers.
        lst2 (list): A list of integers.

    Returns:
        list: A list of integers with factors raised to highest power.
    """
    # Create an empty list to store the result
    result = []
    # Count how many times each factor appears in each list
    freq1 = frequency(lst1)
    freq2 = frequency(lst2)
    # Loop through the keys of freq1 (the factors in lst1)
    for x in freq1:
        # If x is also in freq2 (the factors in lst2), compare their values (the powers)
        if x in freq2:
            # If freq1[x] is greater than or equal to freq2[x], append x raised to freq1[x] to the result list
            if freq1[x] >= freq2[x]:
                result.append(x ** freq1[x])
            # Otherwise, append x raised to freq2[x] to the result list
            else:
                result.append(x ** freq2[x])
        # Otherwise, append x raised to freq1[x] to the result list
        else:
            result.append(x ** freq1[x])
    # Loop through the keys of freq2 (the factors in lst2)
    for y in freq2:
        # If y is not in freq1 (the factors in lst1), append y raised to freq2[y] to the result list
        if y not in freq1:
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
    """Prompt the user to enter two numbers and display their LCM."""

    # Prompt the user to enter two numbers and convert them to integers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Find the prime factors of each number using the get_prime_factors function
    factors1 = get_prime_factors(num1)
    factors2 = get_prime_factors(num2)

    # Find the union of all the prime factors with highest power using the union_of_highest_powers function
    all_factors = union_of_highest_powers(factors1, factors2)

    # Find the LCM by multiplying all the factors using the product function
    lcm = product(all_factors)

    # Display the LCM
    print(f"prime factors of {num1} is{factors1}.")
    print(f"prime factors of {num2} is{factors2}.")
    print(f"LCM({num1}, {num2}) is {lcm}; the product of {all_factors}.")


# Check if the script is run directly and call the main function
if __name__ == "__main__":
    main()

'''
Enter the first number: 12
Enter the second number: 18
prime factors of 12 is[2, 2, 3].
prime factors of 18 is[2, 3, 3].
LCM(12, 18) is 36; the product of [4, 9]. 
'''