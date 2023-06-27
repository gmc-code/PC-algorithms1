def even_numbers(numbers):
    """
    Takes a set of numbers and returns a new set containing only the even numbers.
    """
    result = set()
    for num in numbers:
        if num % 2 == 0:
            result.add(num)
    return result

numbers = set(range(1,11))
even_nums = even_numbers(numbers)
print(even_nums)
