N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
prices.pop()

result = 0
stack = []
tmp = 0
curr = -1
for i, price in enumerate(prices):
    if stack:
        if stack[-1] > price:
            result += tmp * prices[curr]
            tmp = distances[i]
            curr = i
        else:
            tmp += distances[i]
    else:
        tmp = distances[i]
        curr = i
    stack.append(prices[i])
result += tmp * prices[curr]
print(result)

