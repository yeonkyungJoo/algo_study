class Solution:
    def isValid(self, s: str) -> bool:
        result = True

        if len(s) % 2 != 0:
            return False

        stack = []
        open = ['(', '{', '[']
        for i in range(len(s)):

            c = s[i]
            if c in open:
                stack.append(c)
            else:
                if c == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        result = False
                        break
                elif c == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        result = False
                        break
                elif c == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        result = False
                        break

        if stack:
            result = False

        return result

if __name__ == "__main__":
    s = ""
    print(Solution().isValid(s))