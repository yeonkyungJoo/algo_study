# 회문 문자열 검사

import sys

sys.stdin = open("input.txt", "r")

# # 1
# N = int(input())
#
# for i in range(N):
#     word = input().rstrip()
#     word = word.lower()
#     size = len(word)
#     for j in range(size//2):
#         if word[j] != word[-1 - j]:
#             print("#%d NO" %(i+1))
#             break
#     else:
#         print("#%d YES" %(i+1))

# 2
N = int(input())

for i in range(N):
    word = input().rstrip()
    word = word.lower()
    if word == word[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))