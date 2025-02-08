def array_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

print(array_intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]
