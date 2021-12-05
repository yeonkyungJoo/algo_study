import math
def reverse(x):
    nums = []
    while x > 0:
        r = x % 10
        if r != 0 or (r == 0 and nums):
            nums.append(str(r))
        x -= r
        x //= 10
    return int(''.join(nums))

def isPrime(x):

    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x))+1):
        if x != i and x % i == 0:
            return False
    return True

N = int(input())
nums = list(map(int, input().split()))
for num in nums:
    n = reverse(num)
    if isPrime(n):
        print(n, end=' ')