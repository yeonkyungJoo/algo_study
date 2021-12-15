import sys
nums = []
for _ in range(9):
    nums.append(list(map(int, input().split())))

numbers = [1] * 9
# 행
for i in range(len(nums)):
    tmp = numbers.copy()
    for j in range(len(nums)):
        n = nums[i][j]
        if 1 <= n <= 9:
            if tmp[n-1] == 1:
                tmp[n-1] = 0
            else:
                print('NO')
                sys.exit()
        else:
            print('NO')
            sys.exit()

# 열
for j in range(len(nums)):
    tmp = numbers.copy()
    for i in range(len(nums)):
        n = nums[i][j]
        if 1 <= n <= 9:
            if tmp[n-1] == 1:
                tmp[n-1] = 0
            else:
                print('NO')
                sys.exit()
        else:
            print('NO')
            sys.exit()

# 3x3
for i in range(0, len(nums), 3):
    for j in range(0, len(nums), 3):

        tmp = numbers.copy()
        for l in range(i, i+3):
            for k in range(j, j+3):
                n = nums[l][k]
                if 1 <= n <= 9:
                    if tmp[n - 1] == 1:
                        tmp[n - 1] = 0
                    else:
                        print('NO')
                        sys.exit()
                else:
                    print('NO')
                    sys.exit()
print('YES')