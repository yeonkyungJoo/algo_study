import math
N = int(input())

nums = [n for n in range(N+1)]
nums[0], nums[1] = -1, -1
i = 0
while i < math.sqrt(N) + 1:
    if nums[i] != -1:
        num = nums[i]
        for n in range(num + num, N+1, num):
            nums[n] = -1
    i += 1

count = 0
for num in nums:
    if num != -1:
        count += 1
print(count)

