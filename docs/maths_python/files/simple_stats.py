"""simple stats
"""

from statistics import mean, median, multimode

mylist = [17, 13, 14, 16, 12, 12]
mylist = [7, 6, 5, 6, 5, 8, 7, 6, 6, 5, 6, 5, 5, 8, 5]

mymean = sum(mylist)/len(mylist)
print("Mean:", mymean)
# 14.0

mymean = mean(mylist)
print("Mean usings statistics module:", mymean)
# 14

##########################################

mylist.sort()
print("Sorted list:", mylist)
# [12, 12, 13, 14, 16, 17]

# Find the median
n = len(mylist)
if n % 2 == 0:
    # average of middle 2 for even number of numbers
    mymedian = (mylist[n//2 - 1] + mylist[n//2]) / 2
else:
    # middle number of odd number of numbers
    mymedian = mylist[n//2]

print("Median:", mymedian)
# 13.5

mymedian = median(mylist)
print("Median usings statistics module:", mymedian)
# 13.5

##########################################

mymode = multimode(mylist)
print("Mode usings statistics module:",mymode)
# [12]

# Count the occurrences of each number
num_counts = {}
for num in mylist:
    if num in num_counts:
        num_counts[num] += 1
    else:
        num_counts[num] = 1

# Print the result
for num, cnt in num_counts.items():
    print(f"{num}: {cnt}")
# Find the number with the highest count
mode_count = max(num_counts.values())
mode_num = [num for num, cnt in num_counts.items() if cnt == mode_count]

# Print the result
print("Mode:", mode_num)


##########################################

myrange = max(mylist) - min(mylist)
print("Range:", myrange)
# 5

