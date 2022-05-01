import sys
import heapq

input = sys.stdin.readline

N = int(input())
_input = sorted(
    [list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1]
)

ans = []

for pay, day in _input:
    heapq.heappush(ans, pay)

    if day < len(ans):
        heapq.heappop(ans)

print(sum(ans))
