n = int(input())

x, y = n // 5, 0
flag = False
while x >= 0:
    r = n - (5 * x)
    if r % 2 == 0:
        y = r // 2
        flag = True
        break
    x -= 1

if flag:
    print(x + y)
else:
    print(-1)
