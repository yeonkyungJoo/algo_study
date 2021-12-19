N = int(input())

def recursive(n):
    if n < 2:
        return str(n % 2)
    return recursive(n // 2) + str(n % 2)
print(recursive(N))

'''
import sys
#sys.stdin = open("input.txt", "rt")

N = int(input())

def recursive(N):
    if N == 1:
        return str(N)

    return recursive(N//2) + str(N%2)

print(recursive(N))
'''