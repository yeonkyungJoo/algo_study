import heapq
nums = []
while True:
    n = int(input())
    if n == -1:
        break

    if n == 0:
        print(heapq.heappop(nums) * (-1))
    else:
        heapq.heappush(nums, n * (-1))