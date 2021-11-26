class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        result = []
        size = len(nums)
        for i in range(size - 2):
            l, r = i+1, size - 1
            while l < r:
                if nums[l] + nums[r] == nums[i] * (-1):
                    tmp = [nums[l], nums[r], nums[i]]
                    if tmp not in result:
                        result.append(tmp)
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < nums[i] * (-1):
                    l += 1
                elif nums[l] + nums[r] > nums[i] * (-1):
                    r -= 1
        return result

if __name__ == "__main__":
    nums = [0]
    print(Solution().threeSum(nums))