from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  # create a result array of same size
        left = 0           # start pointer
        right = n - 1      # end pointer
        pos = n - 1        # position to fill in result (from end)
        
        # Loop until all elements are placed
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                left += 1
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1  # move to next position from end
        
        return result

# Example usage:
nums = [-4, -1, 0, 3, 10]
print(Solution().sortedSquares(nums))  # Output: [0, 1, 9, 16, 100]
