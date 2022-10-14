import sys
import heapq

input = sys.stdin.readline

N, H, T = map(int, input().split())
tall = [-int(input()) for _ in range(N)]
heapq.heapify(tall)

cnt = 0
for _ in range(T):
    if -tall[0] == 1 or -tall[0] < H:
        break
    else:
        heapq.heappush(tall, -(-heapq.heappop(tall) // 2))
        cnt += 1

if -tall[0] < H:
    print("YES", cnt, sep="\n")
else:
    print("NO", -tall[0], sep="\n")
