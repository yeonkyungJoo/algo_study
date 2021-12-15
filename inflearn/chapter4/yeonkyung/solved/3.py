import sys
N, M = map(int, input().split())
songs = list(map(int, input().split()))

result = sys.maxsize
l, r = 0, sum(songs)

while l <= r:
    mid = (l + r) // 2

    cnt = 0
    tmp = 0
    for i in range(N):
        tmp += songs[i]
        if tmp > mid:
            cnt += 1
            tmp = songs[i]
    if tmp != 0:
        cnt += 1

    if cnt <= M:
        result = min(result, mid)
        r = mid - 1
    else:
        l = mid + 1
print(result)