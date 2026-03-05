str1 = input()
str2 = input()
result = ""
for ch in str1:
    if ch not in str2:
        result += ch
print(result)