def manipulate_numbers(numbers):
    """
    Takes a set of numbers and applies the following rule to each number:
    If the number is even, halve it.
    If the number is odd, subtract 1 then halve it.
    Returns a new set of manipulated numbers.
    """
    result = set()
    for num in numbers:
        if num % 2 == 0:
            result.add(num // 2)
        else:
            result.add((num - 1) // 2)
    return result

numbers = set(range(1, 11))
manipulated_numbers = manipulate_numbers(numbers)
print(manipulated_numbers)
# {0, 1, 2, 3, 4, 5}