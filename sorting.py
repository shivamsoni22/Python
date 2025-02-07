#  Sorting & Searching - Find Missing Number
# Question:
# Ek sorted array diya gaya hai jisme 1 se n tak numbers hone chahiye, ek number missing hai, use find karo.
def find_missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)

# Example
print(find_missing_number([1, 2, 4, 5, 6]))  # Output: 3
