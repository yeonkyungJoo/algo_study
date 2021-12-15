N = int(input())
nums = []
nums.append([0 for _ in range(N+2)])
for _ in range(N):
    tmp = [0]
    tmp.extend(list(map(int, input().split())))
    tmp.append(0)
    nums.append(tmp)
nums.append([0 for _ in range(N+2)])
# print(nums)

def check(i, j):
    result = True
    n = nums[i][j]
    if nums[i-1][j] >= n or nums[i+1][j] >= n or nums[i][j-1] >= n or nums[i][j+1] >= n:
        result = False
    return result

count = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if (check(i, j)):
            count += 1
print(count)