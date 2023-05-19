from collections import deque


def bfs(i, j, place):
    # movdir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    movdir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    q = deque([[i, j]])
    visited = [[True] * N for _ in range(N)]
    visited[i][j] = False

    for _ in range(2):
        cur = len(q)

        for _ in range(cur):
            y, x = q.popleft()

            for dy, dx in movdir:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and visited[ny][nx]:
                    visited[ny][nx] = False
                    if place[ny][nx] == "O":
                        q.append([ny, nx])
                    if place[ny][nx] == "P":
                        return False

    return True


def sol(place):
    for i in range(N):
        for j in range(N):
            if place[i][j] == "P":
                if not bfs(i, j, place):
                    return 0
    else:
        return 1


def solution(places):
    global N
    answer = []
    N = 5

    for place in places:
        answer.append(sol(place))
    return answer


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
)
