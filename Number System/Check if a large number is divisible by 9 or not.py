# -----------------------------
# Check divisibility by 9
# -----------------------------

# 1️⃣ Using a number
def is_divisible_by_9_num(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10   # get last digit
        n //= 10               # remove last digit
    return digit_sum % 9 == 0

# 2️⃣ Using a string
def is_divisible_by_9_str(s):
    digit_sum = 0
    for ch in s:
        digit_sum += int(ch)   # convert char to number and add
    return digit_sum % 9 == 0

# -----------------------------
# Examples
# -----------------------------
num = 69354
s = "69354"

print("Number version:", is_divisible_by_9_num(num))  # False
print("String version:", is_divisible_by_9_str(s))    # False
