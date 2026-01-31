"""
Move all Zeros to End of Array

Given an array of integers arr[], move all the zeros to the end of the array
while maintaining the relative order of all non-zero elements.

We will cover three approaches:

1. Naive Approach (Using Temporary Array)
2. Better Approach (Two Traversals, in-place)
3. Expected Approach (One Traversal with Swap, in-place)
"""

# --------------------------
# 1️⃣ Naive Approach: Using Temporary Array
# Time Complexity: O(n), Space Complexity: O(n)
# --------------------------
def pushZerosToEnd_naive(arr):
    n = len(arr)
    temp = [0] * n  # Create a temporary array of same size
    
    # Copy all non-zero elements to temp
    j = 0
    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1
    
    # Remaining positions in temp are already 0
    # Copy temp back to original array
    for i in range(n):
        arr[i] = temp[i]

# --------------------------
# 2️⃣ Better Approach: Two Traversals (In-place)
# Time Complexity: O(n), Space Complexity: O(1)
# --------------------------
def pushZerosToEnd_two_traversals(arr):
    count = 0  # Pointer for next non-zero element
    
    # First traversal: shift non-zero elements to front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    
    # Second traversal: fill remaining elements with zeros
    while count < len(arr):
        arr[count] = 0
        count += 1

# --------------------------
# 3️⃣ Expected Approach: One Traversal with Swap (In-place)
# Time Complexity: O(n), Space Complexity: O(1)
# --------------------------
def pushZerosToEnd_one_traversal(arr):
    count = 0  # Pointer for next non-zero element
    
    for i in range(len(arr)):
        if arr[i] != 0:
            # Swap the current element with element at index 'count'
            arr[i], arr[count] = arr[count], arr[i]
            count += 1

# --------------------------
# DRIVER CODE to test all approaches
# --------------------------
if __name__ == "__main__":
    arr1 = [1, 2, 0, 4, 3, 0, 5, 0]
    arr2 = arr1.copy()
    arr3 = arr1.copy()

    # Using Naive Approach
    pushZerosToEnd_naive(arr1)
    print("Naive Approach:", arr1)  # Output: [1, 2, 4, 3, 5, 0, 0, 0]

    # Using Two Traversals
    pushZerosToEnd_two_traversals(arr2)
    print("Two Traversals:", arr2)  # Output: [1, 2, 4, 3, 5, 0, 0, 0]

    # Using One Traversal with Swap
    pushZerosToEnd_one_traversal(arr3)
    print("One Traversal with Swap:", arr3)  # Output: [1, 2, 4, 3, 5, 0, 0, 0]
