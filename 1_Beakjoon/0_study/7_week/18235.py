import sys
from collections import deque

input = sys.stdin.readline


def solve():
    N, A, B = map(int, input().split())
    lst = [0] * (N + 1)
    lst[A] = 5

    if A == B:
        print(0)
    else:
        queue, qqueue = deque(), deque()
        queue.append([A, 1])  # 위치, 날짜
        qqueue.append([B, 1])

        while queue and qqueue:
            five_length = len(queue)
            for _ in range(five_length):
                five, day = queue.popleft()
                lst[five] -= 5

                for i in [-1, 1]:
                    next_five = five + (2 ** (day - 1)) * i
                    if 0 < next_five <= N:
                        queue.append([next_five, day + 1])
                        lst[next_five] += 5

            six_length = len(qqueue)
            for _ in range(six_length):
                six, day = qqueue.popleft()

                for i in [-1, 1]:
                    next_six = six + (2 ** (day - 1)) * i
                    if 0 < next_six <= N:
                        if lst[next_six] != 0:
                            print(day)
                            return
                        qqueue.append([next_six, day + 1])
        print(-1)


if __name__ == "__main__":
    solve()
