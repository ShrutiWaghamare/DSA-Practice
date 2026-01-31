"""
PROBLEM STATEMENT:
Given an integer array nums and an integer val,
remove all occurrences of val in nums IN-PLACE.
The order of elements may be changed.

Return k, where k is the number of elements in nums
that are NOT equal to val.

After removal:
- The first k elements of nums should be valid
- The remaining elements do not matter
"""

"""
EXAMPLE:
Input:
nums = [3, 2, 2, 3]
val = 3

After removing 3:
nums = [2, 2, _, _]
k = 2

Output:
2
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


# -------- DRIVER CODE (for normal Python run) --------
nums = [3, 2, 2, 3]
val = 3

obj = Solution()
k = obj.removeElement(nums, val)

print("k =", k)
print("Updated nums (first k elements):", nums[:k])
