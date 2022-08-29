import sys
from collections import deque
#sys.stdin = open("../input.txt", "rt")

_nums, R = input().split()
nums = deque(map(int, list(_nums)))
# print(nums)
R = int(R)
stack = []

while nums and R > 0:

    if (not stack) or (stack[-1] >= nums[0]):
        stack.append(nums.popleft())
    else:
        while stack and stack[-1] < nums[0]:
            stack.pop()
            R -= 1
            if R == 0:
                break

while R > 0:
    stack.pop()
    R -= 1
stack.extend(nums)
print(''.join(map(str, stack)))

