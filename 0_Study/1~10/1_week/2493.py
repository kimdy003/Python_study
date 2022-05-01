import sys


input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = [0] * N
stack = []

for i in range(N - 1, -1, -1):
    while stack and stack[-1][1] < arr[i]:
        answer[stack.pop()[0]] = i + 1
    stack.append((i, arr[i]))

print(*answer)
