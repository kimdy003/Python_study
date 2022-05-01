import sys
import heapq

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
hq = [(arr[0][1], arr[0][0])]

for i in range(1, N):
    if hq[0][0] <= arr[i][0]:
        heapq.heappop(hq)
    heapq.heappush(hq, (arr[i][1], arr[i][0]))

print(len(hq))
