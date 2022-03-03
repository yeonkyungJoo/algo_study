N, M = map(int, input().split())
place = []
for _ in range(N):
    place.append(list(map(int, input().split())))
# print(place)

arr = [[0 for _ in range(N)] for _ in range(M)]
_x, _y = 5, 4
# 서
x, y = _x, _y
while True:
    if x < 0 or y < 0 or x >= N or y >= M:
        break
    arr[x][y] = 1
    if place[x][y] == 1:
        break
    x -= 1

# 동
x, y = _x, _y
while True:
    if x < 0 or y < 0 or x >= N or y >= M:
        break
    arr[x][y] = 1
    if place[x][y] == 1:
        break
    x += 1

# 남
x, y = _x, _y
while True:
    if x < 0 or y < 0 or x >= N or y >= M:
        break
    arr[x][y] = 1
    if place[x][y] == 2:
        break
    y += 1

# 북
x, y = _x, _y
while True:
    if x < 0 or y < 0 or x >= N or y >= M:
        break
    arr[x][y] = 1
    if place[x][y] == 2:
        break
    y -= 1

print(arr)

