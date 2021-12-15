from collections import deque
N = int(input())
nums = []
for _ in range(N):
    nums.append(deque(map(int, input().split())))
# print(nums)

M = int(input())
for _ in range(M):
    r, d, c = map(int, input().split())
    row = nums[r-1]
    while c > 0:
        if d == 0:
            row.append(row.popleft())
        else:
            row.appendleft(row.pop())
        c -= 1
count = 0
mid = N//2
for i in range(N):
    for j in range(mid-abs(mid-i), mid+abs(mid-i)+1):
        count += nums[i][j]
print(count)

