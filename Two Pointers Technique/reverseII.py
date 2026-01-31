from typing import List

# ================================
# Reverse String II - Brute Force
# ================================
def reverseStrBrute(s: str, k: int) -> str:
    """
    Brute-force approach:
    - Step 1: Iterate through string in blocks of 2k characters.
    - Step 2: Reverse the first k characters of each block using slicing [::-1].
    - Step 3: Leave the next k characters as-is.
    - Step 4: Concatenate all blocks into a new result string.

    Time Complexity: O(n)
    Space Complexity: O(n)  -> creates a new string
    """
    n = len(s)
    result = ""

    # Process string in blocks of 2k
    for i in range(0, n, 2*k):
        # Reverse first k characters of the block
        first_k = s[i:i+k][::-1]
        # Keep next k characters unchanged
        next_k = s[i+k:i+2*k]
        # Combine and append to result
        result += first_k + next_k

    return result


# ================================
# Reverse String II - Optimal Approach (Two-Pointer In-Place)
# ================================
def reverseStrOptimal(s: str, k: int) -> str:
    """
    Optimal two-pointer approach:
    - Step 1: Convert string to list to modify in-place.
    - Step 2: Iterate over string in blocks of 2k characters.
    - Step 3: Reverse first k characters of each block using two pointers.
    - Step 4: Handle edge cases where remaining characters < k.
    - Step 5: Convert list back to string.

    Time Complexity: O(n)
    Space Complexity: O(1) extra space (in-place)
    """
    # Convert string to list since strings are immutable
    s_list = list(s)
    n = len(s_list)

    # Process string in blocks of 2k
    for i in range(0, n, 2*k):
        # Set left pointer to start of block
        left = i
        # Set right pointer to end of first k characters of block
        # Use min() to avoid going out of bounds for the last block
        right = min(i + k - 1, n - 1)

        # Reverse first k characters using two-pointer swapping
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

    # Convert list back to string
    return "".join(s_list)


# ================================
# Example Usage
# ================================
if __name__ == "__main__":
    s = "abcdefghijk"
    k = 3

    print("Original string:", s)

    # Brute-force approach
    result_brute = reverseStrBrute(s, k)
    print("Brute-force result:", result_brute)  # Output: "cbadefihgjk"

    # Optimal two-pointer approach
    result_optimal = reverseStrOptimal(s, k)
    print("Optimal (in-place) result:", result_optimal)  # Output: "cbadefihgjk"
