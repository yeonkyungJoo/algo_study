# 이분검색
import sys

sys.stdin = open('input4.txt','r')

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
l_ptr = 0
r_ptr = n - 1

while l_ptr <= r_ptr:
    m_ptr = (l_ptr + r_ptr) // 2
    if num[m_ptr] == m:
        print(m_ptr + 1)
        break
    elif num[m_ptr] > m:
        r_ptr = m_ptr - 1
    else:
        l_ptr = m_ptr + 1
