N, K = map(int, input().split())
arr = list(map(int, input().split()))
r_ptr, l_ptr = 0, 0
arr_cnt = [0 for _ in range(max(arr) + 1)]
result = 0

while r_ptr < N:
    if arr_cnt[arr[r_ptr]] < K:
        arr_cnt[arr[r_ptr]] += 1
        r_ptr += 1
    else:
        arr_cnt[arr[l_ptr]] -= 1
        l_ptr += 1
    result = max(result, r_ptr - l_ptr)
print(result)