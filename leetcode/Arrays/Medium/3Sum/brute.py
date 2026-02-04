def sum(nums):
    n = len(nums)
    result = set()
    for i in range(0, n):
        for j in range(i + 1, n-1):
            for k in range(j + 1, n-1):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)
    return list(result)

nums = [-1,0,1,2,-1,-4]
print("3 Sum is: ", sum(nums))