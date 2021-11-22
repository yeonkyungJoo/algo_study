import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums_N = list(map(int, input().split()))
sum_nums = [0]
tmp = 0

for i in nums_N:
     tmp += i
     sum_nums.append(tmp)

for i in range(M):
    i, j = map(int, input().split())
    result = sum_nums[j] - sum_nums[i - 1]
    print(result)

# 1트 시간초과
# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# nums_N = list(map(int, input().split()))
# for _ in range(M):
#     result = 0
#     i, j = map(int, input().split())
#     for k in range(i - 1, j):
#         result += nums_N[k]
#     print(result)