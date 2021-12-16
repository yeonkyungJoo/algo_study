N, M = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()

cnt = 0
l, r = 0, N-1
while l < r:
    if weights[l] + weights[r] > M:
        cnt += 1
        r -= 1
    else:
        cnt += 1
        l += 1
        r -= 1

if l == r:
    cnt += 1
print(cnt)