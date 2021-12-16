N = int(input())

players = []
for _ in range(N):
    h, w = map(int, input().split())
    players.append((h, w))
players.sort(key=lambda x:-x[0])
# print(players)

stack = []
for h, w in players:
    if not stack:
        stack.append(w)
    else:
        if w > stack[-1]:
            stack.append(w)
print(len(stack))