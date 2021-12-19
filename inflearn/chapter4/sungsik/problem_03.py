# 뮤직비디오
import sys
sys.stdin = open('input4.txt','r')
def Count(capacity):
    cnt = 1
    sum = 0
    for x in song:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

n, m = map(int, input().split())
song = list(map(int, input().split()))
l_ptr = 1
r_ptr = sum(song)
result = 0
while l_ptr <= r_ptr:
    m_ptr = (l_ptr + r_ptr) // 2
    if Count(m_ptr) <= m:
        res = m_ptr
        r_ptr = m_ptr - 1
    else:
        l_ptr = m_ptr + 1
print(result)