import sys

input = sys.stdin.readline

N = int(input())
color = [0] + list(map(int, input().split()))
graph = {i: [] for i in range(N + 1)}
graph_color = [0 for _ in range(N + 1)]


def DFS(node, color):
    graph_color[node] = color

    for nxt in graph[node]:
        DFS(nxt, color)


for _ in range(N - 1):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    graph[a].append(b)

ans = 0
for i in range(1, N + 1):
    if color[i] != 0 and color[i] != graph_color[i]:
        ans += 1
        DFS(i, color[i])

print(ans)
