import sys

input = sys.stdin.readline


class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.heapsize = 0

    def Swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def Push(self, x):
        self.heapsize += 1
        if self.heapsize == len(self.heap):
            self.heap.append(x)
        else:
            self.heap[self.heapsize] = x

        child = self.heapsize
        while child > 1:
            parent = child // 2
            if x < self.heap[parent]:
                self.Swap(child, parent)
                child = parent
            else:
                break

    def Pop(self):
        if self.heapsize == 0:
            return 0
        Min_heap = self.heap[1]

        self.heap[1] = self.heap[self.heapsize]
        self.heap[self.heapsize] = -1
        self.heapsize -= 1

        idx, temp = 1, 0
        while 2 * idx + 1 <= self.heapsize:
            if (
                self.heap[idx] < self.heap[2 * idx]
                and self.heap[idx] < self.heap[2 * idx + 1]
            ):
                break
            elif self.heap[2 * idx + 1] < self.heap[2 * idx]:
                temp = 2 * idx + 1
            else:
                temp = 2 * idx

            self.Swap(idx, temp)
            idx = temp

        if 2 * idx <= self.heapsize and self.heap[2 * idx] < self.heap[idx]:
            self.Swap(idx, 2 * idx)

        return Min_heap


N = int(input())
heap = MinHeap()
for _ in range(N):
    x = int(input())
    if x == 0:
        print(heap.Pop())
    else:
        heap.Push(x)
