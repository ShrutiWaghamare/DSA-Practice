from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1


# -------- Function Call --------
nums = [0, 1, 0, 3, 12]

obj = Solution()          # create object of Solution class
obj.moveZeroes(nums)      # call function

print("After moving zeroes:", nums)
