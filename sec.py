# Python Data Structures & Algorithms (DSA) Questions
# Q5: Write a Python function to find the second largest number in a list.
# ✅ Solution:

def second_largest(arr):
    arr = list(set(arr))  # Remove duplicates
    arr.sort(reverse=True)
    return arr[1] if len(arr) > 1 else None

print(second_largest([10, 20, 4, 45, 99, 99]))  # Output: 45
