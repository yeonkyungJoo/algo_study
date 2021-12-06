from collections import deque

N = int(input())
nums1 = deque(map(int, input().split()))
M = int(input())
nums2 = deque(map(int, input().split()))
# print(nums1, nums2)

result = []
while nums1 and nums2:
    if nums1[0] <= nums2[0]:
        result.append(nums1.popleft())
    else:
        result.append(nums2.popleft())

if nums1:
    result.extend(nums1)
if nums2:
    result.extend(nums2)

for n in result:
    print(n, end=' ')