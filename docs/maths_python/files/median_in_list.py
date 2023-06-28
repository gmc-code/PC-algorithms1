def find_median(sorted_numbers):
    n = len(sorted_numbers)
    if n % 2 == 0:
        median1 = sorted_numbers[n//2]
        median2 = sorted_numbers[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = sorted_numbers[n//2]
    return median

sorted_numbers = [1, 9, 10, 13, 14, 18, 25, 29, 37, 67]
median = find_median(sorted_numbers)
print(median)
