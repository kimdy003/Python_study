import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    heap = []

    for _ in range(N):
        num = int(input())
        if num != 0:
            heapq.heappush(heap, (abs(num), num))
        else:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0)
