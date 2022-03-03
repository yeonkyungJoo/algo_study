M, N = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))
# print(arr)

max_len = 0
dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
for i in range(1, M+1):
    for j in range(1, N+1):
        if arr[i-1][j-1] > 0:
            continue
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        max_len = max(dp[i][j], max_len)
print(max_len)
