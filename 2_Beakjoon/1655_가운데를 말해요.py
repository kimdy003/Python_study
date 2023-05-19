import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    maxHeap = []  # 마이너스를 이용한 maxheap
    minHeap = []  # minheap
    for _ in range(N):
        num = int(input())

        if len(maxHeap) == len(minHeap):
            heapq.heappush(maxHeap, -num)
        else:
            heapq.heappush(minHeap, num)

        # print("maxHeap : ", maxHeap)
        # print("minHeap : ", minHeap)

        if minHeap and minHeap[0] < -maxHeap[0]:
            leftVal = heapq.heappop(maxHeap)
            rightVal = heapq.heappop(minHeap)

            heapq.heappush(maxHeap, -rightVal)
            heapq.heappush(minHeap, -leftVal)

        print(-maxHeap[0])
