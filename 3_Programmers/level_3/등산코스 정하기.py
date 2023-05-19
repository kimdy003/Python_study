def solution(n, paths, gates, summits):
    INF = int(1e9)
    field = {}
    for a, b, c in paths:
        for x, y in ((a, b), (b, a)):
            try:
                field[x].append((y, c))
            except:
                field[x] = [(y, c)]

    distance = [INF] * (n + 1)

    for gate in gates:
        distance[gate] = 0  # 모든 출발지에서 다익스트라를 수행가능

    check = set(summits)
    while gates:
        target = set()

        while gates:
            now = gates.pop()

            for to, time in field[now]:
                maxTime = max(distance[now], time)

                if distance[to] > maxTime:
                    distance[to] = maxTime

                    if to not in check:
                        target.add(to)

        gates = list(target)

    return min([[summit, distance[summit]] for summit in summits], key=lambda x: (x[1], x[0]))


print(
    solution(
        6,
        [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
        [1, 3],
        [5],
    )
)
