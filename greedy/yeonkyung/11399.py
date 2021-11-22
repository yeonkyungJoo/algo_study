N = int(input())
times = list(map(int, input().split()))
times.sort()

stack = []
for time in times:
    if stack:
        stack.append(stack[-1] + time)
    else:
        stack.append(time)
print(sum(stack))