import sys

input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

# # 입력 확인
# print(N)
# for i in range(N):
#     print(paper[i])
white = 0
blue = 0

def cnt_paper_color(x, y, N):
    global white, blue
    tmp_color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if tmp_color != paper[i][j]:
                # 1사분면
                cnt_paper_color(x, y, N//2)
                # 2사분면
                cnt_paper_color(x, y + N//2, N//2)
                # 3사분면
                cnt_paper_color(x + N//2, y, N//2)
                # 4사분면
                cnt_paper_color(x + N//2, y + N//2, N//2)
                return

    if tmp_color == 0:
        white += 1
        return
    else:
        blue += 1
        return

cnt_paper_color(0, 0, N)
print(white)
print(blue)