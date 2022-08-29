import sys
from collections import deque
#sys.stdin = open("../input.txt", "rt")

N, K = map(int, input().split())
nums = deque([i for i in range(1, N+1)])

i = 1
while len(nums) > 1:
    if i == K:
        nums.popleft()
        i = 1
    else:
        nums.append(nums.popleft())
        i += 1
print(nums[0])