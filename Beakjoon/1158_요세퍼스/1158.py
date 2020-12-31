from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
dq = deque()
for i in range(n):
    dq.append(i+1)

removed = []

while len(dq) > 0:
    for _ in range(k-1):
        dq.append(dq.popleft())
    removed.append(dq.popleft())

print("<", end="")
for i in range(len(removed)-1):
    print(str(removed[i])+", ", end="")
print(str(removed[-1])+">")
