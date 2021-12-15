cards = [n for n in range(1, 21)]
for _ in range(10):

    a, b = map(int, input().split())
    l, r = a-1, b-1
    while l < r:
        cards[l], cards[r] = cards[r], cards[l]
        l += 1
        r -= 1
for c in cards:
    print(c, end=' ')