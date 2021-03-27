ans = 987654321


def BFS(board):
    global ans
    movdir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = [(0, 0, 0, 0), (0, 0, 2, 0)]

    while q:
        y, x, dir, cost = q.pop(0)

        if y == len(board)-1 and x == len(board)-1:
            ans = min(ans, cost)
            continue
        
        for i in range(4):
            ny = y + movdir[i][0]
            nx = x + movdir[i][1]

            if 0 <= ny < len(board) and 0 <= nx < len(board):
                if(board[ny][nx] != 1):
                    new_cost = cost
                    if(i == dir):
                        new_cost += 100
                    else:
                        new_cost += 600
                
                    if board[ny][nx] == 0 or new_cost <= board[ny][nx]:
                        q.append((ny, nx, i, new_cost))
                        board[ny][nx] = new_cost
                        

def solution(board):

    BFS(board)
    return ans

print(solution([[0,0,0],[0,0,0],[0,0,0]]))