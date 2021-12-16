from collections import deque
N = int(input())
nums = deque(map(int, input().split()))

last = -1
result = []
while nums:
    if min(nums[0], nums[-1]) >= last:
        if nums[0] <= nums[-1]:
            result.append('L')
            last = nums.popleft()
        else:
            result.append('R')
            last = nums.pop()
    elif nums[0] >= last and nums[-1] < last:
        result.append('L')
        last = nums.popleft()
    elif nums[0] < last and nums[-1] >= last:
        result.append('R')
        last = nums.pop()
    else:
        break

print(len(result))
print(''.join(result))