def missing(arr, n):
    total = n * (n + 1)//2
    actual = sum(arr)
    return total - actual

arr = [1, 2, 3, 5]
print(missing(arr, 5))
    