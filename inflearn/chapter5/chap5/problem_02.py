# 쇠막대기
import sys
sys.stdin = open('input5.txt', 'r')
inp = list(map(str, input()))
stack = []
stick = 0
for x in range(len(inp)):
    if inp[x] == '(':
        stack.append(inp[x])
    else:
        if inp[x - 1] == '(':
            stack.pop()
            stick += len(stack)
        else:
            stack.pop()
            stick += 1
    # if inp[x] == ')' and inp[x - 1] == ')':
    #     stack.pop(x - 1)
    #     stick += len(stack)

print(stick)