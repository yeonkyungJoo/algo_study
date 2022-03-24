import heapq

def solution(operations):
    queue = []
    _queue = []

    heapq.heapify(queue)
    heapq.heapify(_queue)
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
                    heapq.heappop(queue)
                elif n == 1:
                    heapq.heappop(_queue)
        print(queue, _queue)
    if size == 0:
        return [0, 0]
    return [heapq.heappop(_queue) * (-1), heapq.heappop(queue)]

if __name__ == "__main__":
    operations = ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]
    print(solution(operations))