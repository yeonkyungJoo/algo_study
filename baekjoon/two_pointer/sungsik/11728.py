import sys

A, B = map(int, sys.stdin.readline().split())
array_A = list(map(int, sys.stdin.readline().split()))
array_B = list(map(int, sys.stdin.readline().split()))

result = array_A + array_B
set(result)
result.sort()
print(*result)