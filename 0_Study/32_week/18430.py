import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
movdir = [[0, 1, 1, 0], [1, 0, 0, -1], [0, -1, -1, 0], [-1, 0, 0, 1]]
visit = [[False] * M for _ in range(N)]
ans = 0


def dfs(i, j, sum):
    global ans

    if j == M:
        i, j = i + 1, 0

    if i == N:
        ans = max(ans, sum)
        return

    if not visit[i][j]:
        for m in movdir:
            ny, nx, nny, nnx = i + m[0], j + m[1], i + m[2], j + m[3]
            if (
                0 <= ny < N
                and 0 <= nx < M
                and 0 <= nny < N
                and 0 <= nnx < M
                and not visit[ny][nx]
                and not visit[nny][nnx]
            ):
                visit[ny][nx] = visit[nny][nnx] = visit[i][j] = True
                dfs(i, j + 1, sum + board[i][j] * 2 + board[ny][nx] + board[nny][nnx])
                visit[ny][nx] = visit[nny][nnx] = visit[i][j] = False
    dfs(i, j + 1, sum)


dfs(0, 0, 0)
print(ans)
