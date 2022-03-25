import heapq

def solution(jobs):
    answer = 0

    jobs.sort()
    i = 0
    start, now = -1, 0
    queue = []
    while i < len(jobs):

        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(queue, (job[1], job[0]))
        if len(queue) > 0:
            _job = heapq.heappop(queue)
            start = now
            now += _job[0]
            answer += (now - _job[1])
            i += 1
        else:
            now += 1

    return answer // len(jobs)

if __name__ == "__main__":
    jobs = [[0, 3], [4, 5], [7, 3]]
    print(solution(jobs))