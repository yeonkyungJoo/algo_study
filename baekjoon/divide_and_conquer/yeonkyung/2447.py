N = int(input())

result = [[' ' for _ in range(N)] for _ in range(N)]
def func(x, y, N):

    if N == 1:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                result[x+i][y+j] = '*'
        return

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            print(i, j, x//3*i, y//3*j, N//3)
            func(x//3*i, y//3*j, N//3)
            return
func(0, 9, 9)
for i in range(len(result)):
    print(''.join(result[i]))