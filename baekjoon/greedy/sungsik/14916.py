n = int(input())

amount_coin = 0
def exchange(n):
    global amount_coin
    while n > 0:
        if n % 5 == 0:
            return (n // 5 + amount_coin)
        n -= 2
        amount_coin += 1
    if n < 0:
        return -1

print(exchange(n))
