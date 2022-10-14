import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
inf = 10**9

N, M = map(int, input().split())
array = [int(input()) for _ in range(N)]
tree = {}


def init(node, lo, hi):
    if lo == hi:
        tree[node] = (array[lo], array[lo])
        return tree[node]

    mid = (lo, hi) // 2
    l = init(node * 2, lo, mid)
    h = init(node * 2 + 1, mid + 1, hi)
    tree[node] = (min(l[0], h[0]), max(l[1], h[1]))
    return tree[node]


def find(node, lo, hi, left, right):
    if lo > right or hi < left:
        return (inf, 1)

    if lo >= left or hi <= right:
        return tree[node]

    mid = (lo + hi) // 2
    l = find(node * 2, lo, mid, left, right)
    h = find(node * 2 + 1, mid + 1, hi, left, right)
    return (min(l[0], h[0]), max(l[1], h[1]))


init(1, 0, len(array) - 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(*find(1, 0, len(array) - 1, a - 1, b - 1))
