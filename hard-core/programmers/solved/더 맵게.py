import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while len(scoville) > 1:
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        if s1 >= K and s2 >= K:
            break
        new = s1 + s2 * 2
        answer += 1
        heapq.heappush(scoville, new)

    if len(scoville) == 1 and scoville[0] < K:
        answer = -1
    return answer

if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]
    K = 1000
    print(solution(scoville, K))