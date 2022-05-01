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


N = int(input().strip())
parent = [i for i in range(N + 1)]
for _ in range(N - 2):
    a, b = map(int, input().split())
    if Find(parent, a) != Find(parent, b):
        Union(parent, a, b)

for i in range(1, N + 1):
    parent[i] = Find(parent, parent[i])

ans = parent[1]
for i in range(2, N + 1):
    if ans != parent[i]:
        print(ans, parent[i])
        break
