from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)

        # Find common elements
        return list(set1 & set2)


# -------------------- Driver Code --------------------

if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    sol = Solution()
    result = sol.intersection(nums1, nums2)

    print("Intersection:", result)
