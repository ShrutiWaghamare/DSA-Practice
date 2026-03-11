n = int(input())
min_digit = 9
max_digit = 0
while n > 0:
    digit = n % 10
    min_digit = min(min_digit, digit)
    max_digit = max(max_digit, digit)
    n = n // 10
print(min_digit, max_digit)