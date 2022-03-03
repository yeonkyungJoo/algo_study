# 침몰하는 타이타닉
import sys
from collections import deque
#deque형 자료구조를 사용하면 list와 다르게 pop(0)을 하고나서 뒤의 인덱스를 전부다 앞으로 한칸씩 끌어오지 않고, 시작 포인터의 위치가 바뀐다.
sys.stdin = open('input4.txt', 'r')
n, m = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
w = deque(w)
cnt = 0
while w:
    if len(w) == 1:
        cnt += 1
        break
    if w[0] + w[-1] > m:
        w.pop()
        cnt += 1
    else:
        w.popleft()
        w.pop()
        cnt += 1

print(cnt)