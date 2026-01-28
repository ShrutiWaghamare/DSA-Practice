def majority_element(nums):
    candidate = None
    count = 0

    # Step 1: Find candidate
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Step 2: Verify candidate
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return None

# Example usage
arr = [3, 3, 4, 2, 3, 3, 3]
print("Majority element is:", majority_element(arr))
