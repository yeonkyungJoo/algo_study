N, K = map(int, input().split())

list = []
for n in range(1, N+1):
    if N % n == 0:
        list.append(n)
# print(list)
if len(list) < K:
    print(-1)
else:
    print(list[K-1])
