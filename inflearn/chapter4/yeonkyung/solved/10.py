N = int(input())
nums = list(map(int, input().split()))

result = [0] * N
for i, num in enumerate(nums):
    n = i+1

    cnt = 1
    j = 0
    while True:

        if cnt == num + 1 and result[j] == 0:
            result[j] = n
            break

        if result[j] == 0:
            cnt += 1
        j += 1

for n in result:
    print(n, end=' ')
