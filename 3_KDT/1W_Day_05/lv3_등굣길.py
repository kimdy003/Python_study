#
#  lv3_등굣길.py
#  등굣길
#
#  Create by 김도영 on 2021/04/25
#


def solution(m, n, puddles):
    map = [[0] * (m + 1) for _ in range(n + 1)]
    map[1][1] = 1

    for x, y in puddles:
        map[y][x] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if map[i][j] == -1:
                map[i][j] = 0
                continue

            map[i][j] += (map[i - 1][j] + map[i][j - 1]) % 1000000007

    return map[n][m]