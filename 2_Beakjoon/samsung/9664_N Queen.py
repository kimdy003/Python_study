import sys


input = sys.stdin.readline


def check(row, col):
    for r in range(row):
        q = queen[r]

        if col == q:
            return False

        a = abs(q - col)
        b = row - r
        if a == b:
            return False
    return True


def placeQueen(row):
    if row == N:
        return 1

    cnt = 0
    for col in range(N):
        if check(row, col):
            queen[row] = col
            cnt += placeQueen(row + 1)

    return cnt


def solQueen(row):
    if row == N:
        return 1

    count = 0
    for col in range(N):
        if column[col] and slash[row + col] and backSlash[row - col]:
            column[col] = slash[row + col] = backSlash[row - col] = False
            count += solQueen(row + 1)
            column[col] = slash[row + col] = backSlash[row - col] = True
    return count


if __name__ == "__main__":
    N = int(input())
    queen = [0] * N
    # answer = placeQueen(0)

    column = [True] * N
    slash = [True] * (2 * N - 1)
    backSlash = [True] * (2 * N - 1)
    answer = solQueen(0)

    print(answer)
