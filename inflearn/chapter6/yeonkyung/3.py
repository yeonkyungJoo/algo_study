import sys
# sys.stdin = open("input.txt", "r")

N = int(input())
ch = [0 for _ in range(N+1)]

def dfs(n):
    if n > N:
        if sum(ch) == 0:
            return
        for i in range(1, N+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
        return

    ch[n] = 1
    dfs(n+1)
    ch[n] = 0
    dfs(n+1)

dfs(1)

