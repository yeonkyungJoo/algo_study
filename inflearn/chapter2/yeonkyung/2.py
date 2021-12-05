T = int(input())
for i in range(1, T+1):
    N, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print('#{0} {1}'.format(i, sorted(nums[s-1:e])[k-1]))