from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [stdin.readline().rstrip() for _ in range(n)]
visit = [[0]*m for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

#BFS
queue = [(0,0)]
visit[0][0] = 1

while queue:
    y, x = queue.pop(0)

    if y == n-1 and x == m-1:
        print(visit[y][x])
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if visit[ny][nx] == 0 and graph[ny][nx] == '1':
                visit[ny][nx] = visit[y][x]+1
                queue.append((ny, nx))