from collections import deque


def bfs(graph, node, visited=[]):
    visited.append(node)
    q = deque([node])

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if nxt not in visited:
                visited.append(nxt)
                q.append(nxt)

    return visited


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}
    print(bfs(graph, "A"))
