import sys
#sys.stdin = open("../input.txt", "rt")

N = int(input())
words = dict()

for _ in range(N):
    key = input()
    words[key] = 1

for _ in range(N-1):
    key = input()
    words[key] -= 1

for k, v in words.items():
    if v == 1:
        print(k)
        break