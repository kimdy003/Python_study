import sys

input = sys.stdin.readline

for _ in range(int(input())):
    sep = input()
    N, M = map(int, input().split())

    lst = []
    for i in range(1, M + 1):
        x, w = map(int, input().split())
        lst.append([x, w, i])

    lst.sort(key=lambda l: l[1])
    lst = lst[: 2 * N]
    lst.sort(key=lambda l: l[0])

    _sum = 0
    for _, w, _ in lst:
        _sum += w

    print("===========================")
    print(_sum)
    for i in range(1, N + 1):
        print(lst[i - 1][2], lst[-i][2])
    print("===========================")
