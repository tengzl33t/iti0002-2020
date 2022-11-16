"""Sample text."""
nums = [5, 3, 6, 6, 6, 4, 6, 3, 45, 95, 66, 6]
counter = 0
for x, item in enumerate(nums):
    if item == 6 and nums[x - 1] == 6:
        counter = counter + 1
print(counter)
