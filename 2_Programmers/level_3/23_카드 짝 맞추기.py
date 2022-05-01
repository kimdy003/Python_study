from itertools import permutations
from collections import deque

size = 4
myboard = [[] for _ in range(4)]
card_pos = {}
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = int(1e4)
answer = INF
orders = []


# 전역 변수를 이용한 보드(myboard), 카드 2장의 위치(card_pos) 초기화
# 지우는 순서에 대한 순열(orders) 초기화
# card_pos 예시 : card_pos[1] = [[0, 0], [1, 2]] // 카드 1은 보드의 [0,0], [1,2]에 존재
def init(board):
    global myboard, card_pos, orders
    for i in range(size):
        for j in range(size):
            if board[i][j] != 0:
                card = board[i][j]

                if card not in card_pos:
                    card_pos[card] = [[i, j]]
                else:
                    card_pos[card].append([i, j])

            myboard[i].append(board[i][j])

    orders = [key for key in card_pos.keys()]
    orders = list(permutations(orders))


# 이동한 결과가 보드 범위내 있는지 판단하는 함수
def isin(y, x):
    if -1 < y < size and -1 < x < size:
        return True
    return False


# ctrl + 방향키
def move(y, x, mv):
    global myboard
    ny, nx = y, x

    while True:
        _ny = ny + mv[0]
        _nx = nx + mv[1]
        if isin(_ny, _nx) == False:
            return ny, nx

        if myboard[_ny][_nx] != 0:
            return _ny, _nx

        ny, nx = _ny, _nx


# 카드 1장 찾을 때 나오는 거리르 반환하는 함수(목표 위치도 반환)
# 시작 위치: myboard[sy][sx], 찾아야 할 위치 : myboard[ey][ex]
def BFS(sy, sx, ey, ex):
    if [sy, sx] == [ey, ex]:
        return sy, sx, 1  # 그자리 그대로 enter로 인한 count는 1증가

    global myboard
    q = []
    q = deque(q)
    dist = [[0] * size for _ in range(size)]
    visit = [[False] * size for _ in range(size)]
    q.append([sy, sx])
    visit[sy][sx] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            # 한칸씩 이동
            ny = y + d[i][0]
            nx = x + d[i][1]

            if (isin(ny, nx) == True) and (visit[ny][nx] == False):
                visit[ny][nx] = True
                dist[ny][nx] = dist[y][x] + 1
                if [ny, nx] == [ey, ex]:
                    return ny, nx, dist[ny][nx] + 1

                q.append([ny, nx])

            # ctrl 이동
            ny, nx = move(y, x, d[i])
            if visit[ny][nx] == False:
                visit[ny][nx] = True
                dist[ny][nx] = dist[y][x] + 1
                if [ny, nx] == [ey, ex]:
                    return ny, nx, dist[ny][nx] + 1
                q.append([ny, nx])

    return sy, sx, INF


# 찾은 2장의 카드를 myboard에서 지워주는 함수
def remove(card):
    global myboard, card_pos
    for y, x in card_pos[card]:
        myboard[y][x] = 0


# 지워진 2장의 카드를 myboard에서 복원해주는 함수
def restore(card):
    global myboard, card_pos
    for y, x in card_pos[card]:
        myboard[y][x] = card


def backtrack(sy, sx, k, m, count):
    global orders, myboard, answer, card_pos
    if k == len(card_pos):
        answer = min(answer, count)
        return

    card = orders[m][k]
    left_y, left_x = card_pos[card][0][0], card_pos[card][0][1]
    right_y, right_x = card_pos[card][1][0], card_pos[card][1][1]

    # S -> XA -> XB
    ry1, rx1, res1 = BFS(sy, sx, left_y, left_x)
    ry2, rx2, res2 = BFS(ry1, rx1, right_y, right_x)

    remove(card)
    backtrack(ry2, rx2, k + 1, m, count + res1 + res2)
    restore(card)

    # S -> XB -> XA
    ry1, rx1, res1 = BFS(sy, sx, right_y, right_x)
    ry2, rx2, res2 = BFS(ry1, rx1, left_y, left_x)

    remove(card)
    backtrack(ry2, rx2, k + 1, m, count + res1 + res2)
    restore(card)
    return


def solution(board, r, c):
    global answer
    init(board)

    for i in range(len(orders)):
        backtrack(r, c, 0, i, 0)

    return answer


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
