import sys
from collections import deque

input = sys.stdin.readline


def bfs(node):
    queue = deque([[node, 0]])  # 위치, 경로에 위치한 얼음 수
    visit = [True] * (N + 1)
    visit[node] = False

    ans = []
    while queue:
        cur, cnt = queue.popleft()

        for nxt in graph[cur]:
            if 1 <= nxt <= S:  # 지지대 얼음 도착
                ans.append(cnt + 1)
                if len(ans) == 2:
                    return ans
            else:
                if visit[nxt]:
                    visit[nxt] = False
                    queue.append([nxt, cnt + 1])


if __name__ == "__main__":
    N, S, P = map(int, input().split())
    graph = {i: [] for i in range(1, N + 1)}
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(N - sum(bfs(P)) - 1)
