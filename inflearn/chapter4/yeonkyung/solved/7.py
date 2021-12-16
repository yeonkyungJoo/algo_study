import sys

L = int(input())
nums = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    max_h, xi = -sys.maxsize, -1
    min_h, ni = sys.maxsize, -1

    for i in range(len(nums)):
        if nums[i] >= max_h:
            max_h = nums[i]
            xi = i
        if nums[i] <= min_h:
            min_h = nums[i]
            ni = i
    nums[xi] -= 1
    nums[ni] += 1

max_h, min_h = -sys.maxsize, sys.maxsize
for i in range(len(nums)):
    if nums[i] >= max_h:
        max_h = nums[i]
    if nums[i] <= min_h:
        min_h = nums[i]
print(max_h - min_h)

'''
import sys
#sys.stdin = open("input.txt", "rt")

L = int(input()) # 창고 가로 길이
heights = list(map(int, input().split()))
M = int(input()) # 높이 조정 횟수
#print(L, M, heights)

sorted_heights = sorted(heights, reverse=True)
count = 0
while count <= M:
    sorted_heights = sorted(sorted_heights, reverse=True)
    set_sorted_heights = sorted(list(set(sorted_heights)), reverse=True)

    if sorted_heights[0] == sorted_heights[1] and sorted_heights[-2] == sorted_heights[-1]:
        move = min(sorted_heights[0]-set_sorted_heights[1], set_sorted_heights[-2]-sorted_heights[-1])

    elif sorted_heights[0] != sorted_heights[1] and sorted_heights[-2] == sorted_heights[-1]:
        move = min(sorted_heights[0]-sorted_heights[1], set_sorted_heights[-2]-sorted_heights[-1])

    elif sorted_heights[0] == sorted_heights[1] and sorted_heights[-2] != sorted_heights[-1]:
        move = min(sorted_heights[0]-set_sorted_heights[1], sorted_heights[-2]-sorted_heights[-1])

    else:
        move = min(sorted_heights[0] - sorted_heights[1], sorted_heights[-2] - sorted_heights[-1])

    if M >= count + move :
        count += move
        sorted_heights[0] -= move
        sorted_heights[-1] += move
    else:
        count += (M - count)
        sorted_heights[0] -= (M - count)
        sorted_heights[-1] += (M - count)
        break

print(sorted_heights[0] - sorted_heights[-1])

'''