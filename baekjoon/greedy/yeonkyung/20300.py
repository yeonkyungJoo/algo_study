N = int(input())
lost = list(map(int, input().split()))
lost.sort()

size = len(lost)
result = []
if size % 2 != 0:
    max_lost = lost.pop()
    size -= 1
    l, r = 0, size - 1
    while l < r:
        result.append(lost[l] + lost[r])
        l += 1
        r -= 1
    print(max(max_lost, max(result)))
else:
    l, r = 0, size - 1
    while l < r:
        result.append(lost[l] + lost[r])
        l += 1
        r -= 1
    print(max(result))
