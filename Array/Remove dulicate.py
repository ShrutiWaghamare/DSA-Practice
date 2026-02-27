from typing import List

class Solution:
    # ✅ Approach 1: Two Pointer (ONLY for SORTED array)
    def removeDuplicates_sorted(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k

    # ✅ Approach 2: Seen Set (Works for UNSORTED array, preserves order)
    def removeDuplicates_seen(self, nums: List[int]) -> int:
        seen = set()
        k = 0

        for i in nums:
            if i not in seen:
                seen.add(i)
                nums[k] = i
                k += 1
        return k


# -------- DRIVER CODE --------
solution = Solution()

# Example 1 (Sorted array)
nums1 = [1, 1, 2]
k1 = solution.removeDuplicates_sorted(nums1)
print("Sorted approach:")
print("k =", k1)
print("nums =", nums1[:k1], "_ beyond k")

# Example 2 (Unsorted array)
nums2 = [1, 2, 1, 2, 3]
k2 = solution.removeDuplicates_seen(nums2)
print("\nSeen approach:")
print("k =", k2)
print("nums =", nums2[:k2], "_ beyond k")