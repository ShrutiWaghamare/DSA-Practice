from collections import Counter
s = input("Enter String: ")
count = Counter(s)
for ch in s:
    if count[ch] == 1:
        print(ch)
        break
else:
    print(-1)