N = int(input())
prices = []
for _ in range(N):
    prices.append(int(input()))
prices.sort(reverse=True)

total = sum(prices)
for i, price in enumerate(prices):
    if (i + 1) % 3 == 0:
        total -= price
print(total)