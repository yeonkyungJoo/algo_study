from collections import deque
N, K = map(int, input().split())

queue = deque([i for i in range(1, N+1)])
n = 0
while len(queue) > 1:

    n += 1
    if n == K:
        queue.popleft()
        n = 0
    else:
        queue.append(queue.popleft())
print(queue[0])