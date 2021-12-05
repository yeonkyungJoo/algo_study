input = '(())()'

def isValid(x: str) -> bool:
    stack = []
    for char in x:
        if char in ('(', '[', '{'):
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        elif char == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
    if stack:
        return False
    else: return True

if __name__ == '__main__':
    print(isValid(input))