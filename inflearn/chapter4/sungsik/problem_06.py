# 씨름 선수
import sys
sys.stdin = open('input4.txt','r')
n = int(input())
member = []
for i in range(n):
    h, w = map(int, input().split())
    member.append((h, w))

member.sort(reverse=True)
largest = 0
cnt = 0
for h, w in member:
    if w > largest:
        largest = w
        cnt += 1
print(cnt)