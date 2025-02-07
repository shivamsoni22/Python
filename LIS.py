from bisect import bisect_left

def length_of_lis(nums):
    sub = []
    for num in nums:
        idx = bisect_left(sub, num)
        if idx == len(sub):
            sub.append(num)
        else:
            sub[idx] = num
    return len(sub)

print(length_of_lis([10,9,2,5,3,7,101,18]))  # Output: 4
