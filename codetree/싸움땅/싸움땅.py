import sys

input = sys.stdin.readline


class Player:
    def __init__(self, num=0, y=-1, x=-1, d=-1, state=0, gun=0) -> None:
        self.num = num
        self.y = y
        self.x = x
        self.d = d
        self.state = state
        self.gun = gun

    def __str__(self) -> str:
        return "번호 {}, 위치 ({}, {}), 방향 {}, 총 {}".format(self.num, self.y, self.x, self.d, self.gun)

    def reverseDir(self, d):
        if d == 0:
            return 2
        elif d == 1:
            return 3
        elif d == 2:
            return 0
        else:
            return 1

    def fight(self, you, point, flag):
        """
        winner -> 각 플레이어의 초기 능력치와 총의 공격력의 합의 차이만큼 포인트 획득

        losser -> 본인의 총을 해당 칸에 내려놓기, 방향대로 한 칸 이동
                이동할 칸에 플레이어가 있거나, 격자밖이라면 오른쪽 90도 회전 -> 빈칸으로
                총이 있으면 공격력이 높은거 획득

        winner -> 총 비교해서 줍기
        """

        if flag:  # 내가 이김
            ans[self.num] += point  # 나에게 포인트 적립
            winner = playerList[self.num]
            losser = playerList[you]

        else:  # 내가 짐
            ans[playerList[you].num] += point  # 상대방 포인트 적립
            winner = playerList[you]
            losser = playerList[self.num]

        gunBoard[losser.y][losser.x].append(losser.gun)
        losser.gun = 0

        # losser 이동
        for _ in range(4):
            ny, nx = losser.y + movdir[losser.d][0], losser.x + movdir[losser.d][1]
            if 0 <= ny < N and 0 <= nx < N and playerBoard[ny][nx] == 0:
                playerBoard[ny][nx] = losser.num
                losser.y, losser.x = ny, nx

                # losser 총 들기
                for i in range(len(gunBoard[ny][nx])):
                    if losser.gun < gunBoard[ny][nx][i]:
                        temp = losser.gun
                        losser.gun = gunBoard[ny][nx][i]
                        gunBoard[ny][nx][i] = temp
                break

            # 격자 밖이거나, 플레이어가 있으면 방향 회전
            losser.d = (losser.d + 1) % 4

        # 해당 칸은 winner 차지
        playerBoard[winner.y][winner.x] = winner.num

        # winner 총 들기
        y, x = winner.y, winner.x
        for i in range(len(gunBoard[y][x])):
            if winner.gun < gunBoard[y][x][i]:
                temp = winner.gun
                winner.gun = gunBoard[y][x][i]
                gunBoard[y][x][i] = temp

    def play(self):
        # 1. 본인이 향하고 있는 방향대로 한 칸 이동
        #    i. 격자를 벗어나면 정반대로 방향을 바꿔서 이동
        playerBoard[self.y][self.x] = 0
        ny, nx = self.y + movdir[self.d][0], self.x + movdir[self.d][1]
        if not (0 <= ny < N and 0 <= nx < N):
            self.d = self.reverseDir(self.d)  # 방향 반대로 바꾸고 다시
            ny, nx = self.y + movdir[self.d][0], self.x + movdir[self.d][1]
        self.y, self.x = ny, nx

        ## 플레이어가 없음 -> 해당 칸 총이 있는지 확인
        ##    i. 해당 칸의 총과 자신이 들고 있는 총 중 제일 쎈거 갖기
        if playerBoard[ny][nx] == 0:
            playerBoard[ny][nx] = self.num
            # 총이 있는지 확인
            for i in range(len(gunBoard[ny][nx])):
                if self.gun < gunBoard[ny][nx][i]:
                    temp = self.gun
                    self.gun = gunBoard[ny][nx][i]
                    gunBoard[ny][nx][i] = temp

        ## 있음 -> 플레이어와 싸우기
        ##         i. 해당 플레이어의 초기 능력치 + 총의 공격력 비교 -> 초기 능력치가 더 높은게 승리
        ##         이김 -> 각 플레이어의 초기 능력치와 총의 공격력의 합의 차이만큼 포인트 획득

        ##         짐   -> 본인의 총을 해당 칸에 내려놓기, 방향대로 한 칸 이동
        ##                 이동할 칸에 플레이어가 있거나, 격자밖이라면 오른쪽 90도 회전 -> 빈칸으로
        ##                 총이 있으면 공격력이 높은거 획득

        ##         이김 -> 총 비교해서 줍기
        else:
            you = playerBoard[ny][nx]
            myAttack = self.state + self.gun  # 나의 공격력
            youAttack = playerList[you].state + playerList[you].gun  # 상대방의 공격력

            # 공격력 비교, True : 승리, False : 패패
            if myAttack > youAttack:
                self.fight(you, abs(myAttack - youAttack), True)
            elif myAttack < youAttack:
                self.fight(you, abs(myAttack - youAttack), False)
            else:
                # 공격력이 같다면, 초기 능력치가 높은게 승리
                if self.state > playerList[you].state:
                    self.fight(you, abs(myAttack - youAttack), True)
                elif self.state < playerList[you].state:
                    self.fight(you, abs(myAttack - youAttack), False)


def checkPrint():
    print()
    print("------- gunBoard ---------")
    for i in range(N):
        print(gunBoard[i])
    print()
    print("------- playerBoard -------------")
    for i in range(N):
        print(playerBoard[i])
    print()
    print("------- player 상태-------------")
    for i in range(1, M + 1):
        print(playerList[i])
    print("ans point : ", ans)
    print()


def solution():
    """
    각 플레이어 순차적으로 / 한꺼번에 움직임X
    1. 본인이 향하고 있는 방향대로 한 칸 이동
        i. 격자를 벗어나면 정반대로 방향을 바꿔서 이동
    2. 이동한 방향에 플레이어 확인
        없음 -> 해당 칸 총이 있는지 확인
                i. 해당 칸의 총과 자신이 들고 있는 총 중 제일 쎈거 갖기
        있음 -> 플레이어와 싸우기
                i. 해당 플레이어의 초기 능력치 + 총의 공격력 비교 -> 초기 능력치가 더 높은게 승리
                이김 -> 각 플레이어의 초기 능력치와 총의 공격력의 합의 차이만큼 포인트 획득

                짐   -> 본인의 총을 해당 칸에 내려놓기, 방향대로 한 칸 이동
                        이동할 칸에 플레이어가 있거나, 격자밖이라면 오른쪽 90도 회전 -> 빈칸으로
                        총이 있으면 공격력이 높은거 획득

                이김 -> 총 비교해서 줍기

    """
    for r in range(K):
        print("==================== {} 라운드 ==============".format(r))
        for idx in range(1, M + 1):
            playerList[idx].play()

            checkPrint()


if __name__ == "__main__":
    movdir = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상 우 하 좌
    N, M, K = map(int, input().split())  # 격자크기, 플레이어수, 라운드 수
    ans = [0] * (M + 1)
    gunBoard = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j, num in enumerate(list(map(int, input().split()))):
            if num != 0:
                gunBoard[i][j].append(num)

    playerBoard = [[0] * N for _ in range(N)]
    playerList: list[Player] = [Player() for _ in range(M + 1)]
    for i in range(1, M + 1):
        y, x, d, s = map(int, input().split())
        y, x = y - 1, x - 1
        playerList[i] = Player(i, y, x, d, s)
        playerBoard[y][x] = i

    solution()
    print(*ans[1:])
