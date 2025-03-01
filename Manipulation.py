# Ek array diya gaya hai aur ek target sum, tumhe do aise indices dhoondhne hain jinka sum target ke barabar ho.
# Array Manipulation - Two Sum Problem
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Example
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
