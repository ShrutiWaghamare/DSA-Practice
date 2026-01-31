def reverse(s):
    """
    Problem: Reverse a string while preserving space positions
    ----------------------------------------------------------
    Given a string s, reverse all characters but keep spaces in their original positions.

    Example:
    Input:  "shruti deepak waghamare"
    Output: "eramah gawkap eediturhs"

    Key Points:
    - Reverse letters only.
    - Spaces must stay at the same index.
    - Two-pointer approach is optimal.
    - This is a classic string manipulation problem that can appear in interviews.
    - Problem difficulty: Medium (requires careful pointer handling and attention to details).
    """

    # Convert string to list because strings are immutable in Python
    arr = list(s)
    left = 0               # Pointer starting from beginning
    right = len(arr) - 1   # Pointer starting from end

    # Traverse the string until pointers meet
    while left < right:
        if arr[left] == " ":
            # Skip spaces from the left
            left += 1
        elif arr[right] == " ":
            # Skip spaces from the right
            right -= 1
        else:
            # Swap letters at left and right pointers
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # Convert list back to string and return
    return "".join(arr)


# Example Usage
s = "shruti deepak waghamare"
print("Reverse string is: ", reverse(s))
# Output: "eramah gawkap eediturhs"
