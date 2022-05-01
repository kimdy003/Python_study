"""
2021.10.28
23290_마법사 상어와 복제
5 1
4 3 5
1 3 5
2 4 2
2 1 6
3 4 4
4 2
"""

import sys
from copy import deepcopy

input = sys.stdin.readline


def test_print(arr):
    print()
    for i in range(len(arr)):
        print(arr[i])


movdir = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
shark_dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # 상 좌 하 우

M, S = map(int, input().split())  # 물고기 수, 마법을 연습한 횟수
fishs, fish_index = {}, 1
for _ in range(M):
    y, x, d = map(int, input().split())  # 물고기 위치, 방향
    fishs[fish_index] = [
        y - 1,
        x - 1,
        d - 1,
        1,
    ]  # 물고기 위치, 방향, 죽음 여부(1: live, 0: dead)
    fish_index += 1

temp = list(map(int, input().split()))
shark = [temp[0] - 1, temp[1] - 1]
board = [[0] * 4 for _ in range(4)]  # 상어의 위치(-2) & 물고기 시체 위치 표시(양수)
dead = []
board[shark[0]][shark[1]] = -2

for _ in range(S):
    # step 1. 알 낳기
    Egg = []
    for idx, fish in fishs.items():
        if fish[3] == 1:
            Egg.append([fish[0], fish[1], fish[2]])  # 위치, 방향

    # step 2. 물고기 이동
    for idx, fish in fishs.items():
        if fish[3] == 1:
            ny, nx = fish[0] + movdir[fish[2]][0], fish[1] + movdir[fish[2]][1]
            if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx] == 0:
                fishs[idx] = [ny, nx, fish[2], 1]  # 물고기 이동
            else:
                nd = (fish[2] - 1) % 8
                while nd != fish[2]:
                    ny, nx = fish[0] + movdir[nd][0], fish[1] + movdir[nd][1]
                    if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx] == 0:
                        fishs[idx] = [ny, nx, nd, 1]
                        break
                    else:
                        nd = (nd - 1) % 8

    # step 3. 상어 이동
    cand = []
    fish_board = [[[] for _ in range(4)] for _ in range(4)]
    for idx, fish in fishs.items():
        if fish[3] == 1:
            fish_board[fish[0]][fish[1]].append(idx)

    def move_shark(cur, cnt, path, food, food_lst, fish_board):
        if cnt == 3:
            global cand
            if not cand or cand[0] < food:
                t_path = deepcopy(path)
                cand = [food, t_path, food_lst, cur]
            return

        temp = deepcopy(fish_board)
        temp_lst = deepcopy(food_lst)
        for idx, [dy, dx] in enumerate(shark_dir):
            ny, nx = cur[0] + dy, cur[1] + dx
            if 0 <= ny < 4 and 0 <= nx < 4:
                path.append(idx)
                if fish_board[ny][nx]:  # 물고기가 존재하면
                    for i in fish_board[ny][nx]:
                        food_lst.append(i)
                    fish_board[ny][nx] = []

                    move_shark(
                        [ny, nx], cnt + 1, path, food + 1, food_lst, fish_board
                    )

                else:
                    move_shark(
                        [ny, nx], cnt + 1, path, food, food_lst, fish_board
                    )

                path.pop()
                fish_board = deepcopy(temp)
                food_lst = deepcopy(temp_lst)

    move_shark(shark, 0, [], 0, [], fish_board)  # [food, path, food_lst, shark]

    board[shark[0]][shark[1]] = 0
    shark = cand[3]
    board[shark[0]][shark[1]] = -2

    # step 4. 물고기 시체 만들기 & 2년 지우기
    length = len(dead)
    for _ in range(length):
        idx, time = dead.pop(0)
        y, x = fishs[idx][0], fishs[idx][1]
        if time == 2:
            board[y][x] -= 1
        else:
            time += 1
            dead.append([idx, time])

    for c in cand[2]:
        fishs[c][3] = 0
        dead.append([c, 0])  # idx, 시간
        board[fishs[c][0]][fishs[c][1]] += 1

    # step 5. 알 부화
    for e in Egg:
        fishs[fish_index] = [*e, 1]  # 물고기 위치, 방향, 죽음 여부
        fish_index += 1

    # test_print(board)
    # _fish_board = [[[] for _ in range(4)] for _ in range(4)]
    # for idx, fish in fishs.items():
    #     if fish[3] == 1:
    #         _fish_board[fish[0]][fish[1]].append(idx)
    # test_print(_fish_board)
    # print(fishs)


ans = 0
for fish in fishs.values():
    if fish[3] == 1:
        ans += 1
print(ans)
