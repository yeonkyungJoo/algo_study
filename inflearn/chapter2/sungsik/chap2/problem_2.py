# K번째 수

T = int(input())
for j in range(T):
    N, s, e, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    n_list = []
    for i in range(s - 1, e):
        n_list.append(num_list[i])
    n_list.sort()
    print('#', end='')
    print(j + 1, end=' ')
    print(n_list[k - 1])
