def selection_sort(numbers):
    numbers = list(numbers.items())
    for i in range(len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j][1] < numbers[min_index][1]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return dict(numbers)


life_expectancy = {
    "Victoria": 81.8,
    "Australian Capital Territory": 82.7,
    "Western Australia": 80.9,
    "New South Wales": 80.7,
    "South Australia": 80.4,
    "Queensland": 80.3,
    "Tasmania": 79.5,
    "Northern Territory": 76.3,
}

sorted_dictionary_by_values = selection_sort(life_expectancy)
print(sorted_dictionary_by_values)
# {
#     "Northern Territory": 76.3,
#     "Tasmania": 79.5,
#     "Queensland": 80.3,
#     "South Australia": 80.4,
#     "New South Wales": 80.7,
#     "Western Australia": 80.9,
#     "Victoria": 81.8,
#     "Australian Capital Territory": 82.7,
# }
