class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Problem: Reverse Words in a String III
        --------------------------------------
        Given a string s, reverse the characters of each word while keeping the word order and spaces the same.
        
        Example:
        Input:  "Let's take LeetCode contest"
        Output: "s'teL ekat edoCteeL tsetnoc"
        
        Key Points:
        - Reverse characters only inside each word.
        - Words are separated by spaces.
        - Spaces remain in their original positions.
        - Use two-pointer technique to reverse each word in place.
        """
        
        # Convert string to list because strings are immutable in Python
        arr = list(s)
        n = len(arr)
        i = 0  # Pointer to traverse the string

        # Traverse the string character by character
        while i < n:
            if arr[i] != " ":  # If we find the start of a word
                start = i  # Mark the start of the word

                # Move i to the end of the word
                while i < n and arr[i] != " ":
                    i += 1
                end = i - 1  # Last character of the word

                # Reverse characters between start and end
                while start < end:
                    arr[start], arr[end] = arr[end], arr[start]
                    start += 1
                    end -= 1
            else:
                # If arr[i] is a space, just skip it
                i += 1

        # Convert the list back to string and return
        return ''.join(arr)


# Example Usage
s = "Let's take LeetCode contest"
solution = Solution()
print(solution.reverseWords(s))
# Output: "s'teL ekat edoCteeL tsetnoc"
