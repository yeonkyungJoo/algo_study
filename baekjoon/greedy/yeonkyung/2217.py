from collections import deque

N = int(input())
weights = []
for _ in range(N):
    weights.append(int(input()))

result = []
weights.sort()
size = len(weights)
weights = deque(weights)
while weights:
    n = weights.popleft()
    result.append(n * size)
    size -= 1
print(max(result))