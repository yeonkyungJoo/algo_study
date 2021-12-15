N = int(input())
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))

count = 0
mid = N//2
for i in range(mid+1):
    count += nums[i][mid]
    j = 1
    while j <= i:
        count += nums[i][mid-j]
        count += nums[i][mid+j]
        j += 1

for i in range(mid+1, N):
    count += nums[i][mid]
    j = 1
    while j <= (2 * mid - i):
        count += nums[i][mid-j]
        count += nums[i][mid+j]
        j += 1
print(count)