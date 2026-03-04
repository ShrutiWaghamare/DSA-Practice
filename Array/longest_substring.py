def longest_substring(s):
    maxlength = 0
    seen = set()
    left = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        maxlength = max(maxlength, right - left + 1)
    return maxlength
        
s = "abcabcbb" 
print(longest_substring(s))