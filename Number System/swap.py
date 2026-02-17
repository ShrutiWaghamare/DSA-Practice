s = "hello world shruti"
w = s.split()
# w[0], w[1] = w[1], w[0] #if there are only two words in a strinng
w[0], w[-1] = w[-1], w[0] #if string is large
print(" ".join(w))

print(" ".join(s.split()[::-1]))

def swap(s):
    w = s.split()
    result = []
    for i in range(len(w)-1, -1, -1):
        result.append(w[i])
    return " ".join(result)
    
print(swap("Shreyash Deepak Waghamare"))


# a, b = b , a
# temp = a
# a = b
# b = temp