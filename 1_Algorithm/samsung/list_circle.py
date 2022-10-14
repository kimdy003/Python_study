# 배열 돌리기
N = 5
board = [[i * N + j for j in range(N)] for i in range(N)]


def rotate45():
    # 시계방향으로 배열을 45도 회전하는 함수
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[N - j - 1][i]
    return new_board


def rotate90():
    # 시계방향으로 배열을 90도 회전하는 함수
    new_board = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_board[c][N - 1 - r] = board[r][c]
    return new_board


def rotate180():
    # 시계방향으로 배열을 180도 회전하는 함수
    new_board = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_board[N - 1 - r][N - 1 - c] = board[r][c]
    return new_board


def rotate270():
    # 시계방향으로 배열을 270도 회전하는 함수
    new_board = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_board[N - 1 - c][r] = board[r][c]
    return new_board


print("origin")
for row in board:
    print(row)
print()

print("시계방향 45도 회전")
rotated = rotate45()
for row in rotated:
    print(row)


### 💡파이썬 기반 회전 코드
list(zip(*board[::-1]))
