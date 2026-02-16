def power(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n // 2
    if n == 1:
        return True
    else:
        return False

print("Power of 2 is 4: ", power(4))