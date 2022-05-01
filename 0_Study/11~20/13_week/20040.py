import sys

input = sys.stdin.readline


def Find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = Find(parent, parent[x])
    return parent[x]


def Union(parent, a, b):
    a = Find(parent, a)
    b = Find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [i for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    if Find(parent, a) == Find(parent, b):
        print(i + 1)
        break
    Union(parent, a, b)
else:
    print(0)
