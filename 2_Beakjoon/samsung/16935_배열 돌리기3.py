import sys

input = sys.stdin.readline


def upDown():
    """상하 반전 함수"""
    return list(reversed(board))


def leftRight():
    """좌우 반전 함수"""
    return [list(b[::-1]) for b in board]


def rotation():
    """시계 방향 90도 회전"""
    return list(zip(*board[::-1]))


def rrotation():
    """반시계 방향 90도 회전"""
    return list(reversed(list(zip(*board))))


def groupRotation():
    """구역별 시계 방향 회전"""
    movdir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    n, m = len(board) // 2, len(board[0]) // 2
    newBoard = [[0] * (m * 2) for _ in range(n * 2)]

    for i in range(n):
        for j in range(m):
            y, x = i, j
            for dy, dx in movdir:
                ny, nx = y + (dy * n), x + (dx * m)
                newBoard[ny][nx] = board[y][x]
                y, x = ny, nx
    return newBoard


def groupRRotation():
    """구역별 반시계 방향 회전"""
    movdir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    n, m = len(board) // 2, len(board[0]) // 2
    newBoard = [[0] * (m * 2) for _ in range(n * 2)]

    for i in range(n):
        for j in range(m):
            y, x = i, j
            for dy, dx in movdir:
                ny, nx = y + (dy * n), x + (dx * m)
                newBoard[ny][nx] = board[y][x]
                y, x = ny, nx
    return newBoard


if __name__ == "__main__":
    N, M, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    orders = list(map(int, input().split()))

    for order in orders:
        if order == 1:
            board = upDown()
        elif order == 2:
            board = leftRight()
        elif order == 3:
            board = rotation()
        elif order == 4:
            board = rrotation()
        elif order == 5:
            board = groupRotation()
        else:
            board = groupRRotation()

    for b in board:
        print(*b)
