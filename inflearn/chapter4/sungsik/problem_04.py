# 마구간 정하기
import sys
sys.stdin = open('input4.txt','r')
def Count(len):
    cnt = 1
    ep = dist[0]
    for i in range(1, n):
        if dist[i] - ep >= len:
            cnt += 1
            ep = dist[i]
    return cnt

n, c = map(int, input().split())
dist = [int(input()) for _ in range(n)]
dist.sort()
l_ptr = 1
r_ptr = dist[n - 1]

while l_ptr <= r_ptr:
    m_ptr = (l_ptr + r_ptr) // 2
    if Count(m_ptr) >= c:
        res = m_ptr
        l_ptr = m_ptr + 1
    else:
        r_ptr = m_ptr - 1
print(res)
