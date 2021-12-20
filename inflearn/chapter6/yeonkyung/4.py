import sys
def dfs(idx):
    if idx == N:
        total = 0
        _total = 0
        for i in range(N):
            if ch[i] == 1:
                total += nums[i]
            else:
                _total += nums[i]
        if total == _total:
            print('YES')
            sys.exit()
        return

    ch[idx] = 1
    dfs(idx + 1)
    ch[idx] = 0
    dfs(idx + 1)

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    ch = [0 for _ in range(N)]

    dfs(0)
    print('NO')