import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
movdir = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def Search(visit, board, i, j):
    queue = deque()
    queue.append([i, j])
    block, rainbow = 1, 0
    pivot = board[i][j]
    block_list, rainbow_list = [[i, j]], []

    while queue:
        y, x = queue.popleft()

        for k in range(4):
            ny, nx = y + movdir[k][0], x + movdir[k][1]
            if 0 <= ny < N and 0 <= nx < N:
                if visit[ny][nx] == 0 and (
                    board[ny][nx] == 0 or board[ny][nx] == pivot
                ):
                    block += 1
                    visit[ny][nx] = 1
                    block_list.append([ny, nx])
                    queue.append([ny, nx])
                    if board[ny][nx] == 0:
                        rainbow += 1
                        rainbow_list.append([ny, nx])

    # 무지개 블럭 방문 해제
    for y, x in rainbow_list:
        visit[y][x] = 0

    return [block, rainbow, block_list]


def Remove(board, lst):
    for y, x in lst:
        board[y][x] = -2


def Gravity(board):
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if board[i][j] >= 0:
                row = i
                while 0 <= row + 1 < N and board[row + 1][j] == -2:
                    board[row + 1][j] = board[row][j]
                    board[row][j] = -2
                    row += 1


def Rotation(board):
    return list(map(list, zip(*board)))[::-1]


def Print(board):
    print()
    for i in range(N):
        print(board[i])


score = 0
while True:
    visit = [[0] * N for _ in range(N)]
    lst = []

    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 and board[i][j] > 0:
                visit[i][j] = 1
                lst.append(Search(visit, board, i, j))

    if not lst:
        break

    lst.sort(reverse=True)
    if lst[0][0] < 2:
        break
    score += lst[0][0] ** 2
    Remove(board, lst[0][2])

    Gravity(board)
    board = Rotation(board)
    Gravity(board)


print(score)
