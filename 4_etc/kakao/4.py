from collections import deque


def BFS(node, end, traps, visit, dic, flag, dist):
    q = deque()
    q.append((node, dist, flag))

    while q:
        node, dist, flag = q.popleft()
        if node == end:
            return dist

        for nxt, cost in dic[flag][node]:
            if visit[nxt] == 2:
                continue

            visit[nxt] += 1
            if nxt in traps:
                temp = (flag + 1) % 2
                q.append((nxt, dist + cost, temp))

            else:
                q.append((nxt, dist + cost, flag))


def solution(n, start, end, roads, traps):
    answer = 0
    dic = [{i: [] for i in range(n + 1)} for _ in range(2)]
    for s, e, w in roads:
        dic[0][s] += [(e, w)]
        dic[1][e] += [(s, w)]

    visit = [0] * (n + 1)

    answer = BFS(start, end, traps, visit, dic, 0, 0)

    return answer


print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))