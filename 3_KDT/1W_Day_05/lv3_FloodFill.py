#
#  lv3_FloodFill.py
#  FloodFill
#
#  Create by 김도영 on 2021/04/23
#


movdir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def solution(n, m, image):
    answer = 0
    N, M = len(image), len(image[0])
    visit = [[False for _ in range(M)] for _ in range(N)]

    def BFS(i, j):
        q = [[i, j]]
        visit[i][j] = True

        while q:
            y, x = q.pop(0)

            for i in range(4):
                ny, nx = y + movdir[i], x + movdir[i]
                if 0 <= ny < N and 0 <= nx < M:
                    if visit[ny][nx] == False and image[y][x] == image[ny][nx]:
                        visit[ny][nx] = True
                        q.append([ny, nx])

    for i in range(N):
        for j in range(M):
            if visit[i][j] == False:
                BFS(i, j)
                answer += 1
    return answer


print(solution(2, 3, [[1, 2, 3], [3, 2, 1]]))