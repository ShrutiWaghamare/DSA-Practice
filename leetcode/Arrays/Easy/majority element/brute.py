def majority_element(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > len(nums) // 2:
            return num
    return None  # if no majority element

# Example usage
arr = [3, 3, 4, 2, 3, 3, 3]
print("Majority element is:", majority_element(arr))
