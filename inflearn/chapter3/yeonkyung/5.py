N, M = map(int, input().split())
nums = list(map(int, input().split()))

total_list = [0] * N
dic = dict()
total = 0
for i in range(N):
    total += nums[i]
    total_list[i] = total

    if total not in dic:
        dic[total] = 0
    dic[total] += 1
# print(total_list)

count = 0
for total in total_list:
    if total == M:
        count += 1
        continue
    if total - M in dic:
        count += dic[total - M]
print(count)

'''
N, M = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(N):
    s = 0
    if nums[i] == M:
        count += 1
        continue
    elif nums[i] > M:
        continue
    else:
        s += nums[i]
    for j in range(i+1, N):
        s += nums[j]
        if s == M:
            count += 1
        elif s > M:
            break
print(count)
'''
