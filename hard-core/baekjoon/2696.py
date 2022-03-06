import heapq

T = int(input())
for _ in range(T):
    M = int(input()) # 홀수
    # 중앙값의 개수
    print((M+1) // 2)

    _input = []
    for _ in range(M//10 + 1):
        _input.extend(list(map(int, input().split())))

    min_heap = []
    max_heap = []
    middle = _input[0]
    result = [middle]
    for i, v in enumerate(_input[1:], 1):
        if v > middle:
            heapq.heappush(max_heap, v)
        else:
            heapq.heappush(min_heap, v * (-1))

        if i % 2 == 0:
            if len(min_heap) < len(max_heap):
                heapq.heappush(min_heap, middle * (-1))
                middle = heapq.heappop(max_heap)
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, middle)
                middle = heapq.heappop(min_heap) * (-1)
            result.append(middle)

    # print(result)
    for k in range(len(result)//10 + 1):
        print(' '.join(map(str, result[k*10:k*10+10])))