import sys

input = sys.stdin.readline

def quad_Tree(x, y, n):
    if n == 1:
        return bw_image[x][y]
    else:
        comp = bw_image[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if comp != bw_image[i][j]:
                    print('(', end='')
                    quad_Tree(x, y, n//2)
                    quad_Tree(x, y + n//2, n//2)
                    quad_Tree(x + n//2, y, n//2)
                    quad_Tree(x + n//2, y + n//2, n//2)
                    print(')', end='')
                    return

        if comp == 0:
            print('0', end='')
            return
        else:
            print('1', end='')
            return



N = int(input())
bw_image = [list(map(int, input().strip())) for _ in range(N)]
# #입력 확인
# print(N)
# print(bw_image)

quad_Tree(0, 0, N)