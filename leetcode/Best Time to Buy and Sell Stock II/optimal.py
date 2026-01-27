from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit


# -------- Function Call --------
prices = [7, 1, 5, 3, 6, 4]

obj = Solution()                 # create object of Solution class
result = obj.maxProfit(prices)   # call the function

print("Maximum Profit:", result)
