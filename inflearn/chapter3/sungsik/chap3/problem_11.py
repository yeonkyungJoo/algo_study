# 격자판 회문수
import sys
sys.stdin = open('input.txt','r')
arr = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(3):
    for j in range(7):
        tmp = arr[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if arr[i + k][j] != arr[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1
print(cnt)