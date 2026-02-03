class Solution:
    """
    Problem: Reverse the words in a string.
    - Remove extra spaces
    - Keep words in reverse order
    - Only one space between words
    """

    # -------------------------
    # Approach 1: Brute Force
    # -------------------------
    def reverseWordsBruteForce(self, s: str) -> str:
        """
        Brute force approach:
        - Build words character by character
        - Ignore extra spaces
        - Reverse the word list
        - Join words with single space
        """
        words = []          # List to store words
        current_word = ""   # Temporary string to build each word

        # Step 1: Read each character in the string
        for ch in s:
            if ch != " ":                  # If character is not a space
                current_word += ch         # Add it to the current word
            else:                          # If character is a space
                if current_word != "":     # Save word if current_word is not empty
                    words.append(current_word)
                    current_word = ""      # Reset for the next word

        # Step 2: Add the last word if string didn't end with a space
        if current_word != "":
            words.append(current_word)

        # Step 3: Reverse the list of words
        words.reverse()

        # Step 4: Join words with a single space
        return " ".join(words)


    # -------------------------
    # Approach 2: Python Built-in (Optimal)
    # -------------------------
    def reverseWordsOptimized(self, s: str) -> str:
        """
        Python built-in approach:
        - split() automatically removes extra spaces
        - reverse the list of words
        - join() them with single space
        """
        # Step 1: Split the string into words (ignores extra spaces)
        words = s.split()

        # Step 2: Reverse the word list
        words.reverse()

        # Step 3: Join the reversed words with a single space
        return " ".join(words)


# -------------------------
# Example Usage
# -------------------------
s = "  shruti   deepak  waghamare "

solution = Solution()

# Using brute force approach
result_brute = solution.reverseWordsBruteForce(s)
print("Brute Force Output:", result_brute)

# Using Python built-in approach
result_opt = solution.reverseWordsOptimized(s)
print("Optimized Output:  ", result_opt)
