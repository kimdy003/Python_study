g_path = []


def DFS(graph, info, start, visit, path):
    global g_path
    if info[start] == 0:
        g_path.append([path[:], True])

    for nxt in graph[start]:
        if visit[nxt] == True:
            visit[nxt] = False
            path.append(nxt)
            DFS(graph, info, nxt, visit, path)
            path.pop()


def solution(info, edges):
    global g_path
    animal = [0, 0]  # 0: 양, 1:늑대
    graph = {i: [] for i in range(len(info))}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    visit = [True for _ in range(len(info))]
    visit[0] = False
    DFS(graph, info, 0, visit, [0])

    for l in range(1, len(g_path) + 2):
        for idx, [path, flag] in enumerate(g_path):
            if flag == True and len(path) <= l:
                for p in path:
                    if info[p] == 0:  # 양
                        animal[0] += 1
                        info[p] = -1

                    elif info[p] == 1:
                        if animal[0] > animal[1] + 1:
                            animal[1] += 1
                            info[p] = -1
                        else:
                            break
                else:
                    g_path[idx][1] = False

    return animal[0]


print(
    solution(
        [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [
            [0, 1],
            [1, 2],
            [1, 4],
            [0, 8],
            [8, 7],
            [9, 10],
            [9, 11],
            [4, 3],
            [6, 5],
            [4, 6],
            [8, 9],
        ],
    )
)
