def longestSubarray(arr):
    maxlength = 0
    for i in range(len(arr)):
        count0 = 0
        count1 = 0
        for j in range(i, len(arr)):
            if arr[j] == 0:
                count0 += 1
            else:
                count1 += 1
            
            if count0 == count1:
                maxlength = max(maxlength, j - i + 1)
    return maxlength, arr[:maxlength]

arr = [0, 1, 1, 0, 0, 1, 1]
print(longestSubarray(arr))