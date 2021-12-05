N, M = map(int, input().split())

count = [0] * (N+M+1)
for n in range(1, N+1):
    for m in range(1, M+1):
        count[n+m] += 1
# print(result)
result = []
max_count = 0
for i, c in enumerate(count):
    if c > max_count:
        result = [i]
        max_count = c
    elif c == max_count:
        result.append(i)

for n in result:
    print(n, end=' ')