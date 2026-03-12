n = int(input())
arr = list(map(int, input().split()))

current_sum = 0
max_sum = float('-inf')

for num in arr:
    current_sum += num
    max_sum = max(max_sum, current_sum)

    if current_sum < 0:
        current_sum = 0

print(max_sum)