if __name__ == "__main__":
    INF = int(1e9)

    # 노드의 개수, 간선의 개수
    N, M = map(int, input().split())
    # graph 생성 및 자기 자신으로 가는 비용은 0, 나머지 비용은 무한으로 초기화
    graph = [[0 if a == b else INF for b in range(N + 1)] for a in range(N + 1)]

    # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
    for _ in range(M):
        # A에서 B로 가는 비용은 C라고 설정
        a, b, c = map(int, input().split())
        graph[a][b] = c

    # 점화식에 따라 플로이드 와샬 알고리즘 수행
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 수행됭 결과를 출력
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            # 도달할 수 없는 경우, "INFINITY" 출력
            if graph[a][b] == INF:
                print("INFINITY", end=" ")
            else:
                print(graph[a][b], end=" ")
        print()
