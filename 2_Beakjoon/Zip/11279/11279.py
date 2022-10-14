#
#  11279.py
#  최대 힙
#
#  Create by 김도영 on 2021/05/05
#


from sys import stdin
import heapq


N = int(stdin.readline())
hq = []

for _ in range(N):
    input = int(stdin.readline())

    if input == 0:
        if not hq:
            print(0)
        else:
            print(-heapq.heappop(hq))

    else:
        heapq.heappush(hq, -input)
