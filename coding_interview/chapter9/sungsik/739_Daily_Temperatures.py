from typing import List

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        result = [0] * len(temp)
        stack = []
        for i, cur in enumerate(temp):
            while stack and cur > temp[stack[-1]]:
                last = stack.pop()
                result[last] = i - last
            stack.append(i)
        return result

if __name__ == '__main__':
    s = Solution()
    temp = [73,74,75,71,69,72,76,73]
    print(s.dailyTemperatures(temp))
