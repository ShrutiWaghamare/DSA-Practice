class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # This will keep adding numbers as we move through the array
        total = 0
        
        # This will store the final count of valid subarrays
        answer = 0
        
        # This dictionary remembers how many times
        # a particular remainder has appeared
        # We start with remainder 0 seen once
        # (this helps count subarrays starting from index 0)
        seen = {0: 1}

        # Go through each number in the array
        for num in nums:
            # Add current number to running total
            total += num
            
            # Find remainder when divided by k
            r = total % k
            
            # Fix negative remainder (important in Python)
            if r < 0:
                r += k
            
            # If we have seen this remainder before,
            # it means numbers in between form a sum divisible by k
            if r in seen:
                answer += seen[r]
            
            # Record this remainder for future subarrays
            seen[r] = seen.get(r, 0) + 1

        # Return total count of valid subarrays
        return answer
