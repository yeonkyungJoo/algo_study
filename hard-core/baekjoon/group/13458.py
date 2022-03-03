N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = N
for i in range(0, N):
    if A[i] >= B:
        A[i] -= B
    else:
        A[i] = 0

    if A[i] != 0:
        answer += A[i] // C
        if A[i] % C != 0:
            answer += 1
print(answer)