arr = list(map(int, input().split()))
m = int(input())
min_diff = float('inf')
arr.sort()
for i in range(len(arr)-m+1):
    diff = arr[i+m-1]-arr[i]
    min_diff = min(min_diff, diff)
print(min_diff)