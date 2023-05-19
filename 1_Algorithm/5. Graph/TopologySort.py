from collections import deque


def topologySort():
    result = []
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for nxt in graph[now]:
            indegree[nxt] -= 1

            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[nxt] == 0:
                q.append(nxt)

    for res in result:
        print(res, end=" ")


if __name__ == "__main__":
    v, e = map(int, input().split())

    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    topologySort()
