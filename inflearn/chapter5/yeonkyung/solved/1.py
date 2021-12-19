n, m = input().split()

stack = []
nums = list(n)
m = int(m)
i = 0
while i < len(nums) and m > 0:
    num = int(nums[i])
    if not stack:
        stack.append(num)

    else:
        while stack:
            if stack[-1] < num:
                stack.pop()
                m -= 1
                if m == 0:
                    break
            else:
                break
        stack.append(num)
    i += 1

if m > 0:
    while m > 0:
        stack.pop()
        m -= 1
    stack = list(map(str, stack))
    print(''.join(stack))
else:
    stack = list(map(str, stack))
    print(''.join(stack) + ''.join(nums[i:]))

'''
import sys
#sys.stdin = open("input.txt", "rt")

number, N = input().split()
#print(number, N)
nums = [int(n) for n in list(number)]
N = int(N)
#print(nums, N)

stack = []
count = N
for num in nums:

    while stack and stack[-1] < num:
        if count == 0:
            break
        stack.pop()
        count -= 1
    stack.append(num)

while count > 0:
    stack.pop()
    count -= 1

for n in stack:
    print(n, end='')
'''