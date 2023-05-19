def delBlock(M, N, board):
    popSet = set()

    # search
    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] == board[i - 1][j] == board[i][j - 1] == board[i - 1][j - 1] != ".":
                popSet |= set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])

    for i, j in popSet:
        board[i][j] = 0
    for i, row in enumerate(board):
        empty = ["."] * row.count(0)
        board[i] = empty + [block for block in row if block != 0]
    return len(popSet)


def solution(m, n, board):
    answer = 0

    board = list(map(list, zip(*board)))
    while True:
        pop = delBlock(m, n, board)
        if pop == 0:
            return answer
        answer += pop


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))  # 14
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))  # 15
