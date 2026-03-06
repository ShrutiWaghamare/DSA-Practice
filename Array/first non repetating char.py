from collections import Counter
s = input()
count = Counter(s)
for ch in s:
    if count[ch] == 1:
        print(ch)
        break
else:
    print(-1)