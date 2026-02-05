# ------------------------------------
# 1️⃣ Print Fibonacci series (normal printing)
# ------------------------------------
def print_fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # new line


# ------------------------------------
# 2️⃣ Sum of first n Fibonacci numbers
# (F(0) to F(n-1))
# ------------------------------------
def fib_sum_first_n(n):
    a, b = 0, 1
    total = 0

    for i in range(n):
        total += a
        a, b = b, a + b

    return total


# ------------------------------------
# 3️⃣ Sum of Fibonacci numbers from F(0) to F(n)
# ------------------------------------
def fib_sum_upto_n(n):
    a, b = 0, 1
    total = 0

    for i in range(n + 1):
        total += a
        a, b = b, a + b

    return total


# ------------ Testing ------------
print("Fibonacci series (first 5 terms):")
print_fib(5)                      # 0 1 1 2 3

print("Sum of first 4 Fibonacci numbers:")
print(fib_sum_first_n(4))         # 4  -> 0+1+1+2

print("Sum of Fibonacci numbers up to n = 4:")
print(fib_sum_upto_n(4))          # 7  -> 0+1+1+2+3
