#
#  lv3_배달.py
#  배달
#
#  Create by 김도영 on 2021/04/25
#

import heapq


def solution(N, road, K):
    answer = 0

    dist = [int(1e9)] * (N + 1)
    graph = {}
    for r in road:
        graph[r[0]] = graph.get(r[0], []) + [(r[1], r[2])]
        graph[r[1]] = graph.get(r[1], []) + [(r[0], r[2])]

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        dist[start] = 0

        while q:
            d, node = heapq.heappop(q)

            if dist[node] < d:
                continue

            for next in graph[node]:
                cost = d + next[1]

                if cost < dist[next[0]]:
                    dist[next[0]] = cost
                    heapq.heappush(q, (cost, next[0]))

    dijkstra(1)

    for i in range(1, len(dist)):
        if dist[i] <= K:
            answer += 1

    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
