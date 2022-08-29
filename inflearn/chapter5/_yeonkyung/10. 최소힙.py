import sys
import heapq
# sys.stdin = open("../input.txt", "rt")

nums = []
# heapq.heapify(nums)

while True:
    n = int(input())
    if n == -1:
        break

    if n > 0:
        heapq.heappush(nums, n)
    elif n == 0:
        if nums:
            print(heapq.heappop(nums))
        else:
            print(-1)

