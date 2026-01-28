from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]

            if left == right:
                return i

            left = left + nums[i]

        return -1


# -------- Driver Code --------
nums = [1, 7, 3, 6, 5, 6]
obj = Solution()
result = obj.pivotIndex(nums)

print("Pivot Index:", result)
