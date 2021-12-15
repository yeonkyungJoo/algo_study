N = int(input())
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))
# print(nums)

max_sum = 0

# 행의 합
for i in range(N):
    r = 0
    c = 0
    for j in range(N):
        r += nums[i][j]
        c += nums[j][i]
    max_sum = max(max_sum, r)
    max_sum = max(max_sum, c)

# 대각선의 합
t1 = 0
t2 = 0
for i in range(N):
    for j in range(N):
        if i == j:
            t1 += nums[i][j]
            t2 += nums[i][N-1-j]
    max_sum = max(max_sum, t1)
    max_sum = max(max_sum, t2)
print(max_sum)