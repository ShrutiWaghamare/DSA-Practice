class Solution:
    def fib(self, n: int) -> int:
        # Initialize first two Fibonacci numbers
        a, b = 0, 1
        
        # Loop n times to reach the nth Fibonacci number
        for _ in range(n):
            a, b = b, a + b  # Update a to b, and b to a+b
        
        # Return the nth Fibonacci number
        return a

# Example usage:
sol = Solution()
n = 10
print(f"The {n}th Fibonacci number is:", sol.fib(n))  # Output: 55
