import sys

input = sys.stdin.readline
N, M = map(int, input().split())
field = [list(map(int, input().strip().split())) for _ in range(N)]
skills = [list(map(int, input().strip().split())) for _ in range(M)]  # 상어 스킬
direction = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]  # 상 하 좌 우
# shark = [(N + 1) // 2 - 1, (N + 1) // 2 - 1]
# shark = [N // 2 , N // 2]
bomb_marble = [0, 0, 0]

indexing = {}


def Init():
    rodir = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # 좌 하 우 상
    temp_field = [[0] * N for _ in range(N)]
    index = 1
    turn = 0
    depth = 1
    y = (N + 1) // 2 - 1
    x = (N + 1) // 2 - 1

    cnt = 0
    while x > -1 and y > -1:
        indexing[index] = [y, x]
        temp_field[y][x] = index
        y += rodir[turn][0]
        x += rodir[turn][1]
        cnt += 1
        index += 1

        if cnt == depth:
            if turn in [1, 3]:
                depth += 1

            turn = (turn + 1) % 4
            cnt = 0


def Change():
    new_field = [[0] * N for _ in range(N)]
    start = 2
    end = 3
    index = 2
    count = 1

    # 그룹 구슬 정의 -> A : 구슬의 갯수, B : 구슬의 번호
    while start < N * N and end <= N * N:
        sy, sx = indexing[start]
        ey, ex = indexing[end]
        if field[sy][sx] == field[ey][ex]:
            count += 1
            end += 1
        else:
            cy, cx = indexing[index]
            new_field[cy][cx] = count  # 구슬의 갯수
            cy, cx = indexing[index + 1]
            new_field[cy][cx] = field[sy][sx]  # 구슬의 번호
            index += 2
            count = 1
            start = end
            end = end + 1

        if index > N * N:
            break

    for i in range(N):
        for j in range(N):
            field[i][j] = new_field[i][j]


def Bomb():
    result = False
    start = 2
    end = 3
    count = 1
    while start < N * N and end <= N * N:
        sy, sx = indexing[start]
        ey, ex = indexing[end]
        if field[sy][sx] == field[ey][ex]:
            count += 1
            end += 1
        else:
            if count >= 4:
                result = True
                for i in range(start, end):
                    by, bx = indexing[i]
                    bomb_marble[field[by][bx] - 1] += 1
                    field[by][bx] = 0
            count = 1
            start = end
            end = end + 1

    return result


def Move():
    start = 2
    end = 3
    while start < N * N and end <= N * N:
        # 구슬이 없는 위치 찾기
        while start < N * N:
            sy, sx = indexing[start]
            if not field[sy][sx]:
                break
            start += 1
        else:
            return  # 더 이상 빈 칸이 없다

        if end <= start:
            end = start + 1  # 부터 시작

        # 구슬이 존재하는 위치 찾기
        while end <= N * N:
            ey, ex = indexing[end]
            if field[ey][ex]:
                break
            end += 1
        else:
            return  # 더 이상 당길 구슬이 없다.

        field[sy][sx] = field[ey][ex]
        field[ey][ex] = 0


def Attack(d, s):
    x = (N + 1) // 2 - 1
    y = (N + 1) // 2 - 1
    for k in range(1, s + 1):
        ny = y + direction[d][0] * k
        nx = x + direction[d][1] * k
        if field[ny][nx]:
            field[ny][nx] = 0


def Print(arr):
    print()
    for i in range(len(arr)):
        print(arr[i])


Init()
for skill in skills:
    d, s = skill
    Attack(d, s)
    Move()

    # 이동 & 폭발
    while Bomb():
        Move()

    Change()

print(bomb_marble[0] + bomb_marble[1] * 2 + bomb_marble[2] * 3)
