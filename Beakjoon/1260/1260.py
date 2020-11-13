import sys

n, m, v = map(int, sys.stdin.readline().split())
matrix = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    line = list(map(int, sys.stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

def DFS(node, visit):
    visit += [node]
    for next in range(len(matrix[node])):
        if matrix[node][next] == 1 and (next not in visit):
            DFS(next, visit)
    
    return visit

def BFS(node):
    visit = [node]
    queue = [node]

    while queue:
        n = queue.pop(0)
        for next in range(len(matrix[node])):
            if matrix[n][next] == 1 and (next not in visit):
                visit.append(next)
                queue.append(next)
    return visit

print(*DFS(v, []))
print(*BFS(v))