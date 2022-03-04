N, M = map(int, input().split())
place = []
for _ in range(N):
    place.append(list(map(int, input().split())))
# print(place)

arr = [[0 for _ in range(M)] for _ in range(N)]
_x, _y = 0, 0
for i in range(N):
    for j in range(M):
        if place[i][j] == 9:
            _x, _y = i, j

# 방향(서, 북, 동, 남, x), 물건
def change(d, b):
    if b == 0:
        return d
    if d == 'w':
        if b == 1:
            return 'x'
        elif b == 3:
            return 's'
        elif b == 4:
            return 'n'
        else:
            return d
    elif d == 'n':
        if b == 2:
            return 'x'
        elif b == 3:
            return 'e'
        elif b == 4:
            return 'w'
        else:
            return d
    elif d == 'e':
        if b == 1:
            return 'x'
        elif b == 3:
            return 'n'
        elif b == 4:
            return 's'
        else:
            return d
    elif d == 's':
        if b == 2:
            return 'x'
        elif b == 3:
            return 'w'
        elif b == 4:
            return 'e'
        else:
            return d

for d in ['w', 'n', 'e', 's']:
    x, y = _x, _y
    ch = d
    while True:
        if x < 0 or y < 0 or x >= N or y >= M:
            break
        arr[x][y] = 1
        ch = change(ch, place[x][y])
        if ch == 'x':
            break
        elif ch == 'w':
            y -= 1
        elif ch == 'n':
            x -= 1
        elif ch == 'e':
            y += 1
        elif ch == 's':
            x += 1
print(sum([sum(a) for a in arr]))