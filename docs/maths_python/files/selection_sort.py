def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

numbers = [29, 10, 14, 37, 13, 25, 1, 67, 18, 9]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)
#  [1, 9, 10, 13, 14, 18, 25, 29, 37, 67]
