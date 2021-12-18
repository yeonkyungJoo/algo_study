# K번째 큰 수

# N, K = map(int, input().split())
# cards = list(map(int, input().split()))
N, K = 10, 3
cards = [13, 15, 34, 23, 45, 65, 33, 11, 26, 42]
result = set()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            result.add(cards[i] + cards[j] + cards[k])

result = list(result)
print(result)
result.sort(reverse=True)
print(result)
print(result[K - 1])