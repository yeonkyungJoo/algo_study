N = int(input())
nums = list(map(int, input().split()))

result = False
def dfs(i, s1, s2):
    global result
    if i == N:
        if s1 == s2:
            result = True
        return

    dfs(i+1, s1+nums[i], s2)
    dfs(i+1, s1, s2+nums[i])

dfs(0, 0, 0)
if (result):
    print('YES')
else:
    print('NO')
