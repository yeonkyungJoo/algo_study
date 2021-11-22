N = int(input())
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))

def func(N, size):

    for i in range(0, N, size):
        for j in range(0, N, size):
            tmp = [nums[i][j], nums[i+(size//2)][j], nums[i][j+(size//2)], nums[i+(size//2)][j+(size//2)]]
            tmp.sort()
            nums[i][j] = tmp[2]
            nums[i+(size//2)][j], nums[i][j+(size//2)], nums[i+(size//2)][j+(size//2)] = 0, 0, 0

    if N == size:
        print(nums[0][0])
        return

    func(N, size * 2)

func(N, 2)