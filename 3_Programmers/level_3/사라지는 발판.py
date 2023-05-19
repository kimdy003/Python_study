def canMove(board, y, x):
    for dy, dx in movdir:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1:
            return True
    return False


def dfs(board, aloc, bloc, step):
    y, x = aloc if step % 2 == 0 else bloc

    if canMove(board, y, x) == False:  # 움직임이 불가능한 경우
        return (False, 0)
    if aloc == bloc:  # 같은 위치에 있는 경우
        return (True, 1)

    nboard = [b[:] for b in board]
    nboard[y][x] = 0
    canWin = False
    maxTurn, minTurn = 0, int(1e9)
    for dy, dx in movdir:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and nboard[ny][nx] == 1:
            if step % 2 == 0:
                ret = dfs(nboard, [ny, nx], bloc, step + 1)
            else:
                ret = dfs(nboard, aloc, [ny, nx], step + 1)

            if ret[0] == False:  # 상대가 지면 나는 이기는 경우
                canWin = True
                minTurn = min(minTurn, ret[1])
            else:  # 상대가 이기면 나는 지는 경우
                maxTurn = max(maxTurn, ret[1])

    if canWin == True:  # 이기는 경우에
        return (canWin, minTurn + 1)  # 최소의 움직임 반환
    else:  # 지는 경우에
        return (canWin, maxTurn + 1)  # 최대의 움직임 반환


def solution(board, aloc, bloc):
    """
    '이기는 플레이어'는 최소의 움직임으로 '지는 플레이어' 최대의 움직임으로 게임을 진행해야 한다
    """
    global movdir, N, M
    N, M = len(board), len(board[0])
    movdir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    answer = dfs(board, aloc, bloc, 0)
    return answer[1]


print("정답 : 5, sol : ", solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
print("정답 : 4, sol : ", solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
print("정답 : 5, sol : ", solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4]))
print("정답 : 0, sol : ", solution([[1]], [0, 0], [0, 0]))
