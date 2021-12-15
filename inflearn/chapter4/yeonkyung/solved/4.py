N, C = map(int, input().split())
points = []
for _ in range(N):
    points.append(int(input()))
points.sort()

result = 0
l, r = points[1] - points[0], points[-1] - points[0]
while l <= r:
    mid = (l + r) // 2

    curr = 0
    cnt = 1
    i = 1
    while i < len(points):
        if points[i] - points[curr] >= mid:
            cnt += 1
            curr = i
        i += 1

    if cnt >= C:
        result = max(result, mid)
        l = mid + 1
    else:
        r = mid - 1
print(result)

'''
if __name__ == "__main__":
    import sys
    # sys.stdin = open("input.txt", "rt")

    N, C = map(int, input().split())
    nums = []
    for _ in range(N):
        v = int(input())
        nums.append(v)
    nums.sort()

    l, r = nums[0], nums[-1]
    answer = 0
    while l <= r:
        # 가장 가까운 두 말의 최대 거리
        m = (l + r) // 2

        i = 1
        count = 1
        cur = nums[0]
        while i < len(nums):
            if nums[i] - cur >= m:
                count += 1
                cur = nums[i]
            i += 1

        if count < C:
            r = m - 1
        elif count >= C:
            answer = max(answer, m)
            l = m + 1

    print(answer)
'''