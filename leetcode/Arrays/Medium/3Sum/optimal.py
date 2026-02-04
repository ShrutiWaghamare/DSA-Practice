def sum(nums):
    n = len(nums)
    result = []
    nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left = i + 1
        right = n - 1
        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            if cur_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left]==nums[left-1]:
                    left += 1
                while left < right and nums[left]==nums[left-1]:
                    right -= 1
            elif cur_sum < 0:
                left += 1
            else:
                right -= 1
    return result
            
    

nums = [-1,0,1,2,-1,-4]
print("3 Sum is: ", sum(nums))