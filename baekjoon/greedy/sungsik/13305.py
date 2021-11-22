import sys

input = sys.stdin.readline

num_city = int(input())
dist_road = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

cost = 0
chk_price = oil_price[0]
for i in range(num_city - 1):
    if oil_price[i] < chk_price:
        chk_price = oil_price[i]
    cost += chk_price * dist_road[i]
print(cost)