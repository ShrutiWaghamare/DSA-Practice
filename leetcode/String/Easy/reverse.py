from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse a list of characters in-place.
        
        Approach: Two-Pointer Swapping
        - We use two pointers, 'left' starting at the beginning of the list
          and 'right' starting at the end of the list.
        - Swap the elements at 'left' and 'right'.
        - Move 'left' forward and 'right' backward.
        - Stop when left >= right.
        
        Time Complexity: O(n) -> each element swapped at most once
        Space Complexity: O(1) -> in-place, no extra array used
        """

        # Step 1: Initialize two pointers
        left = 0              # Start of the list
        right = len(s) - 1    # End of the list

        # Step 2: Loop until pointers meet or cross
        while left < right:
            # Swap elements at left and right positions
            s[left], s[right] = s[right], s[left]

            # Move pointers towards the center
            left += 1
            right -= 1

        # No return needed because 's' is modified in-place
