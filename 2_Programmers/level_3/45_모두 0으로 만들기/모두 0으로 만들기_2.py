from collections import defaultdict


def solution(a, edges):
    answer = 0
    if sum(a) != 0:
        return -1
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    while len(graph) > 1:
        for node in graph:
            if len(graph[node]) == 1:
                graph[graph[node][0]].remove(node)
                a[graph[node][0]] += a[node]
                answer += abs(a[node])
                a[node] = 0
                del graph[node]
                break

    if sum(a) == 0:
        return answer
    return -1


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
