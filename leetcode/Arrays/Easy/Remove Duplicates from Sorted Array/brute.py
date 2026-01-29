from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique = []  # new array to store unique elements

        for num in nums:
            if num not in unique:  # check if already added
                unique.append(num)

        # Copy back to nums (optional, depends on requirement)
        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)  # number of unique elements

# Example usage
nums = [0, 0, 1, 1, 1, 2, 2, 3]
sol = Solution()
k = sol.removeDuplicates(nums)

print("Number of unique elements:", k)      # 4
print("Array after removing duplicates:", nums[:k])  # [0, 1, 2, 3]
