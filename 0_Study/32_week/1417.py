import sys
import heapq


def solve():
    input = sys.stdin.readline
    N = int(input())
    if N == 1:
        print(0)
        return

    som = int(input())
    lst = [-int(input()) for _ in range(N - 1)]
    heapq.heapify(lst)

    cnt = 0
    while True:
        temp = -heapq.heappop(lst)
        if temp < som:
            break
        cnt += 1
        som, temp = som + 1, temp - 1
        heapq.heappush(lst, -temp)

    print(cnt)
    return


solve()
