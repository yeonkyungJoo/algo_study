class Solution:
    def trap(self, height: list[int]) -> int:

        max_height = 0
        max_height_idx = -1
        for i in range(len(height)):
            if height[i] >= max_height:
                max_height = height[i]
                max_height_idx = i

        result = 0
        l, r = 0, len(height) - 1
        tmp = height[l]
        while l < max_height_idx:
            if height[l] > tmp:
                tmp = height[l]
            if tmp > height[l]:
                result += tmp - height[l]
            l += 1

        tmp = height[r]
        while max_height_idx < r:
            if height[r] > tmp:
                tmp = height[r]
            if tmp > height[r]:
                result += tmp - height[r]
            r -= 1

        return result

if __name__ == "__main__":
    height = [4,2,0,3,2,5]
    print(Solution().trap(height))