class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Case 1: power is 0
        if n == 0:
            return 1

        # Case 2: negative power
        if n < 0:
            x = 1 / x
            n = -n

        # Case 3: positive power
        result = 1
        for _ in range(n):
            result *= x

        return result


# ----- Driver Code -----
if __name__ == "__main__":
    sol = Solution()

    print(sol.myPow(2.0, 10))   # 1024.0
    print(sol.myPow(2.1, 3))    # 9.261
    print(sol.myPow(2.0, -2))   # 0.25
    print(sol.myPow(5.0, 0))    # 1
