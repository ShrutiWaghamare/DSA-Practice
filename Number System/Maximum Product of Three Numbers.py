def maximumProduct(nums):
    # Step 1: Sort the array
    nums.sort()
    n = len(nums)

    # Step 2: Two possible maximum products
    # Case 1: product of three largest numbers
    product1 = nums[n-1] * nums[n-2] * nums[n-3]

    # Case 2: product of two smallest numbers (can be negative)
    # and the largest number
    product2 = nums[0] * nums[1] * nums[n-1]

    # Step 3: Return the maximum of both
    return max(product1, product2)


# ----------------------------
# Example
# ----------------------------
nums = [-10, -10, 5, 2]
print("Maximum product:", maximumProduct(nums))
