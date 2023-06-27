def sequential_addition(numbers):
    """
    Takes a set of numbers and forms a new list by sequentially adding them.
    Returns the new list of numbers.
    """
    result = list()
    current_sum = 0
    for num in numbers:
        current_sum += num
        result.append(current_sum)
    return result

numbers = set(range(1,11))
new_numbers = sequential_addition(numbers)
print(new_numbers)
# [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]