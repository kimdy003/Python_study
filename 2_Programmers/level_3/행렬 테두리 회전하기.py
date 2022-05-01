movdir = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 하 우 상 좌


def Rotation(query, board):
    height, width = (query[2] - query[0]), (query[3] - query[1])
    y, x = query[0] - 1, query[1] - 1

    temp, Min = board[y][x], board[y][x]
    d = 0
    for _ in range(2):
        for _ in range(height):
            ny, nx = y + movdir[d][0], x + movdir[d][1]
            board[y][x] = board[ny][nx]
            Min = min(Min, board[ny][nx])
            y, x = ny, nx
        d += 1
        for _ in range(width):
            ny, nx = y + movdir[d][0], x + movdir[d][1]
            board[y][x] = board[ny][nx]
            Min = min(Min, board[ny][nx])
            y, x = ny, nx
        d += 1
    board[y][x + 1] = temp

    return Min


def solution(rows, columns, queries):
    answer = []
    board = [
        [i * columns + j for j in range(1, columns + 1)] for i in range(rows)
    ]

    for query in queries:
        answer.append(Rotation(query, board))

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
