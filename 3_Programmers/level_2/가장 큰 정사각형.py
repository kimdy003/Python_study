def solution(board):
    raw = len(board)
    col = len(board[0])

    for y in range(1, raw):
        for x in range(1, col):
            if board[y][x] == 1:
                board[y][x] = min(board[y-1][x], min(board[y][x-1], board[y-1][x-1]))+1
    
    return max([item for raw in board for item in raw])**2