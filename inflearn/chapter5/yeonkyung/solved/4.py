from collections import deque
s = deque(input())

stack = []
while s:
    c = s.popleft()
    if c.isnumeric():
        stack.append(int(c))
    else:
        n = stack.pop()
        m = stack.pop()

        if c == '+':
            stack.append(m + n)
        elif c == '-':
            stack.append(m - n)
        elif c == '*':
            stack.append(m * n)
        elif c == '/':
            stack.append(m // n)

print(stack[0])