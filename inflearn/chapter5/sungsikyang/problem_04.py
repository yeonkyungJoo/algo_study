# 후위식 연산
import sys
sys.stdin = open('input5.txt', 'r')
s = input()
stack = []
res = ''
for x in s:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif x == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif x == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif x == '/':
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)

print(*stack)