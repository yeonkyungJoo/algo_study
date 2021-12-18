# 대표값
# N = int(input())
# scores = list(map(int, input().split()))
N = 10
scores = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]

def near_avg(scores: list) -> list:
    pass

### round_half_even, round_half_up
# a = sum(scores)/N
# print(a)
# a = a + 0.5
# print(a)
# a = int(a)
# print(a)
avg = round(sum(scores)/N)
min = float('inf')
for idx, x in enumerate(scores):
    tmp = abs(x - avg)
    if tmp < min:
        min = tmp
        score = x
        result = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            result = idx + 1

print(avg, result)