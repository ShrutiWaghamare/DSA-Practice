n = input()
min_digit = 9
max_digit = 0
for digit in n:
    digit = int(digit)
    min_digit = min(min_digit, digit)
    max_digit = max(max_digit, digit)
print(min_digit, max_digit)