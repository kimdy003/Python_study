from copy import deepcopy
import sys

input = sys.stdin.readline


class Shark:
    def __init__(self, y: int, x: int, s: int, d: int, z: int, life: bool = True) -> None:
        self.y = y
        self.x = x
        self.speed = self.speedDiv(s, d)  # 속력
        self.dir = d  # 방향
        self.size = z  # 크기
        self.life = life  # 생존 유무

    def speedDiv(self, s: int, d: int) -> int:
        if d == 1 or d == 2:  # 세로 방향
            return s % ((R - 1) * 2)
        else:
            return s % ((C - 1) * 2)

    def move(self) -> None:
        def inverse(d):
            if d == 1:
                return 2
            elif d == 2:
                return 1
            elif d == 3:
                return 4
            return 3

        y, x = self.y, self.x
        cnt = 0
        while True:
            if cnt == self.speed:
                self.y, self.x = y, x
                break
            ny, nx = y + movdir[self.dir][0], x + movdir[self.dir][1]
            if 0 <= ny < R and 0 <= nx < C:
                y, x = ny, nx
            else:
                self.dir = inverse(self.dir)
                continue

            cnt += 1

    def __str__(self) -> str:
        return "위치 = ({}, {}) 속력 = {}, 방향 = {}, 크기 = {}, 생존 유무 = {} ".format(
            self.y, self.x, self.speed, self.dir, self.size, self.life
        )


def sharkPrint(sharkList):
    for i, shark in enumerate(sharkList):
        print("{}번 상어 \n {}".format(i, shark))


def boardPring(fishing, arr):
    tempArr = deepcopy(arr)
    for i in range(R):
        for j in range(C):
            if tempArr[i][j] == -1:
                tempArr[i][j] = 0
    print()
    print("---------{}-----------------------".format(fishing))
    for i in range(R):
        print(tempArr[i])


def solution():
    ans = 0
    board = [[-1] * C for _ in range(R)]
    sharkList: list[Shark] = []
    initBoard = [[-1] * C for _ in range(R)]
    for i in range(M):
        temp = list(map(int, input().split()))
        temp = [temp[0] - 1, temp[1] - 1] + temp[2:]
        sharkList.append(Shark(*temp))

        board[temp[0]][temp[1]] = i

    for fishing in range(C):  # 1. 낚시왕이 오른쪽 한 칸 이동
        # boardPring(fishing, board)

        # 2. 같은 열 상어 잡기
        for i in range(R):
            if board[i][fishing] != -1 and sharkList[board[i][fishing]].life:  # 상어 존재
                sharkId = board[i][fishing]
                sharkList[sharkId].life = False

                ans += sharkList[sharkId].size
                break

        # 3. 상어 이동
        board = deepcopy(initBoard)
        for idx, shark in enumerate(sharkList):
            if shark.life:
                shark.move()

                if board[shark.y][shark.x] != -1:  # 상어가 있는 경우, i(new) vs sharkId(ori) 크기 비교
                    sharkId = board[shark.y][shark.x]

                    if sharkId != idx:
                        oriShark = sharkList[sharkId].size
                        newShark = sharkList[idx].size

                        if newShark > oriShark:
                            board[shark.y][shark.x] = idx
                            sharkList[sharkId].life = False
                        else:
                            sharkList[idx].life = False

                else:
                    board[shark.y][shark.x] = idx

    return ans


if __name__ == "__main__":
    R, C, M = map(int, input().split())
    movdir = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1]]
    print(solution())
