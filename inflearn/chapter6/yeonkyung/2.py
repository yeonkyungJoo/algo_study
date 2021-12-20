def dfs(n):
    if n > 7:
        return

    dfs(2 * n)
    dfs(2 * n + 1)
    print(n, end=' ')

if __name__ == "__main__":
    dfs(1)