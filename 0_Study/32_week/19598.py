import sys
import heapq

input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

rooms, ans = [0], 1
for s, e in lst:
    if s >= rooms[0]:
        heapq.heappop(rooms)
    else:
        ans += 1
    heapq.heappush(rooms, e)

print(ans)
