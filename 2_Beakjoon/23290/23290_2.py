"""
2021.10.28
23290_마법사 상어와 복제
"""

import sys

input = sys.stdin.readline
movdir = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
shark_dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # 상 좌 하 우


def make_board():
    return [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]


def move_fish(board, t):
    new_board = make_board()
    for y in range(4):
        for x in range(4):
            for d in range(8):
                if board[y][x][d]:  # 물고기가 존재하면
                    copy_d = d
                    for _ in range(8):
                        ny, nx = y + movdir[copy_d][0], x + movdir[copy_d][1]
                        if (
                            not (0 <= ny < 4 and 0 <= nx < 4)
                            or [ny, nx] == shark
                            or dead[ny][nx] >= t - 2
                        ):  # 격자밖, 상어가 있는 경우, 시체가 2년채 되지 않은 경우
                            copy_d = (copy_d - 1) % 8
                        else:
                            new_board[ny][nx][copy_d] += board[y][x][d]
                            break
                    else:
                        new_board[y][x][d] += board[y][x][d]
    return new_board


def shark_swim(y, x, path, shark_dict, kill, visited):
    if len(path) == 3:
        shark_dict[path] = kill
        return
    else:
        for d in range(4):
            ny, nx = y + shark_dir[d][0], x + shark_dir[d][1]
            if 0 <= ny < 4 and 0 <= nx < 4:
                if (ny, nx) not in visited:
                    new_kill = sum(board[ny][nx])
                    visited.add((ny, nx))
                    shark_swim(
                        ny,
                        nx,
                        path + str(d),
                        shark_dict,
                        kill + new_kill,
                        visited,
                    )
                    visited.remove((ny, nx))
                else:
                    shark_swim(ny, nx, path + str(d), shark_dict, kill, visited)


def shark_move(shark, t):
    y, x = shark
    shark_dict = {}

    # 상어 경로 탐색
    shark_swim(y, x, "", shark_dict, 0, set())

    # 우선순위가 제일 높은 path에 맞춰 상어 이동
    # 물고기 잡아먹기
    move_sort = sorted(shark_dict.keys(), key=lambda x: (-shark_dict[x], x))
    for d in move_sort[0]:
        d = int(d)
        ny, nx = y + shark_dir[d][0], x + shark_dir[d][1]
        for i in range(8):
            if board[ny][nx][i]:
                board[ny][nx][i] = 0
                dead[ny][nx] = t
        y, x = ny, nx
    return [y, x]


M, S = map(int, input().split())  # 물고기 수, 마법을 연습한 횟수
board = make_board()

for _ in range(M):
    y, x, d = map(int, input().split())  # 물고기 위치, 방향
    board[y - 1][x - 1][d - 1] += 1

dead = [[-float("inf") for _ in range(4)] for _ in range(4)]
shark = list(map(lambda x: x - 1, map(int, input().split())))

for t in range(S):
    # 알 낳기
    Egg_board = [[col[:] for col in row] for row in board]  # deepcopy보다 빠름

    # 물고기 이동
    board = move_fish(board, t)

    # 상어 이동
    shark = shark_move(shark, t)

    # 알 부화하기
    for y in range(4):
        for x in range(4):
            for d in range(8):
                board[y][x][d] += Egg_board[y][x][d]

ans = 0
for y in range(4):
    for x in range(4):
        ans += sum(board[y][x])
print(ans)
