def digit_sum(x):
    numbers = list(map(int, list(str(x))))
    return sum(numbers)

N = int(input())
nums = list(map(int, input().split()))

max_sum = 0
result = 0
for num in nums:
    tmp = digit_sum(num)
    if tmp > max_sum:
        max_sum = tmp
        result = num
print(result)