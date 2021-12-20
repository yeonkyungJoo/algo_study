def dfs(idx):
    if idx == N + 1:
        for i in range(1, N+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
        return

    ch[idx] = 1
    dfs(idx + 1)
    ch[idx] = 0
    dfs(idx + 1)

if __name__ == "__main__":
    N = int(input())
    ch = [0 for _ in range(N+1)]
    dfs(1)
