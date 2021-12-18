# 수들의 합
import sys

sys.stdin = open("input.txt", 'r')
N, M = map(int, input().split())
arr = list(map(int, input().split()))

r_ptr, l_ptr = 1, 0
total = arr[0]
cnt = 0

while True:
    if total < M:
        if r_ptr < N:
            total += arr[r_ptr]
            r_ptr += 1
        else:
            break
    elif total == M:
        cnt += 1
        total -= arr[l_ptr]
        l_ptr += 1
    else:
        total -= arr[l_ptr]
        l_ptr += 1
print(cnt)