import sys
import heapq

input = sys.stdin.readline
N, k = map(int, input().split())
hq, out = [], []

for i in range(k):
    heapq.heappush(hq, (0, i))  # 계산 시간, 계산대

for _ in range(N):
    id, w = map(int, input().split())

    calcu_time, calcu = heapq.heappop(hq)
    heapq.heappush(hq, (calcu_time + w, calcu))
    heapq.heappush(out, (calcu_time + w, -calcu, id))

ans = sum([i * heapq.heappop(out)[2] for i in range(1, N + 1)])
print(ans)
