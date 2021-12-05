N, K = map(int, input().split())
nums = list(map(int, input().split()))

result = set()
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            result.add(nums[i] + nums[j] + nums[k])
print(sorted(list(result), reverse=True)[K-1])