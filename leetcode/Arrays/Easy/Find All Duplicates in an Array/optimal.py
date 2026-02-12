from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}      # dictionary to store count of each number
        result = []    # list to store duplicates

        # Step 1: Count frequency of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Collect numbers that appear exactly twice
        for num, count in freq.items():
            if count == 2:
                result.append(num)

        return result


# ----------------- Example Usage -----------------
if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    sol = Solution()
    print(sol.findDuplicates(nums))   # Output: [3, 2]
