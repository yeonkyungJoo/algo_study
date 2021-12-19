s = list(input())

dic = {
    '(': 9,
    ')': 9,
    '+': 2,
    '-': 2,
    '*': 1,
    '/': 1
}
stack = []
ops = []
for n in s:

    if n.isnumeric():
        stack.append(n)
    else:

        if not ops:
            ops.append(n)
            continue

        if n == '(':
            ops.append(n)
        elif n == ')':
            while ops and ops[-1] != '(':
                stack.append(ops.pop())
            ops.pop()
        else:
            while ops and dic[ops[-1]] <= dic[n]:
                stack.append(ops.pop())
            ops.append(n)

for c in stack:
    print(c, end='')
while ops:
    print(ops.pop(), end='')

'''
import sys
#sys.stdin = open("input.txt", "rt")

formula = list(input())
#print(formula)

rank = {
    '(' : 1,
    '*' : 2,
    '/' : 2,
    '+' : 3,
    '-' : 3
}
stack = []
answer = []
for c in formula:

    if c.isnumeric():
        answer.append(c)
    else:
        if not stack:
            stack.append(c)
            continue

        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                answer.append(stack.pop())
            stack.pop()
        else:
            if stack[-1] == '(':
                stack.append(c)
            elif rank[stack[-1]] > rank[c]:
                stack.append(c)
            else:
                while stack and stack[-1] != '(' and rank[stack[-1]] <= rank[c]:
                    answer.append(stack.pop())
                stack.append(c)

while stack:
    answer.append(stack.pop())

print(''.join(answer))
'''