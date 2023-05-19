import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    parent[b] = a


if __name__ == "__main__":
    N, M = int(input()), int(input())
    parent = [0] * (N + 1)

    for i in range(1, N + 1):
        parent[i] = i

    edges, result = [], 0

    for _ in range(M):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    edges.sort()
    for edge in edges:
        cost, a, b = edge

        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost

    print(result)
