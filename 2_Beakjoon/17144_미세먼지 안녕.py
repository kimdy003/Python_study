import sys
from copy import deepcopy

input = sys.stdin.readline


def Print(arr):
    print()
    for i in range(len(arr)):
        print(arr[i])
    print()


def solution():
    R, C, T = list(map(int, input().split()))
    board, machine = [], []

    flag = True
    for i in range(R):
        temp = []
        for j, val in enumerate(list(map(int, input().split()))):
            temp.append(val)
            if flag and val == -1:
                flag = False
                machine = [i, j, i + 1, j]

        board.append(temp)

    for _ in range(T):
        # 확산
        movdir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        tempBoard = [[0] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if board[i][j] > 0:
                    dust = board[i][j]
                    cand, cnt = dust // 5, 0

                    for dy, dx in movdir:
                        ny, nx = i + dy, j + dx
                        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] != -1:
                            cnt += 1
                            tempBoard[ny][nx] += cand

                    tempBoard[i][j] += dust - (cand * cnt)
        board = deepcopy(tempBoard)

        # Print(board)

        # 공기청정기
        y1, x1, y2, x2 = machine
        board[y1][x1], board[y2][x2] = 0, 0
        y1, y2 = y1 - 1, y2 + 1

        # 반시계방향
        dd = 0
        ddir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        while dd < 4:
            ny, nx = y1 + ddir[dd][0], x1 + ddir[dd][1]
            if 0 <= ny < machine[2] and 0 <= nx < C:
                board[y1][x1] = board[ny][nx]
                y1, x1 = ny, nx
            else:
                dd += 1
        board[machine[0]][machine[1]] = -1

        # 시계방향
        d = 0
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while d < 4:
            ny, nx = y2 + dir[d][0], x2 + dir[d][1]
            if machine[2] <= ny < R and 0 <= nx < C:
                board[y2][x2] = board[ny][nx]
                y2, x2 = ny, nx
            else:
                d += 1
        board[machine[2]][machine[3]] = -1
        # Print(board)

    ans = 0
    for i in range(R):
        ans += sum(board[i])
    return ans + 2


if __name__ == "__main__":
    print(solution())
