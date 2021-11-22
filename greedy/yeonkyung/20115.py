N = int(input())
drinks = list(map(int, input().split()))

total = 0
max_drink = 0
for drink in drinks:
    if drink > max_drink:
        max_drink = drink
    total += drink
result = max_drink + ((total - max_drink) / 2)
print(result)