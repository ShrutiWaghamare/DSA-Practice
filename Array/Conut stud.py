N, M = map(int, input().split())
marks = []
for i in range(N):
    row = list(map(int, input().split()))
    marks.append(row)
avg = []
for j in range(M):
    total = 0
    for i in range(N):
        total += marks[i][j]
    avg.append(total/N)

count = 0
for i in range(N):
    for j in range(M):
        if marks[i][j] > avg[j]:
            count += 1
            break
print(count)