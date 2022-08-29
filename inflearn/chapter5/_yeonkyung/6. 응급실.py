import sys
from collections import deque
# sys.stdin = open("../input.txt", "rt")

N, M = map(int, input().split())
nums = list(map(int, input().split()))

patients = deque()
for i, num in enumerate(nums):
    patients.append((i, num))
# print(patients)

order = 1
while patients:

    p = patients.popleft()

    rv = False
    for i, h in patients:
        if h > p[1]:
            rv = True
            break
    if rv:
        patients.append(p)
    else:
        if p[0] == M:
            print(order)
            break
        order += 1