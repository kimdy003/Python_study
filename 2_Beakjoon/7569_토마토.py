import sys
from collections import deque

input = sys.stdin.readline


def printBox():
    print()
    for h in range(H):
        for i in range(N):
            print(box[h][i])
        print()


def check():
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if box[h][i][j] == 0:
                    return False
    return True


if __name__ == "__main__":
    # 상 하 좌 우 앞 뒤
    movdir = [[0, 1, 0], [0, -1, 0], [0, 0, -1], [0, 0, 1], [-1, 0, 0], [1, 0, 0]]
    M, N, H = map(int, input().split())
    # 익은 토마토 : 1, 익지 않은 토마토 : -1, 빈 칸 : -1
    box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

    q = deque(
        [[h, i, j] for h in range(H) for i in range(N) for j in range(M) if box[h][i][j] == 1]
    )

    cnt = -1

    while q:
        currLength = len(q)
        for _ in range(currLength):
            h, y, x = q.popleft()

            for dh, dy, dx in movdir:
                nh, ny, nx = h + dh, y + dy, x + dx
                if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M and box[nh][ny][nx] == 0:
                    box[nh][ny][nx] = 1
                    q.append([nh, ny, nx])

        cnt += 1

    # printBox()
    print(cnt if check() else -1)
