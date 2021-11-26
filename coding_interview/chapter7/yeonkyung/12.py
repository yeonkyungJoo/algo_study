from collections import deque
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        stack = []
        queue = deque(prices)

        result = 0
        while queue:
            n = queue.popleft()
            if not stack:
                stack.append(n)
            else:
                if stack[-1] > n:
                    stack.append(n)
                else:
                    result = max(n - stack[-1], result)
        return result

if __name__ == "__main__":
    prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))