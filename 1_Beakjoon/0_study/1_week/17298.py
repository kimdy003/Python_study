import sys


input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = [-1] * N
stack = []

for i, a in enumerate(arr):
    while stack and stack[-1][1] < a:
        answer[stack.pop()[0]] = a
    stack.append((i, a))

print(*answer)
