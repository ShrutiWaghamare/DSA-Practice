def sum_using_index(arr):
    total = 0
    for i in range(len(arr)):   # i is index
        total += arr[i]
    return total


def sum_using_value(arr):
    total = 0
    for i in arr:               # i is value
        total += i
    return total


arr = [1, 2, 3, 4]

print("Sum using index:", sum_using_index(arr))
print("Sum using value:", sum_using_value(arr))