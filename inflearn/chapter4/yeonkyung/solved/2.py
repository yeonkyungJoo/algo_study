K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))
lines.sort()

result = 0
l, r = 0, max(lines)
while l <= r:
    mid = (l + r) // 2

    cnt = 0
    for line in lines:
        cnt += line // mid

    if cnt >= N:
        result = max(result, mid)
        l = mid + 1
    else:
        r = mid - 1
print(result)