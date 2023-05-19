import heapq


def sectionPrint(y1, x1, y2, x2):
    for i in range(y1, y2 + 1):
        print(board[i][x1 : x2 + 1])
    print()


def init():
    global board, N, M
    board = [[0] * M for _ in range(N)]

    idx = 1
    for i in range(N):
        for j in range(M):
            board[i][j] = idx
            idx += 1
    return board


def rotation(y1, x1, y2, x2):
    global board, N, M
    result = []
    newboard = [board[i][:] for i in range(N)]

    d = 0
    movdir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    y, x = y1, x1
    while d < 4:
        ny, nx = y + movdir[d][0], x + movdir[d][1]
        if y1 <= ny <= y2 and x1 <= nx <= x2:
            board[ny][nx] = newboard[y][x]
            heapq.heappush(result, newboard[y][x])
            y, x = ny, nx
        else:
            d += 1

    return heapq.heappop(result)


def solution(rows, columns, queries):
    global N, M
    N, M = rows, columns
    init()

    ans = []
    for query in queries:
        ans.append(rotation(*[q - 1 for q in query]))
    return ans


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))
