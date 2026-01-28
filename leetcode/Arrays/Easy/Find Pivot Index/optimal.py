from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1


# ---- Driver Code ----
nums = [1, 7, 3, 6, 5, 6]
solution = Solution()
result = solution.pivotIndex(nums)

print("Pivot Index:", result)
