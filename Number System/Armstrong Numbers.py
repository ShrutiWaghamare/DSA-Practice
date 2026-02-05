# -------------------------------
# Palindrome Check for STRING
# -------------------------------
def is_palindrome_string(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


# -------------------------------
# Palindrome Check for NUMBER
# -------------------------------
def is_palindrome_number(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return original == reverse


# -------------------------------
# Examples
# -------------------------------
print(is_palindrome_string("madam"))   # True
print(is_palindrome_string("hello"))   # False

print(is_palindrome_number(121))       # True
print(is_palindrome_number(123))       # False
