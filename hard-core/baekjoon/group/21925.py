# 시간 초과
N = int(input())
A = list(map(int, input().split()))

dic = {}
dp = [[0 for _ in range(N)] for _ in range(N)]
for k in range(1, N, 2):
    # 시작
    for i in range(0, N):
        if i+k < N:
            j = i + k
            if k == 1:
                if A[i] == A[j]:
                    dp[i][j] = 1
                    if i not in dic:
                        dic[i] = []
                    dic[i].append(j)
            else:
                if (i+1 < N and j-1 < N) and dp[i+1][j-1] == 1 and A[i] == A[j]:
                    dp[i][j] = 1
                    if i not in dic:
                        dic[i] = []
                    dic[i].append(j)
                else:
                    dp[i][j] = 0
# print(dp)
cnt = 0
s = 0
while True:
    if s not in dic:
        break
    t = min(dic[s])
    cnt += 1
    s = t + 1
if s == N:
    print(cnt)
else:
    print(-1)
