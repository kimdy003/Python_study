from collections import defaultdict


def BFS(i, j, graph):
    queue = [i]
    visit = set()

    while queue:
        cur = queue.pop(0)
        visit.add(cur)

        for nxt in graph[cur]:
            if nxt == j:
                return 1
            else:
                if nxt not in visit:
                    visit.add(nxt)
                    queue.append(nxt)

    return 0


def solution(n, signs):
    graph = defaultdict(set)
    for i in range(n):
        for j in range(n):
            if signs[i][j] == 1:
                graph[i].add(j)

    answer = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            answer[i][j] = BFS(i, j, graph)

    return answer