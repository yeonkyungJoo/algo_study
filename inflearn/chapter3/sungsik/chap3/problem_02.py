# 숫자만 추출

import sys

sys.stdin = open("input.txt", "r")

words = input().rstrip()
list = []
for x in words:
    if x.isdigit():
        list.append(x)
num = 0
for i in range(len(list)):
    num += int(list[i]) * (10**(len(list) - i - 1))

cnt = 0
for i in range(1, num + 1):
    if num % i == 0:
        cnt += 1
print(num)
print(cnt)

# # 2
# for x in words:
#     if x.isdecimal():
#         num = num * 10 + int(x)
# cnt = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         cnt += 1
