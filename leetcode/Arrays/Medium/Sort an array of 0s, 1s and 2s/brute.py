def sort(nums):
    # n = len(nums)
    # count0, count1, count2 = 0, 0, 0
    # for i in range(n):
    #     if nums[i] == 0:
    #         count0 += 1
    #     elif nums[i] == 1:
    #         count1 += 1
    #     else:
    #         count2 += 1
    # index = 0
    # for _ in range(count0):
    #     nums[index] = 0
    #     index += 1
        
    # for _ in range(count1):
    #     nums[index] = 1
    #     index += 1
        
    # for _ in range(count2):
    #     nums[index] = 2
    #     index += 1
        
    # return nums
    nums.sort()
    return nums

nums = [0, 1, 2, 0, 1, 2]
print("After Sort: ", sort(nums))
        
        
        