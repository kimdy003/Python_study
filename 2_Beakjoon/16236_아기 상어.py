import sys
from collections import deque

input = sys.stdin.readline


class Shark:
    def __init__(self, y: int = 0, x: int = 0, size: int = 2) -> None:
        self.y = y
        self.x = x
        self.size = size
        self.count = 0

    def move(self, y: int, x: int) -> None:
        self.y = y
        self.x = x

    def eating(self) -> None:
        self.count += 1
        if self.count == self.size:
            self.size += 1
            self.count = 0


def BFS(N, shark: Shark, board: list):
    def boundary(y, x):
        if 0 <= y < N and 0 <= x < N:
            return True
        return False

    movdir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    visited = [[True] * N for _ in range(N)]

    q = deque([[shark.y, shark.x]])
    visited[shark.y][shark.x] = False
    result, time = [], 0

    while q:
        curr = len(q)
        time += 1

        for _ in range(curr):
            y, x = q.popleft()

            for dy, dx in movdir:
                ny, nx = y + dy, x + dx
                if boundary(ny, nx) and visited[ny][nx] and board[ny][nx] <= shark.size:
                    visited[ny][nx] = False
                    q.append([ny, nx])
                    if 0 < board[ny][nx] < shark.size:
                        result.append([ny, nx])

        if result:
            break
    else:
        return [], 0

    result.sort()
    return result[0], time


def solution():
    ans = 0
    N = int(input())
    board = []

    for i in range(N):
        temp = []
        for j, state in enumerate(list(map(int, input().split()))):
            if state == 9:
                shark = Shark(i, j)
                temp.append(0)
                continue
            temp.append(state)
        board.append(temp)

    while True:
        lst, time = BFS(N, shark, board)
        if not lst:
            break  # 먹을 수 있는 물고기가 없다

        # 상어 이동, 먹이 카운트, 크기 증가
        shark.move(lst[0], lst[1])  # 상어 이동
        shark.eating()  # 먹이 카운트 + 상어 크기 증가
        ans += time  # 시간 초 증가
        board[lst[0]][lst[1]] = 0  # 물고기 삭제

    return ans


if __name__ == "__main__":
    print(solution())
