"""
나선형 알고리즘
홀수 길이의 2차원 배열의 중심에서 시작하여 방향을 바꾸며 이동(혹은 탐색)을 하는데,
방향을 2번 바꿀 때마다 이동거리가 1씩 증가
"""


def init(board):
    """
    depth : 같은 방향으로 몇번 진행하는지 결정해주는 변수
    cnt : 몇번 진행했는지 확인하는 변수
    """
    movdir = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상 우 하 좌
    num, depth = 1, 1
    dir = 0

    y = x = N // 2

    cnt = 0
    while y > -1 and x > -1:
        board[y][x] = num
        indexing[num] = (y, x)

        y, x = y + movdir[dir][0], x + movdir[dir][1]
        cnt += 1
        num += 1

        if cnt == depth:  # 한 방향으로 depth만큼 이동. 따라서 방향 change
            if dir in [1, 3]:  # 이 때 방향이 좌 or 우 였다면 depth 증가
                depth += 1

            dir = (dir + 1) % 4
            cnt = 0


if __name__ == "__main__":
    indexing = {}
    N = int(input())
    board = [[0] * N for _ in range(N)]
    init(board)


""" 출력 결과
9 2 3
8 1 4
7 6 5
"""
