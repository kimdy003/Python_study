import heapq

def dijkstra(graph, n, s, e):
    INF = int(1e9)
    dist = [INF] * (n+1)
    
    q = []
    heapq.heappush(q, [0, s])
    dist[s] = 0

    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        
        for n, c in graph[node]:
            c += cost
            if c < dist[n]:
                dist[n] = c
                heapq.heappush(q, [c, n])

    return dist[e]

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for x,y,c in fares:
        graph[x].append([y, c])
        graph[y].append([x, c])

    #각자 따로 집으로 가는 경우
    res = dijkstra(graph, n, s, a) + dijkstra(graph, n, s, b)

    #어느 지점까지 같이 갔다가 따로 가는 경우
    for i in range(1, n+1):
        if s != i:
            res = min(res, dijkstra(graph, n, s, i) + dijkstra(graph, n, i, a) + dijkstra(graph, n, i, b))
    return res

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))