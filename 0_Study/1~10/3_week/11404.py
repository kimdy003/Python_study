"""
21.10.15
11404_플로이드
"""

import sys
import math

input = sys.stdin.readline
INF = math.inf

N = int(input())
M = int(input())
dist = [[INF if i != j else 0 for j in range(N + 1)] for i in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dist[i][j] == INF:
            dist[i][j] = 0
    print(" ".join(map(str, dist[i][1:])))
