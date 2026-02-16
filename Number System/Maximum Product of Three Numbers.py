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


# def maxprod(nums):
#     max1 = max2 = max3 = float('-inf') 
#     min1 = min2 = float('inf') 
    
#     for num in nums:
#         if num > max1:
#             max3 = max2
#             max2 = max1
#             max1 = num
#         elif num > max2:
#             max3 = max2
#             max2 = num
#         elif num > max3:
#             max3 = num
            
            
#         if num < min1:
#             min2 = min1
#             min1 = num
#         elif num < min2:
#             min2 = num
            
#     return max(max1 * max2 * max3, min1 * min2 * max1)
    
# nums = [-10, 2, 4, 3, 1]
# print("Max of three number is: ", maxprod(nums))
            