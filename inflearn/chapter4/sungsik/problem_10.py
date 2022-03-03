# 역수열
import sys
sys.stdin = open('input4.txt', 'r')
n = int(input())
r_arr = list(map(int, input().split()))
arr = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if r_arr[i] == 0 and arr[j] == 0:
            arr[j] = i + 1
            break
        elif arr[j] == 0:
            r_arr[i] -= 1
for x in arr:
    print(x, end=' ')