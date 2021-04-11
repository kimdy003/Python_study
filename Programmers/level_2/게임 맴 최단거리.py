movdir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(maps):
    N, M = len(maps), len(maps[0])
    

    queue = [(0, 0)]
    visit = [[False for _ in range(M)] for _ in range(N)]
    visit[0][0] = True
    cnt = 1

    while queue:

        cur = len(queue)
        for _ in range(cur):
            y, x = queue.pop(0)

            if y == N-1 and x == M-1:
                return cnt

            for i in range(4):
                ny, nx = y + movdir[i][0], x + movdir[i][1]

                if ny < 0 or N <= ny or nx < 0 or M <= nx:
                    continue
                    
                if maps[ny][nx] == 1 and visit[ny][nx] == False:
                    visit[ny][nx] = True
                    queue.append((ny, nx))
        cnt += 1

    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))