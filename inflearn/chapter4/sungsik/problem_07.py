# 창고 정리
import sys
sys.stdin = open('input4.txt', 'r')
l = int(input())
h = list(map(int, input().split()))
m = int(input())
h.sort(reverse=True)
while m > 0:
    h[0] -= 1
    h[-1] += 1
    m -= 1
    h.sort(reverse=True)
result = h[0] - h[-1]
print(result)