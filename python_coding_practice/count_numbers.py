def list_count_6(nums):
  count = 0  
  for num in nums:
    if num == 6:
      count = count + 1

  return count

print(list_count_6([1, 4, 6, 7, 6]))
print(list_count_6([1, 6, 6, 6, 7, 6]))