def larsub(arr):
    prefixsum = 0
    hashmap = {}
    maxlength = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            prefixsum += -1
        else:
            prefixsum += 1
        
        if prefixsum == 0:
            maxlength = i + 1
        
        if prefixsum in hashmap:
            length = i - hashmap[prefixsum]
            maxlength = max(maxlength, length)
        else:
            hashmap[prefixsum] = i
    return maxlength

arr = [0, 1, 1, 0, 0, 1, 1]
print(larsub(arr))