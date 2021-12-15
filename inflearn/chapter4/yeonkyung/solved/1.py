N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

l, r = 0, N-1
while l <= r:
    mid = (l + r) // 2
    if nums[mid] == M:
        print(mid + 1)
        break
    elif nums[mid] < M:
        l = mid + 1
    elif nums[mid] > M:
        r = mid - 1
