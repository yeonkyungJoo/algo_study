import sys
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

result = [0]
tmp = 0
for num in nums:
    tmp += num
    result.append(tmp)
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(result[j] - result[i-1])