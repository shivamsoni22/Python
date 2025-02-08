def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2  # Sum of first N natural numbers
    return total_sum - sum(arr)

print(find_missing_number([1, 2, 4, 5, 6], 6))  # Output: 3
