from collections import deque

first = [(0, 0), (-1, 0), (-1, -1), (0, -1)]
movdir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def solution(maps, p, r):
    answer = 0
    half_r, half_p = r // 2, p // 2

    def attack(i, j):
        q = deque()
        visit = [[False] * len(maps) for _ in range(len(maps))]

        for k in range(4):
            ni, nj = i + first[k][0], j + first[k][1]
            if 0 <= ni < len(maps) and 0 <= nj < len(maps):
                visit[ni][nj] = True
                q.append((ni, nj))

        cnt, monster = 1, 0
        while q and cnt <= half_r:

            cur = len(q)
            for _ in range(cur):
                y, x = q.popleft()

                if cnt < half_r:
                    if maps[y][x] <= p:
                        monster += 1
                else:
                    if maps[y][x] <= half_p:
                        monster += 1

                for i in range(4):
                    ny, nx = y + movdir[i][0], x + movdir[i][1]

                    if 0 <= ny < len(maps) and 0 <= nx < len(maps) and visit[ny][nx] == False:
                        visit[ny][nx] = True
                        q.append((ny, nx))

            cnt += 1
        return monster

    for i in range(len(maps)):
        for j in range(len(maps)):
            answer = max(answer, attack(i, j))

    return answer


print(
    solution(
        [
            [1, 28, 41, 22, 25, 79, 4],
            [39, 20, 10, 17, 19, 18, 8],
            [21, 4, 13, 12, 9, 29, 19],
            [58, 1, 20, 5, 8, 16, 9],
            [5, 6, 15, 2, 39, 8, 29],
            [39, 7, 17, 5, 4, 49, 5],
            [74, 46, 8, 11, 25, 2, 11],
        ],
        19,
        6,
    )
)
