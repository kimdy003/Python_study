from collections import deque

N = 5
movdir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def search(i, j, place, visit):
    q = deque()
    q.append((i, j))

    cnt = 0
    while q and cnt < 2:
        cur = len(q)

        for _ in range(cur):
            y, x = q.popleft()

            for d in range(4):
                ny, nx = y + movdir[d][0], x + movdir[d][1]
                if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == False:
                    visit[ny][nx] == True
                    if place[ny][nx] == "P":
                        return False

                    if place[ny][nx] == "O":
                        q.append((ny, nx))
        cnt += 1

    return True


def check(place):
    visit = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if place[i][j] == "P":
                visit[i][j] = True
                if search(i, j, place, visit) == False:
                    return False
    return True


def solution(places):
    answer = []

    for place in places:
        if check(place) == True:
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
)
