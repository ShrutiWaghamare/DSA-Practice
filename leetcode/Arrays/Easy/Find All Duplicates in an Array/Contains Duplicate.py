from typing import List

# --------------------------------------------------
# Approach 1: Dictionary / Frequency Map (Your Approach)
# --------------------------------------------------
class SolutionDict:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] >= 2:
                return True

        return False


# --------------------------------------------------
# Approach 2: Set-Based (Optimal Approach)
# --------------------------------------------------
class SolutionSet:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


# --------------------------------------------------
# Driver Code (Main Program)
# --------------------------------------------------
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 1]

    dict_solution = SolutionDict()
    set_solution = SolutionSet()

    print("Input Array:", nums)
    print("Using Dictionary Approach:", dict_solution.containsDuplicate(nums))
    print("Using Set (Optimal) Approach:", set_solution.containsDuplicate(nums))
