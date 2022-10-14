import sys
from collections import deque

input = sys.stdin.readline


class Taxi:
    def __init__(self, y, x, fuel):
        self.y = y
        self.x = x
        self.fuel = fuel


class Passenger:
    def __init__(self, info: list):
        self.sy = info[0] - 1
        self.sx = info[1] - 1
        self.ey = info[2] - 1
        self.ex = info[3] - 1
        self.dist = self.calDistance()
        self.life = True  # 승객 존재 여부 -> 목적지에 데려다 줬으면 False

    def calDistance(self):  # 벽 이슈를 생각해야 한다.
        visited = [[True] * N for _ in range(N)]
        q = deque([[self.sy, self.sx]])
        visited[self.sy][self.sx] = False

        cnt = 0
        while q:
            curSize = len(q)

            for _ in range(curSize):
                y, x = q.popleft()
                if [y, x] == [self.ey, self.ex]:
                    return cnt

                for dy, dx in movdir:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] and board[ny][nx] != -1:
                        visited[ny][nx] = False
                        q.append([ny, nx])
            cnt += 1
        else:
            return -1  # 목적지까지 못 가는 경우

    def __str__(self):
        return "출발지 ({}, {}), 목적지 ({}, {}), 거리 {}".format(
            self.sy, self.sx, self.ey, self.ex, self.dist
        )


def bfs():
    # BFS + 토마토기법
    if board[taxi.y][taxi.x] > 0:  # 택시 위치에 승객이 있는 경우
        return taxi.y, taxi.x, 0

    visited = [[True] * N for _ in range(N)]
    q = deque([[taxi.y, taxi.x]])
    visited[taxi.y][taxi.x] = False
    cand = []

    cnt = 1
    while q:
        curSize = len(q)

        for _ in range(curSize):
            y, x = q.popleft()

            for dy, dx in movdir:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] and board[ny][nx] != -1:
                    visited[ny][nx] = False
                    q.append([ny, nx])

                    if board[ny][nx] > 0:
                        cand.append([ny, nx])

        if cand:
            cand.sort()
            return cand[0][0], cand[0][1], cnt
        cnt += 1
    else:
        return -1, -1, -1


def check():
    for i in range(1, M + 1):
        if psgrList[i].life:
            return False
    return True


def printBoard():
    print()
    print("----------------------")
    for i in range(N):
        print(board[i])


def solution():
    while True:
        # 택시 이동
        y, x, dist = bfs()

        if [y, x, dist] == [-1, -1, -1]:  # 갈 수 있는 승객이 없는 경우
            return -1

        psgr = psgrList[board[y][x]]
        board[y][x] = 0

        if (taxi.fuel < dist) or (
            (taxi.fuel - dist) < psgr.dist
        ):  # 연료가 없어 승객을 태우러 못가는 경우 or 목적지에 못가는 경우
            return -1

        # 승객을 목적지에 이동
        psgr.life = False

        # 연료 계산
        taxi.fuel = taxi.fuel - dist + psgr.dist
        taxi.y, taxi.x = psgr.ey, psgr.ex

        # printBoard()

        if check():
            return taxi.fuel


if __name__ == "__main__":
    movdir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    N, M, fuel = list(map(int, input().split()))
    board = [[-1 if j == 1 else j for j in list(map(int, input().split()))] for _ in range(N)]

    y, x = map(int, input().split())
    taxi = Taxi(y - 1, x - 1, fuel)

    psgrList: list[Passenger] = [
        Passenger(list(map(int, input().split()))) if i != 0 else [] for i in range(M + 1)
    ]

    for i in range(1, M + 1):
        psgr = psgrList[i]
        # print(psgr)
        if psgr.dist == -1:
            print(-1)
            exit(1)

        board[psgr.sy][psgr.sx] = i

    print(solution())
