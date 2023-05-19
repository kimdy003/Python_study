import sys

input = sys.stdin.readline

if __name__ == "__main__":
    w, h, f, c, x1, y1, x2, y2 = map(int, input().split())
    make_x_len = w - f
    reverse_x = False

    if make_x_len < w // 2:
        make_x_len = w - make_x_len
        reverse_x = True

    split_y = c + 1
    total_ = w * h

    for x in range(x1, x2):
        if not reverse_x:
            if x < f:
                count = 2
            else:
                count = 1
        else:
            if x >= x - f:
                count = 1
            else:
                count = 2

        count *= split_y
        if (x >= x1) and (x < x2):
            total_ -= count * (y2 - y1)

    print(total_)


def main():
    w, h, f, c, x1, y1, x2, y2 = map(int, input().split())
    make_x_len = w - f
    if make_x_len < w // 2:  # 뒤집어져서 make_x_len이 작아졌을 때 변경
        make_x_len = w - make_x_len
    split_y = c + 1
    total_ = w * h
    split_x = w - make_x_len
    n = x2 - x1
    if x1 < split_x:
        if x2 > split_x:  # 겹치는 부분이 x1은 포함, x2는 미포함일 때
            n += split_x - x1
        else:  # 겹치는 부분이 x1, x2모두 포함일 때
            n *= 2
    print(total_ - (n * (y2 - y1) * split_y))  # y는 x접어서 동등하게 나누므로 그냥 곱하기 가능
