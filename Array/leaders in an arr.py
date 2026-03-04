def leaders(arr):
    result = []
    n = len(arr)
    maxright = arr[n-1]
    result.append(maxright)
    for i in range(n-2,-1,-1):
        if arr[i] >= maxright:
            maxright = arr[i]
            result.append(maxright)
    return result[::-1]
    

arr = [16, 17, 4, 3, 5, 2]
print(leaders(arr))