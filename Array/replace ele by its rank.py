n = int(input())
arr = list(map(int, input().split()))
sorted_uni = sorted(set(arr))
rank = {}
for i in range(len(sorted_uni)):
    rank[sorted_uni[i]] = i + 1
result = []
for num in arr:
    result.append(rank[num])
print(*result)