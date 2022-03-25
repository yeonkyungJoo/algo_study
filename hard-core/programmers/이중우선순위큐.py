import heapq

def solution(operations):
    queue = []
    _queue = []

    size = 0
    for op in operations:
        n = int(op.split()[-1])
        if op[0] == 'I':
            size += 1
            heapq.heappush(queue, n)
            heapq.heappush(_queue, n * (-1))
        else:
            if size != 0:
                size -= 1
                if n == -1:
                    v1 = heapq.heappop(queue)
                    _queue.remove(v1 * (-1))
                elif n == 1:
                    v2 = heapq.heappop(_queue)
                    queue.remove(v2 * (-1))
    if size == 0:
        return [0, 0]
    return [heapq.heappop(_queue) * (-1), heapq.heappop(queue)]

'''
import heapq

def solution(operations):
    min_heap = list()
    max_heap = list()

    insert = 0
    delete = 0
    for operation in operations:
        op, n = operation.split()
        n = int(n)
        if op == 'I':
            insert += 1
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, n * (-1))
        else:
            delete += 1
            if n == -1:
                if len(min_heap) != 0:
                    heapq.heappop(min_heap)
            else:
                if len(max_heap) != 0:
                    heapq.heappop(max_heap)

    if delete >= insert:
        return [0, 0]
    else:
        m = heapq.heappop(min_heap)
        while True:
            if m * (-1) not in max_heap:
                m = heapq.heappop(min_heap)
            else:
                break

        n = heapq.heappop(max_heap)
        while True:
            if n * (-1) not in min_heap:
                n = heapq.heappop(max_heap)
            else:
                break

        return [n * (-1), m]
'''

if __name__ == "__main__":
    operations = ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]
    print(solution(operations))