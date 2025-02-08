def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b

fibonacci(50)  # Output: 0 1 1 2 3 5 8 13 21 34
