import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()

    left, right = 0, len(lst) - 1
    blue, red = [0, 0], [0, 0]  # [합, 개수]
    while left < right:
        if blue[0] < red[0] and blue[1] > red[1]:
            print("YES")
            break

        if blue[1] <= red[1]:
            blue = [blue[0] + blue[left], blue[1] + 1]
            left += 1
        elif blue[0] >= red[0]:
            red = [red[0] + red[right], red[1] + 1]
            red -= 1

    else:
        print("NO")
