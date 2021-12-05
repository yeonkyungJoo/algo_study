N = int(input())
quiz = list(map(int, input().split()))

result = 0
tmp = 0
cnt = 0
for q in quiz:
    if q == 1:
        cnt += 1
        tmp += cnt * 1
    else:
        result += tmp
        tmp = 0
        cnt = 0
result += tmp
print(result)