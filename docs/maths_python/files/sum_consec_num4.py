start_num = 4
end_num = 12
step_size = 2
nums = list(range(start_num, end_num + 1, step_size))
print(nums)
sum = 0
for num in nums:
    sum += num
print(sum)