C, N = map(int, input().split())
weights = []
for _ in range(N):
    weights.append(int(input()))

max_weight = 0
def dfs(i, total):
    global max_weight

    if i == N:
        max_weight = max(max_weight, total)
        return

    if total + weights[i] <= C:
        dfs(i+1, total + weights[i])
    dfs(i+1, total)

dfs(0, 0)
print(max_weight)