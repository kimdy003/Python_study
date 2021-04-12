import heapq

def solution(N, road, K):
    answer = 0
    dist = [int(1e9)] * (N+1)
    graph = [[] for i in range(N+1)]
    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        dist[start] = 0
        
        while q:
            d, now = heapq.heappop(q)
            
            if dist[now] < d:
                continue
                
            for i in graph[now]:
                cost = d+i[1]
                if cost < dist[i[0]]:
                    dist[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(1)
    
    for i in range(1, len(dist)):
        if dist[i] <= K:
            answer += 1

    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))