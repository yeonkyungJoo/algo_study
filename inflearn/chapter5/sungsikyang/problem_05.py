# 공주 구하기(큐 자료구조로 해결)
# 큐 자료구조는 FIFO, First In First Out 이다
import sys
from collections import deque
sys.stdin = open('input5.txt', 'r')
n, k = map(int, input().split())
dq = list(range(1, n + 1))
dq = deque(dq)
while dq:
    for _ in range(k - 1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()