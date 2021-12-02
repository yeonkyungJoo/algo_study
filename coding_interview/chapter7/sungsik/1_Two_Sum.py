from typing import List

nums = [2, 7, 11, 5]
target = 9

# 1. brute force
def sum_To_Nine(nums:List[int], target:int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(sum_To_Nine(nums, target))

# 2. using 'in'
def sum_To_Nine(nums:List[int], target:int) -> List[int]:
    for i,n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

print(sum_To_Nine(nums, target))

# 3. find key with pop first num
def sum_To_Nine(nums:List[int], target:int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]
print(sum_To_Nine(nums, target))

# 4. look-up structure improving
def sum_To_Nine(nums:List[int], target:int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

print(sum_To_Nine(nums, target))

# 5. using two-pointer
def sum_To_Nine(nums:List[int], target:int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
    return [left - 1, right]
print(sum_To_Nine(nums, target))
