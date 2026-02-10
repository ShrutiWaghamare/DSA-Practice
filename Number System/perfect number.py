import math

# -------------------------------
# Approach 1: Brute Force
# Time: O(n)
# -------------------------------
def isPerfect_bruteforce(n: int) -> bool:
    if n <= 1:
        return False

    divisor_sum = 0

    # check all numbers from 1 to n-1
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i

    return divisor_sum == n


# -------------------------------
# Approach 2: Optimized (√n)
# Time: O(√n)
# -------------------------------
def isPerfect_optimized(n: int) -> bool:
    if n <= 1:
        return False

    divisor_sum = 1   # 1 is always a proper divisor
    i = 2

    while i * i <= n:
        if n % i == 0:
            divisor_sum += i

            # add the paired divisor
            if i != n // i:
                divisor_sum += n // i

        i += 1

    return divisor_sum == n


# -------------------------------
# Testing
# -------------------------------
nums = [6, 15, 28, 12]

for n in nums:
    print(f"{n}: BruteForce={isPerfect_bruteforce(n)}, Optimized={isPerfect_optimized(n)}")
