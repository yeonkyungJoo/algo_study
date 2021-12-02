class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            t = temperatures[i]
            if not stack:
                stack.append((i, t))
            else:
                while stack and stack[-1][1] < t:
                    result[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append((i, t))
        return result

if __name__ == "__main__":
    temperatures = [30,60,90]
    print(Solution().dailyTemperatures(temperatures))