import sys

input = sys.stdin.readline

N = int(input())

array = []
for _ in range(N):
    n = int(input())
    if n:
        array.append(n)
    else:
        array.pop()

print(sum(array))
