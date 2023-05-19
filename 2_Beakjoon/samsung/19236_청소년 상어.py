from copy import deepcopy
import sys

input = sys.stdin.readline


def findFish(fish, board):
    for i in range(N):
        for j in range(N):
            if board[i][j][0] == fish:
                return (i, j)


def moveFish(sharkY, sharkX, board):
    for fish in range(1, 17):
        position = findFish(fish, board)

        if position:
            fishY, fishX = position[0], position[1]
            dir = board[fishY][fishX][1]

            for _ in range(8):
                ny, nx = fishY + movdir[dir][0], fishX + movdir[dir][1]

                if 0 <= ny < N and 0 <= nx < N:
                    if not (ny == sharkY and nx == sharkX):
                        board[fishY][fishX][1] = dir
                        board[ny][nx], board[fishY][fishX] = board[fishY][fishX], board[ny][nx]
                        break

                dir = (dir + 1) % 8


def getMoveablePosition(sharkY, sharkX, board):
    dir = board[sharkY][sharkX][1]
    position = []

    for i in range(1, N):
        ny, nx = sharkY + movdir[dir][0] * i, sharkX + movdir[dir][1] * i

        if 0 <= ny < N and 0 <= nx < N and board[ny][nx][0] != -1:
            position.append((ny, nx))
    return position


def dfs(sharkY, sharkX, eat, board):
    global answer
    board = deepcopy(board)
    eat += board[sharkY][sharkX][0]
    board[sharkY][sharkX][0] = -1
    moveFish(sharkY, sharkX, board)
    position = getMoveablePosition(sharkY, sharkX, board)

    if position:
        for ny, nx in position:
            dfs(ny, nx, eat, board)
    else:
        answer = max(answer, eat)
        return


if __name__ == "__main__":
    movdir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

    N = 4
    board = [[None] * N for _ in range(N)]
    for i in range(N):
        data = list(map(int, input().split()))
        for j in range(N):
            board[i][j] = [data[2 * j], data[2 * j + 1] - 1]

    answer = 0
    sharkY = sharkX = 0
    dfs(sharkY, sharkX, 0, board)
    print(answer)
