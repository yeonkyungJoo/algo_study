# 정다면체

N, M = map(int, input().split())
arr = [0] * (N + M + 3)
max = -float('inf')
for i in range(1, N + 1):
    for j in range(1, M + 1):
        plus = i + j
        arr[plus] += 1

for i in range(N + M + 1):
    if arr[i] > max:
        max = arr[i]

for i in range(N + M + 1):
    if arr[i] == max:
        print(i, end = ' ')