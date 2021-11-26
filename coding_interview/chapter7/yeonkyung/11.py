# TODO - re-try
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        result = []
        p = 1
        for num in nums:
            result.append(p)
            p = num * p

        p = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= p
            p = nums[i] * p
        # print(result)

        return result

if __name__ == "__main__":
    nums = [-1,1,0,-3,3]
    print(Solution().productExceptSelf(nums))