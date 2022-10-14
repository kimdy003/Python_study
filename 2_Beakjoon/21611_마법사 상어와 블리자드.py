import sys

input = sys.stdin.readline


def snailFunc():
    snaildir = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # 좌 하 우 상
    y = x = N // 2
    depth = 1
    num = 2
    dir = 0

    cnt = 0
    while y > -1 and x > -1:
        ny, nx = y + snaildir[dir][0], x + snaildir[dir][1]
        indexing[num] = [ny, nx]

        y, x = ny, nx
        cnt += 1
        num += 1
        if cnt == depth:
            if dir in [1, 3]:
                depth += 1
            dir = (dir + 1) % 4
            cnt = 0


def attack(d, s):
    y, x = N // 2, N // 2
    for i in range(1, s + 1):
        ny, nx = y + movdir[d][0] * i, x + movdir[d][1] * i
        board[ny][nx] = 0


def move():
    start, end = 2, 3
    while start < N * N and end <= N * N:
        # 구슬의 없는 시작점 위치 찾기
        while start < N * N:
            sy, sx = indexing[start]
            if board[sy][sx] == 0:
                break
            start += 1
        else:
            return  # 빈 칸이 없다.

        # start + 1 부터 검사해서 구슬이 존재하는 위치 찾기
        end = start + 1
        while end <= N * N:
            ey, ex = indexing[end]
            if board[ey][ex]:
                break
            end += 1
        else:
            return

        board[sy][sx] = board[ey][ex]
        board[ey][ex] = 0


def Bomb():
    flag = False
    start, end = 2, 3
    count = 1
    while start < N * N and end <= N * N:
        sy, sx = indexing[start]
        ey, ex = indexing[end]

        if board[sy][sx] == board[ey][ex]:
            count += 1
            end += 1

        else:
            if count >= 4:
                flag = True
                for i in range(start, end):
                    y, x = indexing[i]
                    ans[board[y][x] - 1] += 1
                    board[y][x] = 0

            count = 1
            start = end
            end += 1

    return flag


def change():
    newBoard = [[0] * N for _ in range(N)]
    start, end = 2, 3
    index = 2
    count = 1

    # 그룹 구슬 정의 -> A : 구슬의 갯수, B : 구슬 번호
    while start < N * N and end <= N * N:
        sy, sx = indexing[start]
        ey, ex = indexing[end]

        if board[sy][sx] == board[ey][ex]:
            count += 1
            end += 1
        else:
            y, x = indexing[index]
            newBoard[y][x] = count
            ny, nx = indexing[index + 1]
            newBoard[ny][nx] = board[sy][sx]

            index += 2
            count = 1
            start = end
            end += 1

        if index > N * N:
            break

    for i in range(N):
        for j in range(N):
            board[i][j] = newBoard[i][j]


def solution():
    """
    1. 구슬 파괴
    2. 구슬 땡기기
    3. 같은 구슬이 4개 이상있으면 폭발
    4. 폭발하는 구슬이 없을때까지 계속 수행
    5. 구슬 증가
    """
    snailFunc()
    for _ in range(M):
        d, s = map(int, input().split())

        # 1. 구슬 파괴
        attack(d, s)
        move()

        while Bomb():
            move()

        change()


if __name__ == "__main__":
    ans = [0, 0, 0]
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    movdir = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]  # 상 하 좌 우
    indexing = {}

    solution()
    print(ans[0] + (2 * ans[1]) + (3 * ans[2]))
