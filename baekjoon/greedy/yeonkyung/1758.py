from collections import deque

N = int(input())
tips = []
for _ in range(N):
    tips.append(int(input()))
tips.sort(reverse=True)
tips = deque(tips)

idx = 1
result = 0
while tips:
    n = tips.popleft()
    result += n - (idx - 1) if n - (idx - 1) >= 0 else 0
    idx += 1
print(result)