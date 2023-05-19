import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    N = int(input())
    parent = [0] * (N + 1)

    for i in range(N + 1):
        parent[i] = i

    lst = []
    edges, result = [], 0

    for i in range(N):
        x, y, z = map(int, input().split())
        lst.append((i, x, y, z))

    for i in [1, 2, 3]:
        temp = sorted(lst, key=lambda x: x[i])
        edge = [(abs(b[i] - a[i]), a[0], b[0]) for a, b, in zip(temp[:-1], temp[1:])]
        edges += edge

    edges.sort()
    for edge in edges:
        cost, a, b = edge

        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost

    print(result)
