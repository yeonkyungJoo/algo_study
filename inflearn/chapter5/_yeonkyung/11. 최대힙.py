import sys
import heapq
# sys.stdin = open("../input.txt", "rt")

nums = []
while True:
    n = int(input())
    if n == -1:
        break

    if n > 0:
        heapq.heappush(nums, n * (-1))
    elif n == 0:
        if nums:
            print(heapq.heappop(nums) * (-1))
        else:
            print(-1)