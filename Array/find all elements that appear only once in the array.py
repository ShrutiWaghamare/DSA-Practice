arr = [1, 2, -1, 1, 3, 1]
n = len(arr)
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
for num in arr:
    if freq[num] == 1:
        print(num, end= " ")