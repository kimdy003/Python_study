import sys
import heapq

input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    nums = list(map(int, input().split()))

    if not hq:
        for num in nums:
            heapq.heappush(hq, num)

    else:
        for num in nums:
            if hq[0] < num:
                heapq.heappush(hq, num)
                heapq.heappop(hq)

print(hq[0])
