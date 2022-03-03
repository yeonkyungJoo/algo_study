import math
N = int(input())
A = list(map(int, input().split()))

# 소수
primes = set()
for i in range(0, N):
    n = A[i]
    for m in range(2, int(math.sqrt(n)) + 1):
        if n % m == 0:
            break
    else:
        primes.add(n)

if len(primes) == 0:
    print(-1)
else:
    answer = 1
    for p in primes:
        answer *= p
    print(answer)