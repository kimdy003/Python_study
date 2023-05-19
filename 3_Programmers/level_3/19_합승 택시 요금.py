def solution(n, s, a, b, fares):
    distance = [[0 if i == j else int(1e9) for j in range(n + 1)] for i in range(n + 1)]
    for c, d, f in fares:
        distance[c][d] = f
        distance[d][c] = f

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    minv = int(1e9)
    for i in range(1, n + 1):
        minv = min(minv, distance[s][i] + distance[i][a] + distance[i][b])
    return minv


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
