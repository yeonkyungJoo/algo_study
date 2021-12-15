nums = []
for _ in range(7):
    nums.append(list(map(int, input().split())))

count = 0
# 가로
for i in range(7):
    for j in range(3):
        s = nums[i][j:j+5]
        if s[:] == s[::-1]:
            count += 1

# 세로
for j in range(7):
    for i in range(3):
        s = []
        for k in range(i, i+5):
            s.append(nums[k][j])
        if s[:] == s[::-1]:
            count += 1
print(count)