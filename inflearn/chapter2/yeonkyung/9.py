N = int(input())
result = []
for _ in range(N):
    nums = sorted(list(map(int, input().split())))
    a, b, c = nums[0], nums[1], nums[2]
    if a == c:
        result.append(10000 + a * 1000)
    elif a == b and b != c:
        result.append(1000 + a * 100)
    elif a != b and b == c:
        result.append(1000 + b * 100)
    elif a != b and b != c:
        result.append(c * 100)
print(max(result))
