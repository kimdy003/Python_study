import heapq

movdir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def solution(land, height):
    N = len(land)
    visit = [[False] * N for _ in range(N)]

    def bfs():
        ans = 0
        q = [(0, 0, 0)]  # 높이, y, x
        visit[0][0] = True

        while q:
            h, y, x = heapq.heappop(q)

            if height < h and visit[y][x] == False:
                visit[y][x] = True
                ans += h

            for i in range(4):
                ny, nx = y + movdir[i][0], x + movdir[i][1]

                if 0 <= ny < N and 0 <= nx < N:
                    if visit[ny][nx] == False:
                        temp = abs(land[ny][nx] - land[y][x])
                        if temp <= height:
                            visit[ny][nx] = True
                        heapq.heappush(q, (temp, ny, nx))

        return ans

    return bfs()


print(
    solution(
        [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3
    )
)
