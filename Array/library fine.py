arr = list(map(int, input().split()))
k = int(input())
total_fine = 0
for i in range(len(arr)):
    if arr[i] > k:
        extra_days = arr[i] - k
        total_fine += extra_days
print(total_fine)
        
