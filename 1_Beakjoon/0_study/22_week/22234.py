import sys
from collections import deque

input = sys.stdin.readline

N, T, W = map(int, input().split())
q = deque()

for _ in range(N):
    # id값, 업무 처리 시간
    q.append(list(map(int, input().split())))

M = int(input())
con = []
for _ in range(M):
    # id값, 업무 처리 시간, c초 후에 들어옴
    con.append(list(map(int, input().split())))
con.sort(key=lambda x: -x[2])

data = q.popleft()
temp = T
for time in range(1, W + 1):
    if con and con[-1][2] <= time:
        p, t, c = con.pop()
        q.append([p, t])

    print(data[0])

    data[1] -= 1
    temp -= 1
    if temp == 0 or data[1] == 0:
        if data[1] > 0:
            q.append(data)
        temp = T
        if q:
            data = q.popleft()
