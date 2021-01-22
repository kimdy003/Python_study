def BFS(node, graph, visit):
    cnt = 0
    queue = [(node, cnt)]
    while queue:
        v, cnt = queue.pop(0)
        if visit[v] == -1:
            visit[v] = cnt
            cnt += 1
            for e in graph[v]:
                queue.append((e, cnt))


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visit = [-1]*(n+1)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    BFS(1, graph, visit)
    for v in visit:
        if v == max(visit):
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))