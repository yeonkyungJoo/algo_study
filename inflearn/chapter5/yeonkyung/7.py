from collections import deque
order = deque(input())
N = int(input())

for i in range(N):
    result = 'YES'

    _order = order.copy()
    plan = deque(input())
    while plan:
        p = plan.popleft()
        if _order and p == _order[0]:
            _order.popleft()

    if _order:
        result = 'NO'
    print('#{} {}'.format(i+1, result))