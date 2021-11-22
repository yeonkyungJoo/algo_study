N, X = map(int, input().split())
visit = list(map(int, input().split()))

total_list = [0]
total = 0
for v in visit:
    total += v
    total_list.append(total)

# result = []
max_total = 0
cnt = 1
for i in range(X, N+1):
    if max_total == total_list[i] - total_list[i-X]:
        cnt += 1
    elif max_total < total_list[i] - total_list[i-X]:
        max_total = total_list[i] - total_list[i-X]
        cnt = 1
    # result.append(total_list[i] - total_list[i-X])

if max_total == 0:
    print('SAD')
else:
    print(max_total)
    print(cnt)