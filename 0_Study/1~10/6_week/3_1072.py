"""
1072_Z
"""
import sys

input = sys.stdin.readline


def div(size, start_row, start_col):
    global ans
    if size == 2:
        if start_row == r and start_col == c:
            print(ans)
            return
        ans += 1
        if start_row == r and start_col + 1 == c:
            print(ans)
            return
        ans += 1
        if start_row + 1 == r and start_col == c:
            print(ans)
            return
        ans += 1
        if start_row + 1 == r and start_col + 1 == c:
            print(ans)
            return
        ans += 1
    else:
        div(size // 2, start_row, start_col)
        div(size // 2, start_row + size // 2, start_col)
        div(size // 2, start_row, start_col + size // 2)
        div(size // 2, start_row + size // 2, start_col + size // 2)


N, r, c = map(int, input().split())
ans = 0
div(2 ** N, 0, 0)
