N, M = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(N):
    if nums[i] == M:
        count += 1
        continue
    for j in range(i+1, N):
        s = sum(nums[i:j+1])
        if s == M:
            count += 1
        elif s > M:
            break
print(count)