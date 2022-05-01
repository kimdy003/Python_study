import sys
from collections import deque

input = sys.stdin.readline

Max = 100001
N, k = map(int, input().split())
q = deque()
q.append(N)
visit = [-1] * Max
visit[N] = 0

while q:
    cur = q.popleft()

    if cur == k:
        print(visit[cur])
        break

    if 0 <= cur - 1 < Max and visit[cur - 1] == -1:
        visit[cur - 1] = visit[cur] + 1
        q.append(cur - 1)
    if 0 <= cur * 2 < Max and visit[cur * 2] == -1:
        visit[cur * 2] = visit[cur]
        q.appendleft(cur * 2)
    if 0 <= cur + 1 < Max and visit[cur + 1] == -1:
        visit[cur + 1] = visit[cur] + 1
        q.append(cur + 1)
