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
    N, M = map(int, input().split())
    parent = [0] * (N + 1)

    for i in range(1, N + 1):
        parent[i] = i

    for _ in range(M):
        order, a, b = map(int, input().split())

        if order:  # 확인 출력
            print("YES" if find(parent, a) == find(parent, b) else "NO")
        else:
            union(parent, a, b)
