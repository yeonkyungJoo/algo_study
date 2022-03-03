def solution(N, dist, graph):
    answer = 'NO'

    dist[1] = 0
    for ch in range(N):
        for v in range(1, N+1):
            for next_v, next_c in graph[v]:
                if dist[next_v] > dist[v] + next_c:
                    dist[next_v] = dist[v] + next_c
                    if ch == N-1:
                        answer = 'YES'
    return answer

if __name__ == "__main__":
    TC = int(input())
    INF = int(100000)
    for _ in range(TC):
        N, M, W = map(int, input().split())

        graph = [[] for _ in range(N+1)]
        dist = [INF] * (N+1)
        for _ in range(M):
            S, E, T = map(int, input().split())
            graph[S].append([E, T])
            graph[E].append([S, T])
        for _ in range(W):
            S, E, T = map(int, input().split())
            graph[S].append([E, -T])

        print(solution(N, dist, graph))