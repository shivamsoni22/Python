def max_subarray_sum(nums):
    max_sum = float('-inf')
    curr_sum = 0
    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
