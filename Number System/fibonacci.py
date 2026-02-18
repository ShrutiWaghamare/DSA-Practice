def fib(n):
    result = []
    if n <= 1:
        return n
    a, b = 0, 1
    for _  in range(2, n+1):
        result.append(a)
        a, b = b, a + b
    return result
print(fib(10))
    
    