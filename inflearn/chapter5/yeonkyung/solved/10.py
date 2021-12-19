import heapq
nums = []
# heapq.heapify(nums)
while True:
    n = int(input())
    if n == -1:
        break

    if n == 0:
        print(heapq.heappop(nums))
    else:
        heapq.heappush(nums, n)