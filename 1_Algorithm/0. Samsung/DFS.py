def dfs(graph, node, visited=[]):
    visited.append(node)

    for nxt in graph[node]:
        if nxt not in visited:
            dfs(graph, nxt, visited)

    return visited


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}
    print(dfs(graph, "A"))
