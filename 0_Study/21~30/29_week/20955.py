import sys

input = sys.stdin.readline


def Find(x):
    if parent[x] != x:
        parent[x] = Find(parent[x])

    return parent[x]


def Union(a, b):
    a = Find(a)
    b = Find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
cycle = 0
for _ in range(M):
    a, b = map(int, input().split())
    if Find(a) != Find(b):
        Union(a, b)
    else:
        cycle += 1  # 싸이클 부분도 뉴런을 끊어줘야한다

edge = 0
for i in range(1, N):
    if Find(i) != Find(i + 1):
        Union(i, i + 1)
        edge += 1

print(cycle + edge)
