N = int(input())
scores = list(map(int, input().split()))

avg = int(round(sum(scores) / len(scores), 0))
result, diff = -1, 101
for i, score in enumerate(scores):
    tmp = abs(score - avg)
    if tmp < diff:
        diff = tmp
        result = i
    elif tmp == diff:
        if score > scores[result]:
            diff = tmp
            result = i
print(avg, result + 1)