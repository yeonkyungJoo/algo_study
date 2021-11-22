N = int(input())
rope = []
max_weight = []
for _ in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
for i in range(1, N + 1):
    max_weight.append(rope[i - 1] * i)
print(max(max_weight))