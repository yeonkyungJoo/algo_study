from collections import deque
import sys

K = int(input())
W, H = map(int, input().split())
board =[]
for _ in range(H):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
hdx = [-2, -1, 1, 2, 2, 1, -1, -2]
hdy = [1, 2, 2, 1, -1, -2, -2, -1]
ch = [[0 for _ in range(W)] for _ in range(H)]
queue = deque()
queue.append((0, 0, 0, K))
min_cnt = sys.maxsize

def bfs():
    global min_cnt

    while queue:
        x, y, cnt, k = queue.popleft()
        if k > 0:
            for i in range(8):
                _x = x + hdx[i]
                _y = y + hdy[i]
                if 0 <= _x < H and 0 <= _y < W and board[_x][_y] == 0:
                    if ch[_x][_y] == 0:
                        pass
        else:
            for i in range(4):
                _x = x + dx[i]
                _y = y + dy[i]
                if 0 <= _x < H and 0 <= _y < W and board[_x][_y] == 0:
                    if ch[_x][_y] == 0:
                        queue.append((_x, _y, cnt))

bfs()
print(min_cnt)