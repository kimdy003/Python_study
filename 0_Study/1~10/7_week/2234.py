import sys
from collections import deque

input = sys.stdin.readline

# 서, 북, 동 남
mov_dir = [[0, -1], [-1, 0], [0, 1], [1, 0]]

if __name__ == "__main__":
    answer = [0, 0, 0]
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt_board = [[0] * M for _ in range(N)]
    visit = [[True] * M for _ in range(N)]

    def bfs(i, j, idx):
        queue = deque()
        queue.append([i, j])
        cnt_board[i][j] = idx
        visit[i][j] = False

        count = 1
        while queue:
            y, x = queue.popleft()

            for i in range(4):
                if bin(board[y][x] & (1 << i)) == bin((1 << i)):  # 벽 존재
                    continue

                ny, nx = y + mov_dir[i][0], x + mov_dir[i][1]
                if 0 <= ny < N and 0 <= nx < M and visit[ny][nx]:
                    visit[ny][nx] = False
                    cnt_board[ny][nx] = idx
                    count += 1
                    queue.append([ny, nx])
        return count

    dic, idx = {}, 1
    for i in range(N):
        for j in range(M):
            if visit[i][j] == True:
                dic[idx] = bfs(i, j, idx)
                idx += 1

    print(len(dic))
    print(max(dic, key=dic.get))

    # 벽 허물기
    Max = 0
    for y in range(N):
        for x in range(M):
            for d in range(4):
                ny, nx = y + mov_dir[d][0], x + mov_dir[d][1]
                if 0 <= ny < N and 0 <= nx < M:
                    if cnt_board[y][x] != cnt_board[ny][nx]:
                        Max = max(
                            Max, dic[cnt_board[y][x]] + dic[cnt_board[ny][nx]]
                        )

    print(Max)
