from collections import deque
order = deque(input())
arr = [0 for _ in range(26)]
for c in order:
    arr[ord(c) - ord('A')] = 1
N = int(input())

for i in range(N):
    result = 'YES'

    _order = order.copy()
    plan = deque(input())
    while plan:
        p = plan.popleft()
        if arr[ord(p) - ord('A')] != 0:
            if _order:
                if p == _order[0]:
                    _order.popleft()
                else:
                    result = 'NO'
                    break

    if _order:
        result = 'NO'
    print('#{} {}'.format(i+1, result))