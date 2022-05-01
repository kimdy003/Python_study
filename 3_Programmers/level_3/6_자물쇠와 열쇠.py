def push_pop(y, x, m, key, board, flag):

    for i in range(m):
        for j in range(m):
            if flag:
                board[y + i][x + j] += key[i][j]
            else:
                board[y + i][x + j] -= key[i][j]


def Rotation(key):
    return list(zip(*key[::-1]))


def check(board, m, n):
    for i in range(n):
        for j in range(n):
            if board[m + i][m + j] != 1:
                return False
    return True


def solution(key, lock):
    m, n = len(key), len(lock)

    board = [[0] * (m * 2 + n) for _ in range(m * 2 + n)]

    for i in range(n):
        for j in range(n):
            board[m + i][m + j] = lock[i][j]

    for b in board:
        print(b)

    for _ in range(4):
        for y in range(1, m + n):
            for x in range(1, m + n):
                push_pop(y, x, m, key, board, 1)
                if check(board, m, n):
                    return True
                push_pop(y, x, m, key, board, 0)

        key = Rotation(key)

    return False


solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
