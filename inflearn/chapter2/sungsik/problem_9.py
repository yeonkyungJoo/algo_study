import sys
sys.stdin = open("input.txt", "rt")
N = int(input())
res = 0
for i in range(N):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        prize = 10000 + a * 1000
    elif a == b or a == c:
        prize = 1000 + (a * 100)
    elif b == c:
        prize = 1000 + (b * 100)
    else:
        prize = c * 100
    if prize > res:
        res = prize
print(res)
