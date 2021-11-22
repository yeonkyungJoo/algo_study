N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
# result = []
i, j = 0, 0
while i < N and j < M:
    if A[i] <= B[j]:
        # result.append(A[i])
        print(A[i], end=' ')
        i += 1
    else:
        # result.append(B[j])
        print(B[j], end=' ')
        j += 1

while i < N:
    print(A[i], end=' ')
    i += 1

while j < M:
    print(B[j], end=' ')
    j += 1