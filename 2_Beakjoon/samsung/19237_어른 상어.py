import sys
from collections import defaultdict

input = sys.stdin.readline


class Shark:
    def __init__(self, num: int = -1, y: int = -1, x: int = -1):
        """상어 데이터 초기화

        :param num: 상어 번호 (default: -1)
        :param y: 상어의 row번호 (default: -1)
        :param x: 상어의 col번호 (default: -1)
        """
        self.num = num
        self.y = y
        self.x = x
        self.d = -1
        self.pri = defaultdict(list)
        self.life = True

    def __str__(self):
        return "상어 번호 {}, 위치 ({}, {}), 방향 {}, 생존 여부: {}".format(
            self.num, self.y, self.x, self.d, self.life
        )

    def updateDirection(self, d: int):
        """상어 방향 update"""
        self.d = d

    def insertPriority(self, priority: list[list]):
        """방향별 우선순위. insert"""
        for i in range(1, 5):
            self.pri[i] = priority[i - 1]

    def smellSpread(self, time):
        """현재 위치에 냄새 뿌리기"""
        board[self.y][self.x] = [self.num, time + K]

    def checkShark(self, position):
        y, x = position[0], position[1]
        if board[y][x][0] == 0 or self.num == board[y][x][0]:
            return True

        if self.num < board[y][x][0]:
            sharkList[board[y][x][0]].life = False
            return True

        self.life = False
        return False

    def move(self, time):
        """상어 이동."""
        position, mySmellPosition = [], []
        y, x = self.y, self.x
        tempBoard = [each[:] for each in board]

        for nd in self.pri[self.d]:
            ny, nx = y + movdir[nd][0], x + movdir[nd][1]

            if 0 <= ny < N and 0 <= nx < N:
                if not position and tempBoard[ny][nx][1] <= time:  # 빈 칸으로 이동
                    position = [ny, nx, nd]
                    break

                if not mySmellPosition and tempBoard[ny][nx][0] == self.num:  # 자기 냄새 칸으로 이동
                    mySmellPosition = [ny, nx, nd]

        if position:
            if self.checkShark(position):
                board[position[0]][position[1]][0] = self.num
                self.y, self.x, self.d = position

        elif mySmellPosition:
            self.y, self.x, self.d = mySmellPosition


def check():
    for i in range(2, M + 1):
        if sharkList[i].life:
            return False
    return True


def solution():
    for time in range(1, 1001):

        # 냄새 초기화
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j][1] == time:
                    board[i][j] = [0, 0]

        # 1. 냄새 뿌리기
        for i in range(1, M + 1):
            if sharkList[i].life:
                sharkList[i].smellSpread(time)

        # 2. 상어 이동 + 같은 칸 상어 제거
        for i in range(1, M + 1):
            if sharkList[i].life:
                sharkList[i].move(time)

        if check():
            return time
    else:
        return -1


if __name__ == "__main__":
    movdir = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
    N, M, K = map(int, input().split())
    sharkList: list[Shark] = [Shark() for _ in range(M + 1)]
    board: list[list[list[int]]] = [[] for _ in range(N)]  # board[i][j] = [번호, 현재 시간+k초]

    for i in range(N):
        temp = list(map(int, input().split()))
        for j, num in enumerate(temp):
            board[i].append([num, 0])
            if num > 0:
                sharkList[num] = Shark(num, i, j)

    for idx, val in enumerate(list(map(int, input().split())), start=1):
        sharkList[idx].updateDirection(val)

    for i in range(1, M + 1):
        temp = []
        for _ in range(4):
            temp.append(list(map(int, input().split())))
        sharkList[i].insertPriority(temp)

    print(solution())
