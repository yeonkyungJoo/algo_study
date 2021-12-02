# TODO - re-try
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        # print(counter)
        boolean = [False] * 26
        index = ord('a')
        stack = []
        for i in range(len(s)):
            c = s[i]
            if not stack:
                stack.append(c)
                boolean[ord(c) - index] = True
            else:
                while stack and ord(stack[-1]) >= ord(c):
                    last = stack[-1]
                    if counter[last] > 1:
                        counter[last] -= 1
                        boolean[ord(last) - index] = False
                        stack.pop()
                    else:
                        break
                if not boolean[ord(c) - index]:
                    stack.append(c)
                    boolean[ord(c) - index] = True
        return ''.join(stack)

if __name__ == "__main__":
    s = "bcabc"
    print(Solution().removeDuplicateLetters(s))