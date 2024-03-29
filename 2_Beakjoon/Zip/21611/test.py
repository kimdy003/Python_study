# Pypy3 통과

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
field = [list(map(int, input().strip().split())) for _ in range(N)]
skills = [list(map(int, input().strip().split())) for _ in range(M)]  # 상어 스킬
direction = [[0, 0], [0, -1], [0, 1], [-1, 0], [1, 0]]  # 상하좌우
broken_marble = [0, 0, 0]  # 파괴한 구슬의 수

indexing = {}


def init():  # 각 필드에 번호와 좌표를 매칭시킨다
    tmpdir = [[0, -1], [-1, 0], [0, 1], [1, 0]]  # 좌(서) 상(북) 우(동) 하(남)
    tmpfield = [[0] * N for _ in range(N)]
    index = 1
    turn = 1  # 현재 방향
    depth = 1
    x = (N + 1) // 2 - 1
    y = (N + 1) // 2 - 1
    cnt = 0  # 같은 방향으로 이동한 횟수
    while x > -1 and y > -1:
        indexing[index] = [x, y]
        tmpfield[y][x] = index
        x += tmpdir[turn][0]
        y += tmpdir[turn][1]
        cnt += 1
        index += 1
        if cnt == depth:
            if turn in [0, 2]:
                depth += 1
            turn = (turn + 1) % 4
            cnt = 0


def changeMarble():  # 구슬의 변화
    newfield = [[0] * N for _ in range(N)]
    index = 2
    start = 2
    end = 3
    same = 1

    # 그룹에 대한 구슬 정의 -> A : 구슬의 갯수, B : 구슬의 번호
    while start < N * N and end <= N * N:
        sx, sy = indexing[start]
        ex, ey = indexing[end]
        if field[sy][sx] == field[ey][ex]:
            same += 1
            end += 1
        else:  # 구슬이 달라졌을때
            ix, iy = indexing[index]
            newfield[iy][ix] = same  # A:구슬갯수
            ix, iy = indexing[index + 1]
            newfield[iy][ix] = field[sy][sx]  # B:구슬번호
            index += 2
            same = 1
            start = end
            end = start + 1

        if index > N * N:
            break

    for i in range(N):
        for j in range(N):
            field[i][j] = newfield[i][j]


# 연속하는 구슬이 4개 이상일 때 파괴된다.
def bombMarble():  # 구슬의 파괴
    result = False
    start = 2
    end = 3
    same = 1

    # 같은 구슬 수 카운팅
    while start < N * N and end <= N * N:
        sx, sy = indexing[start]
        ex, ey = indexing[end]
        if field[sy][sx] == field[ey][ex]:  # 구슬 같으면?
            same += 1
            end += 1
        else:  # 구슬이 달라졌을때
            if same >= 4:  # 동일 구슬 4개 이상은 폭파 대상
                result = True  # 한 번이라도 폭파되면 결과값 True

                # #start ~ end-1까지 폭파한다
                for i in range(start, end):
                    bx, by = indexing[i]
                    broken_marble[field[by][bx] - 1] += 1
                    field[by][bx] = 0  # 폭파
            same = 1
            start = end
            end = start + 1
    return result  # False라는건 더이상 폭파할 구슬이 없다는 뜻


def moveMarble():  # 구슬의 이동
    start = 2  # 시작 인덱스 2
    end = 3  # 다음 인덱스 3로 시작
    while start < N * N and end <= N * N:
        while start < N * N:  # 비어있는 필드 찾기
            sx, sy = indexing[start]
            if not field[sy][sx]:  # 비어있다면
                break
            start += 1
        else:
            return

        if end <= start:
            end = start + 1

        while end <= N * N:
            ex, ey = indexing[end]
            if field[ey][ex]:
                break
            end += 1
        else:
            return  # 더이상 당길 구슬이 없다

        field[sy][sx] = field[ey][ex]
        field[ey][ex] = 0


def blizzard(d, s):  # 상어의 블리자드
    cx = (N + 1) // 2 - 1
    cy = (N + 1) // 2 - 1
    for i in range(1, s + 1):
        nx = cx + direction[d][0] * i
        ny = cy + direction[d][1] * i
        if field[ny][nx]:
            field[ny][nx] = 0


def testPrint():
    for i in range(N):
        for j in range(N):
            print(field[i][j], end=" ")

        print()


init()
for skill in skills:
    d, s = skill
    blizzard(d, s)
    moveMarble()

    while bombMarble():
        moveMarble()  # 이동과 폭파를 반복한다

    changeMarble()


print(broken_marble[0] + broken_marble[1] * 2 + broken_marble[2] * 3)
