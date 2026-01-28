from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        current_sum = 0

        for num in nums:
            current_sum += num
            result.append(current_sum)

        return result


# -------- Function Call --------
nums = [1, 2, 3, 4]

obj = Solution()                    # create object
output = obj.runningSum(nums)       # call function

print("Running Sum:", output)
