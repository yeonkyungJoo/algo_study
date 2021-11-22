def pooling(arr, N):
    if N == 1:
        return arr[0][0]
    # 새로운 행렬을 만들어준다! 이 행렬에 재귀적으로 새로 만들어진 배열이 삽입된다.
    new_arr = [[] for _ in range(N//2)]
    # 2 by 2로 새로운 행렬을 쪼개게 된다.
    for i in range(0, N, 2):
        for j in range(0, N, 2):
            new_arr[i//2].append(sorted([arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]])[2])
    return pooling(new_arr, N//2)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(pooling(arr, N))