from collections import deque

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def can_move(y1, x1, y2, x2, shape, size, board):
    cand = []

    for i in range(4):
            ny1, nx1 = y1+d[i][0], x1+d[i][1]
            ny2, nx2 = y2+d[i][0], x2+d[i][1]

            if (0<= ny1 < size) and (0 <= nx1 < size) and (0<= ny2 < size) and (0 <= nx2 < size):
                if (board[ny1][nx1] == 0) and (board[ny2][nx2] == 0):
                    cand.append((ny1, nx1, ny2, nx2, shape))

    if shape == 0: # 가로방향
        if (y1+1 < size) and (y2+1 < size):
            if (board[y1+1][x1] == 0) and (board[y2+1][x2] == 0):
                cand.append((y1, x1, y1+1, x1, 1))
                cand.append((y2+1, x2, y2, x2, 1))
        if (0 <= y1-1) and (0 <= y2-1):
            if (board[y1-1][x1] == 0) and (board[y2-1][x2] == 0):
                cand.append((y1, x1, y1-1, x1, 1))
                cand.append((y2-1, x2, y2, x2, 1))
    
    else:
        if (x1+1 < size) and (x2+1 < size):
            if(board[y1][x1+1] == 0) and (board[y2][x2+1] == 0):
                cand.append((y1, x1, y1, x1+1, 0))
                cand.append((y2, x2+1, y2, x2, 0))
        if (0 <= x1-1) and (0 <= x2-1):
            if(board[y1][x1-1] == 0) and (board[y2][x2-1] == 0):
                cand.append((y1, x1, y1, x1-1, 0))
                cand.append((y2, x2-1, y2, x2, 0))

    return cand

def solution(board):
    size = len(board)
    q = deque([])
    q.append((0, 0, 0, 1, 0, 0))    #y1, x1, y2, x2, shape, time
    confirm = set([((0,0,0,1))])

    while q:
        y1, x1, y2, x2, shape, time = q.popleft()

        if(y1 == size-1 and x1 == size-1) or (y2 == size-1 and x2 == size-1):
            return time
        
        for nxt in can_move(y1, x1, y2, x2, shape, size, board):
            if nxt not in confirm:
                q.append((*nxt, time+1))
                confirm.add(nxt)

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))