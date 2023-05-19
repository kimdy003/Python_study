import sys

input = sys.stdin.readline


def init(board):
    """
    depth : 같은 방향으로 몇번 진행하는지 결정해주는 변수
    cnt : 몇번 진행했는지 확인하는 변수
    """
    ans = [0, 0]
    movdir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    num, depth = 1, 1
    dir = 0

    y = x = N // 2

    cnt = 0
    while y > -1 and x > -1:
        board[y][x] = num
        if num == search:
            ans = [y, x]

        y, x = y + movdir[dir][0], x + movdir[dir][1]
        cnt += 1
        num += 1

        if cnt == depth:  # 한 방향으로 depth만큼 이동. 따라서 방향 change
            if dir in [1, 3]:  # 이 때 방향이 좌 or 우 였다면 depth 증가
                depth += 1

            dir = (dir + 1) % 4
            cnt = 0

    for i in board:
        print(*i)
    print(ans[0] + 1, ans[1] + 1)


if __name__ == "__main__":
    N = int(input())
    search = int(input())
    board = [[0] * N for _ in range(N)]

    init(board)
