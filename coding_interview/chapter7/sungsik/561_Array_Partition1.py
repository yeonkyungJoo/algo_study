from typing import List

input = [1, 4, 3, 2]

def arrayPairSum(nums: List[int]) -> int:
    # # 1. 오름차순 풀이
    # sum = 0
    # pair = []
    # nums.sort()
    #
    # for n in nums:
    #     pair.append(n)
    #     if len(pair) == 2:
    #         sum += min(pair)
    #         pair = []
    #
    # return sum


    # # 2. 짝수 번째 값 계산
    # sum = 0
    # nums.sort()
    #
    # for i, n in enumerate(nums):
    #     if i % 2 == 0:
    #         sum += n
    #
    # return sum

    # # 3. 파이썬다운 방식
    return sum(sorted(nums)[::2])

print(arrayPairSum(input))