# 랜선자르기
import sys
sys.stdin = open('input4.txt','r')
def Count(a):
    cnt = 0
    for x in line:
        cnt += (x // a)
    return cnt

k, n = map(int, input().split())
line = []
result = 0
longest = 0
for i in range(k):
    tmp = int(input())
    line.append(tmp)
    longest = max(longest, tmp)
l_ptr = 1
r_ptr = longest
while l_ptr < r_ptr:
    m_ptr = (l_ptr + r_ptr) // 2
    if Count(m_ptr) >= n:
        result = m_ptr
        l_ptr = m_ptr + 1
    else:
        r_ptr = m_ptr - 1
print(result)