from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # handle empty array
            return 0

        i = 0  # pointer to last unique element

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # found a new unique element
                i += 1
                nums[i] = nums[j]  # overwrite duplicate

        return i + 1  # number of unique elements

# Example usage:
nums = [0, 0, 1, 1, 1, 2, 2, 3]
sol = Solution()
k = sol.removeDuplicates(nums)

print("Number of unique elements:", k)      # Output: 4
print("Array after removing duplicates:", nums[:k])  # Output: [0, 1, 2, 3]
