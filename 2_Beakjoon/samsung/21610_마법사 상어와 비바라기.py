import sys

input = sys.stdin.readline


def printBoard():
    for i in range(N):
        print(waterBoard[i])
    print()


def moveCloud(d, s):
    newClouds = []
    for y, x in clouds:
        ny, nx = (y + movDir[d][0] * s) % N, (x + movDir[d][1] * s) % N
        waterBoard[ny][nx] += 1
        newClouds.append((ny, nx))

    for y, x in newClouds:
        for d in [2, 4, 6, 8]:
            ny, nx = y + movDir[d][0], x + movDir[d][1]
            if 0 <= ny < N and 0 <= nx < N and waterBoard[ny][nx] > 0:
                waterBoard[y][x] += 1
    return newClouds


def createCloud(newClouds):
    clouds = []
    for i in range(N):
        for j in range(N):
            if (i, j) in newClouds or waterBoard[i][j] < 2:
                continue
            waterBoard[i][j] -= 2
            clouds.append((i, j))
    return clouds


def solution():
    global clouds
    for d, s in moveInfo:

        # 구름 이동 + 비 내리기 + 대각선 검사
        newClouds = moveCloud(d, s)

        # 구름 생성
        clouds = createCloud(newClouds)

    res = 0
    for i in range(N):
        for j in range(N):
            res += waterBoard[i][j]

    return res


if __name__ == "__main__":
    movDir = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    N, M = map(int, input().split())
    waterBoard = [list(map(int, input().split())) for _ in range(N)]
    moveInfo = [tuple(map(int, input().split())) for _ in range(M)]
    clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

    print(solution())
