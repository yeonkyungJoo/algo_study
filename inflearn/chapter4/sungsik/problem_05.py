# 회의실 배정
import sys

sys.stdin = open('input4.txt','r')
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e)) # 튜플 형태로 리스트에 추가
meeting.sort(key = lambda x : (x[1], x[0])) # sorting 우선순위 정해줌
end_time = 0
cnt = 0
for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1

print(cnt)