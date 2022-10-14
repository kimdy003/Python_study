import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def calculation(type):
    q = deque()

    # right
    if type == 0:
        for i in range(N):
            for j in range(N - 1, -1, -1):
                if board[i][j]:
                    q.append(board[i][j])
                board[i][j] = 0

            idx = N - 1
            while q:
                data = q.popleft()

                if board[i][idx] == 0:
                    board[i][idx] = data
                elif board[i][idx] == data:
                    board[i][idx] *= 2
                    idx -= 1
                else:
                    idx -= 1
                    board[i][idx] = data

    # left
    elif type == 1:
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    q.append(board[i][j])
                board[i][j] = 0

            idx = 0
            while q:
                data = q.popleft()

                if board[i][idx] == 0:
                    board[i][idx] = data
                elif board[i][idx] == data:
                    board[i][idx] *= 2
                    idx += 1
                else:
                    idx += 1
                    board[i][idx] = data

    # up
    elif type == 2:
        for j in range(N):
            for i in range(N):
                if board[i][j]:
                    q.append(board[i][j])
                board[i][j] = 0

            idx = 0
            while q:
                data = q.popleft()

                if board[idx][j] == 0:
                    board[idx][j] = data
                elif board[idx][j] == data:
                    board[idx][j] *= 2
                    idx += 1
                else:
                    idx += 1
                    board[idx][j] = data

    # down
    elif type == 3:
        for j in range(N):
            for i in range(N - 1, -1, -1):
                if board[i][j]:
                    q.append(board[i][j])
                board[i][j] = 0

            idx = N - 1
            while q:
                data = q.popleft()

                if board[idx][j] == 0:
                    board[idx][j] = data
                elif board[idx][j] == data:
                    board[idx][j] *= 2
                    idx -= 1
                else:
                    idx -= 1
                    board[idx][j] = data

    return


def get_max():
    Max = 0
    for i in range(N):
        Max = max(Max, max(board[i]))
    return Max


def show():
    for i in range(N):
        print(board[i])
    print("\n", "----------------", "\n")


def dfs(cnt):
    global ans, board
    if cnt == 5:
        ans = max(ans, get_max())
        return

    temp = deepcopy(board)

    for i in range(4):
        calculation(i)
        dfs(cnt + 1)
        board = deepcopy(temp)


def solve():
    dfs(0)
    print(ans)


solve()
