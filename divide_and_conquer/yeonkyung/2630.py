N = int(input())
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))

w, b = 0, 0
def func(x, y, N):
    global w, b

    total = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            total += nums[i][j]
    if N == 1:
        if total == 0:
            w += 1
            return
        if total == N * N:
            b += 1
            return

    if total == 0:
        w += 1
        return
    if total == N * N:
        b += 1
        return

    func(x, y, N//2)
    func(x + N//2, y, N//2)
    func(x, y + N//2, N//2)
    func(x + N//2, y + N//2, N//2)

func(0, 0, N)
print(w)
print(b)
