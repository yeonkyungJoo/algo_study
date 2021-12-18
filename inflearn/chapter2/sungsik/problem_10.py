import sys

sys.stdin = open("input.txt", "rt")
N = int(input())
result = list(map(int, input().split()))
score = 0
cnt = 0
for x in result:
    if x == 1:
        cnt += 1
        score += cnt
    else:
        cnt = 0

print(score)
