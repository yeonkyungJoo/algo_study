from collections import deque
board = deque(input())
queue = deque()

tmp = []
while board:
    c = board.popleft()
    if tmp:
        if c == tmp[-1]:
            tmp.append(c)
        else:
            queue.append(''.join(tmp))
            tmp = [c]
    else:
        tmp.append(c)
queue.append(''.join(tmp))
# print(queue)

result = []
for s in queue:
    if s.startswith('X'):

        if len(s) % 2 != 0:
            print(-1)
            break

        n = len(s) // 4
        result.append('AAAA' * n)

        r = len(s) - (n * 4)
        if r != 0:
            result.append('BB' * (r // 2))
    else:
        result.append(s)
else:
    print(''.join(result))
