# K번째 약수
N, K = map(int, input().split())

def get_divisor(x):
    list = []
    for i in range(1, N + 1):
        if N % i == 0:
            list.append(i)
    if len(list) >= K: return list[K - 1]
    else: return -1

print(get_divisor(N))

# list = []
# for i in range(1, N + 1):
#     if N % i == 0:
#         list.append(i)
#
# print(list)
# print(list[K - 1])