class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort(key=lambda x:x[0])
        l, r = 0, len(nums) - 1
        while l < r:
            tmp = nums[l][0] + nums[r][0]
            if tmp == target:
                return [nums[l][1], nums[r][1]]
            elif tmp < target:
                l += 1
            elif tmp > target:
                r -= 1

        return []

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    print(Solution().twoSum(nums, target))