import heapq


def solution(n, s, a, b, fares):
    answer = 0
    graph = {i: [] for i in range(n + 1)}
    for fare in fares:
        c, d, f = fare
        graph[c].append([d, f])
        graph[d].append([c, f])

    def dijkstra(s, e):
        distance = [int(1e9) for _ in range(n + 1)]

        hq = []
        heapq.heappush(hq, [0, s])
        distance[s] = 0

        while hq:
            cost, node = heapq.heappop(hq)

            if distance[node] < cost:
                continue

            for nxt, f in graph[node]:
                dist = cost + f
                if dist < distance[nxt]:
                    distance[nxt] = dist
                    heapq.heappush(hq, [dist, nxt])

        return distance[e]

    # 각자 가는 경우
    answer = dijkstra(s, a) + dijkstra(s, b)

    for i in range(1, n + 1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
